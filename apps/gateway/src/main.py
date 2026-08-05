from fastapi import FastAPI

app = FastAPI(
    title="AkceVision Gateway",
    description="Enterprise AI-Native Decision Intelligence Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "AkceVision",
        "service": "Gateway",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }
