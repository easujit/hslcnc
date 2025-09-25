"""
Quick test to verify consent system is working
"""
import requests
import json

def test_consent_system():
    """Test the consent system quickly"""
    base_url = "http://localhost:8000"
    
    headers = {
        'Content-Type': 'application/json',
        'X-Tenant': 'TENANT_A',
        'X-User-ID': 'test_user',
        'X-Roles': 'Doctor',
        'X-Departments': 'Endocrinology'
    }
    
    print("🧪 Testing Consent Management System...")
    
    # Test 1: Check consent for patient P123 (should have valid consent)
    print("\n1. Testing consent check for P123...")
    try:
        response = requests.post(f"{base_url}/api/consent/consent/check/", 
                               headers=headers,
                               json={
                                   "patient_id": "P123",
                                   "purpose": "treatment",
                                   "data_categories": ["demographics", "vitals"],
                                   "action": "read"
                               })
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Result: {result}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: Test runtime rules evaluation for P123
    print("\n2. Testing runtime rules evaluation for P123...")
    try:
        response = requests.post(f"{base_url}/api/runtime/rules/evaluate/visit_opd/", 
                               headers=headers,
                               json={
                                   "external_id": "P123",
                                   "name": "John Doe",
                                   "age": 45,
                                   "height_cm": 175,
                                   "weight_kg": 80,
                                   "hba1c": 8.5
                               })
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Result: {result}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 3: Test consent check for patient P999 (should not have valid consent)
    print("\n3. Testing consent check for P999...")
    try:
        response = requests.post(f"{base_url}/api/consent/consent/check/", 
                               headers=headers,
                               json={
                                   "patient_id": "P999",
                                   "purpose": "treatment",
                                   "data_categories": ["demographics", "vitals"],
                                   "action": "read"
                               })
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Result: {result}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 4: Test runtime rules evaluation for P999 (should fail)
    print("\n4. Testing runtime rules evaluation for P999...")
    try:
        response = requests.post(f"{base_url}/api/runtime/rules/evaluate/visit_opd/", 
                               headers=headers,
                               json={
                                   "external_id": "P999",
                                   "name": "Jane Doe",
                                   "age": 35,
                                   "height_cm": 165,
                                   "weight_kg": 60,
                                   "hba1c": 7.2
                               })
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Result: {result}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n✅ Consent system test completed!")

if __name__ == "__main__":
    test_consent_system()
