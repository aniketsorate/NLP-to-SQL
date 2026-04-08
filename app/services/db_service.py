import sqlite3
from app.core.config import settings

def execute_query(sql: str):
    conn = sqlite3.connect(settings.DB_PATH)
    cursor = conn.cursor()

    cursor.execute(sql)
    rows = cursor.fetchall()
    cols = [d[0] for d in cursor.description] if cursor.description else []

    conn.close()
    return cols, rows