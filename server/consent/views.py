"""
Consent Management Views
"""
import uuid
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import transaction
from core.tenant import get_current_tenant, require_tenant
from .models import Consent, ConsentRequest, AuditEvent
from .serializers import (
    ConsentSerializer, ConsentRequestSerializer, AuditEventSerializer,
    ConsentCheckSerializer, ConsentCheckResponseSerializer,
    ConsentCreateSerializer, ConsentRevokeSerializer
)
from .abdm_connector import abdm_connector

class ConsentViewSet(viewsets.ModelViewSet):
    """ViewSet for Consent management"""
    queryset = Consent.objects.all()
    serializer_class = ConsentSerializer
    lookup_field = 'consent_id'
    
    def get_queryset(self):
        """Filter consents by tenant and patient if specified"""
        queryset = Consent.objects.all()
        
        # Filter by patient if specified
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        return queryset.order_by('-created_at')
    
    def create(self, request, *args, **kwargs):
        """Create new consent"""
        serializer = ConsentCreateSerializer(data=request.data)
        if serializer.is_valid():
            consent = serializer.save(tenant_id=get_current_tenant())
            return Response(ConsentSerializer(consent).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConsentRequestViewSet(viewsets.ModelViewSet):
    """ViewSet for ConsentRequest management"""
    queryset = ConsentRequest.objects.all()
    serializer_class = ConsentRequestSerializer
    
    def get_queryset(self):
        """Filter consent requests by tenant and patient if specified"""
        queryset = ConsentRequest.objects.all()
        
        # Filter by patient if specified
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        return queryset.order_by('-created_at')

class AuditEventViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for AuditEvent (read-only)"""
    queryset = AuditEvent.objects.all()
    serializer_class = AuditEventSerializer
    
    def get_queryset(self):
        """Filter audit events by tenant and patient if specified"""
        queryset = AuditEvent.objects.all()
        
        # Filter by patient if specified
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        
        # Filter by action if specified
        action = self.request.query_params.get('action')
        if action:
            queryset = queryset.filter(action=action)
        
        return queryset.order_by('-timestamp')

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def check_consent(request):
    """
    Check if consent exists for given patient, purpose, and data categories
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    serializer = ConsentCheckSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    data = serializer.validated_data
    patient_id = data['patient_id']
    purpose = data['purpose']
    data_categories = data['data_categories']
    action = data.get('action', 'read')
    resource = data.get('resource', '')
    fields = data.get('fields', [])
    
    # Find valid consent
    from django.db import models
    consent = Consent.objects.filter(
        tenant_id=tenant_id,
        patient_id=patient_id,
        purpose=purpose,
        status='granted'
    ).filter(
        models.Q(date_range_start__lte=timezone.now()) &
        models.Q(date_range_end__gte=timezone.now()) &
        models.Q(expiry__gte=timezone.now())
    ).first()
    
    if not consent:
        # Check if treatment consent covers this purpose
        consent = Consent.objects.filter(
            tenant_id=tenant_id,
            patient_id=patient_id,
            purpose='treatment',
            status='granted'
        ).filter(
            models.Q(date_range_start__lte=timezone.now()) &
            models.Q(date_range_end__gte=timezone.now()) &
            models.Q(expiry__gte=timezone.now())
        ).first()
    
    if not consent:
        # Log audit event
        _log_audit_event(
            tenant_id=tenant_id,
            request_id=str(uuid.uuid4()),
            user_id=request.META.get('HTTP_X_USER_ID', 'unknown'),
            patient_id=patient_id,
            action=action,
            resource=resource,
            fields=fields,
            purpose=purpose,
            data_categories=data_categories,
            consent_id=None,
            decision='DENY',
            ip_address=_get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            reason="No valid consent found"
        )
        
        return Response(ConsentCheckResponseSerializer({
            'allow': False,
            'consent_id': None,
            'reason': 'No valid consent found for the specified purpose and data categories',
            'required_consent': {
                'purpose': purpose,
                'data_categories': data_categories,
                'patient_id': patient_id
            }
        }).data)
    
    # Check if consent covers all required data categories
    missing_categories = [cat for cat in data_categories if not consent.covers_data_category(cat)]
    
    if missing_categories:
        # Log audit event
        _log_audit_event(
            tenant_id=tenant_id,
            request_id=str(uuid.uuid4()),
            user_id=request.META.get('HTTP_X_USER_ID', 'unknown'),
            patient_id=patient_id,
            action=action,
            resource=resource,
            fields=fields,
            purpose=purpose,
            data_categories=data_categories,
            consent_id=consent.consent_id,
            decision='DENY',
            ip_address=_get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            reason=f"Consent does not cover data categories: {missing_categories}"
        )
        
        return Response(ConsentCheckResponseSerializer({
            'allow': False,
            'consent_id': consent.consent_id,
            'reason': f'Consent does not cover data categories: {missing_categories}',
            'required_consent': {
                'purpose': purpose,
                'data_categories': data_categories,
                'patient_id': patient_id
            }
        }).data)
    
    # Log successful audit event
    _log_audit_event(
        tenant_id=tenant_id,
        request_id=str(uuid.uuid4()),
        user_id=request.META.get('HTTP_X_USER_ID', 'unknown'),
        patient_id=patient_id,
        action=action,
        resource=resource,
        fields=fields,
        purpose=purpose,
        data_categories=data_categories,
        consent_id=consent.consent_id,
        decision='ALLOW',
        ip_address=_get_client_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        reason="Valid consent found"
    )
    
    return Response(ConsentCheckResponseSerializer({
        'allow': True,
        'consent_id': consent.consent_id,
        'reason': 'Valid consent found',
        'required_consent': None
    }).data)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def revoke_consent(request, consent_id):
    """
    Revoke a consent
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    try:
        consent = Consent.objects.get(tenant_id=tenant_id, consent_id=consent_id)
    except Consent.DoesNotExist:
        return Response({"error": "Consent not found"}, status=404)
    
    serializer = ConsentRevokeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    
    data = serializer.validated_data
    consent.status = 'revoked'
    consent.save()
    
    # Log audit event
    _log_audit_event(
        tenant_id=tenant_id,
        request_id=str(uuid.uuid4()),
        user_id=request.META.get('HTTP_X_USER_ID', 'unknown'),
        patient_id=consent.patient_id,
        action='write',
        resource=f'consent/{consent_id}',
        fields=['status'],
        purpose=consent.purpose,
        data_categories=consent.data_categories,
        consent_id=consent_id,
        decision='ALLOW',
        ip_address=_get_client_ip(request),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        reason=data.get('reason', 'Consent revoked')
    )
    
    return Response({"status": "success", "message": "Consent revoked"})

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def patient_consents(request, patient_id):
    """
    Get all consents for a patient
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    consents = Consent.objects.filter(
        tenant_id=tenant_id,
        patient_id=patient_id
    ).order_by('-created_at')
    
    serializer = ConsentSerializer(consents, many=True)
    return Response(serializer.data)

def _log_audit_event(tenant_id, request_id, user_id, patient_id, action, resource, 
                    fields, purpose, data_categories, consent_id, decision, 
                    ip_address, user_agent, reason):
    """Helper function to log audit events"""
    from django.db import models
    
    # Get previous hash for chain continuity
    previous_hash = AuditEvent.get_latest_hash(tenant_id)
    
    audit_event = AuditEvent.objects.create(
        tenant_id=tenant_id,
        request_id=request_id,
        user_id=user_id,
        patient_id=patient_id,
        action=action,
        resource=resource,
        fields=fields,
        purpose=purpose,
        data_categories=data_categories,
        consent_id=consent_id,
        decision=decision,
        ip_address=ip_address,
        user_agent=user_agent,
        reason=reason,
        previous_hash=previous_hash
    )
    
    return audit_event

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def abdm_request_consent(request):
    """
    Create ABDM consent request
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    data = request.data
    patient_id = data.get('patient_id')
    purpose = data.get('purpose')
    data_categories = data.get('data_categories', [])
    
    if not all([patient_id, purpose]):
        return Response({"error": "patient_id and purpose are required"}, status=400)
    
    try:
        consent_request = abdm_connector.request_consent(
            patient_id=patient_id,
            purpose=purpose,
            data_categories=data_categories,
            tenant_id=tenant_id
        )
        
        serializer = ConsentRequestSerializer(consent_request)
        return Response(serializer.data, status=201)
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def abdm_notify(request):
    """
    Handle ABDM consent response notification
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    data = request.data
    request_id = data.get('request_id')
    status = data.get('status')
    artefact_id = data.get('artefact_id')
    
    if not all([request_id, status]):
        return Response({"error": "request_id and status are required"}, status=400)
    
    try:
        consent_request = abdm_connector.notify_consent_response(
            request_id=request_id,
            status=status,
            artefact_id=artefact_id
        )
        
        serializer = ConsentRequestSerializer(consent_request)
        return Response(serializer.data)
    
    except ValueError as e:
        return Response({"error": str(e)}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def abdm_fetch_artefact(request):
    """
    Fetch consent artefact from ABDM
    """
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    data = request.data
    artefact_id = data.get('artefact_id')
    
    if not artefact_id:
        return Response({"error": "artefact_id is required"}, status=400)
    
    try:
        artefact_data = abdm_connector.fetch_artefact(artefact_id)
        return Response(artefact_data)
    
    except Exception as e:
        return Response({"error": str(e)}, status=500)

def _get_client_ip(request):
    """Get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip