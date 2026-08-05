from pydantic_settings import BaseSettings

from src.version import VERSION


class Settings(BaseSettings):
    APP_NAME: str = "AkceVision Market Intelligence"
    VERSION: str = VERSION
    DEBUG: bool = False


settings = Settings()
