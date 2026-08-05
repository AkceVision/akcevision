from fastapi import FastAPI

from src.routers.health import router as health_router

app = FastAPI(
    title="AkceVision Market Intelligence",
    description="AI-powered market intelligence service.",
    version="0.1.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "service": "market-intelligence",
        "status": "running",
        "version": "0.1.0"
    }
