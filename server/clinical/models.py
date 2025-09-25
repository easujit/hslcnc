from django.db import models
import os
from core.models import AbstractTenantModel, TenantManager

def upload_to_documents(instance, filename):
    return f"documents/{instance.tenant_id}/{instance.patient.external_id}/{filename}"

class Patient(AbstractTenantModel):
    external_id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    custom_data = models.JSONField(default=dict, blank=True)
    
    objects = TenantManager()

    class Meta:
        unique_together = ('tenant_id', 'external_id')
        indexes = [
            models.Index(fields=['tenant_id', 'external_id']),
            models.Index(fields=['tenant_id', 'created_at']),
        ]

    def __str__(self):
        return f"{self.external_id} - {self.name}"

class Visit(AbstractTenantModel):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending_consent', 'Pending Consent'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_type = models.CharField(max_length=100, default='OPD')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    custom_data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = TenantManager()

    class Meta:
        indexes = [
            models.Index(fields=['tenant_id', 'created_at']),
            models.Index(fields=['tenant_id', 'patient']),
            models.Index(fields=['tenant_id', 'status']),
        ]

    def __str__(self):
        return f"Visit {self.id} - {self.patient.name} ({self.status})"

class Document(AbstractTenantModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, null=True, blank=True)
    document_type = models.CharField(max_length=50, default='birth_certificate')
    file = models.FileField(upload_to=upload_to_documents)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(default=0)
    
    objects = TenantManager()

    class Meta:
        indexes = [
            models.Index(fields=['tenant_id', 'patient']),
            models.Index(fields=['tenant_id', 'created_at']),
        ]
    
    def __str__(self):
        return f"{self.patient.name} - {self.document_type}"
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)