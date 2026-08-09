from fastapi import APIRouter, Depends

from src.services.macro_service import MacroService

router = APIRouter()


def get_macro_service():
    """
    Dependency provider for MacroService.
    """
    return MacroService()


@router.get("/macro")
def get_macro(
    indicator: str = "FEDFUNDS",
    service: MacroService = Depends(get_macro_service),
):
    """
    Get macroeconomic indicator.
    """
    return service.get_indicator(indicator)


@router.get("/macro/health")
def macro_health(
    service: MacroService = Depends(get_macro_service),
):
    """
    Macro provider health.
    """
    return service.health_check()