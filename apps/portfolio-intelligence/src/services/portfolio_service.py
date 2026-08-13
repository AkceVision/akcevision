from src.models.portfolio import (
    AllocationItem,
    Holding,
    Portfolio,
    PortfolioAllocation,
    PortfolioValuation,
    ValuationItem,
)
from src.repositories.portfolio_repository import PortfolioRepository
from src.clients.market_intelligence import MarketIntelligenceClient


class PortfolioService:
    def __init__(self, repository: PortfolioRepository | None = None):
        self.repository = repository or PortfolioRepository()

    def create_portfolio(
        self,
        name: str,
        base_currency: str,
    ) -> Portfolio:
        return self.repository.create(name, base_currency)

    def get_portfolio(
        self,
        portfolio_id: str,
    ) -> Portfolio | None:
        return self.repository.get(portfolio_id)

    def add_holding(
        self,
        portfolio_id: str,
        holding: Holding,
    ) -> Portfolio | None:
        return self.repository.add_holding(portfolio_id, holding)

    def get_allocation(
        self,
        portfolio_id: str,
    ) -> PortfolioAllocation | None:
        portfolio = self.repository.get(portfolio_id)

        if portfolio is None:
            return None

        values = [
            holding.quantity * holding.average_price
            for holding in portfolio.holdings
        ]

        total_value = sum(values)

        items = []

        for holding, value in zip(portfolio.holdings, values):
            allocation = (
                (value / total_value) * 100
                if total_value > 0
                else 0
            )

            items.append(
                AllocationItem(
                    symbol=holding.symbol,
                    market_value=value,
                    allocation_percent=allocation,
                )
            )

        return PortfolioAllocation(
            portfolio_id=portfolio.id,
            total_value=total_value,
            items=items,
        )


    def get_live_allocation(
        self,
        portfolio_id: str,
        market_client: MarketIntelligenceClient | None = None,
    ) -> PortfolioAllocation | None:
        portfolio = self.repository.get(portfolio_id)

        if portfolio is None:
            return None

        client = market_client or MarketIntelligenceClient()

        values = []
        for holding in portfolio.holdings:
            quote = client.get_quote(holding.symbol)
            current_price = float(quote["price"])
            values.append(holding.quantity * current_price)

        total_value = sum(values)

        items = []

        for holding, value in zip(portfolio.holdings, values):
            allocation = (
                (value / total_value) * 100
                if total_value > 0
                else 0
            )

            items.append(
                AllocationItem(
                    symbol=holding.symbol,
                    market_value=value,
                    allocation_percent=allocation,
                )
            )

        return PortfolioAllocation(
            portfolio_id=portfolio.id,
            total_value=total_value,
            items=items,
        )


    def get_valuation(
        self,
        portfolio_id: str,
        market_client: MarketIntelligenceClient | None = None,
    ) -> PortfolioValuation | None:
        portfolio = self.repository.get(portfolio_id)

        if portfolio is None:
            return None

        client = market_client or MarketIntelligenceClient()

        items = []
        total_cost = 0.0
        total_value = 0.0

        for holding in portfolio.holdings:
            quote = client.get_quote(holding.symbol)
            current_price = float(quote["price"])

            cost = holding.quantity * holding.average_price
            market_value = holding.quantity * current_price
            pnl = market_value - cost

            total_cost += cost
            total_value += market_value

            return_percent = (
                (pnl / cost) * 100
                if cost > 0
                else 0
            )

            items.append(
                ValuationItem(
                    symbol=holding.symbol,
                    quantity=holding.quantity,
                    average_price=holding.average_price,
                    current_price=current_price,
                    cost=cost,
                    market_value=market_value,
                    unrealized_pnl=pnl,
                    return_percent=return_percent,
                )
            )

        total_pnl = total_value - total_cost

        total_return = (
            (total_pnl / total_cost) * 100
            if total_cost > 0
            else 0
        )

        return PortfolioValuation(
            portfolio_id=portfolio.id,
            total_cost=total_cost,
            total_value=total_value,
            unrealized_pnl=total_pnl,
            return_percent=total_return,
            items=items,
        )
