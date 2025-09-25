from django.db import models
from django.utils import timezone
import json
from core.models import TenantManager

class PolicyRule(models.Model):
    """Policy rules for RBAC with field, record, and workflow-level permissions"""
    
    RESOURCE_TYPES = [
        ('field', 'Field'),
        ('record', 'Record'),
        ('workflow', 'Workflow'),
        ('workflow_step', 'Workflow Step'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    EFFECT_CHOICES = [
        ('allow', 'Allow'),
        ('deny', 'Deny'),
    ]
    
    tenant_id = models.CharField(max_length=100, help_text="Tenant identifier")
    version = models.IntegerField(default=1, help_text="Policy version")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    action = models.CharField(max_length=50, help_text="Action (read, write, execute, publish, etc.)")
    selector = models.JSONField(default=dict, help_text="Resource selector criteria")
    effect = models.CharField(max_length=10, choices=EFFECT_CHOICES)
    condition = models.TextField(null=True, blank=True, help_text="Optional condition expression")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = TenantManager()
    
    class Meta:
        unique_together = ['tenant_id', 'version', 'status']
        ordering = ['-version', '-created_at']
    
    def __str__(self):
        return f"{self.tenant_id} v{self.version} {self.resource_type}:{self.action} -> {self.effect}"
    
    def to_dict(self):
        """Convert to dictionary for caching"""
        return {
            'id': self.id,
            'tenant_id': self.tenant_id,
            'resource_type': self.resource_type,
            'action': self.action,
            'selector': self.selector,
            'effect': self.effect,
            'condition': self.condition,
        }