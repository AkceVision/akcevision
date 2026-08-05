from fastapi import APIRouter

from src.version import SERVICE_NAME, VERSION

router = APIRouter()


@router.get("/health")
def health():
    return {
        "service": SERVICE_NAME,
        "status": "healthy",
        "version": VERSION,
    }
