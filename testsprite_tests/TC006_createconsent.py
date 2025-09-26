import requests

BASE_URL = "http://localhost:8000"
CONSENTS_ENDPOINT = f"{BASE_URL}/api/consent/consents/"
TIMEOUT = 30

def test_create_consent():
    # Example valid consent payload based on PRD schema
    consent_payload = {
        "patient_id": "patient-12345",
        "purpose": "treatment",
        "data_categories": ["medical_history", "prescriptions"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            CONSENTS_ENDPOINT,
            json=consent_payload,
            headers=headers,
            timeout=TIMEOUT
        )
        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        resp_json = response.json()
        # Validate response contains expected keys (at minimum)
        assert isinstance(resp_json, dict), "Response is not a JSON object"
        for key in ["patient_id", "purpose", "data_categories"]:
            assert key in resp_json, f"Response missing key: {key}"
        # Validate response values match input
        assert resp_json["patient_id"] == consent_payload["patient_id"], "patient_id mismatch"
        assert resp_json["purpose"] == consent_payload["purpose"], "purpose mismatch"
        assert resp_json["data_categories"] == consent_payload["data_categories"], "data_categories mismatch"

    except requests.RequestException as e:
        assert False, f"HTTP request failed: {e}"

test_create_consent()