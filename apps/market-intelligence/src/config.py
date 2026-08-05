from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AkceVision Market Intelligence"
    VERSION: str = "0.1.0"
    DEBUG: bool = False


settings = Settings()
