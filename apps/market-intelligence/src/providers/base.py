from abc import ABC, abstractmethod

from src.models.news import NewsItem


class BaseNewsProvider(ABC):
    """
    Base interface for all news providers.
    """

    @abstractmethod
    def get_latest(
        self,
        country: str = "us",
        category: str = "business",
    ) -> list[NewsItem]:
        """
        Return normalized news.
        """
        raise NotImplementedError