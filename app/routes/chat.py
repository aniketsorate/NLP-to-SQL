from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm_service import generate_sql

from app.services.chart_service import generate_chart
from app.services.memory_service import get_memory_examples, save_memory

from app.utils.sql_validator import validate_sql
from app.utils.sql_extractor import extract_sql

from app.core.cache import get_cache, set_cache
from app.core.rate_limiter import check_rate_limit

from app.prompts.prompt import sql_prompt

router = APIRouter()

class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    if not request.question.strip():
        return {"error": "Empty question"}

    if not check_rate_limit():
        return {"error": "Too many requests"}

    cached = get_cache(request.question)
    if cached:
        return {"source": "cache", **cached}

#    examples = await get_memory_examples()
    prompt = sql_prompt.format_prompt(question=request.question).to_string()

    sql = await generate_sql(sql_prompt, request.question)

    if not sql:
        return {"error": "SQL generation failed"}

    valid, msg = validate_sql(sql)
    if not valid:
        return {"error": msg, "sql": sql}

    # result = {
    #     "sql": sql,
    #     "columns": cols,
    #     "rows": rows,
    #     "count": len(rows)
    # }

    # chart = generate_chart(rows, cols)
    # if chart:
    #     result["chart"] = chart

    # set_cache(request.question, result)
    # save_memory(request.question, sql)

    return sql
