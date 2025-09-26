import requests

BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def test_listallconsents():
    url = f"{BASE_URL}/api/consent/consents/"
    headers = {
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        data = response.json()
        assert isinstance(data, list), "Response JSON is not a list"
    except requests.RequestException as e:
        assert False, f"Request failed: {e}"

test_listallconsents()