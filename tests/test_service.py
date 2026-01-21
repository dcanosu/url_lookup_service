import pytest
from app.main import app

@pytest.fixture
def client():
    # This sets up a "virtual" browser to test our API
    with app.test_client() as client:
        yield client

def test_safe_url(client):
    """Test a URL that is NOT in the malware list"""
    response = client.get('/urlinfo/1/google.com/search')
    assert response.status_code == 200
    assert response.json['is_safe'] is True
    assert response.json['action'] == "ALLOW"

def test_malicious_url(client):
    """Test a URL that IS in the malware list"""
    response = client.get('/urlinfo/1/malware.com/bad-file.exe')
    assert response.status_code == 200
    assert response.json['is_safe'] is False
    assert response.json['action'] == "BLOCK"