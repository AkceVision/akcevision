from src.adapters.newsapi import NewsApiAdapter
from src.config import settings


class NewsProviderFactory:
    """
    Factory responsible for creating news providers.
    """

    @staticmethod
    def create():
        provider = settings.NEWS_PROVIDER.lower()

        if provider == "newsapi":
            return NewsApiAdapter()

        raise ValueError(
            f"Unsupported news provider: {provider}"
        )