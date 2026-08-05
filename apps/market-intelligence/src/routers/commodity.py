from fastapi import APIRouter

from src.services.commodity_service import CommodityService

router = APIRouter()

service = CommodityService()


@router.get("/commodities")
def get_commodities():
    return service.get_commodities()
