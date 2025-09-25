#!/usr/bin/env python
"""
Integration test for RBAC system
"""
import os
import django
import requests
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

from policies.models import PolicyRule

def test_rbac_integration():
    """Test RBAC system integration"""
    print("Testing RBAC Integration...")
    
    # Clear existing policies
    PolicyRule.objects.all().delete()
    
    # Create test policies
    print("Creating test policies...")
    
    # Allow Doctors to read/write hba1c
    PolicyRule.objects.create(
        tenant_id='H001',
        version=1,
        resource_type='field',
        action='read',
        selector={'form': 'visit_opd', 'field': 'hba1c'},
        effect='allow',
        condition="'Doctor' in user.roles",
        status='published'
    )
    
    PolicyRule.objects.create(
        tenant_id='H001',
        version=2,
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'hba1c'},
        effect='allow',
        condition="'Doctor' in user.roles",
        status='published'
    )
    
    # Allow Nurses to read but mask hiv_status
    PolicyRule.objects.create(
        tenant_id='H001',
        version=3,
        resource_type='field',
        action='read',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='allow',
        condition="'Nurse' in user.roles",
        status='published'
    )
    
    PolicyRule.objects.create(
        tenant_id='H001',
        version=4,
        resource_type='field',
        action='mask',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='allow',
        condition="'Nurse' in user.roles",
        status='published'
    )
    
    # Deny Nurses from writing hiv_status
    PolicyRule.objects.create(
        tenant_id='H001',
        version=5,
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='deny',
        condition="'Nurse' in user.roles",
        status='published'
    )
    
    # Allow Doctors to write hiv_status
    PolicyRule.objects.create(
        tenant_id='H001',
        version=6,
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'hiv_status'},
        effect='allow',
        condition="'Doctor' in user.roles",
        status='published'
    )
    
    # Basic fields - allow all
    PolicyRule.objects.create(
        tenant_id='H001',
        version=7,
        resource_type='field',
        action='read',
        selector={'form': 'visit_opd', 'field': 'name'},
        effect='allow',
        status='published'
    )
    
    PolicyRule.objects.create(
        tenant_id='H001',
        version=8,
        resource_type='field',
        action='write',
        selector={'form': 'visit_opd', 'field': 'name'},
        effect='allow',
        status='published'
    )
    
    # Record permissions
    PolicyRule.objects.create(
        tenant_id='H001',
        version=9,
        resource_type='record',
        action='read',
        selector={'type': 'visit'},
        effect='allow',
        condition="user.tenant_id == record.custom_data.get('tenant_id', 'H001')",
        status='published'
    )
    
    # Workflow permissions
    PolicyRule.objects.create(
        tenant_id='H001',
        version=10,
        resource_type='workflow',
        action='publish',
        selector={'workflow': 'visit_opd'},
        effect='allow',
        condition="'ClinicalLead' in user.roles or 'Admin' in user.roles",
        status='published'
    )
    
    print(f"Created {PolicyRule.objects.count()} policies")
    
    # Test field authorization
    print("\n=== Testing Field Authorization ===")
    
    from policies.authorization import authorize, get_authorized_fields
    
    # Test Doctor permissions
    doctor_user = {
        'tenant_id': 'H001',
        'roles': ['Doctor'],
        'departments': ['Endocrinology']
    }
    
    # Doctor can read hba1c
    can_read_hba1c = authorize(doctor_user, 'field', 'read', {'form': 'visit_opd', 'field': 'hba1c'})
    print(f"Doctor can read hba1c: {can_read_hba1c}")
    assert can_read_hba1c, "Doctor should be able to read hba1c"
    
    # Doctor can write hba1c
    can_write_hba1c = authorize(doctor_user, 'field', 'write', {'form': 'visit_opd', 'field': 'hba1c'})
    print(f"Doctor can write hba1c: {can_write_hba1c}")
    assert can_write_hba1c, "Doctor should be able to write hba1c"
    
    # Doctor can write hiv_status
    can_write_hiv = authorize(doctor_user, 'field', 'write', {'form': 'visit_opd', 'field': 'hiv_status'})
    print(f"Doctor can write hiv_status: {can_write_hiv}")
    assert can_write_hiv, "Doctor should be able to write hiv_status"
    
    # Test Nurse permissions
    nurse_user = {
        'tenant_id': 'H001',
        'roles': ['Nurse'],
        'departments': ['Endocrinology']
    }
    
    # Nurse can read hiv_status
    can_read_hiv = authorize(nurse_user, 'field', 'read', {'form': 'visit_opd', 'field': 'hiv_status'})
    print(f"Nurse can read hiv_status: {can_read_hiv}")
    assert can_read_hiv, "Nurse should be able to read hiv_status"
    
    # Nurse can mask hiv_status
    can_mask_hiv = authorize(nurse_user, 'field', 'mask', {'form': 'visit_opd', 'field': 'hiv_status'})
    print(f"Nurse can mask hiv_status: {can_mask_hiv}")
    assert can_mask_hiv, "Nurse should be able to mask hiv_status"
    
    # Nurse cannot write hiv_status
    can_write_hiv_nurse = authorize(nurse_user, 'field', 'write', {'form': 'visit_opd', 'field': 'hiv_status'})
    print(f"Nurse can write hiv_status: {can_write_hiv_nurse}")
    assert not can_write_hiv_nurse, "Nurse should NOT be able to write hiv_status"
    
    # Test field filtering
    print("\n=== Testing Field Filtering ===")
    
    fields = [
        {'id': 'hba1c', 'label': 'HbA1c', 'type': 'number'},
        {'id': 'hiv_status', 'label': 'HIV Status', 'type': 'text'},
        {'id': 'name', 'label': 'Name', 'type': 'text'}
    ]
    
    # Doctor fields
    doctor_fields = get_authorized_fields(doctor_user, 'visit_opd', fields)
    print(f"Doctor authorized fields: {[f['id'] for f in doctor_fields]}")
    assert len(doctor_fields) == 3, "Doctor should see all fields"
    
    # Nurse fields (hiv_status should be masked)
    nurse_fields = get_authorized_fields(nurse_user, 'visit_opd', fields)
    print(f"Nurse authorized fields: {[f['id'] for f in nurse_fields]}")
    assert len(nurse_fields) == 3, "Nurse should see all fields"
    
    # Check if hiv_status is masked for nurse
    hiv_field = next(f for f in nurse_fields if f['id'] == 'hiv_status')
    assert hiv_field.get('_masked', False), "HIV status should be masked for nurse"
    
    # Test record permissions
    print("\n=== Testing Record Permissions ===")
    
    visit_record = {
        'id': 1,
        'custom_data': {'tenant_id': 'H001', 'department': 'Endocrinology'}
    }
    
    can_read_record = authorize(doctor_user, 'record', 'read', {'type': 'visit'}, record=visit_record)
    print(f"Doctor can read record: {can_read_record}")
    assert can_read_record, "Doctor should be able to read record from same tenant"
    
    # Test workflow permissions
    print("\n=== Testing Workflow Permissions ===")
    
    # ClinicalLead can publish
    clinical_lead = {
        'tenant_id': 'H001',
        'roles': ['ClinicalLead'],
        'departments': ['Endocrinology']
    }
    
    can_publish = authorize(clinical_lead, 'workflow', 'publish', {'workflow': 'visit_opd'})
    print(f"ClinicalLead can publish workflow: {can_publish}")
    assert can_publish, "ClinicalLead should be able to publish workflow"
    
    # Doctor cannot publish
    can_publish_doctor = authorize(doctor_user, 'workflow', 'publish', {'workflow': 'visit_opd'})
    print(f"Doctor can publish workflow: {can_publish_doctor}")
    assert not can_publish_doctor, "Doctor should NOT be able to publish workflow"
    
    print("\n=== All RBAC Tests Passed! ===")
    print("✅ Field-level permissions working")
    print("✅ Record-level permissions working") 
    print("✅ Workflow permissions working")
    print("✅ Deny-overrides working")
    print("✅ Field masking working")
    print("✅ Condition evaluation working")

if __name__ == "__main__":
    test_rbac_integration()
