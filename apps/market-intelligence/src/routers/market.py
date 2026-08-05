from fastapi import APIRouter

from src.services.market_service import MarketService

router = APIRouter()

service = MarketService()


@router.get("/market")
def get_market():
    return service.get_quotes()
