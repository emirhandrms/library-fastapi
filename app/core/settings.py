from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    SQL_CONNECTION_STRING: str = Field(..., env="SQL_CONNECTION_STRING")

    class Config:
        env_file = ".env"

settings = Settings()