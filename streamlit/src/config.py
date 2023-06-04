import os
from pathlib import Path

from pydantic import BaseSettings

FILE = Path(__file__)
ROOT = str(FILE.parent.parent)
APP_DIR = FILE.parent.absolute()
PROJECT_DIR = APP_DIR.parent.absolute()


class Settings(BaseSettings):
    TRANSCRIBE_ENDPOINT: str
    QUIZ_GENERATION_ENDPOINT: str

    class Config:
        env_file = os.path.join(ROOT, '.env')


class AppSettings(BaseSettings):
    PAGE_EMOJI: str = '🦉'
    PROJECT_DIR: Path = PROJECT_DIR
    SOURCE_TYPE: list[str] = ['Upload', 'Youtube']
    AUDIO_EXTENSION: list[str] = ['mp4', 'mov', 'mkv', 'mp3', 'wav']

    LLM_SERVICES: dict[str, str] = {
        'GoogleBard': 'Bard cookie [read](https://github.com/dsdanielpark/Bard-API#authentication)',
        'OpenAIGPT': 'OpenAI GPT API [read](https://platform.openai.com/account/api-keys)',
    }
    DEFAULT_QUIZ_TYPES_CONFIG: dict[str, dict] = {
        'multiple_choice': {'num_choices': 4},
    }
    DEFAULT_QUIZ_TYPE: str = 'multiple_choice'


settings = Settings()
app_settings = AppSettings()
