from src.providers.news import NewsProvider


class NewsService:
    """
    News Service.
    """

    def __init__(self):
        self.provider = NewsProvider()

    def get_latest(
        self,
        country: str = "us",
        category: str = "business",
    ):
        return self.provider.get_latest(
            country=country,
            category=category,
        )

    def health_check(self):
        return self.provider.health_check()
