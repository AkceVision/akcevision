from src.adapters.alphavantage import AlphaVantageAdapter
from src.adapters.newsapi import NewsApiAdapter
from src.providers.factory import (
    MarketProviderFactory,
    NewsProviderFactory,
)


def test_news_provider_factory():
    """
    NewsProviderFactory should return NewsApiAdapter.
    """

    provider = NewsProviderFactory.create()

    assert isinstance(provider, NewsApiAdapter)


def test_market_provider_factory():
    """
    MarketProviderFactory should return AlphaVantageAdapter.
    """

    provider = MarketProviderFactory.create()

    assert isinstance(provider, AlphaVantageAdapter)