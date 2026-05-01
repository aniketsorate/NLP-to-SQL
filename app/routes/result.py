from app.services.db_service import execute_query
from pydantic import BaseModel
import numpy as np
import pandas as pd

from fastapi import APIRouter
class SQLRequest(BaseModel):
    question: str
    sql: str

router = APIRouter()
@router.post("/result")
async def get_result(request: SQLRequest):

    df = execute_query(request.sql)

    df = df.replace([np.inf, -np.inf], None)
    df = df.dropna() 
    print(df)
    return {
        "question": request.question,
        "sql": request.sql,
        "data": df.to_dict(orient="records")
    }