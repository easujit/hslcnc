import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30
HEADERS = {
    "Content-Type": "application/json"
}

def test_updatevisitstatus():
    # Step 1: Get the list of visits to obtain a visit_id
    list_visits_url = f"{BASE_URL}/api/clinical/visits/"
    list_response = requests.get(list_visits_url, headers=HEADERS, timeout=TIMEOUT)
    assert list_response.status_code == 200, f"Failed to list visits, status code: {list_response.status_code}"
    visits = list_response.json()
    assert isinstance(visits, list) and len(visits) > 0, "No visits available to test update status."
    visit_id = visits[0].get('id')
    assert isinstance(visit_id, int), "Visit ID not found or invalid in list."

    # Step 2: Update visit status
    update_url = f"{BASE_URL}/api/clinical/visits/{visit_id}/update-status/"
    update_payload = {
        "status": "completed"
    }
    update_response = requests.post(update_url, json=update_payload, headers=HEADERS, timeout=TIMEOUT)
    assert update_response.status_code == 200, f"Update status failed, status code: {update_response.status_code}"

    # Optional: Verify the status was updated by fetching the visit details
    get_url = f"{BASE_URL}/api/clinical/visits/{visit_id}/"
    get_response = requests.get(get_url, headers=HEADERS, timeout=TIMEOUT)
    assert get_response.status_code == 200, f"Getting visit details failed, status code: {get_response.status_code}"
    visit_details = get_response.json()
    assert visit_details.get("status") == "completed", f"Visit status not updated, actual status: {visit_details.get('status')}"


test_updatevisitstatus()
