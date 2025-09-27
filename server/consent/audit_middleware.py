"""
Audit Middleware for WORM-like logging of all data access
"""
import uuid
import json
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from .models import AuditEvent
from .utils import get_client_ip, extract_data_categories_from_request

class AuditMiddleware(MiddlewareMixin):
    """
    Middleware to automatically log all data access/write/share operations
    """
    
    # Paths to exclude from audit logging
    EXCLUDED_PATHS = [
        '/admin/',
        '/static/',
        '/media/',
        '/favicon.ico',
        '/health/',
        '/metrics/',
    ]
    
    # API endpoints that require audit logging
    AUDIT_ENDPOINTS = [
        '/api/clinical/',
        '/api/submit/',
        '/api/runtime/',
        '/api/config/',
        '/api/consent/',
    ]
    
    def process_request(self, request):
        """Process incoming request"""
        # Skip if path should be excluded
        if any(request.path.startswith(path) for path in self.EXCLUDED_PATHS):
            return None
        
        # Skip if not an audit endpoint
        if not any(request.path.startswith(path) for path in self.AUDIT_ENDPOINTS):
            return None
        
        # Generate request ID for tracking
        request.audit_request_id = str(uuid.uuid4())
        
        # Extract user context
        request.audit_user_id = self._extract_user_id(request)
        request.audit_patient_id = self._extract_patient_id(request)
        request.audit_purpose = self._extract_purpose(request)
        request.audit_data_categories = self._extract_data_categories(request)
        
        return None
    
    def process_response(self, request, response):
        """Process outgoing response"""
        # Skip if no audit context
        if not hasattr(request, 'audit_request_id'):
            return response
        
        # Skip if path should be excluded
        if any(request.path.startswith(path) for path in self.EXCLUDED_PATHS):
            return response
        
        # Skip if not an audit endpoint
        if not any(request.path.startswith(path) for path in self.AUDIT_ENDPOINTS):
            return response
        
        try:
            # Determine action type
            action = self._determine_action(request, response)
            
            # Extract resource and fields
            resource = self._extract_resource(request)
            fields = self._extract_fields(request, response)
            
            # Determine decision
            decision = 'ALLOW' if response.status_code < 400 else 'DENY'
            
            # Log audit event
            self._log_audit_event(
                request=request,
                response=response,
                action=action,
                resource=resource,
                fields=fields,
                decision=decision
            )
        
        except Exception as e:
            # Don't let audit logging break the request
            print(f"Audit logging error: {e}")
        
        return response
    
    def _extract_user_id(self, request):
        """Extract user ID from request"""
        # Try JWT claims first
        user_claims = getattr(request, 'user_claims', {})
        if user_claims.get('user_id'):
            return user_claims['user_id']
        
        # Try headers
        return request.META.get('HTTP_X_USER_ID', 'anonymous')
    
    def _extract_patient_id(self, request):
        """Extract patient ID from request"""
        # Try URL parameters
        if hasattr(request, 'resolver_match') and request.resolver_match:
            kwargs = request.resolver_match.kwargs
            if 'patient_id' in kwargs:
                return kwargs['patient_id']
        
        # Try request body for POST requests
        if request.method == 'POST' and hasattr(request, 'body'):
            try:
                data = json.loads(request.body)
                return data.get('patient_id') or data.get('external_id')
            except:
                pass
        
        # Try query parameters
        return request.GET.get('patient_id')
    
    def _extract_purpose(self, request):
        """Extract purpose from request"""
        # Try headers
        purpose = request.META.get('HTTP_X_PURPOSE')
        if purpose:
            return purpose
        
        # Try request body
        if request.method == 'POST' and hasattr(request, 'body'):
            try:
                data = json.loads(request.body)
                purpose = data.get('purpose')
                if purpose:
                    return purpose
            except:
                pass
        
        # Try to extract from form configuration
        try:
            from configurator.models import Config
            from core.tenant import get_current_tenant
            tenant_id = get_current_tenant()
            if tenant_id:
                form_config = Config.objects.filter(
                    tenant_id=tenant_id,
                    form_type='visit_opd',
                    status='published'
                ).first()
                if form_config and 'purpose' in form_config.spec_json:
                    return form_config.spec_json['purpose']
        except:
            pass
        
        # Default to treatment
        return 'treatment'
    
    def _extract_data_categories(self, request):
        """Extract data categories from request"""
        # Try headers
        categories = request.META.get('HTTP_X_DATA_CATEGORIES')
        if categories:
            try:
                return json.loads(categories)
            except:
                pass
        
        # Try request body
        if request.method == 'POST' and hasattr(request, 'body'):
            try:
                data = json.loads(request.body)
                return data.get('data_categories', [])
            except:
                pass
        
        # Extract from form configuration if available
        return extract_data_categories_from_request(request)
    
    def _determine_action(self, request, response):
        """Determine the action type based on request method and endpoint"""
        method = request.method.upper()
        path = request.path
        
        if method == 'GET':
            return 'read'
        elif method in ['POST', 'PUT', 'PATCH']:
            if 'submit' in path or 'create' in path:
                return 'write'
            elif 'share' in path or 'export' in path:
                return 'share'
            else:
                return 'write'
        elif method == 'DELETE':
            return 'delete'
        else:
            return 'read'
    
    def _extract_resource(self, request):
        """Extract resource identifier from request"""
        path = request.path
        method = request.method.upper()
        
        # Extract resource type from path
        if '/api/clinical/' in path:
            return f"clinical{path.replace('/api/clinical', '')}"
        elif '/api/submit/' in path:
            return f"submission{path.replace('/api/submit', '')}"
        elif '/api/runtime/' in path:
            return f"runtime{path.replace('/api/runtime', '')}"
        elif '/api/config/' in path:
            return f"config{path.replace('/api/config', '')}"
        elif '/api/consent/' in path:
            return f"consent{path.replace('/api/consent', '')}"
        else:
            return path
    
    def _extract_fields(self, request, response):
        """Extract fields accessed/modified from request and response"""
        fields = []
        
        # Extract from request body
        if request.method in ['POST', 'PUT', 'PATCH'] and hasattr(request, 'body'):
            try:
                data = json.loads(request.body)
                if isinstance(data, dict):
                    fields.extend(data.keys())
            except:
                pass
        
        # Extract from response data
        if hasattr(response, 'data') and response.data:
            try:
                if isinstance(response.data, dict):
                    fields.extend(response.data.keys())
                elif isinstance(response.data, list) and response.data:
                    if isinstance(response.data[0], dict):
                        fields.extend(response.data[0].keys())
            except:
                pass
        
        return list(set(fields))  # Remove duplicates
    
    def _log_audit_event(self, request, response, action, resource, fields, decision):
        """Log audit event to database"""
        from core.tenant import get_current_tenant
        
        tenant_id = get_current_tenant()
        if not tenant_id:
            return
        
        # Get previous hash for chain continuity
        previous_hash = AuditEvent.get_latest_hash(tenant_id)
        
        # Ensure purpose is valid
        purpose = request.audit_purpose or 'treatment'
        if purpose not in ['treatment', 'ops', 'research', 'analytics', 'marketing', 'emergency']:
            purpose = 'treatment'
        
        # Create audit event
        audit_event = AuditEvent.objects.create(
            tenant_id=tenant_id,
            request_id=request.audit_request_id,
            user_id=request.audit_user_id,
            patient_id=request.audit_patient_id or 'unknown',
            action=action,
            resource=resource,
            fields=fields,
            purpose=purpose,
            data_categories=request.audit_data_categories or [],
            consent_id=None,  # Will be filled by consent checking
            decision=decision,
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            reason=f"HTTP {response.status_code}",
            previous_hash=previous_hash
        )
        
        return audit_event
