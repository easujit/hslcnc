from typing import Dict, Any, Optional, List
from django.core.cache import cache
from .models import PolicyRule
from .evaluator import eval_condition
import json

def selector_match(rule_selector: Dict[str, Any], resource_selector: Dict[str, Any]) -> bool:
    """
    Check if a rule selector matches the resource selector
    
    Args:
        rule_selector: Selector from policy rule
        resource_selector: Selector from resource being accessed
        
    Returns:
        True if rule matches resource
    """
    for key, expected_value in rule_selector.items():
        if key not in resource_selector:
            return False
        
        actual_value = resource_selector[key]
        
        # Handle exact match
        if expected_value == actual_value:
            continue
        
        # Handle list contains
        if isinstance(expected_value, list) and actual_value in expected_value:
            continue
        
        # Handle wildcard
        if expected_value == '*':
            continue
        
        # No match
        return False
    
    return True

def load_tenant_policies(tenant_id: str) -> List[Dict[str, Any]]:
    """
    Load published policies for a tenant with caching
    
    Args:
        tenant_id: Tenant identifier
        
    Returns:
        List of policy rule dictionaries
    """
    cache_key = f"policies:{tenant_id}"
    policies = cache.get(cache_key)
    
    if policies is None:
        # Load from database
        rules = PolicyRule.objects.filter(
            tenant_id=tenant_id,
            status='published'
        ).order_by('-version')
        
        # Deduplicate by resource_type + action + selector (latest version wins)
        seen = set()
        policies = []
        
        for rule in rules:
            key = (rule.resource_type, rule.action, json.dumps(rule.selector, sort_keys=True))
            if key not in seen:
                seen.add(key)
                policies.append(rule.to_dict())
        
        # Cache for 60 seconds
        cache.set(cache_key, policies, 60)
    
    return policies

def authorize(
    user: Dict[str, Any], 
    resource_type: str, 
    action: str, 
    selector: Dict[str, Any], 
    record: Optional[Dict[str, Any]] = None, 
    ctx: Optional[Dict[str, Any]] = None
) -> bool:
    """
    Authorize access to a resource
    
    Args:
        user: User claims dictionary
        resource_type: Type of resource (field, record, workflow, workflow_step)
        action: Action being performed (read, write, execute, publish)
        selector: Resource selector criteria
        record: Record data for record-level permissions
        ctx: Additional context
        
    Returns:
        True if access is allowed, False if denied
    """
    tenant_id = user.get('tenant_id')
    if not tenant_id:
        return False  # No tenant = no access
    
    # Load tenant policies
    policies = load_tenant_policies(tenant_id)
    
    # Find matching rules
    matching_rules = []
    for policy in policies:
        if (policy['resource_type'] == resource_type and 
            policy['action'] == action and 
            selector_match(policy['selector'], selector)):
            matching_rules.append(policy)
    
    if not matching_rules:
        return False  # No matching rules = deny by default
    
    # Check for explicit denies first (deny overrides)
    for rule in matching_rules:
        if rule['effect'] == 'deny':
            # Check condition if present
            if rule['condition']:
                if eval_condition(rule['condition'], user, record, ctx):
                    return False  # Explicit deny
            else:
                return False  # Unconditional deny
    
    # Check for allows
    for rule in matching_rules:
        if rule['effect'] == 'allow':
            # Check condition if present
            if rule['condition']:
                if eval_condition(rule['condition'], user, record, ctx):
                    return True  # Explicit allow
            else:
                return True  # Unconditional allow
    
    return False  # No matching allow rules

def get_authorized_fields(user: Dict[str, Any], form_name: str, fields: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filter fields based on field-level permissions
    
    Args:
        user: User claims dictionary
        form_name: Name of the form
        fields: List of field definitions
        
    Returns:
        Filtered list of fields with permission metadata
    """
    authorized_fields = []
    
    for field in fields:
        field_id = field.get('id')
        if not field_id:
            continue
        
        # Check read permission
        can_read = authorize(
            user, 
            'field', 
            'read', 
            {'form': form_name, 'field': field_id}
        )
        
        if not can_read:
            continue  # Skip field entirely
        
        # Check write permission
        can_write = authorize(
            user, 
            'field', 
            'write', 
            {'form': form_name, 'field': field_id}
        )
        
        # Check mask permission
        can_mask = authorize(
            user, 
            'field', 
            'mask', 
            {'form': form_name, 'field': field_id}
        )
        
        # Create field copy with permission metadata
        authorized_field = field.copy()
        authorized_field['_can_write'] = can_write
        authorized_field['_can_mask'] = can_mask
        
        # Apply mask if needed
        if can_mask and not can_write:
            authorized_field['_masked'] = True
            authorized_field['readonly'] = True
        
        authorized_fields.append(authorized_field)
    
    return authorized_fields

def check_field_write_permissions(user: Dict[str, Any], form_name: str, data: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Check field write permissions for submitted data
    
    Args:
        user: User claims dictionary
        form_name: Name of the form
        data: Submitted data dictionary
        
    Returns:
        Dictionary with 'allowed' and 'denied' field lists
    """
    allowed_fields = []
    denied_fields = []
    
    for field_id in data.keys():
        can_write = authorize(
            user, 
            'field', 
            'write', 
            {'form': form_name, 'field': field_id}
        )
        
        if can_write:
            allowed_fields.append(field_id)
        else:
            denied_fields.append(field_id)
    
    return {
        'allowed': allowed_fields,
        'denied': denied_fields
    }
