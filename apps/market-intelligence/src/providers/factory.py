from src.adapters.alphavantage import AlphaVantageAdapter
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


class MarketProviderFactory:
    """
    Factory responsible for creating market providers.
    """

    @staticmethod
    def create():
        provider = settings.MARKET_PROVIDER.lower()

        if provider == "alphavantage":
            return AlphaVantageAdapter()

        raise ValueError(
            f"Unsupported market provider: {provider}"
        )