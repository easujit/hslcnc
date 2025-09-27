from django.db import models
from core.models import AbstractTenantModel, TenantManager

class Outbox(AbstractTenantModel):
    topic = models.CharField(max_length=100)
    payload_json = models.JSONField(default=dict)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = TenantManager()

    class Meta:
        indexes = [
            models.Index(fields=['tenant_id', 'published']),
            models.Index(fields=['tenant_id', 'created_at']),
        ]

class Notification(AbstractTenantModel):
    channel = models.CharField(max_length=50, default='inapp')
    message = models.TextField()
    status = models.CharField(max_length=50, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = TenantManager()

    class Meta:
        indexes = [
            models.Index(fields=['tenant_id', 'status']),
            models.Index(fields=['tenant_id', 'created_at']),
        ]

class Task(AbstractTenantModel):
    team = models.CharField(max_length=100, default='care')
    summary = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    due_at = models.DateTimeField()
    status = models.CharField(max_length=50, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = TenantManager()

    class Meta:
        indexes = [
            models.Index(fields=['tenant_id', 'status']),
            models.Index(fields=['tenant_id', 'due_at']),
            models.Index(fields=['tenant_id', 'created_at']),
        ]