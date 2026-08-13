from pydantic import BaseModel, Field


class Holding(BaseModel):
    symbol: str = Field(min_length=1)
    quantity: float = Field(gt=0)
    average_price: float = Field(gt=0)
    currency: str = "USD"


class PortfolioCreate(BaseModel):
    name: str = Field(min_length=1)
    base_currency: str = "USD"


class Portfolio(BaseModel):
    id: str
    name: str
    base_currency: str
    holdings: list[Holding] = Field(default_factory=list)


class AllocationItem(BaseModel):
    symbol: str
    market_value: float
    allocation_percent: float


class PortfolioAllocation(BaseModel):
    portfolio_id: str
    total_value: float
    items: list[AllocationItem]


class ValuationItem(BaseModel):
    symbol: str
    quantity: float
    average_price: float
    current_price: float
    cost: float
    market_value: float
    unrealized_pnl: float
    return_percent: float


class PortfolioValuation(BaseModel):
    portfolio_id: str
    total_cost: float
    total_value: float
    unrealized_pnl: float
    return_percent: float
    items: list[ValuationItem]
