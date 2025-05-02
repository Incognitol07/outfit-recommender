# app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application settings
    APP_NAME: str 
    APP_DESCRIPTION: str
    ENVIRONMENT: str = "development"
    DEBUG: bool = ENVIRONMENT == "development"

    # JWT and authentication settings
    JWT_SECRET_KEY: str 

    # Other security settings
    ALLOWED_HOSTS: list = ["*"]
    CORS_ORIGINS: list = ["http://localhost:3000", "http://localhost:5173"] if DEBUG else ["*"]  # Add frontend URL if applicable

    class Config:
        env_file=".env"

# Instantiate settings
settings = Settings()
