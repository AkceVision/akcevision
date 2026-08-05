from fastapi import FastAPI

from src.config import settings
from src.routers.health import router as health_router

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered market intelligence service.",
    version=settings.VERSION,
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "service": settings.APP_NAME,
        "status": "running",
        "version": settings.VERSION,
    }
