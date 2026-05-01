import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    SQL_MODEL_NAME = "llama-3.1-8b-instant"
    CODE_MODEL_NAME = "tencent/hy3-preview:free"
    DB_PATH = "data/clinic.db"
    RATE_LIMIT_SECONDS = 2
    MEMORY_LIMIT = 5

settings = Settings()