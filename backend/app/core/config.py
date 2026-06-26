from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


    PROJECT_NAME: str = "NETRA"

    API_V1_PREFIX: str = "/api/v1"

    DEBUG: bool = False


    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    POSTGRES_DB: str

    POSTGRES_HOST: str

    POSTGRES_PORT: int = 5432


    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


    MODEL_PATH: str = "ml/models/xgboost.pkl"


    EVE_JSON_PATH: str = "suricata/logs/eve.json"

    RULES_PATH: str = "suricata/rules/local.rules"


    WS_HEARTBEAT_INTERVAL: int = 30


    LOG_LEVEL: str = "INFO"


    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
    ]

    @property
    def database_url(self) -> str:
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
