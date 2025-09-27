"""
Multi-tenancy middleware for tenant context management
"""
import json
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .tenant import set_current_tenant, clear_current_tenant, get_current_tenant

class TenantContextMiddleware(MiddlewareMixin):
    """
    Middleware to extract tenant context from JWT or headers
    """
    
    def process_request(self, request):
        """Extract tenant from JWT or headers and set thread-local context"""
        # Clear any existing tenant context
        clear_current_tenant()
        
        # Skip tenant context for admin interface and static files
        if request.path.startswith('/admin/') or request.path.startswith('/static/') or request.path.startswith('/media/'):
            return None
        
        tenant_id = None
        
        # Try to extract from JWT token first
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                # Decode JWT token (in production, use proper secret key)
                payload = jwt.decode(token, options={"verify_signature": False})
                tenant_id = payload.get('tenant_id')
            except (jwt.InvalidTokenError, jwt.DecodeError):
                pass
        
        # Fallback to X-Tenant header (for DEBUG mode)
        if not tenant_id and settings.DEBUG:
            tenant_id = request.META.get('HTTP_X_TENANT')

        # If no tenant found, use default tenant for testing
        if not tenant_id:
            if settings.DEBUG:
                tenant_id = "test-tenant"
            else:
                return JsonResponse(
                    {"error": "no tenant", "message": "Tenant context required"},
                    status=401
                )
        
        # Set tenant context
        set_current_tenant(tenant_id)
        
        # Also set in request for easy access
        request.tenant_id = tenant_id
        
        return None
    
    def process_response(self, request, response):
        """Clear tenant context after request"""
        clear_current_tenant()
        return response
    
    def process_exception(self, request, exception):
        """Clear tenant context on exception"""
        clear_current_tenant()
        return None
