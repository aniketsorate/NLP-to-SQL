import sqlite3
from app.core.config import settings
import pandas as pd

def execute_query(sql: str):
    conn = sqlite3.connect(settings.DB_PATH)
    df = pd.read_sql_query(sql, conn)

    conn.close()
    return df