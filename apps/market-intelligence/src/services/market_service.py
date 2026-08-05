from src.providers.market import MarketProvider


class MarketService:
    def __init__(self):
        self.provider = MarketProvider()

def get_market(self):
    return self.provider.get_market()
