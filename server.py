import models
from fastmcp import FastMCP, Client, Context
import fastmcp.server
from fastmcp.server.auth.auth import AccessToken 
from pydantic_ai import RunContext, Tool
from os import getenv

mcp = FastMCP(
    name="MyServer",
    auth=None,
    )

githubmcp = Client(
    "https://api.githubcopilot.com/mcp", 
    headers={
        "Authorization" : f"{getenv('GITHUB_PAT')}", "Content-Type":"application/json"
    })

isAdmin = True

mcp.enable(tags={"public"}, only=True)

if isAdmin:
    mcp.enable(tags={"admin"})

@mcp.tool(tags={"admin"})
async def push_files_to_repository(args: models.pushToGithubParams):
    async with githubmcp as gh:
        return await gh.call_tool(name="push_files", arguments={"owner":ctx.deps.})
    
@mcp.tool(tags={"public"})
async def get_file_contents(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

@mcp.tool(tags={"public"})
async def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"

@mcp.tool(tags={"admin", "developer"})
def commit_to_github(file: str) -> str:
    return f"{file} comitted to GitHub successfully"

@mcp.tool(tags={"developer"})
def experimental_feature():
    return "This feature is for developers only"
    
mcp.run(transport="http", show_banner=False)