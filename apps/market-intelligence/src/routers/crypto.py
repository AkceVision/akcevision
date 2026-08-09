from fastapi import APIRouter, Depends

from src.services.crypto_service import CryptoService

router = APIRouter()


def get_crypto_service():
    """
    Dependency provider for CryptoService.
    """
    return CryptoService()


@router.get("/crypto")
def get_crypto(
    symbol: str = "bitcoin",
    service: CryptoService = Depends(get_crypto_service),
):
    """
    Get crypto quote.
    """
    return service.get_quote(symbol)


@router.get("/crypto/health")
def crypto_health(
    service: CryptoService = Depends(get_crypto_service),
):
    """
    Crypto provider health.
    """
    return service.health_check()