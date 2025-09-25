from django.db import models
import os

def upload_to_documents(instance, filename):
    return f"documents/{instance.patient.external_id}/{filename}"

class Patient(models.Model):
    external_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    custom_data = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.external_id} - {self.name}"

class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_type = models.CharField(max_length=100, default='OPD')
    custom_data = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit {self.id} - {self.patient.name}"

class Document(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE, null=True, blank=True)
    document_type = models.CharField(max_length=50, default='birth_certificate')
    file = models.FileField(upload_to=upload_to_documents)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.patient.name} - {self.document_type}"
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)