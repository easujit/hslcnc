#!/usr/bin/env python
"""
Seed default RBAC policies for the Hospital POC
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

from policies.models import PolicyRule

def create_policy(tenant_id, resource_type, action, selector, effect, condition=None):
    """Create a policy rule"""
    rule = PolicyRule.objects.create(
        tenant_id=tenant_id,
        resource_type=resource_type,
        action=action,
        selector=selector,
        effect=effect,
        condition=condition,
        status='published'
    )
    print(f"Created policy: {rule}")
    return rule

def seed_policies():
    """Seed default policies"""
    print("Seeding RBAC policies...")
    
    # Field-level permissions
    print("\n=== Field-level permissions ===")
    
    # Allow Doctors and Nurses to read/write hba1c
    create_policy(
        tenant_id='TENANT_A',
        resource_type='field',
        action='read',
        selector={'form': 'visit_opd', 'field': 'hba1c'},
        effect='allow',
        condition="'Doctor' in user.roles or 'Nurse' in user.roles"
    )
    
    create_policy(
        tenant_id='TENANT_A',
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'hba1c'},
        effect='allow',
        condition="'Doctor' in user.roles or 'Nurse' in user.roles"
    )
    
    # Allow Nurses to read but mask hiv_status
    create_policy(
        tenant_id='TENANT_A',
        resource_type='field',
        action='read',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='allow',
        condition="'Nurse' in user.roles"
    )
    
    create_policy(
        tenant_id='TENANT_A',
        resource_type='field',
        action='mask',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='allow',
        condition="'Nurse' in user.roles"
    )
    
    # Deny Nurses from writing hiv_status
    create_policy(
        tenant_id='TENANT_A',
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='deny',
        condition="'Nurse' in user.roles"
    )
    
    # Allow Doctors to write hiv_status
    create_policy(
        tenant_id='TENANT_A',
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='allow',
        condition="'Doctor' in user.roles"
    )
    
    # Allow all roles to read/write basic fields
    basic_fields = ['external_id', 'name', 'age', 'height_cm', 'weight_kg', 'bmi']
    for field in basic_fields:
        create_policy(
            tenant_id='TENANT_A',
            resource_type='field',
            action='read',
            selector={'form': 'visit_opd', 'field': field},
            effect='allow'
        )
        
        create_policy(
            tenant_id='TENANT_A',
            resource_type='field',
            action='write',
            selector={'form': 'visit_opd', 'field': field},
            effect='allow'
        )
    
    # Record-level permissions
    print("\n=== Record-level permissions ===")
    
    # Allow users to read records from same tenant and department
    create_policy(
        tenant_id='TENANT_A',
        resource_type='record',
        action='read',
        selector={'type': 'visit'},
        effect='allow',
        condition="user.tenant_id == record.custom_data.get('tenant_id', 'H001') and user.departments[0] == record.custom_data.get('department', 'Endocrinology')"
    )
    
    # Workflow permissions
    print("\n=== Workflow permissions ===")
    
    # Only ClinicalLead and Admin can publish workflows
    create_policy(
        tenant_id='TENANT_A',
        resource_type='workflow',
        action='publish',
        selector={'workflow': 'visit_opd'},
        effect='allow',
        condition="'ClinicalLead' in user.roles or 'Admin' in user.roles"
    )
    
    # Workflow step permissions
    print("\n=== Workflow step permissions ===")
    
    # Allow Doctors and Nurses to execute diabetes educator workflow
    create_policy(
        tenant_id='TENANT_A',
        resource_type='workflow_step',
        action='execute',
        selector={'workflow': 'visit_opd', 'step': 'diabetes_educator'},
        effect='allow',
        condition="'Doctor' in user.roles or 'Nurse' in user.roles"
    )
    
    # Allow Admin and ClinicalLead to execute pediatrics workflow
    create_policy(
        tenant_id='TENANT_A',
        resource_type='workflow_step',
        action='execute',
        selector={'workflow': 'visit_opd', 'step': 'pediatrics_birth_certificate'},
        effect='allow',
        condition="'Admin' in user.roles or 'ClinicalLead' in user.roles"
    )
    
    print("\n=== Policy seeding complete ===")
    print(f"Total policies created: {PolicyRule.objects.count()}")

if __name__ == "__main__":
    seed_policies()
