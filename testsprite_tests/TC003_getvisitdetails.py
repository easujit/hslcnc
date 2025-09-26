import requests

BASE_URL = "http://localhost:8000"
VISITS_URL = f"{BASE_URL}/api/clinical/visits/"
TIMEOUT = 30

def test_getvisitdetails():
    # Helper function to create a visit (assuming minimal required fields)
    def create_visit():
        # Since no POST endpoint for creating visit specified in PRD,
        # create a new visit via the visits list endpoint if supported or
        # skip creation if API does not support visit creation here.
        # For this test, we'll assume creating a visit is not supported.
        # Instead, we fetch the list of visits and pick one.
        try:
            response = requests.get(VISITS_URL, timeout=TIMEOUT)
            response.raise_for_status()
            visits = response.json()
            if isinstance(visits, list) and len(visits) > 0:
                return visits[0]['id'] if 'id' in visits[0] else None
            return None
        except Exception:
            return None

    visit_id = create_visit()
    assert visit_id is not None, "No existing visit found to test with."

    try:
        # Test valid visit_id - expect 200 and valid visit details
        response = requests.get(f"{VISITS_URL}{visit_id}/", timeout=TIMEOUT)
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        visit_details = response.json()
        assert isinstance(visit_details, dict), "Visit details should be a dict"
        assert visit_details.get('id') == visit_id, "Returned visit_id does not match requested"

        # Test invalid visit_id - expect non-200 (404 or similar)
        invalid_visit_id = 999999999
        if invalid_visit_id == visit_id:
            invalid_visit_id += 1
        response_invalid = requests.get(f"{VISITS_URL}{invalid_visit_id}/", timeout=TIMEOUT)
        assert response_invalid.status_code != 200, "Expected non-200 status for invalid visit_id"
        # Optionally check for 404 specifically
        assert response_invalid.status_code in {400, 404}, f"Expected 400 or 404 for invalid visit_id, got {response_invalid.status_code}"

    except requests.RequestException as e:
        assert False, f"Request failed: {str(e)}"


test_getvisitdetails()