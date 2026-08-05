from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AkceVision"
    APP_VERSION: str = "0.1.0"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env.example"


settings = Settings()
