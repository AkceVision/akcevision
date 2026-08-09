from fastapi.testclient import TestClient

from src.main import app
from src.models.market import MarketQuote
from src.routers.market import get_market_service


class FakeMarketService:
    def get_quote(self, symbol: str):
        return MarketQuote(
            symbol=symbol,
            price=123.45,
            change=1.25,
            change_percent=1.02,
        )


app.dependency_overrides[get_market_service] = FakeMarketService

client = TestClient(app)


def test_market():
    """
    Market endpoint should respond successfully.
    """

    response = client.get("/market?symbol=AAPL")

    assert response.status_code == 200

    body = response.json()

    assert body["symbol"] == "AAPL"
    assert body["price"] == 123.45
    assert body["change"] == 1.25
    assert body["change_percent"] == 1.02