from unittest.mock import MagicMock

from src.services.news_service import NewsService


def test_news_service_creation():
    """
    NewsService should be created successfully.
    """
    service = NewsService()

    assert service is not None


def test_get_latest_calls_provider():
    """
    NewsService should delegate to NewsProvider.
    """
    service = NewsService()

    service.provider = MagicMock()

    service.get_latest()

    service.provider.get_latest.assert_called_once()