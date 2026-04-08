import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = "llama-3.1-8b-instant"
    DB_PATH = "data/clinic.db"
    RATE_LIMIT_SECONDS = 2
    MEMORY_LIMIT = 5

settings = Settings()