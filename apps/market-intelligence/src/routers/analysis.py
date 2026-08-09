from fastapi import APIRouter, Depends

from src.services.analysis_service import AnalysisService

router = APIRouter()


def get_analysis_service():
    """
    Dependency provider for AnalysisService.
    """
    return AnalysisService()


@router.get("/analysis")
def analyze_market(
    symbol: str = "AAPL",
    service: AnalysisService = Depends(get_analysis_service),
):
    """
    AI-powered market analysis.
    """
    return service.analyze(symbol)