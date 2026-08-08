from fastapi.testclient import TestClient

from src.main import app
from src.routers.news import get_news_service


class FakeNewsService:
    def get_latest(self, country="us", category="business"):
        return []

    def health_check(self):
        return {
            "provider": "Fake",
            "configured": True,
        }


app.dependency_overrides[get_news_service] = FakeNewsService

client = TestClient(app)


def test_root():
    """
    Root endpoint should return service information.
    """
    response = client.get("/")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "running"
    assert "service" in body
    assert "version" in body


def test_news():
    """
    News endpoint should respond successfully.
    """
    response = client.get("/news")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "success"
    assert body["count"] == 0
    assert body["data"] == []


def test_news_health():
    """
    News health endpoint should respond successfully.
    """
    response = client.get("/news/health")

    assert response.status_code == 200

    body = response.json()

    assert body["provider"] == "Fake"
    assert body["configured"] is True