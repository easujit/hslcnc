#!/usr/bin/env python
import requests
import json

# Test new patient submission
url = 'http://localhost:8000/api/submit/forms/visit_opd/submit/'
headers = {
    'Content-Type': 'application/json',
    'X-Tenant': 'TENANT_A',
    'X-Roles': 'Doctor',
    'Idempotency-Key': 'test_new_patient_123'
}

data = {
    'external_id': 'P_NEW_123',
    'name': 'New Patient Test',
    'age': 25,
    'height_cm': 170,
    'weight_kg': 70
}

print("Testing new patient submission...")
print(f"Patient ID: {data['external_id']}")
print(f"Tenant: {headers['X-Tenant']}")

response = requests.post(url, json=data, headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200:
    print("✅ SUCCESS: New patient created without consent!")
else:
    print("❌ FAILED: New patient creation failed")
