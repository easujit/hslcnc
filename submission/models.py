
from django.db import models
class Submission(models.Model):
    idempotency_key = models.CharField(max_length=64, unique=True)
    form_name = models.CharField(max_length=100)
    payload = models.JSONField(default=dict)
    status = models.CharField(max_length=20, default="accepted")
    errors = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
class Outbox(models.Model):
    topic = models.CharField(max_length=100)
    payload = models.JSONField(default=dict)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
