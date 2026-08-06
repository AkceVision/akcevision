from src.providers.base import BaseNewsProvider
from src.providers.factory import NewsProviderFactory


class NewsProvider(BaseNewsProvider):
    """
    News Provider.
    """

    def __init__(self):
        self.adapter = NewsProviderFactory.create()

    def get_latest(
        self,
        country: str = "us",
        category: str = "business",
    ):
        return self.adapter.get_top_headlines(
            country=country,
            category=category,
        )

    def health_check(self):
        return self.adapter.health_check()