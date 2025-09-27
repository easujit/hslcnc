from datetime import timedelta
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Outbox, Notification, Task
from core.tenant import get_current_tenant, require_tenant
from quotas.rate_limiting import tenant_limited
from consent.utils import check_consent_for_request

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@tenant_limited(metric="process", rate=30, burst=10)
def process_now(request):
    from policies.authorization import authorize
    
    # Ensure tenant context exists
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    created = 0
    user_claims = getattr(request, 'user_claims', {})
    
    for ob in Outbox.objects.filter(tenant_id=tenant_id, published=False).order_by('id'):
        payload = ob.payload_json or {}
        hba1c = payload.get("hba1c")
        patient_name = payload.get("patient_name", "patient")
        is_minor = payload.get("is_minor", False)
        has_birth_certificate = payload.get("has_birth_certificate", False)
        guardian_name = payload.get("guardian_name")
        
        # General visit notification for all visits
        if ob.topic == "visit_saved":
            Notification.objects.create(
                tenant_id=tenant_id,
                channel="inapp",
                message=f"New visit recorded for {patient_name}",
                status="new"
            )
            created += 1
            print(f"Created general notification for visit: {patient_name}")
        
        # Diabetes educator workflow
        if hba1c is not None and float(hba1c) >= 9:
            # Check workflow step permissions (only if policies exist)
            if user_claims and user_claims.get('tenant_id'):
                from policies.models import PolicyRule
                has_policies = PolicyRule.objects.filter(
                    tenant_id=user_claims['tenant_id'],
                    status='published'
                ).exists()
                
                if has_policies:
                    can_execute = authorize(
                        user_claims,
                        'workflow_step',
                        'execute',
                        {'workflow': 'visit_opd', 'step': 'diabetes_educator'}
                    )
                    if not can_execute:
                        continue  # Skip this workflow step
            
            # Check consent for PHI sharing (notifications and tasks)
            patient_id = payload.get('external_id')
            if patient_id:
                data_categories = ['diagnosis', 'labs']  # HbA1c and diagnosis data
                consent_result = check_consent_for_request(
                    request, patient_id, 'treatment', data_categories
                )
                
                if not consent_result['allow']:
                    # Log denied workflow step
                    print(f"Workflow step skipped - no consent: {consent_result['reason']}")
                    continue
            
            Notification.objects.create(
                tenant_id=tenant_id,
                channel="inapp",
                message=f"Book Diabetes Educator session for {patient_name} (HbA1c={hba1c})",
                status="new"
            )
            Task.objects.create(
                tenant_id=tenant_id,
                team="care",
                summary=f"Educator session for {patient_name}",
                details=f"HbA1c is {hba1c}. Auto-created task from workflow.",
                due_at= now() + timedelta(days=7),
                status="open"
            )
            created += 1
        
        # Pediatrics birth certificate workflow
        if is_minor and not has_birth_certificate:
            # Check workflow step permissions (only if policies exist)
            if user_claims and user_claims.get('tenant_id'):
                from policies.models import PolicyRule
                has_policies = PolicyRule.objects.filter(
                    tenant_id=user_claims['tenant_id'],
                    status='published'
                ).exists()
                
                if has_policies:
                    can_execute = authorize(
                        user_claims,
                        'workflow_step',
                        'execute',
                        {'workflow': 'visit_opd', 'step': 'pediatrics_birth_certificate'}
                    )
                    if not can_execute:
                        continue  # Skip this workflow step
            
            # Check consent for PHI sharing (pediatrics workflow)
            patient_id = payload.get('external_id')
            if patient_id:
                data_categories = ['demographics', 'documents']  # Age and document data
                consent_result = check_consent_for_request(
                    request, patient_id, 'treatment', data_categories
                )
                
                if not consent_result['allow']:
                    # Log denied workflow step
                    print(f"Pediatrics workflow step skipped - no consent: {consent_result['reason']}")
                    continue
            
            Notification.objects.create(
                tenant_id=tenant_id,
                channel="inapp",
                message=f"Upload birth certificate for {patient_name} (Age: {payload.get('age', 'unknown')})",
                status="new"
            )
            Task.objects.create(
                tenant_id=tenant_id,
                team="admin",
                summary=f"Upload birth certificate for {patient_name}",
                details=f"Patient is under 18 and birth certificate is missing. Guardian: {guardian_name or 'Not provided'}. Upload within 24 hours.",
                due_at= now() + timedelta(hours=24),
                status="open"
            )
            created += 1
        
        # Process workflow webhooks
        try:
            from configurator.models import Config
            from extensions.models import DeadLetter
            from extensions.utils import call_http, create_webhook_headers
            
            # Get effective workflow configuration
            workflow_config = Config.objects.filter(
                kind='workflow', 
                name='visit_opd', 
                status='published'
            ).order_by('-version').first()
            
            if workflow_config:
                workflow_spec = workflow_config.spec_json
                
                # Process post_save actions
                for action in workflow_spec.get('post_save', []):
                    if action.get('emit'):
                        # This is handled by the existing Outbox logic
                        pass
                    elif action.get('webhook'):
                        webhook_config = action['webhook']
                        url = webhook_config.get('url')
                        method = webhook_config.get('method', 'POST')
                        timeout_ms = webhook_config.get('timeout_ms', 1200)
                        retries = webhook_config.get('retries', 3)
                        body = webhook_config.get('body', {})
                        
                        if not url:
                            continue
                        
                        # Prepare webhook payload
                        webhook_payload = {
                            'event': 'visit_saved',
                            'data': payload,
                            'timestamp': ob.created_at.isoformat(),
                            'visit_id': payload.get('visit_id'),
                            'patient_name': payload.get('patient_name'),
                            **body  # Merge custom body data
                        }
                        
                        # Add HMAC signature (using a default secret for webhooks)
                        webhook_headers = create_webhook_headers(webhook_payload, 'webhook-secret')
                        
                        # Execute webhook
                        success, status_code, response_data, error_msg = call_http(
                            url=url,
                            method=method,
                            json_data=webhook_payload,
                            timeout_ms=timeout_ms,
                            headers=webhook_headers,
                            retries=retries
                        )
                        
                        if not success or status_code not in [200, 201, 202]:
                            error_msg = error_msg or f"HTTP {status_code}: {response_data}"
                            # Create dead letter for failed webhook
                            DeadLetter.objects.create(
                                kind='webhook',
                                target=url,
                                payload_json=webhook_payload,
                                last_error=error_msg,
                                retry_count=0
                            )
                            print(f"Workflow webhook failed, added to dead letter queue: {error_msg}")
                            
        except Exception as e:
            print(f"Workflow webhook error: {str(e)}")

        # Event subscriptions - deliver to external systems
        try:
            from extensions.models import ExtSubscription, DeadLetter
            from extensions.utils import call_http, create_webhook_headers
            
            subscriptions = ExtSubscription.objects.filter(enabled=True)
            
            for subscription in subscriptions:
                # Check if this subscription is interested in this topic
                if ob.topic not in subscription.topics:
                    continue
                
                # Prepare event payload
                event_payload = {
                    'topic': ob.topic,
                    'payload': payload,
                    'timestamp': ob.created_at.isoformat(),
                    'event_id': ob.id
                }
                
                # Add HMAC signature
                webhook_headers = create_webhook_headers(event_payload, subscription.secret)
                
                # Deliver to subscription endpoint
                success, status_code, response_data, error_msg = call_http(
                    url=subscription.endpoint,
                    method='POST',
                    json_data=event_payload,
                    timeout_ms=5000,
                    headers=webhook_headers,
                    retries=subscription.retries
                )
                
                if not success or status_code not in [200, 201, 202]:
                    error_msg = error_msg or f"HTTP {status_code}: {response_data}"
                    if subscription.dead_letter:
                        DeadLetter.objects.create(
                            kind='subscription',
                            target=subscription.endpoint,
                            payload_json=event_payload,
                            last_error=error_msg,
                            retry_count=0
                        )
                    print(f"Subscription {subscription.name} failed: {error_msg}")
                    
        except Exception as e:
            print(f"Event subscription error: {str(e)}")
            
        ob.published = True
        ob.save()
    return Response({"status":"ok","processed_outbox":created})

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def notifications_list(request):
    qs = Notification.objects.order_by('-id')[:100]
    return Response([{"id":n.id,"channel":n.channel,"message":n.message,"status":n.status,"created_at":n.created_at} for n in qs])

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def tasks_list(request):
    qs = Task.objects.order_by('-id')[:100]
    return Response([{"id":t.id,"team":t.team,"summary":t.summary,"details":t.details,"due_at":t.due_at,"status":t.status,"created_at":t.created_at} for t in qs])