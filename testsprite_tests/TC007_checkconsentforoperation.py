import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_check_consent_for_operation():
    headers = {
        "Content-Type": "application/json"
    }

    # Use a valid patient_id string as per PRD
    consent_create_url = f"{BASE_URL}/api/consent/consents/"
    consent_data = {
        "patient_id": "patient123",
        "purpose": "treatment",
        "data_categories": ["demographics", "medical_history"]
    }

    try:
        # Create a new consent
        resp_create = requests.post(consent_create_url, json=consent_data, headers=headers, timeout=TIMEOUT)
        assert resp_create.status_code == 201, f"Consent creation failed with status {resp_create.status_code}"
        patient_id = consent_data["patient_id"]

        check_url = f"{BASE_URL}/api/consent/consent/check/"
        check_payload = {
            "patient_id": patient_id,
            "purpose": "treatment",
            "data_categories": ["demographics", "medical_history"],
            "action": "read"
        }

        resp_check = requests.post(check_url, json=check_payload, headers=headers, timeout=TIMEOUT)
        assert resp_check.status_code == 200, f"Consent check failed with status {resp_check.status_code}"
        check_result = resp_check.json()
        assert isinstance(check_result, dict), "Response is not a JSON object"

    finally:
        # Cleanup: no delete endpoint documented
        pass

test_check_consent_for_operation()
