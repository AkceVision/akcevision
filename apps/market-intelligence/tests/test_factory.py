from src.adapters.alphavantage import AlphaVantageAdapter
from src.adapters.finnhub import FinnhubAdapter
from src.adapters.newsapi import NewsApiAdapter
from src.config import settings
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


def test_market_provider_factory_alphavantage():
    """
    MarketProviderFactory should return AlphaVantageAdapter.
    """

    original = settings.MARKET_PROVIDER

    try:
        settings.MARKET_PROVIDER = "alphavantage"

        provider = MarketProviderFactory.create()

        assert isinstance(provider, AlphaVantageAdapter)

    finally:
        settings.MARKET_PROVIDER = original


def test_market_provider_factory_finnhub():
    """
    MarketProviderFactory should return FinnhubAdapter.
    """

    original = settings.MARKET_PROVIDER

    try:
        settings.MARKET_PROVIDER = "finnhub"

        provider = MarketProviderFactory.create()

        assert isinstance(provider, FinnhubAdapter)

    finally:
        settings.MARKET_PROVIDER = original