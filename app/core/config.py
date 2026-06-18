from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    GOOGLE_API_KEY: str

    MODEL_NAME: str

    TEMPERATURE: float

    class Config:
        env_file = ".env"

settings = Settings()