from src.providers.commodity import CommodityProvider


class CommodityService:
    def __init__(self):
        self.provider = CommodityProvider()
