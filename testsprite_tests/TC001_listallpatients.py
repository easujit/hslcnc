import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_list_all_patients():
    url = f"{BASE_URL}/api/clinical/patients/"
    headers = {
        "Accept": "application/json",
    }
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        patients = response.json()
        assert isinstance(patients, list), "Response JSON is not a list"

        # If there are patients, check data fields in the first patient
        if patients:
            patient = patients[0]
            assert isinstance(patient, dict), "Patient item is not a dict"
            # Check for expected core fields; external_id and name as example fields from PRD
            expected_fields = ["external_id", "name"]
            for field in expected_fields:
                assert field in patient, f"Field '{field}' missing in patient data"
                assert patient[field] is not None, f"Field '{field}' is None in patient data"

    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

test_list_all_patients()