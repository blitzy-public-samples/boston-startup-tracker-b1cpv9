from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    # Database connection URL
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Elasticsearch connection URL
    ELASTICSEARCH_URL: str = Field(..., env="ELASTICSEARCH_URL")

    # Redis connection URL
    REDIS_URL: str = Field(..., env="REDIS_URL")

    # Secret key for JWT token generation
    SECRET_KEY: str = Field(..., env="SECRET_KEY")

    # Access token expiration time in minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # Allowed CORS origins
    CORS_ORIGINS: str = Field("*", env="CORS_ORIGINS")

    # API prefix for all endpoints
    API_PREFIX: str = Field("/api", env="API_PREFIX")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a global instance of the Settings class
settings = Settings()