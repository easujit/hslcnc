from django.db import models

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