from pydantic import BaseModel


class CryptoQuote(BaseModel):
    """
    Standard crypto quote model.
    """

    symbol: str
    name: str | None = None
    price: float
    market_cap: float | None = None
    volume_24h: float | None = None
    change_percent_24h: float | None = None
    currency: str = "USD"
    timestamp: str | None = None