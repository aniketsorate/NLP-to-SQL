from fastapi import FastAPI
from vanna_setup import agent

app = FastAPI()

def validate_sql(sql):
    sql_lower = sql.lower()
    if not sql_lower.startswith("select"):
        return False
    banned = ["drop", "delete", "update", "insert", "alter"]
    return not any(word in sql_lower for word in banned)

@app.post("/chat")
def chat(request: dict):
    question = request.get("question")

    try:
        response = agent.send_message(question)
        return {"message": str(response)}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health():
    return {"status": "ok"}