from django.utils.deprecation import MiddlewareMixin
import json

class ClaimsMiddleware(MiddlewareMixin):
    """
    Middleware to extract user claims from JWT or headers
    """
    
    def process_request(self, request):
        """Extract claims from headers and attach to request"""
        # Initialize user claims
        request.user_claims = {
            'tenant_id': None,
            'roles': [],
            'departments': [],
            'user_id': None,
            'username': None,
        }
        
        # Extract from headers
        tenant_id = request.META.get('HTTP_X_TENANT')
        if tenant_id:
            request.user_claims['tenant_id'] = tenant_id
        
        # Extract roles
        roles_header = request.META.get('HTTP_X_ROLES')
        if roles_header:
            request.user_claims['roles'] = [role.strip() for role in roles_header.split(',')]
        
        # Extract departments
        departments_header = request.META.get('HTTP_X_DEPARTMENTS')
        if departments_header:
            request.user_claims['departments'] = [dept.strip() for dept in departments_header.split(',')]
        
        # Extract user ID and username (could be from JWT in real implementation)
        user_id = request.META.get('HTTP_X_USER_ID')
        if user_id:
            request.user_claims['user_id'] = user_id
        
        username = request.META.get('HTTP_X_USERNAME')
        if username:
            request.user_claims['username'] = username
        
        # For development/testing, set default values if not provided
        if not request.user_claims['tenant_id']:
            request.user_claims['tenant_id'] = 'TENANT_A'  # Default tenant
        
        if not request.user_claims['roles']:
            request.user_claims['roles'] = ['Doctor']  # Default role
        
        if not request.user_claims['departments']:
            request.user_claims['departments'] = ['Endocrinology']  # Default department
        
        if not request.user_claims['user_id']:
            request.user_claims['user_id'] = 'user_001'
        
        if not request.user_claims['username']:
            request.user_claims['username'] = 'test_user'
        
        return None
