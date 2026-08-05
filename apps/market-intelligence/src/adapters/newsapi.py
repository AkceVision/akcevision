from src.clients.http_client import HttpClient
from src.config import settings


class NewsApiAdapter:
    """
    NewsAPI adapter.
    """

    BASE_URL = "https://newsapi.org/v2/top-headlines"

    def __init__(self):
        self.client = HttpClient()

    def get_top_headlines(self, country: str = "us", category: str = "business"):
        params = {
            "country": country,
            "category": category,
            "apiKey": settings.NEWS_API_KEY,
        }

        return self.client.get(
            self.BASE_URL,
            params=params,
        )
