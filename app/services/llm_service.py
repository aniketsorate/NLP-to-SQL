from pandas import DataFrame

from app.core.config import settings
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, Runnable
from app.prompts.prompt import sql_prompt, code_prompt

sql_llm = ChatOpenAI(
    model=settings.SQL_MODEL_NAME,
    openai_api_key=settings.GROQ_API_KEY,
    openai_api_base="https://api.groq.com/openai/v1",
    temperature=0
)

llm = ChatOpenAI(
    model=settings.CODE_MODEL_NAME,
    openai_api_key=settings.OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0
)

sql_chain = sql_prompt | sql_llm | StrOutputParser()
async def generate_sql(chain: Runnable, question: str):
    sql_query = await sql_chain.ainvoke({
        "question": question
    })
    sql_query=sql_query.split("```sql\n")[1].split("\n```")[0]
    return sql_query



async def prepare_df_for_llm(df):
    schema = list(df.columns)
    dtypes = df.dtypes.astype(str).to_dict()
    sample = df.head(3).to_markdown()

    return {
        "schema": schema,
        "dtypes": dtypes,
        "sample": sample
    }

async def execute_code(code: str, df: DataFrame):
    code = code.split("```python")[1].split("```")[0]

    local_vars = {"df": df}
    exec(code, {}, local_vars)
    # capture figure
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    img_base64 = base64.b64encode(buf.read()).decode()

    plt.close()

    return img_base64


code_chain = code_prompt | llm | StrOutputParser()
