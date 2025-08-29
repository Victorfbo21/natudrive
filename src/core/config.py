import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    
    APP_NAME = 'NatuDrive API'
    ENV = os.getenv("ENV", "development")
    DEBUG: bool = ENV == "development"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    ALEMBIC_DATABASE_URL: str = os.getenv("ALEMBIC_DATABASE_URL", "sqlite:///db.sqlite3")
    

settings = Settings()