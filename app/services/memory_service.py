from vanna.integrations.local.agent_memory import DemoAgentMemory
from app.core.config import settings

agent_memory = DemoAgentMemory()

async def get_memory_examples():
    items = await agent_memory.get_recent_memories(settings.MEMORY_LIMIT)
    return "\n".join(
        [f"Q: {m.question}\nA: {m.tool_args.get('sql')}" for m in items]
    )

def save_memory(question, sql):
    agent_memory.save_tool_usage(
        "RunSqlTool",
        {"sql": sql},
        question,
        {}
    )