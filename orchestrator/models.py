
from django.db import models
class Notification(models.Model):
    channel = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=20, default="queued")
    created_at = models.DateTimeField(auto_now_add=True)
class Task(models.Model):
    team = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    details = models.TextField(blank=True, default="")
    due_at = models.DateTimeField()
    status = models.CharField(max_length=20, default="open")
    created_at = models.DateTimeField(auto_now_add=True)
