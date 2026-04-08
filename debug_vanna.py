import asyncio
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
from prompts import build_sql_prompt

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

question = "How many patients do we have?"
prompt = build_sql_prompt(question)

async def main():
    response = await client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message.content

    print("\n===== RAW RESPONSE =====")
    print(result)

asyncio.run(main())