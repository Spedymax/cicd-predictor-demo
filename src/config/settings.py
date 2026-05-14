from functools import lru_cache

from pydantic import BaseModel


class Settings(BaseModel):
    service_name: str = "cicd-predictor-demo"
    version: str = "0.2.0"


@lru_cache
def get_settings() -> Settings:
    return Settings()
