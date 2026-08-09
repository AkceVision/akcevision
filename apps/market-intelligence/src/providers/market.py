from src.providers.factory import MarketProviderFactory


class MarketProvider:
    """
    Market Provider.
    """

    def __init__(self):
        self.adapter = MarketProviderFactory.create()

    def get_quote(
        self,
        symbol: str,
    ):
        """
        Get market quote.
        """
        return self.adapter.get_quote(symbol)