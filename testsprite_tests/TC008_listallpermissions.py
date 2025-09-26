import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_list_all_permissions():
    url = f"{BASE_URL}/api/policies/permissions/"
    headers = {
        "Accept": "application/json",
    }
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as e:
        assert False, f"Request to list permissions failed: {e}"

    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    try:
        permissions = response.json()
    except ValueError:
        assert False, "Response is not valid JSON"

    assert isinstance(permissions, list), "Response JSON is not a list of permissions"

    # Optional: ensure list is not empty
    assert permissions, "Permissions list is empty"

    # Optional: check first item type is dict or str
    first_item = permissions[0]
    assert isinstance(first_item, (dict, str)), "Permission item type is unexpected"

test_list_all_permissions()
