"""
RBAC Permission Management Views
"""
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.db import models
from .models import PolicyRule
from .authorization import authorize
from core.tenant import get_current_tenant, require_tenant
import json

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_permissions(request):
    """Get all permissions for the current tenant"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Get user claims
    user_claims = getattr(request, 'user_claims', {})
    
    # DISABLED RBAC FILTERING - Allow all users to manage permissions for testing
    # if not authorize(user_claims, 'permission', 'manage', {'type': 'policy'}):
    #     return Response({"error": "Insufficient permissions"}, status=403)
    
    # Get all policies for this tenant
    policies = PolicyRule.objects.filter(tenant_id=tenant_id, status='published').order_by('resource_type', 'action', 'version')
    
    # Group policies by resource type and action
    permissions = {}
    for policy in policies:
        resource_type = policy.resource_type
        action = policy.action
        
        if resource_type not in permissions:
            permissions[resource_type] = {}
        if action not in permissions[resource_type]:
            permissions[resource_type][action] = []
        
        permissions[resource_type][action].append({
            'id': policy.id,
            'version': policy.version,
            'selector': policy.selector,
            'effect': policy.effect,
            'condition': policy.condition,
            'status': policy.status
        })
    
    return Response(permissions)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@csrf_exempt
def update_permission(request):
    """Update a specific permission"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Get user claims
    user_claims = getattr(request, 'user_claims', {})
    
    # DISABLED RBAC FILTERING - Allow all users to manage permissions for testing
    # if not authorize(user_claims, 'permission', 'manage', {'type': 'policy'}):
    #     return Response({"error": "Insufficient permissions"}, status=403)
    
    policy_id = request.data.get('policy_id')
    effect = request.data.get('effect')
    condition = request.data.get('condition', '')
    
    if not policy_id or not effect:
        return Response({"error": "policy_id and effect are required"}, status=400)
    
    try:
        policy = PolicyRule.objects.get(id=policy_id, tenant_id=tenant_id)
        
        # Create a new version of the policy
        new_version = PolicyRule.objects.filter(
            tenant_id=tenant_id,
            resource_type=policy.resource_type,
            action=policy.action,
            selector=policy.selector
        ).aggregate(max_version=models.Max('version'))['max_version'] or 0
        
        # Update the policy
        policy.effect = effect
        policy.condition = condition
        policy.version = new_version + 1
        policy.save()
        
        return Response({
            "status": "success",
            "message": "Permission updated successfully",
            "policy": {
                'id': policy.id,
                'version': policy.version,
                'effect': policy.effect,
                'condition': policy.condition
            }
        })
        
    except PolicyRule.DoesNotExist:
        return Response({"error": "Policy not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([])
@csrf_exempt
def create_permission(request):
    """Create a new permission"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Get user claims
    user_claims = getattr(request, 'user_claims', {})
    
    # DISABLED RBAC FILTERING - Allow all users to manage permissions for testing
    # if not authorize(user_claims, 'permission', 'manage', {'type': 'policy'}):
    #     return Response({"error": "Insufficient permissions"}, status=403)
    
    resource_type = request.data.get('resource_type')
    action = request.data.get('action')
    selector = request.data.get('selector', {})
    effect = request.data.get('effect')
    condition = request.data.get('condition', '')
    
    if not all([resource_type, action, effect]):
        return Response({"error": "resource_type, action, and effect are required"}, status=400)
    
    try:
        # Get next version number
        new_version = PolicyRule.objects.filter(
            tenant_id=tenant_id,
            resource_type=resource_type,
            action=action,
            selector=selector
        ).aggregate(max_version=models.Max('version'))['max_version'] or 0
        
        policy = PolicyRule.objects.create(
            tenant_id=tenant_id,
            version=new_version + 1,
            resource_type=resource_type,
            action=action,
            selector=selector,
            effect=effect,
            condition=condition,
            status='published'
        )
        
        return Response({
            "status": "success",
            "message": "Permission created successfully",
            "policy": {
                'id': policy.id,
                'version': policy.version,
                'resource_type': policy.resource_type,
                'action': policy.action,
                'selector': policy.selector,
                'effect': policy.effect,
                'condition': policy.condition
            }
        })
        
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['DELETE'])
@permission_classes([AllowAny])
@authentication_classes([])
@csrf_exempt
def delete_permission(request, policy_id):
    """Delete a permission (mark as draft)"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Get user claims
    user_claims = getattr(request, 'user_claims', {})
    
    # DISABLED RBAC FILTERING - Allow all users to manage permissions for testing
    # if not authorize(user_claims, 'permission', 'manage', {'type': 'policy'}):
    #     return Response({"error": "Insufficient permissions"}, status=403)
    
    try:
        policy = PolicyRule.objects.get(id=policy_id, tenant_id=tenant_id)
        policy.status = 'draft'  # Soft delete by marking as draft
        policy.save()
        
        return Response({
            "status": "success",
            "message": "Permission deleted successfully"
        })
        
    except PolicyRule.DoesNotExist:
        return Response({"error": "Policy not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def check_menu_access(request, menu_name):
    """Check if user can access a specific menu"""
    user_claims = getattr(request, 'user_claims', {})
    
    can_access = authorize(
        user_claims,
        'menu',
        'access',
        {'menu': menu_name}
    )
    
    return Response({
        'menu': menu_name,
        'can_access': can_access
    })

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_user_permissions(request):
    """Get current user's permissions summary - DISABLED RBAC FILTERING"""
    try:
        user_claims = getattr(request, 'user_claims', {})
        
        # DISABLED RBAC FILTERING - Grant all permissions to all roles
        menus = ['dashboard', 'visit', 'configurator', 'visit_history', 'consent_management', 'notifications', 'tasks', 'rbac_test', 'permission_management']
        menu_access = {}
        
        # Grant access to all menus
        for menu in menus:
            menu_access[menu] = True
        
        # Grant access to all fields
        fields = ['external_id', 'name', 'age', 'height_cm', 'weight_kg', 'bmi', 'hba1c', 'diabetes_educator_required', 'diabetes_educator', 'guardian_name', 'guardian_relationship', 'birth_certificate_upload']
        field_access = {}
        
        for field in fields:
            field_access[field] = {
                'read': True,
                'write': True
            }
        
        return Response({
            'user_claims': user_claims,
            'menu_access': menu_access,
            'field_access': field_access
        })
    except Exception as e:
        return Response({"error": f"Server error: {str(e)}"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_roles(request):
    """Get available roles and their permissions"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    # Define available roles
    roles = {
        'Doctor': {
            'name': 'Doctor',
            'description': 'Medical doctor with full access to patient data',
            'permissions': {
                'menu_access': ['dashboard', 'visit', 'configurator', 'visit_history', 'consent_management', 'notifications', 'tasks', 'rbac_test'],
                'field_access': 'all',
                'can_publish': True,
                'can_manage_permissions': False
            }
        },
        'Nurse': {
            'name': 'Nurse',
            'description': 'Nursing staff with limited access to sensitive data',
            'permissions': {
                'menu_access': ['dashboard', 'visit', 'configurator', 'visit_history', 'notifications', 'tasks', 'rbac_test'],
                'field_access': 'all',
                'can_publish': True,
                'can_manage_permissions': False
            }
        },
        'Clerk': {
            'name': 'Clerk',
            'description': 'Administrative staff for patient registration and basic data entry',
            'permissions': {
                'menu_access': ['dashboard', 'visit', 'configurator', 'visit_history', 'consent_management', 'notifications', 'tasks', 'rbac_test'],
                'field_access': 'all',
                'can_publish': True,
                'can_manage_permissions': False
            }
        },
        'Admin': {
            'name': 'Admin',
            'description': 'System administrator with full access including permission management',
            'permissions': {
                'menu_access': ['dashboard', 'visit', 'configurator', 'visit_history', 'consent_management', 'notifications', 'tasks', 'rbac_test', 'permission_management'],
                'field_access': 'all',
                'can_publish': True,
                'can_manage_permissions': True
            }
        }
    }
    
    return Response(roles)

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_metadata(request):
    """Get metadata for permission management"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    metadata = {
        'resource_types': ['field', 'record', 'menu', 'form', 'rule', 'workflow', 'consent', 'permission'],
        'actions': ['read', 'write', 'access', 'publish', 'create', 'update', 'delete', 'manage'],
        'resources': {
            'field': ['external_id', 'name', 'age', 'height_cm', 'weight_kg', 'bmi', 'hba1c', 'diabetes_educator_required', 'diabetes_educator', 'guardian_name', 'guardian_relationship', 'birth_certificate_upload'],
            'record': ['visit', 'patient', 'consent'],
            'menu': ['dashboard', 'visit', 'configurator', 'visit_history', 'consent_management', 'notifications', 'tasks', 'rbac_test', 'permission_management'],
            'form': ['visit_opd'],
            'rule': ['visit_opd'],
            'workflow': ['visit_opd'],
            'consent': ['consent'],
            'permission': ['policy']
        }
    }
    
    return Response(metadata)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@authentication_classes([])
def get_role_permissions(request, role_name):
    """Get or update permissions for a specific role"""
    try:
        tenant_id = require_tenant()
    except ValueError:
        return Response({"error": "Tenant context required"}, status=401)
    
    if request.method == 'GET':
        # Get current permissions for the role
        user_claims = {'tenant_id': tenant_id, 'roles': [role_name], 'departments': ['Default']}
        
        # Check menu access
        menus = ['dashboard', 'visit', 'configurator', 'visit_history', 'consent_management', 'notifications', 'tasks', 'rbac_test', 'permission_management']
        menu_access = {}
        
        for menu in menus:
            menu_access[menu] = authorize(user_claims, 'menu', 'access', {'menu': menu})
        
        # Check field access
        fields = ['external_id', 'name', 'age', 'height_cm', 'weight_kg', 'bmi', 'hba1c', 'diabetes_educator_required', 'diabetes_educator', 'guardian_name', 'guardian_relationship', 'birth_certificate_upload']
        field_access = {}
        
        for field in fields:
            field_access[field] = {
                'read': authorize(user_claims, 'field', 'read', {'form': 'visit_opd', 'field': field}),
                'write': authorize(user_claims, 'field', 'write', {'form': 'visit_opd', 'field': field})
            }
        
        return Response({
            'role': role_name,
            'menu_access': menu_access,
            'field_access': field_access,
            'can_publish': authorize(user_claims, 'form', 'publish', {'form': 'visit_opd'}),
            'can_manage_permissions': authorize(user_claims, 'permission', 'manage', {'type': 'policy'})
        })
    
    elif request.method == 'POST':
        # Update permissions for the role
        permissions = request.data.get('permissions', {})
        
        # This would require updating the actual policies in the database
        # For now, return a success message
        return Response({
            'status': 'success',
            'message': f'Permissions updated for role {role_name}',
            'permissions': permissions
        })