from src.providers.news import NewsProvider


class NewsService:
    def __init__(self):
        self.provider = NewsProvider()

def get_news(self):
    return self.provider.get_news()
