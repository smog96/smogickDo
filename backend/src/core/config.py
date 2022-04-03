from functools import lru_cache

from pydantic import BaseSettings


class _Settings(BaseSettings):
    db_dsn: str
    api_version: str

    class Config:
        env_file = "envs/dev.env"


@lru_cache
def _get_settings() -> _Settings:
    return _Settings()


settings = _get_settings()
