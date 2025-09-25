"""
DRF mixins for tenant-aware views
"""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .tenant import get_current_tenant, require_tenant

class TenantScopedViewSetMixin:
    """
    Mixin for ViewSets that automatically scope to current tenant
    """
    
    def get_queryset(self):
        """Filter queryset by current tenant"""
        queryset = super().get_queryset()
        tenant_id = get_current_tenant()
        
        if tenant_id and hasattr(queryset.model, 'tenant_id'):
            return queryset.filter(tenant_id=tenant_id)
        
        return queryset
    
    def perform_create(self, serializer):
        """Set tenant_id when creating objects"""
        tenant_id = require_tenant()
        serializer.save(tenant_id=tenant_id)
    
    def perform_update(self, serializer):
        """Ensure tenant_id is preserved during updates"""
        tenant_id = require_tenant()
        serializer.save(tenant_id=tenant_id)
    
    def list(self, request, *args, **kwargs):
        """List objects for current tenant"""
        try:
            require_tenant()  # Ensure tenant context exists
            return super().list(request, *args, **kwargs)
        except ValueError:
            return Response(
                {"error": "Tenant context required"},
                status=status.HTTP_401_UNAUTHORIZED
            )
    
    def retrieve(self, request, *args, **kwargs):
        """Retrieve object for current tenant"""
        try:
            require_tenant()  # Ensure tenant context exists
            return super().retrieve(request, *args, **kwargs)
        except ValueError:
            return Response(
                {"error": "Tenant context required"},
                status=status.HTTP_401_UNAUTHORIZED
            )

class TenantAwareAPIViewMixin:
    """
    Mixin for API views that need tenant awareness
    """
    
    def dispatch(self, request, *args, **kwargs):
        """Ensure tenant context exists before processing request"""
        try:
            require_tenant()
            return super().dispatch(request, *args, **kwargs)
        except ValueError:
            return Response(
                {"error": "Tenant context required"},
                status=status.HTTP_401_UNAUTHORIZED
            )
