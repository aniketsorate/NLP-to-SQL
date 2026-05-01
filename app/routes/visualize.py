from pydantic import BaseModel
import io
import re
import base64
from fastapi import APIRouter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app.services.llm_service import code_chain, prepare_df_for_llm,execute_code

class VisualizeRequest(BaseModel):
    question: str
    data: list

router = APIRouter()

@router.post("/visualize")
async def visualize(request: VisualizeRequest):

    import pandas as pd
    df = pd.DataFrame(request.data)

    parsed = await prepare_df_for_llm(df)

    code_input = {
        "question": request.question,
        "schema": parsed["schema"],
        "dtypes": parsed["dtypes"],
        "sample": parsed["sample"]
    }

    code = await code_chain.ainvoke(code_input)

    chart = await execute_code(code, df)

    return {
        "chart": chart  
    }