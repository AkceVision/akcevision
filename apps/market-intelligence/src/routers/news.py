from fastapi import APIRouter

from src.models.news import NewsResponse
from src.services.news_service import NewsService

router = APIRouter()

service = NewsService()


@router.get("/news")
def get_news(
    country: str = "us",
    category: str = "business",
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
def news_health():
    return service.health_check()