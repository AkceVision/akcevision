from fastapi import FastAPI

from src.config import settings
from src.core.exception_handlers import register_exception_handlers
from src.core.logging import setup_logging

from src.routers.commodity import router as commodity_router
from src.routers.crypto import router as crypto_router
from src.routers.health import router as health_router
from src.routers.market import router as market_router
from src.routers.news import router as news_router

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered market intelligence service.",
    version=settings.VERSION,
)

register_exception_handlers(app)

app.include_router(health_router)
app.include_router(news_router)
app.include_router(market_router)
app.include_router(commodity_router)
app.include_router(crypto_router)


@app.get("/")
def root():
    return {
        "service": settings.APP_NAME,
        "status": "running",
        "version": settings.VERSION,
    }