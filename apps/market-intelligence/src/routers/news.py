from fastapi import APIRouter

from src.services.news_service import NewsService

router = APIRouter()

service = NewsService()


@router.get("/news")
def get_news(
    country: str = "us",
    category: str = "business",
):
    return service.get_latest(
        country=country,
        category=category,
    )
