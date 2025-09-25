"""
Consent Management Utilities
"""
import json
from typing import List, Dict, Any

def get_client_ip(request):
    """Get client IP address from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def extract_data_categories_from_request(request) -> List[str]:
    """
    Extract data categories from request based on form configuration
    """
    # Try to get form configuration from request context
    form_config = getattr(request, 'form_config', None)
    if form_config and 'fields' in form_config:
        categories = []
        for field in form_config['fields']:
            if 'data_category' in field:
                categories.append(field['data_category'])
        return list(set(categories))
    
    # Default categories based on endpoint
    path = request.path
    if '/api/clinical/' in path:
        return ['demographics', 'vitals', 'labs', 'diagnosis']
    elif '/api/submit/' in path:
        return ['demographics', 'vitals', 'labs']
    else:
        return ['demographics']

def check_consent_for_request(request, patient_id: str, purpose: str, data_categories: List[str]) -> Dict[str, Any]:
    """
    Check consent for a request
    
    Args:
        request: Django request object
        patient_id: Patient identifier
        purpose: Purpose of data access
        data_categories: List of data categories
        
    Returns:
        Dictionary with consent check result
    """
    from .models import Consent
    from django.utils import timezone
    from django.db import models
    from core.tenant import get_current_tenant
    
    tenant_id = get_current_tenant()
    if not tenant_id:
        return {
            'allow': False,
            'reason': 'No tenant context',
            'consent_id': None
        }
    
    # Find valid consent (order by creation date to get the most recent)
    consent = Consent.objects.filter(
        tenant_id=tenant_id,
        patient_id=patient_id,
        purpose=purpose,
        status='granted'
    ).filter(
        models.Q(date_range_start__lte=timezone.now()) &
        models.Q(date_range_end__gte=timezone.now()) &
        models.Q(expiry__gte=timezone.now())
    ).order_by('-created_at').first()
    
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
        ).order_by('-created_at').first()
    
    if not consent:
        return {
            'allow': False,
            'reason': 'No valid consent found',
            'consent_id': None
        }
    
    # Check if consent covers all required data categories
    missing_categories = [cat for cat in data_categories if not consent.covers_data_category(cat)]
    
    if missing_categories:
        return {
            'allow': False,
            'reason': f'Consent does not cover data categories: {missing_categories}',
            'consent_id': consent.consent_id
        }
    
    return {
        'allow': True,
        'reason': 'Valid consent found',
        'consent_id': consent.consent_id
    }

def log_audit_event(tenant_id: str, request_id: str, user_id: str, patient_id: str,
                   action: str, resource: str, fields: List[str], purpose: str,
                   data_categories: List[str], consent_id: str, decision: str,
                   ip_address: str, user_agent: str, reason: str):
    """
    Log audit event with hash chain continuity
    
    Args:
        tenant_id: Tenant identifier
        request_id: Request identifier
        user_id: User identifier
        patient_id: Patient identifier
        action: Action performed
        resource: Resource accessed
        fields: Fields accessed/modified
        purpose: Purpose of data access
        data_categories: Data categories involved
        consent_id: Consent identifier
        decision: Decision (ALLOW/DENY)
        ip_address: Client IP address
        user_agent: User agent string
        reason: Reason for decision
    """
    from .models import AuditEvent
    
    # Get previous hash for chain continuity
    previous_hash = AuditEvent.get_latest_hash(tenant_id)
    
    # Create audit event
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
