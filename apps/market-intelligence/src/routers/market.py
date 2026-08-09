from fastapi import APIRouter, Depends

from src.services.market_service import MarketService

router = APIRouter()


def get_market_service():
    """
    Dependency provider for MarketService.
    """
    return MarketService()


@router.get("/market")
def get_market(
    symbol: str = "AAPL",
    service: MarketService = Depends(get_market_service),
):
    """
    Get market quote.
    """
    return service.get_quote(symbol)


@router.get("/market/health")
def market_health(
    service: MarketService = Depends(get_market_service),
):
    """
    Market provider health.
    """
    return service.health_check()