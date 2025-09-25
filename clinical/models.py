
from django.db import models
class Patient(models.Model):
    external_id = models.CharField(max_length=36, unique=True)
    name = models.CharField(max_length=200, blank=True, default="")
    custom_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
class Visit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="visits")
    visit_type = models.CharField(max_length=50, default="OPD")
    custom_data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
