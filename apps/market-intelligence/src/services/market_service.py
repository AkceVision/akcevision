from src.providers.market import MarketProvider


class MarketService:
    def __init__(self):
        self.provider = MarketProvider()

    def get_quotes(self):
        return self.provider.get_quotes()
