from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "AkceVision"
    assert data["service"] == "Gateway"
    assert data["status"] == "running"
    assert data["version"] == "0.1.0"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "UP"
    }
