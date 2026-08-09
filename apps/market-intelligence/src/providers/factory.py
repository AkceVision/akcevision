from src.adapters.alphavantage import AlphaVantageAdapter
from src.adapters.finnhub import FinnhubAdapter
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

        print(f"Market Provider Selected: {provider}")

        if provider == "alphavantage":
            return AlphaVantageAdapter()

        if provider == "finnhub":
            return FinnhubAdapter()

        raise ValueError(
            f"Unsupported market provider: {provider}"
        )