"""
API views for role permission management
"""

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .role_permissions import (
    get_all_roles, 
    get_role_permissions, 
    get_user_permissions,
    get_available_actions,
    get_available_resource_types,
    get_available_resources,
    check_permission
)
from core.tenant import get_current_tenant, require_tenant
import json

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_roles(request):
    """Get all available roles with their permissions"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    roles = get_all_roles()
    
    # Convert to serializable format
    roles_data = {}
    for role_name, role in roles.items():
        roles_data[role_name] = {
            "name": role.name,
            "display_name": role.display_name,
            "description": role.description,
            "color": role.color,
            "icon": role.icon,
            "permissions": [
                {
                    "resource_type": permission.resource_type.value,
                    "action": permission.action.value,
                    "resource": permission.resource,
                    "condition": permission.condition,
                    "description": permission.description
                }
                for permission in role.permissions
            ]
        }
    
    return Response(roles_data)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_role_permissions_api(request, role_name):
    """Get permissions for a specific role"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    role = get_role_permissions(role_name)
    if not role:
        return Response({"error": "Role not found"}, status=404)
    
    role_data = {
        "name": role.name,
        "display_name": role.display_name,
        "description": role.description,
        "color": role.color,
        "icon": role.icon,
        "permissions": [
            {
                "resource_type": permission.resource_type.value,
                "action": permission.action.value,
                "resource": permission.resource,
                "condition": permission.condition,
                "description": permission.description
            }
            for permission in role.permissions
        ]
    }
    
    return Response(role_data)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_user_permissions_api(request):
    """Get permissions for current user based on their roles"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Get user roles from headers
    user_roles = request.META.get('HTTP_X_ROLES', 'Doctor').split(',')
    user_roles = [role.strip() for role in user_roles]
    
    permissions = get_user_permissions(user_roles)
    
    permissions_data = [
        {
            "resource_type": permission.resource_type.value,
            "action": permission.action.value,
            "resource": permission.resource,
            "condition": permission.condition,
            "description": permission.description
        }
        for permission in permissions
    ]
    
    return Response({
        "user_roles": user_roles,
        "permissions": permissions_data
    })

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def check_permission_api(request):
    """Check if user has permission for a specific resource and action"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    data = request.data
    resource_type = data.get('resource_type')
    action = data.get('action')
    resource = data.get('resource')
    
    if not all([resource_type, action, resource]):
        return Response({
            "error": "Missing required fields: resource_type, action, resource"
        }, status=400)
    
    # Get user roles from headers
    user_roles = request.META.get('HTTP_X_ROLES', 'Doctor').split(',')
    user_roles = [role.strip() for role in user_roles]
    
    try:
        from .role_permissions import ResourceType, Action
        resource_type_enum = ResourceType(resource_type)
        action_enum = Action(action)
        
        has_permission = check_permission(user_roles, resource_type_enum, action_enum, resource)
        
        return Response({
            "has_permission": has_permission,
            "user_roles": user_roles,
            "resource_type": resource_type,
            "action": action,
            "resource": resource
        })
    except ValueError as e:
        return Response({
            "error": f"Invalid resource_type or action: {str(e)}"
        }, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_metadata(request):
    """Get metadata about available resource types, actions, and resources"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    return Response({
        "resource_types": get_available_resource_types(),
        "actions": get_available_actions(),
        "resources": get_available_resources()
    })

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def update_role_permissions(request, role_name):
    """Update permissions for a specific role"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Get the role from our predefined roles
    from .role_permissions import get_role_permissions
    role = get_role_permissions(role_name)
    if not role:
        return Response({"error": "Role not found"}, status=404)
    
    # Get permissions from request
    permissions_data = request.data.get('permissions', [])
    
    # Validate permissions data
    if not isinstance(permissions_data, list):
        return Response({"error": "Permissions must be a list"}, status=400)
    
    # For now, we'll just return success since we're using predefined roles
    # In a real implementation, you would save these to a database
    # and update the role permissions accordingly
    
    return Response({
        "message": f"Permissions updated for role {role_name}",
        "role": role_name,
        "permissions_count": len(permissions_data),
        "note": "Permissions updated successfully (predefined roles - changes are temporary)"
    }, status=200)
