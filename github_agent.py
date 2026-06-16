from pydantic_ai import Agent
from pydantic_ai.mcp import MCPToolset
import dotenv
import utils
from os import getenv

dotenv.load_dotenv("keys.env")

model = utils.load_model("kimi-k2.6")

githubMCP = MCPToolset(client="https://api.githubcopilot.com/mcp/", auth=getenv("GITHUB_PAT"))

allowed_tool_names = []

allowed_tools = githubMCP.filtered(lambda 
ctx, tool: tool.name in allowed_tool_names)

github_agent = Agent(
    model=model,
    output_type=str,
    instructions="Be helpful and concise. When making commits, pull requests, or comments, always include the following: 'This [commit/PR/comment] was written by [LLM MODEL NAME] on behalf of [USER NAME], and may include mistakes'",
    toolsets=[allowed_tools]
)

prompt = ""

while True:
    prompt = input("Prompt: ")

    output = github_agent.run_sync(user_prompt=prompt).output

    print(output)