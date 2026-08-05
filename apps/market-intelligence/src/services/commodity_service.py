from src.providers.commodity import CommodityProvider


class CommodityService:
    def __init__(self):
        self.provider = CommodityProvider()

    def get_prices(self):
        return self.provider.get_prices()
