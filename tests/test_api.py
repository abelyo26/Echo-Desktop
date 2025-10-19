from fastapi.testclient import TestClient
import sys
import os
import pytest

# Add the root directory to sys.path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import api


@pytest.fixture
def client():
    """Test client fixture for FastAPI app."""
    return TestClient(api)


def test_status_endpoint(client):
    """Test the /status endpoint."""
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "running"
    assert "version" in data


def test_devices_endpoint(client):
    """Test the /devices endpoint."""
    response = client.get("/devices")
    assert response.status_code == 200
    data = response.json()
    assert "devices" in data
    assert isinstance(data["devices"], list)
