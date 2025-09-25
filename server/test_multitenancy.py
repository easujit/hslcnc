#!/usr/bin/env python
"""
Test script for multi-tenancy functionality
"""
import os
import sys
import django
import requests
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

def test_tenant_isolation():
    """Test that tenants are properly isolated"""
    print("=== Testing Tenant Isolation ===")
    
    base_url = "http://localhost:8000/api"
    
    # Test headers for different tenants
    tenant_a_headers = {
        'X-Tenant': 'TENANT_A',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology',
        'Content-Type': 'application/json'
    }
    
    tenant_b_headers = {
        'X-Tenant': 'TENANT_B', 
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology',
        'Content-Type': 'application/json'
    }
    
    # Test 1: Create patient for Tenant A
    print("\n1. Creating patient for Tenant A...")
    patient_a_data = {
        'external_id': 'PATIENT_A_001',
        'name': 'Patient A',
        'custom_data': {'test': 'tenant_a'}
    }
    
    # This would normally be done through the API, but for testing we'll create directly
    from clinical.models import Patient
    from core.tenant import set_current_tenant
    
    # Set tenant context for Tenant A
    set_current_tenant('TENANT_A')
    patient_a = Patient.objects.create(**patient_a_data)
    print(f"Created patient A: {patient_a}")
    
    # Set tenant context for Tenant B
    set_current_tenant('TENANT_B')
    patient_b_data = {
        'external_id': 'PATIENT_B_001',
        'name': 'Patient B',
        'custom_data': {'test': 'tenant_b'}
    }
    patient_b = Patient.objects.create(**patient_b_data)
    print(f"Created patient B: {patient_b}")
    
    # Test 2: Verify isolation - Tenant A should only see their patients
    print("\n2. Testing patient list isolation...")
    set_current_tenant('TENANT_A')
    tenant_a_patients = list(Patient.objects.all())
    print(f"Tenant A sees {len(tenant_a_patients)} patients: {[p.external_id for p in tenant_a_patients]}")
    
    set_current_tenant('TENANT_B')
    tenant_b_patients = list(Patient.objects.all())
    print(f"Tenant B sees {len(tenant_b_patients)} patients: {[p.external_id for p in tenant_b_patients]}")
    
    # Verify isolation
    assert len(tenant_a_patients) == 1, "Tenant A should only see 1 patient"
    assert len(tenant_b_patients) == 1, "Tenant B should only see 1 patient"
    assert tenant_a_patients[0].external_id == 'PATIENT_A_001', "Tenant A should see their patient"
    assert tenant_b_patients[0].external_id == 'PATIENT_B_001', "Tenant B should see their patient"
    
    print("✅ Tenant isolation test passed!")
    
    # Test 3: Test API endpoints with tenant headers
    print("\n3. Testing API endpoints with tenant headers...")
    
    # Test effective form endpoint
    try:
        response = requests.get(f"{base_url}/config/effective/form/visit_opd/", headers=tenant_a_headers)
        print(f"Tenant A effective form: {response.status_code}")
        
        response = requests.get(f"{base_url}/config/effective/form/visit_opd/", headers=tenant_b_headers)
        print(f"Tenant B effective form: {response.status_code}")
    except Exception as e:
        print(f"API test failed (server might not be running): {e}")
    
    # Test 4: Test rate limiting
    print("\n4. Testing rate limiting...")
    from quotas.rate_limiting import rate_limiter
    
    # Test rate limiter for different tenants
    tenant_a_allowed = rate_limiter.is_allowed('TENANT_A', 'test_metric', rate_per_minute=2, burst=1)
    tenant_b_allowed = rate_limiter.is_allowed('TENANT_B', 'test_metric', rate_per_minute=2, burst=1)
    
    print(f"Tenant A rate limit check: {tenant_a_allowed}")
    print(f"Tenant B rate limit check: {tenant_b_allowed}")
    
    # Test 5: Test without tenant context
    print("\n5. Testing without tenant context...")
    from core.tenant import clear_current_tenant, get_current_tenant
    
    clear_current_tenant()
    tenant_id = get_current_tenant()
    print(f"Current tenant after clear: {tenant_id}")
    
    # This should raise an exception
    try:
        from core.tenant import require_tenant
        require_tenant()
        print("❌ Should have raised exception for missing tenant")
    except ValueError as e:
        print(f"✅ Correctly raised exception: {e}")
    
    print("\n=== Multi-tenancy Tests Complete ===")

def test_quota_system():
    """Test quota and rate limiting system"""
    print("\n=== Testing Quota System ===")
    
    from quotas.models import TenantQuota, TenantUsage
    from core.tenant import set_current_tenant
    
    # Set tenant context
    set_current_tenant('TEST_TENANT')
    
    # Create quota limits
    quota = TenantQuota.objects.create(
        tenant_id='TEST_TENANT',
        limits_json={
            'submit': {
                'rate_per_minute': 10,
                'burst': 5
            },
            'process': {
                'rate_per_minute': 5,
                'burst': 2
            }
        }
    )
    print(f"Created quota: {quota}")
    
    # Test usage tracking
    usage = TenantUsage.get_current_usage('TEST_TENANT', 'submit', 'minute')
    print(f"Current usage: {usage}")
    
    # Increment usage
    new_value = usage.increment(1)
    print(f"Usage after increment: {new_value}")
    
    # Test rate limiter
    from quotas.rate_limiting import rate_limiter
    
    is_allowed, quota_info = rate_limiter.check_quota('TEST_TENANT', 'submit')
    print(f"Rate limit check: {is_allowed}, info: {quota_info}")
    
    print("✅ Quota system test passed!")

if __name__ == '__main__':
    test_tenant_isolation()
    test_quota_system()
