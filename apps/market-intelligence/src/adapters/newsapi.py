from src.adapters.base import BaseAdapter
from src.config import settings
from src.models.news import NewsItem


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

        response = self.client.get(
            self.BASE_URL,
            params=params,
        )

        articles = response.get("articles", [])

        return [
            self.map_article(article)
            for article in articles
        ]

    def health_check(self):
        return {
            "provider": "NewsAPI",
            "base_url": self.BASE_URL,
            "configured": bool(settings.NEWS_API_KEY),
        }

    def map_article(self, article: dict) -> NewsItem:
        """
        Convert NewsAPI article to AkceVision NewsItem model.
        """
        return NewsItem(
            title=article.get("title", ""),
            description=article.get("description"),
            url=article.get("url", ""),
            image_url=article.get("urlToImage"),
            source=article.get("source", {}).get("name", "Unknown"),
            published_at=article.get("publishedAt", ""),
        )