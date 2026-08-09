from pydantic_settings import BaseSettings, SettingsConfigDict

from src.version import VERSION


class Settings(BaseSettings):
    APP_NAME: str = "AkceVision Market Intelligence"
    VERSION: str = VERSION
    DEBUG: bool = False

    NEWS_API_KEY: str = ""
    NEWS_API_URL: str = "https://newsapi.org/v2/top-headlines"
    NEWS_PROVIDER: str = "newsapi"

    MARKET_PROVIDER: str = "alphavantage"
    
    ALPHA_VANTAGE_API_KEY: str = ""
    ALPHA_VANTAGE_URL: str = "https://www.alphavantage.co/query"
    FINNHUB_API_KEY: str = ""
    POLYGON_API_KEY: str = ""

    FRED_API_KEY: str = ""

    COINGECKO_API_KEY: str = ""

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()