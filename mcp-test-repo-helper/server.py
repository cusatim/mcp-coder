"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
import math


# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def get_repo_info(repo_name: str) -> str:
    """Get information about a repository"""
    return f"Repository {repo_name} has 1000 commits." # TODO: actually get the info

@mcp.tool()
def area_of_circle(radius: float) -> float:
    """Calculate the area of a circle"""
    return math.pi * radius ** 2

@mcp.tool()
def get_my_moms_name(name: str, nickname: str) -> str:
    """Get my moms name"""
    if nickname:
        return f"Ms whatchacallit" 
    else:
        return f"Ms {name}"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."