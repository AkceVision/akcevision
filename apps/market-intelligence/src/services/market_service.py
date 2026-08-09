from src.providers.market import MarketProvider


class MarketService:
    """
    Market Service.
    """

    def __init__(self):
        self.provider = MarketProvider()

    def get_quote(
        self,
        symbol: str,
    ):
        """
        Get market quote.
        """
        return self.provider.get_quote(symbol)