from unittest.mock import MagicMock

from src.providers.news import NewsProvider


def test_news_provider_creation():
    """
    NewsProvider should be created successfully.
    """
    provider = NewsProvider()

    assert provider is not None


def test_get_latest_calls_adapter():
    """
    NewsProvider should delegate to adapter.
    """
    provider = NewsProvider()

    provider.adapter = MagicMock()

    provider.get_latest()

    provider.adapter.get_top_headlines.assert_called_once()