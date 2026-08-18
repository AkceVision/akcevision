from src.models.portfolio import Holding
from src.repositories.portfolio_repository import PortfolioRepository


def test_portfolio_persists_between_repository_instances(tmp_path):
    db_path = tmp_path / "portfolio.db"

    repository = PortfolioRepository(str(db_path))

    portfolio = repository.create(
        name="Persistent Portfolio",
        base_currency="USD",
    )

    repository.add_holding(
        portfolio.id,
        Holding(
            symbol="AAPL",
            quantity=10,
            average_price=200,
            currency="USD",
        ),
    )

    new_repository = PortfolioRepository(str(db_path))

    restored = new_repository.get(portfolio.id)

    assert restored is not None
    assert restored.id == portfolio.id
    assert restored.name == "Persistent Portfolio"
    assert restored.base_currency == "USD"

    assert len(restored.holdings) == 1
    assert restored.holdings[0].symbol == "AAPL"
    assert restored.holdings[0].quantity == 10
    assert restored.holdings[0].average_price == 200
    assert restored.holdings[0].currency == "USD"
