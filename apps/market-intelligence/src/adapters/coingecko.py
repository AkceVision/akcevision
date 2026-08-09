from src.adapters.base import BaseAdapter
from src.config import settings
from src.models.crypto import CryptoQuote


class CoinGeckoAdapter(BaseAdapter):
    """
    Adapter for CoinGecko.
    """

    BASE_URL = settings.COINGECKO_URL

    def get_quote(
        self,
        symbol: str,
    ) -> CryptoQuote:
        """
        Get latest crypto quote.
        """

        response = self.client.get(
            self.BASE_URL,
            params={
                "ids": symbol,
                "vs_currencies": "usd",
                "include_24hr_change": "true",
                "include_market_cap": "true",
                "include_24hr_vol": "true",
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
    ) -> CryptoQuote:
        """
        Convert CoinGecko response into CryptoQuote.
        """

        quote = response.get(symbol, {})

        return CryptoQuote(
            symbol=symbol,
            price=float(quote.get("usd", 0)),
            market_cap=float(quote.get("usd_market_cap", 0)),
            volume_24h=float(quote.get("usd_24h_vol", 0)),
            change_percent_24h=float(
                quote.get("usd_24h_change", 0)
            ),
            currency="USD",
        )