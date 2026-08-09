from fastapi import APIRouter, Depends

from src.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="",
    tags=["Analysis"],
)


def get_analysis_service():
    """
    Dependency provider for AnalysisService.
    """
    return AnalysisService()


@router.get("/analysis")
def analyze(
    symbol: str = "AAPL",
    service: AnalysisService = Depends(get_analysis_service),
):
    """
    Generate an AI-powered financial analysis.
    """
    return service.analyze(symbol)


@router.get("/analysis/health")
def analysis_health(
    service: AnalysisService = Depends(get_analysis_service),
):
    """
    Analysis service health.
    """
    return service.health_check()