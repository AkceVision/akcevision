from src.providers.news import NewsProvider


class NewsService:
    def __init__(self):
        self.provider = NewsProvider()
