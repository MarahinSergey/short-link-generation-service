from functools import lru_cache
from typing import Optional, List
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = "postgresql://admin:admin@postgres:5432/urls"
    ORIGINS: List[str] = ["http://127.0.0.1:8000", "https://localhost:8000"]
    IN_DOCKER: Optional[bool] = False
    DEBUG: bool = True
    PREFIX: str = "api"

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
