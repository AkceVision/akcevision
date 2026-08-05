from fastapi import APIRouter

from src.services.news_service import NewsService

router = APIRouter()

service = NewsService()


@router.get("/news")
def get_news():
    return service.get_latest()
