from src.adapters.coingecko import CoinGeckoAdapter


class CryptoProvider:
    """
    Crypto Provider.
    """

    def __init__(self):
        self.adapter = CoinGeckoAdapter()

    def get_quote(
        self,
        symbol: str,
    ):
        """
        Get crypto quote.
        """
        return self.adapter.get_quote(symbol)

    def health_check(self):
        """
        Crypto provider health.
        """
        return {
            "provider": self.adapter.__class__.__name__,
            "configured": True,
        }