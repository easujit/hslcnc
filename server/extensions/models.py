from django.db import models
from django.utils import timezone
import json

class ExtensionFunction(models.Model):
    """Runtime extension functions for compute and validation"""
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=[
        ('runtime.compute', 'Runtime Compute'),
        ('runtime.validate', 'Runtime Validate')
    ])
    match_json = models.JSONField(default=dict, help_text="Matching criteria, e.g. {'form': 'visit_opd'}")
    invoke_json = models.JSONField(default=dict, help_text="Invocation config: {method, url, timeout_ms, headers}")
    secret = models.CharField(max_length=200, help_text="HMAC secret for signing requests")
    retries = models.IntegerField(default=3)
    cache_ttl_s = models.IntegerField(null=True, blank=True, help_text="Cache TTL in seconds, null for no cache")
    is_blocking = models.BooleanField(default=False, help_text="If True, failures block the main flow")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.type})"

class ExtensionHook(models.Model):
    """Submission hooks for pre/post processing"""
    name = models.CharField(max_length=100, unique=True)
    phase = models.CharField(max_length=20, choices=[
        ('submission.pre', 'Pre Submission'),
        ('submission.post', 'Post Submission')
    ])
    match_json = models.JSONField(default=dict, help_text="Matching criteria")
    invoke_json = models.JSONField(default=dict, help_text="Invocation config")
    secret = models.CharField(max_length=200, help_text="HMAC secret for signing requests")
    retries = models.IntegerField(default=3)
    is_blocking = models.BooleanField(default=False, help_text="If True, failures block submission")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.phase})"

class ExtSubscription(models.Model):
    """Event subscriptions for external systems"""
    name = models.CharField(max_length=100, unique=True)
    topics = models.JSONField(default=list, help_text="List of topics to subscribe to")
    endpoint = models.URLField(max_length=500)
    secret = models.CharField(max_length=200, help_text="HMAC secret for signing requests")
    retries = models.IntegerField(default=3)
    dead_letter = models.BooleanField(default=True, help_text="Send failed messages to dead letter queue")
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} -> {self.endpoint}"

class DeadLetter(models.Model):
    """Dead letter queue for failed messages"""
    kind = models.CharField(max_length=50, choices=[
        ('hook', 'Extension Hook'),
        ('subscription', 'Event Subscription'),
        ('webhook', 'Workflow Webhook')
    ])
    target = models.CharField(max_length=200, help_text="Target URL or identifier")
    payload_json = models.JSONField(default=dict)
    last_error = models.TextField(blank=True)
    retry_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_attempt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.kind}: {self.target} (retry {self.retry_count})"

    class Meta:
        ordering = ['-created_at']