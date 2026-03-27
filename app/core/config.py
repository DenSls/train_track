from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3'
    db_echo: bool = True

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
