from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = "models/best_credit_model.pkl"

    class Config:
        env_file= ".env"

settings = Settings()
