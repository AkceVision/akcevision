from fastapi import FastAPI

app = FastAPI(
    title="AkceVision Market Intelligence",
    description="AI-powered market intelligence service.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "service": "market-intelligence",
        "status": "running",
        "version": "0.1.0"
    }
