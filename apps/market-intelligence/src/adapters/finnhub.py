from src.adapters.base import BaseAdapter
from src.config import settings
from src.models.market import MarketQuote


class FinnhubAdapter(BaseAdapter):
    """
    Adapter for Finnhub.
    """

    BASE_URL = settings.FINNHUB_URL

    def get_quote(
        self,
        symbol: str,
    ) -> MarketQuote:
        """
        Get latest market quote from Finnhub.
        """

        response = self.client.get(
            self.BASE_URL,
            params={
                "symbol": symbol,
                "token": settings.FINNHUB_API_KEY,
            },
        )

        return self.map_quote(
            symbol,
            response,
        )

    def map_quote(
        self,
        symbol: str,
        response: dict,
    ) -> MarketQuote:
        """
        Convert Finnhub response into MarketQuote.
        """

        return MarketQuote(
            symbol=symbol,
            price=float(response.get("c", 0)),
            change=float(response.get("d", 0)),
            change_percent=float(response.get("dp", 0)),
        )