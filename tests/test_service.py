import pytest
from app.main import app


@pytest.fixture
def client():
    """Configures a Flask test client for the suite."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Ensure the monitoring health check is operational."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


@pytest.mark.parametrize(
    "url, expected_safe, expected_action",
    [
        ("google.com/search", True, "ALLOW"),  # Known safe URL
        ("malware.com/bad-file.exe", False, "BLOCK"),  # Exact match malware
        ("mypagina.com/anything/else", False, "BLOCK"),  # Prefix match malware
        ("unsafe.biz:8080/virus", False, "BLOCK"),  # Malware with port
    ],
)
def test_url_lookup_logic(client, url, expected_safe, expected_action):
    """
    Test various URL scenarios including exact matches,
    prefix matches, and safe URLs.
    """
    response = client.get(f"/urlinfo/1/{url}")

    assert response.status_code == 200
    data = response.get_json()

    # Assert JSON structure and logic
    assert "is_safe" in data
    assert "action" in data
    assert data["is_safe"] == expected_safe
    assert data["action"] == expected_action
    assert url in data["url_checked"]


def test_404_on_invalid_route(client):
    """Ensure the API returns 404 for malformed versions or routes."""
    response = client.get("/urlinfo/v2/google.com")
    assert response.status_code == 404
