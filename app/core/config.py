"""
Application configuration, loaded from environment variables / .env.
"""
from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    PROJECT_NAME: str = "ClearChart API"
    DEBUG: bool = True

    # postgresql://<user>:<password>@<host>:<port>/<database>
    DATABASE_URL: str = "postgresql://clearchart:clearchart@localhost:5432/clearchart"

    JWT_SECRET_KEY: str = "CHANGE_ME_use_openssl_rand_hex_32"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours — simple single-token setup, no refresh flow

    # React Native's Metro bundler / emulator networking uses these origins.
    # 10.0.2.2 is the Android emulator's alias for the host machine.
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://10.0.2.2",
        "http://10.0.2.2:8081",
        "http://localhost",
        "http://localhost:8081",
        "http://localhost:19006",
    ]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def _split_cors(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
