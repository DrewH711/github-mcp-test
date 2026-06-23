from pydantic_ai import Agent, RunContext, WrapperToolset
from pydantic_ai.mcp import MCPToolset
import dotenv
import utils
from models import ghAgentContext

dotenv.load_dotenv("keys.env")

model = utils.load_model("kimi-k2.6")

allowed_tool_names = ["add_issue_comment", "push_files"]

# adding this comment for clarity

def build_mcp_toolset(ctx: RunContext[ghAgentContext]):
    """
    Build the MCP toolset dynamically so it has access to the
    current ghAgentContext for every agent run.
    """

    MCPToolset(
        client="http://127.0.0.1:8000/mcp",
    ).with_metadata(
        user_name=ctx.deps.user_name,
        git_repository=ctx.deps.git_repository,
        git_repo_owner_name=ctx.deps.git_repo_owner_name,
    )

class ContextualToolset(WrapperToolset):
    pass

github_agent = Agent(
    model=model,
    output_type=str,
    deps_type=ghAgentContext,
    instructions="""
    You are working in the git repository DrewH711/github-mcp-test. DrewH711 is the owner

    Be helpful and concise. When making commits, pull requests, or comments, always include the following: 'This [commit/PR/comment] was written by [LLM MODEL NAME] on behalf of DrewH711, and may include mistakes'""",
    toolsets=[build_mcp_toolset, mytools]
)