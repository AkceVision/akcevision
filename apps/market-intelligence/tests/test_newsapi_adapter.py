from unittest.mock import MagicMock

from src.adapters.newsapi import NewsApiAdapter
from src.models.news import NewsItem


def test_map_article():
    """
    NewsAPI article should be converted to NewsItem.
    """

    adapter = NewsApiAdapter()

    article = {
        "title": "Apple launches new AI",
        "description": "Apple announced new AI features.",
        "url": "https://example.com/news",
        "urlToImage": "https://example.com/image.jpg",
        "publishedAt": "2026-08-09T10:00:00Z",
        "source": {
            "name": "Reuters"
        },
    }

    news = adapter.map_article(article)

    assert isinstance(news, NewsItem)
    assert news.title == "Apple launches new AI"
    assert news.source == "Reuters"
    assert news.url == "https://example.com/news"


def test_get_top_headlines():
    """
    Adapter should convert NewsAPI response into NewsItem list.
    """

    adapter = NewsApiAdapter()

    adapter.client = MagicMock()

    adapter.client.get.return_value = {
        "articles": [
            {
                "title": "Tesla rises",
                "description": "Tesla stock jumps.",
                "url": "https://example.com/tesla",
                "urlToImage": None,
                "publishedAt": "2026-08-09",
                "source": {
                    "name": "Bloomberg"
                },
            }
        ]
    }

    result = adapter.get_top_headlines()

    assert len(result) == 1
    assert isinstance(result[0], NewsItem)
    assert result[0].title == "Tesla rises"

    adapter.client.get.assert_called_once()