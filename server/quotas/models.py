"""
Quota and rate limiting models
"""
from django.db import models
from django.utils import timezone
from core.models import AbstractTenantModel
import json

class TenantQuota(AbstractTenantModel):
    """
    Quota limits for tenants
    """
    limits_json = models.JSONField(
        default=dict,
        help_text="JSON object defining quota limits"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['tenant_id']
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Quota for {self.tenant_id}"
    
    def get_limit(self, metric: str, default=None):
        """Get limit for specific metric"""
        return self.limits_json.get(metric, default)
    
    def set_limit(self, metric: str, value):
        """Set limit for specific metric"""
        if not self.limits_json:
            self.limits_json = {}
        self.limits_json[metric] = value
        self.save()

class TenantUsage(AbstractTenantModel):
    """
    Usage tracking for tenants
    """
    PERIOD_CHOICES = [
        ('minute', 'Minute'),
        ('hour', 'Hour'),
        ('day', 'Day'),
        ('month', 'Month'),
    ]
    
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES)
    metric = models.CharField(max_length=50, help_text="Metric being tracked")
    value = models.IntegerField(default=0)
    window_start = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['tenant_id', 'period', 'metric', 'window_start']
        ordering = ['-window_start']
        indexes = [
            models.Index(fields=['tenant_id', 'period', 'metric']),
            models.Index(fields=['tenant_id', 'window_start']),
        ]
    
    def __str__(self):
        return f"{self.tenant_id} {self.metric} {self.period}: {self.value}"
    
    @classmethod
    def get_current_usage(cls, tenant_id: str, metric: str, period: str = 'minute'):
        """Get current usage for tenant and metric"""
        now = timezone.now()
        
        # Calculate window start based on period
        if period == 'minute':
            window_start = now.replace(second=0, microsecond=0)
        elif period == 'hour':
            window_start = now.replace(minute=0, second=0, microsecond=0)
        elif period == 'day':
            window_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif period == 'month':
            window_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            window_start = now
        
        usage, created = cls.objects.get_or_create(
            tenant_id=tenant_id,
            period=period,
            metric=metric,
            window_start=window_start,
            defaults={'value': 0}
        )
        return usage
    
    def increment(self, amount: int = 1):
        """Increment usage by amount"""
        self.value += amount
        self.save(update_fields=['value'])
        return self.value