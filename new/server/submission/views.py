from datetime import datetime, timedelta
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from configurator.models import Config
from runtime_engine.views import evaluate_spec
from clinical.models import Patient, Visit, Document
from .models import Submission
from orchestrator.models import Outbox, Task
from core.tenant import get_current_tenant, require_tenant
from quotas.rate_limiting import tenant_limited
from consent.utils import check_consent_for_request, extract_data_categories_from_request

def _get_effective_rules(form_name):
    tenant_id = get_current_tenant()
    if not tenant_id:
        return {}
    
    obj = Config.objects.filter(
        tenant_id=tenant_id,
        kind='rule', 
        name=form_name, 
        status='published'
    ).order_by('-version').first()
    return obj.spec_json if obj else {}

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@tenant_limited(metric="submit", rate=60, burst=30)
def submit_visit_opd(request):
    idem = request.headers.get('Idempotency-Key') or request.META.get('HTTP_IDEMPOTENCY_KEY')
    if not idem:
        return Response({"error":"Missing Idempotency-Key header"}, status=400)

    existing = Submission.objects.filter(idempotency_key=idem).first()
    if existing and existing.status == 'processed':
        # Return idempotent response
        result = existing.payload_json.get("_result", {})
        return Response({"status":"ok","idempotent":True, **result})

    payload = request.data if isinstance(request.data, dict) else {}
    rules = _get_effective_rules("visit_opd")
    eval_out = evaluate_spec(rules, payload)

    # apply setField
    for sf in eval_out.get("setField", []):
        payload[sf["id"]] = sf["value"]

    # Pre-submission hooks
    try:
        from extensions.models import ExtensionHook
        from extensions.utils import call_http, create_webhook_headers, matches_criteria
        
        pre_hooks = ExtensionHook.objects.filter(
            enabled=True,
            phase='submission.pre'
        )
        
        for hook in pre_hooks:
            if not matches_criteria(payload, hook.match_json):
                continue
                
            invoke_config = hook.invoke_json
            url = invoke_config.get('url')
            method = invoke_config.get('method', 'POST')
            timeout_ms = invoke_config.get('timeout_ms', 5000)
            headers = invoke_config.get('headers', {})
            
            if not url:
                continue
            
            # Prepare payload for pre-hook
            hook_payload = {
                'form_data': payload,
                'hook_phase': hook.phase,
                'hook_name': hook.name,
                'form_name': 'visit_opd'
            }
            
            # Add HMAC signature
            webhook_headers = create_webhook_headers(hook_payload, hook.secret)
            webhook_headers.update(headers)
            
            # Call pre-hook
            success, status_code, response_data, error_msg = call_http(
                url=url,
                method=method,
                json_data=hook_payload,
                timeout_ms=timeout_ms,
                headers=webhook_headers,
                retries=hook.retries
            )
            
            if not success or status_code != 200:
                error_msg = error_msg or f"HTTP {status_code}: {response_data}"
                if hook.is_blocking:
                    sub = existing or Submission.objects.create(idempotency_key=idem, form_name="visit_opd", payload_json=payload)
                    sub.status = 'error'
                    sub.errors_json = [f"Pre-hook {hook.name} failed: {error_msg}"]
                    sub.save()
                    return Response({"error": f"Pre-hook {hook.name} failed: {error_msg}"}, status=400)
                else:
                    # Log warning but continue
                    print(f"Warning: Pre-hook {hook.name} failed (non-blocking): {error_msg}")
            else:
                # Apply any setField results from pre-hook
                ext_setField = response_data.get('setField', [])
                for sf in ext_setField:
                    payload[sf["id"]] = sf["value"]
                    
    except Exception as e:
        print(f"Pre-hook error: {str(e)}")

    sub = existing or Submission.objects.create(idempotency_key=idem, form_name="visit_opd", payload_json=payload)

    # Get effective form configuration for validation
    form_config = Config.objects.filter(kind='form', name='visit_opd', status='published').order_by('-version').first()
    if not form_config:
        sub.status = 'error'
        sub.errors_json = ["Form configuration not found"]
        sub.save()
        return Response({"error":"Form configuration not found"}, status=500)

    # DISABLED FIELD-LEVEL PERMISSIONS - Allow all fields to be written
    # Field-level permissions can be re-enabled later through the Configurator
    print("DEBUG: Field-level permissions disabled - allowing all fields to be written")
    
    # Consent enforcement - check if patient has consent for data submission
    patient_id = payload.get('external_id')
    if patient_id:
        # Check if patient already exists in the system (with tenant context)
        tenant_id = get_current_tenant()
        print(f"DEBUG: Tenant ID for consent check: {tenant_id}")
        
        if not tenant_id:
            print(f"DEBUG: No tenant context for patient {patient_id} - allowing first visit")
            # For new patients without tenant context, allow first visit
            patient_exists = False
        else:
            patient_exists = Patient.objects.filter(tenant_id=tenant_id, external_id=patient_id).exists()
            print(f"DEBUG: Patient {patient_id} exists in tenant {tenant_id}: {patient_exists}")
        
        if patient_exists:
            print(f"DEBUG: Existing patient {patient_id} - checking consent")
            # For existing patients, check consent but don't block - save as draft if missing
            # Extract data categories from form configuration
            if form_config and 'fields' in form_config.spec_json:
                data_categories = []
                for field in form_config.spec_json['fields']:
                    if 'data_category' in field:
                        data_categories.append(field['data_category'])
            else:
                data_categories = extract_data_categories_from_request(request)
            
            # Get purpose from form configuration
            purpose = form_config.spec_json.get('purpose', 'treatment') if form_config else 'treatment'
            
            print(f"DEBUG: Checking consent for existing patient {patient_id}, purpose: {purpose}, categories: {data_categories}")
            
            # Check consent for existing patients
            consent_result = check_consent_for_request(request, patient_id, purpose, data_categories)
            print(f"DEBUG: Consent result: {consent_result}")
            
            if not consent_result['allow']:
                print(f"DEBUG: No consent for existing patient {patient_id} - will save as draft")
                # Don't block - we'll save as draft and set status to pending_consent
                request.consent_missing = True
                request.consent_reason = consent_result['reason']
            else:
                print(f"DEBUG: Valid consent found for existing patient {patient_id}")
                request.consent_missing = False
        else:
            # For new patients, allow first visit but mark as draft since no consent exists yet
            print(f"DEBUG: New patient {patient_id} - allowing first visit but marking as draft (no consent)")
            request.consent_missing = True
            request.consent_reason = "New patient - consent required"
    
    # Validate required fields
    validation_errors = []
    for field in form_config.spec_json.get('fields', []):
        if field.get('required', False):
            field_id = field['id']
            field_value = payload.get(field_id)
            if field_value is None or field_value == '' or field_value == 0:
                validation_errors.append(f"{field['label']} is required")
    
    if validation_errors:
        sub.status = 'error'
        sub.errors_json = validation_errors
        sub.save()
        return Response({"error": validation_errors[0], "errors": validation_errors}, status=400)

    # Upsert patient
    ext = payload.get("external_id")
    name = payload.get("name", "Unknown")
    if not ext:
        sub.status = 'error'
        sub.errors_json = ["external_id required"]
        sub.save()
        return Response({"error":"external_id required"}, status=400)
    
    # Check if this is a new patient (with tenant context)
    tenant_id = get_current_tenant()
    print(f"Tenant ID for patient creation: {tenant_id}")
    if not tenant_id:
        print("No tenant context - using default")
        tenant_id = 'TENANT_A'  # Fallback to default tenant
    
    is_new_patient = not Patient.objects.filter(tenant_id=tenant_id, external_id=ext).exists()
    print(f"Is new patient {ext}: {is_new_patient}")
    
    patient, _ = Patient.objects.get_or_create(
        tenant_id=tenant_id,
        external_id=ext, 
        defaults={"name": name}
    )
    if patient.name != name and name:
        patient.name = name
        patient.save()
    
    # Create consent reminder task for new patients
    if is_new_patient:
        from orchestrator.models import Task
        tenant_id = get_current_tenant()
        
        Task.objects.create(
            tenant_id=tenant_id,
            team="care",
            summary=f"Create Consent for New Patient {ext}",
            details=f"Patient {name} ({ext}) has been registered. Please create appropriate consent for data collection. Data categories needed: demographics, vitals, labs, diagnosis, medications. Purpose: treatment.",
            due_at=now() + timedelta(hours=24),  # Due in 24 hours
            status="open"
        )
        print(f"Created consent reminder task for new patient {ext}")

    # Determine visit status based on consent
    visit_status = 'completed'
    if hasattr(request, 'consent_missing') and request.consent_missing:
        # For new patients, mark as draft; for existing patients, mark as pending_consent
        if is_new_patient:
            visit_status = 'draft'
            print(f"DEBUG: New patient - creating visit with status: {visit_status}")
        else:
            visit_status = 'pending_consent'
            print(f"DEBUG: Existing patient - creating visit with status: {visit_status}")
    else:
        print(f"DEBUG: Valid consent - creating visit with status: {visit_status}")
    
    visit = Visit.objects.create(
        patient=patient, 
        visit_type="OPD", 
        custom_data=payload,
        status=visit_status
    )

    # Check for pediatrics guardian requirements
    age = payload.get("age")
    is_minor = age is not None and int(age) < 18
    guardian_name = payload.get("guardian_name")
    has_birth_certificate = Document.objects.filter(patient=patient, document_type="birth_certificate").exists()
    
    # Validation: Cannot save if age < 18 and no guardian
    if is_minor and not guardian_name:
        sub.status = 'error'
        sub.errors_json = ["Guardian name is required for patients under 18"]
        sub.save()
        return Response({"error": "Guardian name is required for patients under 18"}, status=400)

    # enqueue outbox event
    tenant_id = get_current_tenant()
    outbox_payload = {
        "tenant_id": tenant_id,
        "visit_id": visit.id, 
        "patient_external_id": patient.external_id, 
        "patient_name": patient.name,
        "hba1c": payload.get("hba1c"), 
        "bmi": payload.get("bmi"),
        "age": age,
        "is_minor": is_minor,
        "guardian_name": guardian_name,
        "has_birth_certificate": has_birth_certificate
    }
    
    Outbox.objects.create(tenant_id=tenant_id, topic="visit_saved", payload_json=outbox_payload)

    # Post-submission hooks (best-effort)
    try:
        from extensions.models import ExtensionHook, DeadLetter
        
        post_hooks = ExtensionHook.objects.filter(
            enabled=True,
            phase='submission.post'
        )
        
        for hook in post_hooks:
            if not matches_criteria(payload, hook.match_json):
                continue
                
            invoke_config = hook.invoke_json
            url = invoke_config.get('url')
            method = invoke_config.get('method', 'POST')
            timeout_ms = invoke_config.get('timeout_ms', 5000)
            headers = invoke_config.get('headers', {})
            
            if not url:
                continue
            
            # Prepare payload for post-hook
            hook_payload = {
                'form_data': payload,
                'hook_phase': hook.phase,
                'hook_name': hook.name,
                'form_name': 'visit_opd',
                'visit_id': visit.id,
                'patient_id': patient.id,
                'outbox_payload': outbox_payload
            }
            
            # Add HMAC signature
            webhook_headers = create_webhook_headers(hook_payload, hook.secret)
            webhook_headers.update(headers)
            
            # Call post-hook (best-effort)
            success, status_code, response_data, error_msg = call_http(
                url=url,
                method=method,
                json_data=hook_payload,
                timeout_ms=timeout_ms,
                headers=webhook_headers,
                retries=hook.retries
            )
            
            if not success or status_code != 200:
                error_msg = error_msg or f"HTTP {status_code}: {response_data}"
                # Create dead letter for failed post-hook
                DeadLetter.objects.create(
                    kind='hook',
                    target=url,
                    payload_json=hook_payload,
                    last_error=error_msg,
                    retry_count=0
                )
                print(f"Post-hook {hook.name} failed, added to dead letter queue: {error_msg}")
                
    except Exception as e:
        print(f"Post-hook error: {str(e)}")

    sub.status = 'processed'
    result_data = {
        "visit_id": visit.id, 
        "patient_id": patient.id, 
        "visit_status": visit.status,
        "bmi": payload.get("bmi"),
        "diabetes_educator_required": payload.get("diabetes_educator_required", False),
        "is_minor": is_minor,
        "guardian_required": is_minor and not guardian_name,
        "birth_certificate_required": is_minor and not has_birth_certificate
    }
    
    # Add consent information if missing
    if hasattr(request, 'consent_missing') and request.consent_missing:
        result_data["consent_required"] = True
        result_data["consent_reason"] = getattr(request, 'consent_reason', 'Consent required')
        if is_new_patient:
            result_data["message"] = "New patient visit saved as draft. Please create consent to complete the visit."
        else:
            result_data["message"] = "Visit saved as draft. Please create consent to complete the visit."
    else:
        result_data["consent_required"] = False
        result_data["message"] = "Visit completed successfully."
    
    sub.payload_json["_result"] = result_data
    sub.save()
    return Response({"status":"ok","idempotent":False, **sub.payload_json["_result"]})