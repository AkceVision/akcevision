from pydantic import BaseModel


class MarketQuote(BaseModel):
    """
    Standard market quote model.
    """

    symbol: str
    name: str | None = None
    price: float
    change: float | None = None
    change_percent: float | None = None
    currency: str | None = None
    exchange: str | None = None
    timestamp: str | None = None