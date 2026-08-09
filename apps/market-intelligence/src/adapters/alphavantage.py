from src.adapters.base import BaseAdapter
from src.config import settings
from src.models.market import MarketQuote


class AlphaVantageAdapter(BaseAdapter):
    """
    Adapter for Alpha Vantage.
    """

    BASE_URL = settings.ALPHA_VANTAGE_URL

    def get_quote(
        self,
        symbol: str,
    ) -> MarketQuote:
        """
        Get latest market quote from Alpha Vantage.
        """

        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": settings.ALPHA_VANTAGE_API_KEY,
        }

        response = self.client.get(
            self.BASE_URL,
            params=params,
        )

        return self.map_quote(response)

    def map_quote(
        self,
        response: dict,
    ) -> MarketQuote:
        """
        Convert Alpha Vantage response into MarketQuote.
        """

        quote = response.get("Global Quote", {})

        return MarketQuote(
            symbol=quote.get("01. symbol", ""),
            price=float(quote.get("05. price", 0)),
            change=float(quote.get("09. change", 0)),
            change_percent=float(
                quote.get("10. change percent", "0").replace("%", "")
            ),
        )