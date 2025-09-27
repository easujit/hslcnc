"""
Comprehensive test script for Consent Management system
"""
import requests
import json
from datetime import datetime, timedelta

# Test configuration
BASE_URL = "http://localhost:8000"
TENANT_A = "TENANT_A"
TENANT_B = "TENANT_B"

def test_consent_apis():
    """Test consent management APIs"""
    print("=== Testing Consent Management APIs ===")
    
    headers = {
        'Content-Type': 'application/json',
        'X-Tenant': TENANT_A,
        'X-User-ID': 'test_user',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology'
    }
    
    # Test 1: Create a consent
    print("\n1. Creating consent for patient P123...")
    consent_data = {
        "patient_id": "P123",
        "purpose": "treatment",
        "data_categories": ["demographics", "vitals", "labs"],
        "date_range_start": (datetime.now() - timedelta(days=1)).isoformat(),
        "date_range_end": (datetime.now() + timedelta(days=365)).isoformat(),
        "expiry": (datetime.now() + timedelta(days=365)).isoformat(),
        "notice_lang": "en",
        "consent_method": "digital",
        "consent_version": "1.0",
        "legal_basis": "consent"
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/consents/", 
                           headers=headers, 
                           json=consent_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        consent = response.json()
        print(f"Created consent: {consent['consent_id']}")
        consent_id = consent['consent_id']
    else:
        print(f"Error: {response.text}")
        return
    
    # Test 2: Check consent
    print("\n2. Checking consent for patient P123...")
    check_data = {
        "patient_id": "P123",
        "purpose": "treatment",
        "data_categories": ["demographics", "vitals"],
        "action": "read"
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/consent/check/", 
                           headers=headers, 
                           json=check_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Consent check result: {result}")
    else:
        print(f"Error: {response.text}")
    
    # Test 3: Check consent for different data categories (should fail)
    print("\n3. Checking consent for restricted data categories...")
    check_data_restricted = {
        "patient_id": "P123",
        "purpose": "research",  # Different purpose
        "data_categories": ["demographics", "vitals", "labs"],
        "action": "read"
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/consent/check/", 
                           headers=headers, 
                           json=check_data_restricted)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Consent check result: {result}")
    else:
        print(f"Expected error: {response.text}")
    
    # Test 4: Revoke consent
    print("\n4. Revoking consent...")
    revoke_data = {
        "reason": "Patient requested revocation",
        "revoked_by": "test_user"
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/consent/{consent_id}/revoke/", 
                           headers=headers, 
                           json=revoke_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("Consent revoked successfully")
    else:
        print(f"Error: {response.text}")
    
    # Test 5: Check consent after revocation (should fail)
    print("\n5. Checking consent after revocation...")
    response = requests.post(f"{BASE_URL}/api/consent/consent/check/", 
                           headers=headers, 
                           json=check_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Consent check result: {result}")
    else:
        print(f"Expected error: {response.text}")

def test_runtime_consent_enforcement():
    """Test consent enforcement in runtime engine"""
    print("\n=== Testing Runtime Consent Enforcement ===")
    
    headers = {
        'Content-Type': 'application/json',
        'X-Tenant': TENANT_A,
        'X-User-ID': 'test_user',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology'
    }
    
    # Test 1: Evaluate rules with valid consent
    print("\n1. Evaluating rules with valid consent...")
    form_data = {
        "external_id": "P123",  # Patient with valid consent
        "name": "John Doe",
        "age": 45,
        "height_cm": 175,
        "weight_kg": 80,
        "hba1c": 8.5
    }
    
    response = requests.post(f"{BASE_URL}/api/runtime/evaluate/visit_opd/", 
                           headers=headers, 
                           json=form_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Rules evaluation result: {result}")
    else:
        print(f"Error: {response.text}")
    
    # Test 2: Evaluate rules without consent (should fail)
    print("\n2. Evaluating rules without consent...")
    form_data_no_consent = {
        "external_id": "P999",  # Patient without valid consent
        "name": "Jane Doe",
        "age": 35,
        "height_cm": 165,
        "weight_kg": 60,
        "hba1c": 7.2
    }
    
    response = requests.post(f"{BASE_URL}/api/runtime/evaluate/visit_opd/", 
                           headers=headers, 
                           json=form_data_no_consent)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Rules evaluation result: {result}")
    else:
        print(f"Expected error: {response.text}")

def test_submission_consent_enforcement():
    """Test consent enforcement in submission"""
    print("\n=== Testing Submission Consent Enforcement ===")
    
    headers = {
        'Content-Type': 'application/json',
        'X-Tenant': TENANT_A,
        'X-User-ID': 'test_user',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology',
        'Idempotency-Key': f'test_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    }
    
    # Test 1: Submit form with valid consent
    print("\n1. Submitting form with valid consent...")
    form_data = {
        "external_id": "P123",  # Patient with valid consent
        "name": "John Doe",
        "age": 45,
        "height_cm": 175,
        "weight_kg": 80,
        "hba1c": 8.5
    }
    
    response = requests.post(f"{BASE_URL}/api/submit/forms/visit_opd/submit/", 
                           headers=headers, 
                           json=form_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Submission result: {result}")
    else:
        print(f"Error: {response.text}")
    
    # Test 2: Submit form without consent (should fail)
    print("\n2. Submitting form without consent...")
    headers['Idempotency-Key'] = f'test_no_consent_{datetime.now().strftime("%Y%m%d_%H%M%S")}'
    form_data_no_consent = {
        "external_id": "P999",  # Patient without valid consent
        "name": "Jane Doe",
        "age": 35,
        "height_cm": 165,
        "weight_kg": 60,
        "hba1c": 7.2
    }
    
    response = requests.post(f"{BASE_URL}/api/submit/forms/visit_opd/submit/", 
                           headers=headers, 
                           json=form_data_no_consent)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Submission result: {result}")
    else:
        print(f"Expected error: {response.text}")

def test_abdm_integration():
    """Test ABDM integration"""
    print("\n=== Testing ABDM Integration ===")
    
    headers = {
        'Content-Type': 'application/json',
        'X-Tenant': TENANT_A,
        'X-User-ID': 'test_user',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology'
    }
    
    # Test 1: Create ABDM consent request
    print("\n1. Creating ABDM consent request...")
    abdm_request_data = {
        "patient_id": "P200",
        "purpose": "treatment",
        "data_categories": ["demographics", "vitals", "labs"]
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/abdm/request-consent/", 
                           headers=headers, 
                           json=abdm_request_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        print(f"ABDM request created: {result}")
        request_id = result['abdm_request_id']
    else:
        print(f"Error: {response.text}")
        return
    
    # Test 2: Simulate ABDM notification
    print("\n2. Simulating ABDM notification...")
    abdm_notify_data = {
        "request_id": request_id,
        "status": "granted",
        "artefact_id": f"ARTEFACT_{request_id}"
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/abdm/notify/", 
                           headers=headers, 
                           json=abdm_notify_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"ABDM notification processed: {result}")
    else:
        print(f"Error: {response.text}")
    
    # Test 3: Fetch artefact
    print("\n3. Fetching ABDM artefact...")
    artefact_data = {
        "artefact_id": f"ARTEFACT_{request_id}"
    }
    
    response = requests.post(f"{BASE_URL}/api/consent/abdm/fetch-artefact/", 
                           headers=headers, 
                           json=artefact_data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"Artefact data: {result}")
    else:
        print(f"Error: {response.text}")

def test_audit_logging():
    """Test audit logging"""
    print("\n=== Testing Audit Logging ===")
    
    headers = {
        'Content-Type': 'application/json',
        'X-Tenant': TENANT_A,
        'X-User-ID': 'test_user',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology'
    }
    
    # Test 1: Check audit events
    print("\n1. Checking audit events...")
    response = requests.get(f"{BASE_URL}/api/consent/audit-events/?patient_id=P123", 
                          headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        events = response.json()
        print(f"Found {len(events)} audit events for patient P123")
        for event in events[:3]:  # Show first 3 events
            print(f"  - {event['action']} {event['resource']} ({event['decision']})")
    else:
        print(f"Error: {response.text}")

def main():
    """Run all tests"""
    print("Starting Consent Management System Tests...")
    print("=" * 50)
    
    try:
        # Test consent APIs
        test_consent_apis()
        
        # Test runtime enforcement
        test_runtime_consent_enforcement()
        
        # Test submission enforcement
        test_submission_consent_enforcement()
        
        # Test ABDM integration
        test_abdm_integration()
        
        # Test audit logging
        test_audit_logging()
        
        print("\n" + "=" * 50)
        print("All tests completed!")
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
