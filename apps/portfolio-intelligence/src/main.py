from fastapi import FastAPI

from src.routers.portfolio import router as portfolio_router


app = FastAPI(
    title="AkceVision Portfolio Intelligence",
    description="Portfolio intelligence service.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "service": "AkceVision Portfolio Intelligence",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "portfolio-intelligence",
    }


app.include_router(portfolio_router)
