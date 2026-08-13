import pytest

from fastapi.testclient import TestClient

from src.main import app
from src.models.portfolio import Holding


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_portfolio():
    response = client.post(
        "/portfolio",
        json={
            "name": "Demo Portfolio",
            "base_currency": "USD",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Demo Portfolio"
    assert data["base_currency"] == "USD"
    assert data["holdings"] == []
    assert "id" in data


def test_add_holding():
    portfolio = client.post(
        "/portfolio",
        json={
            "name": "Investment Portfolio",
            "base_currency": "USD",
        },
    ).json()

    response = client.post(
        f"/portfolio/{portfolio['id']}/holdings",
        json={
            "symbol": "AAPL",
            "quantity": 10,
            "average_price": 200,
            "currency": "USD",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["holdings"]) == 1
    assert data["holdings"][0]["symbol"] == "AAPL"
    assert data["holdings"][0]["quantity"] == 10


def test_portfolio_allocation():
    portfolio = client.post(
        "/portfolio",
        json={
            "name": "Allocation Portfolio",
            "base_currency": "USD",
        },
    ).json()

    portfolio_id = portfolio["id"]

    client.post(
        f"/portfolio/{portfolio_id}/holdings",
        json={
            "symbol": "AAPL",
            "quantity": 10,
            "average_price": 200,
            "currency": "USD",
        },
    )

    client.post(
        f"/portfolio/{portfolio_id}/holdings",
        json={
            "symbol": "MSFT",
            "quantity": 5,
            "average_price": 200,
            "currency": "USD",
        },
    )

    response = client.get(
        f"/portfolio/{portfolio_id}/allocation"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_value"] == 3000
    assert len(data["items"]) == 2
    assert data["items"][0]["allocation_percent"] == pytest.approx(66.66666666666667)
    assert data["items"][1]["allocation_percent"] == pytest.approx(33.333333333333336)


def test_portfolio_valuation_multiple_holdings():
    class FakeMarketClient:
        prices = {
            "AAPL": 300.0,
            "MSFT": 400.0,
            "NVDA": 500.0,
        }

        def get_quote(self, symbol: str):
            return {
                "symbol": symbol,
                "price": self.prices[symbol],
            }

    portfolio = client.post(
        "/portfolio",
        json={
            "name": "Multi Asset Portfolio",
            "base_currency": "USD",
        },
    ).json()

    portfolio_id = portfolio["id"]

    holdings = [
        {
            "symbol": "AAPL",
            "quantity": 10,
            "average_price": 200,
            "currency": "USD",
        },
        {
            "symbol": "MSFT",
            "quantity": 5,
            "average_price": 300,
            "currency": "USD",
        },
        {
            "symbol": "NVDA",
            "quantity": 2,
            "average_price": 400,
            "currency": "USD",
        },
    ]

    for holding in holdings:
        response = client.post(
            f"/portfolio/{portfolio_id}/holdings",
            json=holding,
        )
        assert response.status_code == 200

    from src.routers.portfolio import get_portfolio_service

    service = get_portfolio_service()

    valuation = service.get_valuation(
        portfolio_id,
        market_client=FakeMarketClient(),
    )

    assert valuation is not None

    assert valuation.total_cost == pytest.approx(4300.0)
    assert valuation.total_value == pytest.approx(6000.0)
    assert valuation.unrealized_pnl == pytest.approx(1700.0)
    assert valuation.return_percent == pytest.approx(39.5348837209)

    assert len(valuation.items) == 3

    assert valuation.items[0].symbol == "AAPL"
    assert valuation.items[0].market_value == pytest.approx(3000.0)
    assert valuation.items[0].unrealized_pnl == pytest.approx(1000.0)

    assert valuation.items[1].symbol == "MSFT"
    assert valuation.items[1].market_value == pytest.approx(2000.0)
    assert valuation.items[1].unrealized_pnl == pytest.approx(500.0)

    assert valuation.items[2].symbol == "NVDA"
    assert valuation.items[2].market_value == pytest.approx(1000.0)
    assert valuation.items[2].unrealized_pnl == pytest.approx(200.0)


def test_portfolio_live_allocation():
    class FakeMarketClient:
        prices = {
            "AAPL": 300.0,
            "MSFT": 400.0,
            "NVDA": 500.0,
        }

        def get_quote(self, symbol: str):
            return {
                "symbol": symbol,
                "price": self.prices[symbol],
            }

    portfolio = client.post(
        "/portfolio",
        json={
            "name": "Live Allocation Portfolio",
            "base_currency": "USD",
        },
    ).json()

    portfolio_id = portfolio["id"]

    for holding in [
        {
            "symbol": "AAPL",
            "quantity": 10,
            "average_price": 200,
            "currency": "USD",
        },
        {
            "symbol": "MSFT",
            "quantity": 5,
            "average_price": 300,
            "currency": "USD",
        },
        {
            "symbol": "NVDA",
            "quantity": 2,
            "average_price": 400,
            "currency": "USD",
        },
    ]:
        response = client.post(
            f"/portfolio/{portfolio_id}/holdings",
            json=holding,
        )
        assert response.status_code == 200

    from src.routers.portfolio import get_portfolio_service

    service = get_portfolio_service()

    allocation = service.get_live_allocation(
        portfolio_id,
        market_client=FakeMarketClient(),
    )

    assert allocation is not None
    assert allocation.total_value == pytest.approx(6000.0)
    assert len(allocation.items) == 3

    assert allocation.items[0].symbol == "AAPL"
    assert allocation.items[0].market_value == pytest.approx(3000.0)
    assert allocation.items[0].allocation_percent == pytest.approx(50.0)

    assert allocation.items[1].symbol == "MSFT"
    assert allocation.items[1].market_value == pytest.approx(2000.0)
    assert allocation.items[1].allocation_percent == pytest.approx(
        33.3333333333
    )

    assert allocation.items[2].symbol == "NVDA"
    assert allocation.items[2].market_value == pytest.approx(1000.0)
    assert allocation.items[2].allocation_percent == pytest.approx(
        16.6666666667
    )


def test_portfolio_live_allocation_endpoint():
    class FakeMarketClient:
        prices = {
            "AAPL": 300.0,
            "MSFT": 400.0,
            "NVDA": 500.0,
        }

        def get_quote(self, symbol: str):
            return {
                "symbol": symbol,
                "price": self.prices[symbol],
            }

    from src.routers.portfolio import get_portfolio_service

    service = get_portfolio_service()

    portfolio = service.create_portfolio(
        name="Live Allocation API Portfolio",
        base_currency="USD",
    )

    for holding in [
        {
            "symbol": "AAPL",
            "quantity": 10,
            "average_price": 200,
            "currency": "USD",
        },
        {
            "symbol": "MSFT",
            "quantity": 5,
            "average_price": 300,
            "currency": "USD",
        },
        {
            "symbol": "NVDA",
            "quantity": 2,
            "average_price": 400,
            "currency": "USD",
        },
    ]:
        service.add_holding(
            portfolio.id,
            Holding(**holding),
        )

    original_method = service.get_live_allocation

    def fake_live_allocation(portfolio_id):
        return original_method(
            portfolio_id,
            market_client=FakeMarketClient(),
        )

    service.get_live_allocation = fake_live_allocation

    response = client.get(
        f"/portfolio/{portfolio.id}/allocation/live"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total_value"] == pytest.approx(6000.0)
    assert data["items"][0]["symbol"] == "AAPL"
    assert data["items"][0]["allocation_percent"] == pytest.approx(50.0)
    assert data["items"][1]["allocation_percent"] == pytest.approx(
        33.3333333333
    )
    assert data["items"][2]["allocation_percent"] == pytest.approx(
        16.6666666667
    )
