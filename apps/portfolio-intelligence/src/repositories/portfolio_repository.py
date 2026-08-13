from uuid import uuid4

from src.models.portfolio import Holding, Portfolio


class PortfolioRepository:
    def __init__(self):
        self._portfolios: dict[str, Portfolio] = {}

    def create(self, name: str, base_currency: str) -> Portfolio:
        portfolio = Portfolio(
            id=str(uuid4()),
            name=name,
            base_currency=base_currency,
            holdings=[],
        )
        self._portfolios[portfolio.id] = portfolio
        return portfolio

    def get(self, portfolio_id: str) -> Portfolio | None:
        return self._portfolios.get(portfolio_id)

    def add_holding(self, portfolio_id: str, holding: Holding) -> Portfolio | None:
        portfolio = self._portfolios.get(portfolio_id)

        if portfolio is None:
            return None

        portfolio.holdings.append(holding)
        return portfolio
