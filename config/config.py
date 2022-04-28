"""Config."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings."""
    SQLALCHEMY_DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        """Config."""
        env_file = ".env"
          
