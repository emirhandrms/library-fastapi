from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQL_CONNECTION_STRING: str
    

settings = Settings()