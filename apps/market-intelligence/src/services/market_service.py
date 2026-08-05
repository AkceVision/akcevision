from src.providers.market import MarketProvider


class MarketService:
    def __init__(self):
        self.provider = MarketProvider()
