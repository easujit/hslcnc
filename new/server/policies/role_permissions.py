"""
Role Permission Management System
Defines roles, permissions, and provides utilities for role-based access control
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

class ResourceType(Enum):
    FIELD = "field"
    RECORD = "record"
    WORKFLOW = "workflow"
    WORKFLOW_STEP = "workflow_step"
    CONFIG = "config"
    CONSENT = "consent"
    AUDIT = "audit"

class Action(Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    EXECUTE = "execute"
    PUBLISH = "publish"
    MASK = "mask"
    SHARE = "share"
    EXPORT = "export"
    IMPORT = "import"
    MANAGE = "manage"

@dataclass
class Permission:
    """Represents a single permission"""
    resource_type: ResourceType
    action: Action
    resource: str  # e.g., "visit_opd", "patient", "hba1c"
    condition: Optional[str] = None  # Optional condition expression
    description: str = ""

@dataclass
class Role:
    """Represents a role with its permissions"""
    name: str
    display_name: str
    description: str
    permissions: List[Permission]
    color: str = "#3b82f6"  # Default blue color
    icon: str = "👤"  # Default icon

# Define all available roles and their permissions
ROLES = {
    "Doctor": Role(
        name="Doctor",
        display_name="Doctor",
        description="Medical doctor with full patient care access",
        color="#1e40af",
        icon="👨‍⚕️",
        permissions=[
            # Field permissions
            Permission(ResourceType.FIELD, Action.READ, "visit_opd", None, "Read all visit form fields"),
            Permission(ResourceType.FIELD, Action.WRITE, "visit_opd", None, "Write all visit form fields"),
            Permission(ResourceType.FIELD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.FIELD, Action.WRITE, "patient", None, "Write patient records"),
            Permission(ResourceType.FIELD, Action.READ, "hba1c", None, "Read HbA1c values"),
            Permission(ResourceType.FIELD, Action.WRITE, "hba1c", None, "Write HbA1c values"),
            Permission(ResourceType.FIELD, Action.READ, "hiv_status", None, "Read HIV status"),
            Permission(ResourceType.FIELD, Action.WRITE, "hiv_status", None, "Write HIV status"),
            
            # Record permissions
            Permission(ResourceType.RECORD, Action.READ, "visit", None, "Read visit records"),
            Permission(ResourceType.RECORD, Action.WRITE, "visit", None, "Write visit records"),
            Permission(ResourceType.RECORD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.RECORD, Action.WRITE, "patient", None, "Write patient records"),
            
            # Workflow permissions
            Permission(ResourceType.WORKFLOW_STEP, Action.EXECUTE, "diabetes_educator", None, "Execute diabetes educator workflow"),
            Permission(ResourceType.WORKFLOW_STEP, Action.EXECUTE, "pediatrics", None, "Execute pediatrics workflow"),
            
            # Consent permissions
            Permission(ResourceType.CONSENT, Action.READ, "consent", None, "Read consent records"),
            Permission(ResourceType.CONSENT, Action.WRITE, "consent", None, "Write consent records"),
        ]
    ),
    
    "Nurse": Role(
        name="Nurse",
        display_name="Nurse",
        description="Nursing staff with limited access to sensitive data",
        color="#059669",
        icon="👩‍⚕️",
        permissions=[
            # Field permissions
            Permission(ResourceType.FIELD, Action.READ, "visit_opd", None, "Read visit form fields"),
            Permission(ResourceType.FIELD, Action.WRITE, "visit_opd", None, "Write visit form fields"),
            Permission(ResourceType.FIELD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.FIELD, Action.WRITE, "patient", None, "Write patient records"),
            Permission(ResourceType.FIELD, Action.READ, "hba1c", None, "Read HbA1c values"),
            Permission(ResourceType.FIELD, Action.WRITE, "hba1c", None, "Write HbA1c values"),
            Permission(ResourceType.FIELD, Action.READ, "hiv_status", None, "Read HIV status"),
            Permission(ResourceType.FIELD, Action.MASK, "hiv_status", None, "Mask HIV status display"),
            # Note: No WRITE permission for hiv_status
            
            # Record permissions
            Permission(ResourceType.RECORD, Action.READ, "visit", None, "Read visit records"),
            Permission(ResourceType.RECORD, Action.WRITE, "visit", None, "Write visit records"),
            Permission(ResourceType.RECORD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.RECORD, Action.WRITE, "patient", None, "Write patient records"),
            
            # Workflow permissions
            Permission(ResourceType.WORKFLOW_STEP, Action.EXECUTE, "diabetes_educator", None, "Execute diabetes educator workflow"),
            
            # Consent permissions
            Permission(ResourceType.CONSENT, Action.READ, "consent", None, "Read consent records"),
        ]
    ),
    
    "ClinicalLead": Role(
        name="ClinicalLead",
        display_name="Clinical Lead",
        description="Clinical department lead with management permissions",
        color="#7c3aed",
        icon="👨‍💼",
        permissions=[
            # All Doctor permissions
            Permission(ResourceType.FIELD, Action.READ, "visit_opd", None, "Read all visit form fields"),
            Permission(ResourceType.FIELD, Action.WRITE, "visit_opd", None, "Write all visit form fields"),
            Permission(ResourceType.FIELD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.FIELD, Action.WRITE, "patient", None, "Write patient records"),
            Permission(ResourceType.FIELD, Action.READ, "hba1c", None, "Read HbA1c values"),
            Permission(ResourceType.FIELD, Action.WRITE, "hba1c", None, "Write HbA1c values"),
            Permission(ResourceType.FIELD, Action.READ, "hiv_status", None, "Read HIV status"),
            Permission(ResourceType.FIELD, Action.WRITE, "hiv_status", None, "Write HIV status"),
            
            # Record permissions
            Permission(ResourceType.RECORD, Action.READ, "visit", None, "Read visit records"),
            Permission(ResourceType.RECORD, Action.WRITE, "visit", None, "Write visit records"),
            Permission(ResourceType.RECORD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.RECORD, Action.WRITE, "patient", None, "Write patient records"),
            
            # Workflow permissions
            Permission(ResourceType.WORKFLOW, Action.PUBLISH, "visit_opd", None, "Publish visit workflow"),
            Permission(ResourceType.WORKFLOW_STEP, Action.EXECUTE, "diabetes_educator", None, "Execute diabetes educator workflow"),
            Permission(ResourceType.WORKFLOW_STEP, Action.EXECUTE, "pediatrics", None, "Execute pediatrics workflow"),
            
            # Config permissions
            Permission(ResourceType.CONFIG, Action.READ, "form", None, "Read form configurations"),
            Permission(ResourceType.CONFIG, Action.WRITE, "form", None, "Write form configurations"),
            Permission(ResourceType.CONFIG, Action.PUBLISH, "form", None, "Publish form configurations"),
            Permission(ResourceType.CONFIG, Action.READ, "rule", None, "Read rule configurations"),
            Permission(ResourceType.CONFIG, Action.WRITE, "rule", None, "Write rule configurations"),
            Permission(ResourceType.CONFIG, Action.PUBLISH, "rule", None, "Publish rule configurations"),
            
            # Consent permissions
            Permission(ResourceType.CONSENT, Action.READ, "consent", None, "Read consent records"),
            Permission(ResourceType.CONSENT, Action.WRITE, "consent", None, "Write consent records"),
            Permission(ResourceType.CONSENT, Action.MANAGE, "consent", None, "Manage consent policies"),
        ]
    ),
    
    "Admin": Role(
        name="Admin",
        display_name="Administrator",
        description="System administrator with full access",
        color="#dc2626",
        icon="👨‍💻",
        permissions=[
            # All permissions
            Permission(ResourceType.FIELD, Action.READ, "*", None, "Read all fields"),
            Permission(ResourceType.FIELD, Action.WRITE, "*", None, "Write all fields"),
            Permission(ResourceType.FIELD, Action.DELETE, "*", None, "Delete all fields"),
            Permission(ResourceType.FIELD, Action.MASK, "*", None, "Mask all fields"),
            
            Permission(ResourceType.RECORD, Action.READ, "*", None, "Read all records"),
            Permission(ResourceType.RECORD, Action.WRITE, "*", None, "Write all records"),
            Permission(ResourceType.RECORD, Action.DELETE, "*", None, "Delete all records"),
            Permission(ResourceType.RECORD, Action.EXPORT, "*", None, "Export all records"),
            
            Permission(ResourceType.WORKFLOW, Action.READ, "*", None, "Read all workflows"),
            Permission(ResourceType.WORKFLOW, Action.WRITE, "*", None, "Write all workflows"),
            Permission(ResourceType.WORKFLOW, Action.PUBLISH, "*", None, "Publish all workflows"),
            Permission(ResourceType.WORKFLOW, Action.DELETE, "*", None, "Delete all workflows"),
            
            Permission(ResourceType.WORKFLOW_STEP, Action.EXECUTE, "*", None, "Execute all workflow steps"),
            
            Permission(ResourceType.CONFIG, Action.READ, "*", None, "Read all configurations"),
            Permission(ResourceType.CONFIG, Action.WRITE, "*", None, "Write all configurations"),
            Permission(ResourceType.CONFIG, Action.PUBLISH, "*", None, "Publish all configurations"),
            Permission(ResourceType.CONFIG, Action.DELETE, "*", None, "Delete all configurations"),
            
            Permission(ResourceType.CONSENT, Action.READ, "*", None, "Read all consent records"),
            Permission(ResourceType.CONSENT, Action.WRITE, "*", None, "Write all consent records"),
            Permission(ResourceType.CONSENT, Action.MANAGE, "*", None, "Manage all consent policies"),
            Permission(ResourceType.CONSENT, Action.DELETE, "*", None, "Delete consent records"),
            
            Permission(ResourceType.AUDIT, Action.READ, "*", None, "Read audit logs"),
            Permission(ResourceType.AUDIT, Action.EXPORT, "*", None, "Export audit logs"),
        ]
    ),
    
    "Clerk": Role(
        name="Clerk",
        display_name="Clerk",
        description="Administrative clerk with basic data entry access",
        color="#f59e0b",
        icon="👩‍💼",
        permissions=[
            # Basic field permissions
            Permission(ResourceType.FIELD, Action.READ, "visit_opd", None, "Read visit form fields"),
            Permission(ResourceType.FIELD, Action.WRITE, "visit_opd", None, "Write visit form fields"),
            Permission(ResourceType.FIELD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.FIELD, Action.WRITE, "patient", None, "Write patient records"),
            
            # Basic record permissions
            Permission(ResourceType.RECORD, Action.READ, "visit", None, "Read visit records"),
            Permission(ResourceType.RECORD, Action.WRITE, "visit", None, "Write visit records"),
            Permission(ResourceType.RECORD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.RECORD, Action.WRITE, "patient", None, "Write patient records"),
            
            # Consent permissions
            Permission(ResourceType.CONSENT, Action.READ, "consent", None, "Read consent records"),
        ]
    ),
    
    "Researcher": Role(
        name="Researcher",
        display_name="Researcher",
        description="Research staff with read-only access to anonymized data",
        color="#8b5cf6",
        icon="👨‍🔬",
        permissions=[
            # Read-only field permissions
            Permission(ResourceType.FIELD, Action.READ, "visit_opd", None, "Read visit form fields"),
            Permission(ResourceType.FIELD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.FIELD, Action.READ, "hba1c", None, "Read HbA1c values"),
            # Note: No access to hiv_status for privacy
            
            # Read-only record permissions
            Permission(ResourceType.RECORD, Action.READ, "visit", None, "Read visit records"),
            Permission(ResourceType.RECORD, Action.READ, "patient", None, "Read patient records"),
            Permission(ResourceType.RECORD, Action.EXPORT, "visit", None, "Export visit records for research"),
            Permission(ResourceType.RECORD, Action.EXPORT, "patient", None, "Export patient records for research"),
            
            # Consent permissions
            Permission(ResourceType.CONSENT, Action.READ, "consent", None, "Read consent records"),
        ]
    )
}

def get_role_permissions(role_name: str) -> Optional[Role]:
    """Get permissions for a specific role"""
    return ROLES.get(role_name)

def get_all_roles() -> Dict[str, Role]:
    """Get all available roles"""
    return ROLES

def get_permissions_by_resource_type(resource_type: ResourceType) -> List[Permission]:
    """Get all permissions for a specific resource type"""
    permissions = []
    for role in ROLES.values():
        for permission in role.permissions:
            if permission.resource_type == resource_type:
                permissions.append(permission)
    return permissions

def check_permission(user_roles: List[str], resource_type: ResourceType, action: Action, resource: str) -> bool:
    """Check if user has permission for a specific resource and action"""
    for role_name in user_roles:
        role = get_role_permissions(role_name)
        if not role:
            continue
            
        for permission in role.permissions:
            if (permission.resource_type == resource_type and 
                permission.action == action and 
                (permission.resource == resource or permission.resource == "*")):
                return True
    return False

def get_user_permissions(user_roles: List[str]) -> List[Permission]:
    """Get all permissions for a user based on their roles"""
    permissions = []
    for role_name in user_roles:
        role = get_role_permissions(role_name)
        if role:
            permissions.extend(role.permissions)
    return permissions

def get_available_actions() -> List[str]:
    """Get all available actions"""
    return [action.value for action in Action]

def get_available_resource_types() -> List[str]:
    """Get all available resource types"""
    return [rt.value for rt in ResourceType]

def get_available_resources() -> List[str]:
    """Get all available resources"""
    resources = set()
    for role in ROLES.values():
        for permission in role.permissions:
            resources.add(permission.resource)
    return sorted(list(resources))
