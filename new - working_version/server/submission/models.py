from django.db import models

class Submission(models.Model):
    idempotency_key = models.CharField(max_length=200, unique=True)
    form_name = models.CharField(max_length=100)
    payload_json = models.JSONField(default=dict)
    status = models.CharField(max_length=50, default='received')
    errors_json = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.form_name} - {self.idempotency_key}"