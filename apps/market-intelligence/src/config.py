from pydantic_settings import BaseSettings, SettingsConfigDict

from src.version import VERSION


class Settings(BaseSettings):
    APP_NAME: str = "AkceVision Market Intelligence"
    VERSION: str = VERSION
    DEBUG: bool = False

    # News
    NEWS_API_KEY: str = ""
    NEWS_API_URL: str = "https://newsapi.org/v2/top-headlines"
    NEWS_PROVIDER: str = "newsapi"

    # Market
    MARKET_PROVIDER: str = "alphavantage"

    ALPHA_VANTAGE_API_KEY: str = ""
    ALPHA_VANTAGE_URL: str = "https://www.alphavantage.co/query"

    FINNHUB_API_KEY: str = ""
    FINNHUB_URL: str = "https://finnhub.io/api/v1/quote"

    POLYGON_API_KEY: str = ""

    # Macro
    FRED_API_KEY: str = ""
    FRED_URL: str = "https://api.stlouisfed.org/fred/series/observations"

    # Crypto
    COINGECKO_API_KEY: str = ""
    COINGECKO_URL: str = "https://api.coingecko.com/api/v3/simple/price"

    # AI
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    MODEL_NAME: str = "gpt-5.5"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()