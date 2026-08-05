from src.adapters.newsapi import NewsApiAdapter


class NewsProvider:
    """
    Base News Provider.
    """

    def __init__(self):
        self.adapter = NewsApiAdapter()

    def get_latest(self):
        return self.adapter.get_top_headlines()
