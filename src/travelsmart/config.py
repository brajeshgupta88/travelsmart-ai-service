import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "production"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4o"
    FLIGHT_API_KEY: str = ""
    HOTEL_API_KEY: str = ""
    ACTIVITY_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
