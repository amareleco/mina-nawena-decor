from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    APP_NAME: str

    DEBUG: bool
    API_V1_STR: str = "/api/v1"


    class Config:
        env_file = ".env"


settings = Settings()