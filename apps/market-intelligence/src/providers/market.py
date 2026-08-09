from src.adapters.alphavantage import AlphaVantageAdapter


class MarketProvider:
    """
    Market Provider.
    """

    def __init__(self):
        self.adapter = AlphaVantageAdapter()

    def get_quote(
        self,
        symbol: str,
    ):
        """
        Get market quote.
        """
        return self.adapter.get_quote(symbol)