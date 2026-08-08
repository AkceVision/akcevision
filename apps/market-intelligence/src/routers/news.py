from fastapi import APIRouter, Depends

from src.models.news import NewsResponse
from src.services.news_service import NewsService

router = APIRouter()


def get_news_service():
    """
    Dependency provider for NewsService.
    """
    return NewsService()


@router.get("/news")
def get_news(
    country: str = "us",
    category: str = "business",
    service: NewsService = Depends(get_news_service),
):
    news = service.get_latest(
        country=country,
        category=category,
    )

    return NewsResponse(
        status="success",
        count=len(news),
        data=news,
    )


@router.get("/news/health")
def news_health(
    service: NewsService = Depends(get_news_service),
):
    return service.health_check()