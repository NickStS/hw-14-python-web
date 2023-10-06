from pydantic_settings import BaseSettings

SECRET_KEY = "@2hn-1@$*0qes==o6+5wtmq$eh+s(*=g_a6d=4t#-a1p!=(uln"

ALGORITHM = "HS256"

DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    DATABASE_URL: str = "postgresql://postgres:123@localhost:5432/postgres"

    class Config:
        env_file = ".env"

settings = Settings()
