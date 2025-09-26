import requests

BASE_URL = "http://localhost:8000"
VISITS_ENDPOINT = f"{BASE_URL}/api/clinical/visits/"
TIMEOUT = 30

def test_list_all_visits():
    headers = {
        "Accept": "application/json",
    }

    try:
        response = requests.get(VISITS_ENDPOINT, headers=headers, timeout=TIMEOUT)
        # Ensure HTTP 200 OK
        assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
        visits = response.json()
        # Validate response is a list
        assert isinstance(visits, list), f"Expected response type list, got {type(visits)}"
        # If the list is not empty, check that each visit has expected fields
        required_fields = {"id", "patient_id", "visit_date", "status"}
        for visit in visits:
            assert isinstance(visit, dict), "Each visit item should be a dict"
            missing_fields = required_fields - visit.keys()
            assert not missing_fields, f"Visit missing fields: {missing_fields}"

    except requests.RequestException as e:
        assert False, f"HTTP request failed: {e}"

test_list_all_visits()