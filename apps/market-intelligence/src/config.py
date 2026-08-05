from pydantic_settings import BaseSettings

from src.version import VERSION


class Settings(BaseSettings):
    APP_NAME: str = "AkceVision Market Intelligence"
    VERSION: str = VERSION
    DEBUG: bool = False

    NEWS_API_KEY: str = ""

    ALPHA_VANTAGE_API_KEY: str = ""

    FINNHUB_API_KEY: str = ""

    POLYGON_API_KEY: str = ""

    FRED_API_KEY: str = ""

    COINGECKO_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
