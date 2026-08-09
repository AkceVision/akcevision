from fastapi.testclient import TestClient

from src.main import app
from src.routers.crypto import get_crypto_service


class FakeCryptoService:
    def get_quote(self, symbol="bitcoin"):
        return {
            "symbol": symbol,
            "price": 65000,
            "currency": "USD",
        }

    def health_check(self):
        return {
            "provider": "FakeCrypto",
            "configured": True,
        }


app.dependency_overrides[get_crypto_service] = FakeCryptoService

client = TestClient(app)


def test_crypto():
    response = client.get("/crypto")

    assert response.status_code == 200

    body = response.json()

    assert body["symbol"] == "bitcoin"
    assert body["price"] == 65000


def test_crypto_health():
    response = client.get("/crypto/health")

    assert response.status_code == 200

    body = response.json()

    assert body["provider"] == "FakeCrypto"
    assert body["configured"] is True