"""
Rate limiting implementation using token bucket algorithm
"""
import time
import threading
from typing import Dict, Tuple
from django.core.cache import cache
from django.conf import settings
from .models import TenantQuota, TenantUsage

class TokenBucket:
    """
    Token bucket rate limiter
    """
    
    def __init__(self, capacity: int, refill_rate: float):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_refill = time.time()
        self._lock = threading.Lock()
    
    def consume(self, tokens: int = 1) -> bool:
        """
        Try to consume tokens from the bucket
        
        Args:
            tokens: Number of tokens to consume
            
        Returns:
            True if tokens were consumed, False if not enough tokens
        """
        with self._lock:
            now = time.time()
            time_passed = now - self.last_refill
            
            # Refill tokens based on time passed
            self.tokens = min(
                self.capacity,
                self.tokens + (time_passed * self.refill_rate)
            )
            self.last_refill = now
            
            # Check if we have enough tokens
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

class RateLimiter:
    """
    Rate limiter for tenants
    """
    
    def __init__(self):
        self._buckets: Dict[str, TokenBucket] = {}
        self._lock = threading.Lock()
    
    def _get_bucket_key(self, tenant_id: str, metric: str) -> str:
        """Generate cache key for bucket"""
        return f"rate_limit:{tenant_id}:{metric}"
    
    def _get_bucket(self, tenant_id: str, metric: str, rate_per_minute: int, burst: int) -> TokenBucket:
        """Get or create token bucket for tenant and metric"""
        bucket_key = self._get_bucket_key(tenant_id, metric)
        
        with self._lock:
            if bucket_key not in self._buckets:
                # Convert rate per minute to rate per second
                refill_rate = rate_per_minute / 60.0
                self._buckets[bucket_key] = TokenBucket(burst, refill_rate)
            
            return self._buckets[bucket_key]
    
    def is_allowed(self, tenant_id: str, metric: str, rate_per_minute: int = 60, burst: int = 30) -> bool:
        """
        Check if request is allowed for tenant and metric
        
        Args:
            tenant_id: Tenant identifier
            metric: Metric being tracked
            rate_per_minute: Rate limit per minute
            burst: Burst capacity
            
        Returns:
            True if allowed, False if rate limited
        """
        bucket = self._get_bucket(tenant_id, metric, rate_per_minute, burst)
        return bucket.consume()
    
    def get_quota_limits(self, tenant_id: str) -> Dict[str, Dict[str, int]]:
        """
        Get quota limits for tenant
        
        Args:
            tenant_id: Tenant identifier
            
        Returns:
            Dictionary of metric limits
        """
        try:
            quota = TenantQuota.objects.get(tenant_id=tenant_id)
            return quota.limits_json
        except TenantQuota.DoesNotExist:
            return {}
    
    def check_quota(self, tenant_id: str, metric: str) -> Tuple[bool, Dict]:
        """
        Check if tenant is within quota limits
        
        Args:
            tenant_id: Tenant identifier
            metric: Metric being checked
            
        Returns:
            Tuple of (is_allowed, quota_info)
        """
        limits = self.get_quota_limits(tenant_id)
        
        if metric not in limits:
            return True, {"message": "No quota limits defined"}
        
        metric_config = limits[metric]
        rate_per_minute = metric_config.get('rate_per_minute', 60)
        burst = metric_config.get('burst', 30)
        
        # Check token bucket
        is_allowed = self.is_allowed(tenant_id, metric, rate_per_minute, burst)
        
        # Track usage in database
        if is_allowed:
            usage = TenantUsage.get_current_usage(tenant_id, metric, 'minute')
            usage.increment()
        
        quota_info = {
            "metric": metric,
            "rate_per_minute": rate_per_minute,
            "burst": burst,
            "is_allowed": is_allowed
        }
        
        return is_allowed, quota_info

# Global rate limiter instance
rate_limiter = RateLimiter()

def tenant_limited(metric: str = "request", rate: int = 60, burst: int = 30):
    """
    Decorator for rate limiting views
    
    Args:
        metric: Metric name for tracking
        rate: Rate per minute
        burst: Burst capacity
    """
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            from core.tenant import get_current_tenant
            
            tenant_id = get_current_tenant()
            if not tenant_id:
                from rest_framework.response import Response
                return Response(
                    {"error": "Tenant context required"},
                    status=401
                )
            
            is_allowed, quota_info = rate_limiter.check_quota(tenant_id, metric)
            
            if not is_allowed:
                from rest_framework.response import Response
                return Response(
                    {
                        "error": "rate limit",
                        "message": f"Rate limit exceeded for {metric}",
                        "quota_info": quota_info
                    },
                    status=429
                )
            
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
