from app.services.db_service import execute_query
from pydantic import BaseModel

from fastapi import APIRouter
class SQLRequest(BaseModel):
    question: str
    sql: str

router = APIRouter()
@router.post("/result")
async def get_result(request: SQLRequest):

    df = execute_query(request.sql)

    return {
        "question": request.question,
        "sql": request.sql,
        "data": df.to_dict(orient="records")
    }