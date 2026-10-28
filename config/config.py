from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).parent / ".env"

class Settings(BaseSettings):
    bot_token: str
    proxy_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()