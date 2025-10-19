import requests

def test_status_code():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200
