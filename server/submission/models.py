from django.db import models
from core.models import AbstractTenantModel, TenantManager

class Submission(AbstractTenantModel):
    idempotency_key = models.CharField(max_length=200)
    form_name = models.CharField(max_length=100)
    payload_json = models.JSONField(default=dict)
    status = models.CharField(max_length=50, default='received')
    errors_json = models.JSONField(default=list, blank=True)
    
    objects = TenantManager()

    class Meta:
        unique_together = ('tenant_id', 'idempotency_key')
        indexes = [
            models.Index(fields=['tenant_id', 'form_name']),
            models.Index(fields=['tenant_id', 'created_at']),
        ]

    def __str__(self):
        return f"{self.form_name} - {self.idempotency_key}"