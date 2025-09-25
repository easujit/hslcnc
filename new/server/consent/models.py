"""
Consent Management Models for DPDP and ABDM compliance
"""
import hashlib
import json
from django.db import models
from django.utils import timezone
from core.models import AbstractTenantModel, TenantManager

class Consent(AbstractTenantModel):
    """
    Patient consent records for data processing
    """
    PURPOSE_CHOICES = [
        ('treatment', 'Treatment'),
        ('ops', 'Operations'),
        ('research', 'Research'),
        ('analytics', 'Analytics'),
        ('marketing', 'Marketing'),
        ('emergency', 'Emergency'),
    ]
    
    STATUS_CHOICES = [
        ('granted', 'Granted'),
        ('revoked', 'Revoked'),
        ('expired', 'Expired'),
        ('pending', 'Pending'),
    ]
    
    consent_id = models.CharField(max_length=100, unique=True, db_index=True)
    patient_id = models.CharField(max_length=100, db_index=True)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    data_categories = models.JSONField(default=list, help_text="List of data categories covered by this consent")
    date_range_start = models.DateTimeField()
    date_range_end = models.DateTimeField()
    expiry = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='granted')
    notice_lang = models.CharField(max_length=10, default='en')
    withdraw_url = models.URLField(blank=True, null=True)
    abdm_artefact_id = models.CharField(max_length=200, blank=True, null=True, db_index=True)
    
    # Additional DPDP fields
    consent_method = models.CharField(max_length=50, default='digital', help_text="How consent was obtained")
    consent_version = models.CharField(max_length=20, default='1.0')
    legal_basis = models.CharField(max_length=100, default='consent', help_text="Legal basis for processing")
    
    objects = TenantManager()
    
    class Meta:
        unique_together = ('tenant_id', 'consent_id')
        indexes = [
            models.Index(fields=['tenant_id', 'patient_id']),
            models.Index(fields=['tenant_id', 'purpose']),
            models.Index(fields=['tenant_id', 'status']),
            models.Index(fields=['tenant_id', 'expiry']),
        ]
    
    def __str__(self):
        return f"Consent {self.consent_id} - {self.patient_id} ({self.purpose})"
    
    def is_valid(self):
        """Check if consent is currently valid"""
        now = timezone.now()
        return (
            self.status == 'granted' and
            self.date_range_start <= now <= self.date_range_end and
            now <= self.expiry
        )
    
    def covers_data_category(self, category):
        """Check if consent covers a specific data category"""
        return category in self.data_categories
    
    def covers_purpose(self, purpose):
        """Check if consent covers a specific purpose"""
        return self.purpose == purpose or self.purpose == 'treatment'  # Treatment covers all purposes

class ConsentRequest(AbstractTenantModel):
    """
    ABDM consent request state management
    """
    STATUS_CHOICES = [
        ('initiated', 'Initiated'),
        ('pending', 'Pending'),
        ('granted', 'Granted'),
        ('denied', 'Denied'),
        ('expired', 'Expired'),
    ]
    
    request_id = models.CharField(max_length=100, unique=True, db_index=True)
    patient_id = models.CharField(max_length=100, db_index=True)
    purpose = models.CharField(max_length=50, choices=Consent.PURPOSE_CHOICES)
    data_categories = models.JSONField(default=list)
    abdm_request_id = models.CharField(max_length=200, blank=True, null=True)
    abdm_transaction_id = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='initiated')
    consent = models.ForeignKey(Consent, on_delete=models.CASCADE, null=True, blank=True)
    expires_at = models.DateTimeField()
    
    objects = TenantManager()
    
    class Meta:
        indexes = [
            models.Index(fields=['tenant_id', 'patient_id']),
            models.Index(fields=['tenant_id', 'status']),
            models.Index(fields=['tenant_id', 'expires_at']),
        ]
    
    def __str__(self):
        return f"ConsentRequest {self.request_id} - {self.patient_id}"

class AuditEvent(AbstractTenantModel):
    """
    Immutable audit log for all data access/write/share operations
    """
    ACTION_CHOICES = [
        ('read', 'Read'),
        ('write', 'Write'),
        ('share', 'Share'),
        ('export', 'Export'),
        ('delete', 'Delete'),
    ]
    
    DECISION_CHOICES = [
        ('ALLOW', 'Allow'),
        ('DENY', 'Deny'),
    ]
    
    # Immutable fields
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    request_id = models.CharField(max_length=100, db_index=True)
    user_id = models.CharField(max_length=100, db_index=True)
    patient_id = models.CharField(max_length=100, db_index=True)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    resource = models.CharField(max_length=200, help_text="Resource being accessed")
    fields = models.JSONField(default=list, help_text="Fields accessed/modified")
    purpose = models.CharField(max_length=50, choices=Consent.PURPOSE_CHOICES)
    data_categories = models.JSONField(default=list, help_text="Data categories involved")
    consent_id = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    decision = models.CharField(max_length=10, choices=DECISION_CHOICES)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    
    # Hash chain for integrity
    event_hash = models.CharField(max_length=64, unique=True, db_index=True)
    previous_hash = models.CharField(max_length=64, blank=True, null=True, db_index=True)
    
    # Additional context
    reason = models.TextField(blank=True, help_text="Reason for decision")
    metadata = models.JSONField(default=dict, help_text="Additional context")
    
    objects = TenantManager()
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['tenant_id', 'patient_id', 'timestamp']),
            models.Index(fields=['tenant_id', 'action', 'timestamp']),
            models.Index(fields=['tenant_id', 'decision', 'timestamp']),
            models.Index(fields=['tenant_id', 'consent_id']),
        ]
    
    def __str__(self):
        return f"AuditEvent {self.action} - {self.patient_id} ({self.decision})"
    
    def save(self, *args, **kwargs):
        """Generate hash chain on save"""
        if not self.event_hash:
            # Set timestamp if not set
            if not self.timestamp:
                from django.utils import timezone
                self.timestamp = timezone.now()
            self.event_hash = self._generate_hash()
        super().save(*args, **kwargs)
    
    def _generate_hash(self):
        """Generate SHA256 hash for this event"""
        # Use current time if timestamp is not set
        timestamp = self.timestamp or timezone.now()
        
        payload = {
            'timestamp': timestamp.isoformat(),
            'request_id': self.request_id,
            'user_id': self.user_id,
            'patient_id': self.patient_id,
            'action': self.action,
            'resource': self.resource,
            'fields': self.fields,
            'purpose': self.purpose,
            'data_categories': self.data_categories,
            'consent_id': self.consent_id,
            'decision': self.decision,
            'ip_address': str(self.ip_address),
            'metadata': self.metadata,
        }
        
        payload_str = json.dumps(payload, sort_keys=True)
        if self.previous_hash:
            payload_str = self.previous_hash + payload_str
        
        return hashlib.sha256(payload_str.encode()).hexdigest()
    
    @classmethod
    def get_latest_hash(cls, tenant_id):
        """Get the latest event hash for hash chain continuity"""
        latest = cls.objects.filter(tenant_id=tenant_id).order_by('-timestamp').first()
        return latest.event_hash if latest else None