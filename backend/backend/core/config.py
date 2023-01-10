from datetime import timedelta
import typing as t
from pathlib import Path
from functools import lru_cache
from pydantic import (
    BaseSettings,
    DirectoryPath,
    EmailStr,
    PostgresDsn,
    validator,
)
from backend.utils import os_operation


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: t.List[str] = ["*"]  # t.List[AnyHttpUrl] = []
    DEBUG: bool = False
    API_PREFIX: str
    PROJECT_DESCRIPTION: str
    PROJECT_URL: str = "http://127.0.0.1:5000"
    API_VERSION: str
    ENVIRONMENT: str
    # email settings
    EMAIL_SERVER: str
    EMAIL_SERVER_PORT: int
    ADMIN_EMAIL: EmailStr
    ADMIN_PASSWORD: str
    BASE_DIR: DirectoryPath = os_operation.get_base_dir()
    # locate template folder at the root of the project
    TEMPLATE_DIR: DirectoryPath = Path.joinpath(BASE_DIR, "backend/templates")
    MEDIA_DIR: DirectoryPath = Path.joinpath(BASE_DIR, "backend/static/media")
    PDF_MEDIA_DIR: DirectoryPath = Path.joinpath(BASE_DIR, "backend/static/pdf")
    URL_STATIC_PATH: str = "get_media"
    STATIC_DIR: DirectoryPath = Path.joinpath(BASE_DIR, "backend/static")
    # database connection
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    DATABASE_URI: t.Optional[PostgresDsn] = None

    # jwt settings
    SECRET_KEY: str
    REFRESH_KEY: str
    ALGORITHM: str
    REFRESH_TOKEN_EXPIRATION_DURATION: timedelta = timedelta(days=7)
    ACCESS_TOKEN_EXPIRATION_DURATION: timedelta = timedelta(minutes=30)

    # payment
    RAVE_SECRET_KEY: str
    RAVE_PUBLIC_KEY: str

    """Validate the cores origins."""

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls, v: t.Union[str, t.List[str]]
    ) -> t.Union[t.List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(
        cls, v: t.Optional[str], values: t.Dict[str, t.Any]
    ) -> t.Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
