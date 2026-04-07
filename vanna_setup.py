import os
from dotenv import load_dotenv

load_dotenv()

from vanna import Agent, AgentConfig
from vanna.core.registry import ToolRegistry
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.integrations.google import GeminiLlmService

# LLM
llm = GeminiLlmService(api_key=os.getenv("GOOGLE_API_KEY"))

# Tools
tool_registry = ToolRegistry()
tool_registry.register(RunSqlTool(SqliteRunner("clinic.db")))
tool_registry.register(VisualizeDataTool())
tool_registry.register(SaveQuestionToolArgsTool())
tool_registry.register(SearchSavedCorrectToolUsesTool())

# Memory
memory = DemoAgentMemory()

# Agent
agent = Agent(
    config=AgentConfig(),
    llm=llm,
    tool_registry=tool_registry,
    memory=memory
)