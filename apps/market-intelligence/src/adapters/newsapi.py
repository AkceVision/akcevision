from src.adapters.base import BaseAdapter
from src.config import settings


class NewsApiAdapter(BaseAdapter):
    """
    Adapter for NewsAPI.
    """

    BASE_URL = settings.NEWS_API_URL

    def get_top_headlines(
        self,
        country: str = "us",
        category: str = "business",
    ):
        params = {
            "country": country,
            "category": category,
            "apiKey": settings.NEWS_API_KEY,
        }

        return self.client.get(
            self.BASE_URL,
            params=params,
        )
