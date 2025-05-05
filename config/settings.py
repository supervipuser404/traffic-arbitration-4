
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/news_db"

    # Ads
    ADS_FREQUENCY: int = 3  # Insert ad after every 3 content blocks
    ADS_PARTNER_LABEL: bool = True  # Show "Partner News" label

    # Localization
    DEFAULT_LANGUAGE: str = "ru"

    # Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    STATIC_DIR: Path = BASE_DIR / "web/app/static"
    MEDIA_DIR: Path = STATIC_DIR / "media"


settings = Settings()
