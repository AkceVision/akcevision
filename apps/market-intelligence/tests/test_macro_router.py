from fastapi.testclient import TestClient

from src.main import app
from src.routers.macro import get_macro_service


class FakeMacroService:
    def get_indicator(self, indicator="FEDFUNDS"):
        return {
            "indicator": indicator,
            "value": 4.25,
            "unit": "Percent",
            "country": "US",
            "date": "2026-08-01",
        }

    def health_check(self):
        return {
            "provider": "FakeFred",
            "configured": True,
        }


app.dependency_overrides[get_macro_service] = FakeMacroService

client = TestClient(app)


def test_macro():
    response = client.get("/macro")

    assert response.status_code == 200

    body = response.json()

    assert body["indicator"] == "FEDFUNDS"
    assert body["value"] == 4.25


def test_macro_health():
    response = client.get("/macro/health")

    assert response.status_code == 200

    body = response.json()

    assert body["provider"] == "FakeFred"
    assert body["configured"] is True