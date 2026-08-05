from src.adapters.newsapi import NewsApiAdapter


class NewsProvider:
    """
    News Provider.
    """

    def __init__(self):
        self.adapter = NewsApiAdapter()

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
