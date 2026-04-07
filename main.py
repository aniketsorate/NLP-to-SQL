from fastapi import FastAPI
from vanna_setup import agent

app = FastAPI()

# -------------------------------
# ✅ SQL VALIDATION FUNCTION
# -------------------------------
def validate_sql(sql: str):
    sql_lower = sql.lower().strip()

    # Rule 1: Only SELECT allowed
    if not sql_lower.startswith("select"):
        return False, "Only SELECT queries are allowed."

    # Rule 2: Dangerous keywords
    banned_keywords = [
        "insert", "update", "delete", "drop", "alter",
        "exec", "grant", "revoke", "shutdown", "xp_", "sp_"
    ]
    for keyword in banned_keywords:
        if keyword in sql_lower:
            return False, f"Forbidden keyword detected: {keyword}"

    # Rule 3: System tables
    banned_tables = ["sqlite_master", "sqlite_temp_master"]
    for table in banned_tables:
        if table in sql_lower:
            return False, f"Access to system table '{table}' is not allowed."

    return True, "Valid SQL"


# -------------------------------
# ✅ CHAT ENDPOINT
# -------------------------------
import sqlite3

@app.post("/chat")
def chat(request: dict):
    question = request.get("question")

    if not question:
        return {"error": "Question cannot be empty"}

    try:
        # Step 1: Get response from agent
        response = agent.send_message(question)
        response_text = str(response)

        # Step 2: Extract SQL (basic assumption)
        sql_query = response_text

        # Step 3: Validate SQL
        is_valid, message = validate_sql(sql_query)

        if not is_valid:
            return {
                "error": message,
                "sql_query": sql_query
            }

        # Step 4: Execute SQL manually
        try:
            conn = sqlite3.connect("clinic.db")
            cursor = conn.cursor()

            cursor.execute(sql_query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description] if cursor.description else []

            conn.close()

        except Exception as db_error:
            return {
                "error": "Database execution failed",
                "details": str(db_error),
                "sql_query": sql_query
            }

        # Step 5: Handle no data
        if not rows:
            return {
                "message": "No data found",
                "sql_query": sql_query,
                "row_count": 0
            }

        # Step 6: Success response
        return {
            "message": "Query executed successfully",
            "sql_query": sql_query,
            "columns": columns,
            "rows": rows,
            "row_count": len(rows)
        }

    except Exception as e:
        return {
            "error": "Something went wrong",
            "details": str(e)
        }

# -------------------------------
# ✅ HEALTH CHECK ENDPOINT
# -------------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "API is running"
    }