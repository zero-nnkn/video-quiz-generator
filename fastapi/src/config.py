import os
from pathlib import Path

from pydantic import BaseSettings

FILE = Path(__file__)
ROOT = str(FILE.parent.parent)


class Settings(BaseSettings):
    HOST: str
    PORT: int
    CORS_ORIGINS: list[str]
    CORS_HEADERS: list[str]

    class Config:
        env_file = os.path.join(ROOT, '.env')


settings = Settings()
