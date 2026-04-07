import os
from dotenv import load_dotenv

load_dotenv()

from vanna import Agent, AgentConfig
from vanna.core.registry import ToolRegistry
from vanna.core.user import UserResolver, User, RequestContext
from vanna.tools import RunSqlTool, VisualizeDataTool
from vanna.tools.agent_memory import SaveQuestionToolArgsTool, SearchSavedCorrectToolUsesTool
from vanna.integrations.sqlite import SqliteRunner
from vanna.integrations.local.agent_memory import DemoAgentMemory
from vanna.integrations.google import GeminiLlmService

# ✅ Custom User Resolver (required)
class SimpleUserResolver(UserResolver):
    def resolve_user(self, request_context: RequestContext) -> User:
        return User(user_id="default_user")

# ✅ LLM
llm_service = GeminiLlmService(api_key=os.getenv("GOOGLE_API_KEY"))

# ✅ Tool Registry (CORRECT METHOD)
tools = ToolRegistry()

tools.register_local_tool(
    RunSqlTool(sql_runner=SqliteRunner("clinic.db")),
    access_groups=["users"]
)

tools.register_local_tool(
    VisualizeDataTool(),
    access_groups=["users"]
)

tools.register_local_tool(
    SaveQuestionToolArgsTool(),
    access_groups=["users"]
)

tools.register_local_tool(
    SearchSavedCorrectToolUsesTool(),
    access_groups=["users"]
)

# ✅ Memory
agent_memory = DemoAgentMemory()

# ✅ User Resolver
user_resolver = SimpleUserResolver()

# ✅ Agent
agent = Agent(
    llm_service=llm_service,
    tool_registry=tools,
    user_resolver=user_resolver,
    agent_memory=agent_memory,
    config=AgentConfig()
)