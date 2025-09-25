"""
Multi-tenancy support with thread-local tenant context
"""
import threading
from typing import Optional
from django.conf import settings

# Thread-local storage for tenant context
_thread_locals = threading.local()

def set_current_tenant(tenant_id: str) -> None:
    """
    Set the current tenant for this thread
    
    Args:
        tenant_id: The tenant identifier
    """
    _thread_locals.tenant_id = tenant_id

def get_current_tenant() -> Optional[str]:
    """
    Get the current tenant for this thread
    
    Returns:
        The current tenant ID or None if not set
    """
    return getattr(_thread_locals, 'tenant_id', None)

def clear_current_tenant() -> None:
    """
    Clear the current tenant for this thread
    """
    if hasattr(_thread_locals, 'tenant_id'):
        delattr(_thread_locals, 'tenant_id')

def tenant_cache_key(*parts: str) -> str:
    """
    Generate a cache key with tenant prefix
    
    Args:
        *parts: Parts of the cache key
        
    Returns:
        Tenant-prefixed cache key
    """
    tenant_id = get_current_tenant() or 'default'
    return f"t:{tenant_id}:{':'.join(parts)}"

def require_tenant() -> str:
    """
    Get current tenant or raise exception if not set
    
    Returns:
        The current tenant ID
        
    Raises:
        ValueError: If no tenant is set
    """
    tenant_id = get_current_tenant()
    if not tenant_id:
        raise ValueError("No tenant context available")
    return tenant_id

def is_tenant_aware() -> bool:
    """
    Check if tenant context is available
    
    Returns:
        True if tenant is set, False otherwise
    """
    return get_current_tenant() is not None
