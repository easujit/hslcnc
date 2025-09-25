from django.db import models

class Outbox(models.Model):
    topic = models.CharField(max_length=100)
    payload_json = models.JSONField(default=dict)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    channel = models.CharField(max_length=50, default='inapp')
    message = models.TextField()
    status = models.CharField(max_length=50, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    team = models.CharField(max_length=100, default='care')
    summary = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    due_at = models.DateTimeField()
    status = models.CharField(max_length=50, default='open')
    created_at = models.DateTimeField(auto_now_add=True)