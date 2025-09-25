#!/usr/bin/env python
"""
Test script to verify multi-tenancy is working for UI testing
"""
import os
import sys
import django
import requests
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diabetes_poc.settings')
django.setup()

def test_ui_endpoints():
    """Test UI endpoints with different tenant headers"""
    print("=== Testing UI Endpoints for Multi-Tenancy ===")
    
    base_url = "http://localhost:8000/api"
    
    # Test different tenant configurations
    tenants = [
        {
            'name': 'TENANT_A',
            'headers': {
                'X-Tenant': 'TENANT_A',
                'X-Roles': 'Doctor',
                'X-Departments': 'Endocrinology'
            }
        },
        {
            'name': 'TENANT_B', 
            'headers': {
                'X-Tenant': 'TENANT_B',
                'X-Roles': 'Nurse',
                'X-Departments': 'Cardiology'
            }
        }
    ]
    
    endpoints = [
        '/config/effective/form/visit_opd/',
        '/clinical/patients/',
        '/clinical/visits/',
        '/orchestrator/notifications/',
        '/orchestrator/tasks/'
    ]
    
    for tenant in tenants:
        print(f"\n--- Testing {tenant['name']} ---")
        
        for endpoint in endpoints:
            try:
                response = requests.get(
                    f"{base_url}{endpoint}",
                    headers=tenant['headers'],
                    timeout=5
                )
                
                status = "✅" if response.status_code == 200 else "❌"
                print(f"{status} {endpoint}: {response.status_code}")
                
                if response.status_code == 200:
                    data = response.json()
                    if isinstance(data, list):
                        print(f"   Data count: {len(data)}")
                    elif isinstance(data, dict):
                        if 'fields' in data:
                            print(f"   Fields count: {len(data.get('fields', []))}")
                        elif 'name' in data:
                            print(f"   Name: {data.get('name')}")
                
            except requests.exceptions.RequestException as e:
                print(f"❌ {endpoint}: Connection error - {e}")
    
    print("\n=== Testing Rate Limiting ===")
    
    # Test rate limiting by making multiple requests
    tenant_headers = tenants[0]['headers']
    
    for i in range(5):
        try:
            response = requests.post(
                f"{base_url}/submission/submit-visit-opd/",
                headers={
                    **tenant_headers,
                    'Content-Type': 'application/json',
                    'Idempotency-Key': f'test-{i}'
                },
                json={
                    'external_id': f'TEST_PATIENT_{i}',
                    'name': f'Test Patient {i}',
                    'age': 30,
                    'height_cm': 170,
                    'weight_kg': 70,
                    'hba1c': 8.5
                },
                timeout=5
            )
            
            status = "✅" if response.status_code in [200, 201] else "❌"
            print(f"{status} Submit request {i+1}: {response.status_code}")
            
            if response.status_code == 429:
                print("   Rate limit hit!")
                break
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Submit request {i+1}: Connection error - {e}")
    
    print("\n=== UI Testing Complete ===")
    print("\nTo test from the UI:")
    print("1. Start the backend: python manage.py runserver")
    print("2. Start the frontend: cd client && npm run dev")
    print("3. Open http://localhost:5173")
    print("4. Use the Tenant Switcher in the top-right corner")
    print("5. Switch between different tenants and roles")
    print("6. Verify data isolation and RBAC behavior")

if __name__ == '__main__':
    test_ui_endpoints()
