import sys

from malloryai.sdk.api.v1.api import MalloryIntelligenceClient
from mcp.server.fastmcp import FastMCP
import importlib
import pkgutil
from pathlib import Path

from ..config import settings

# Create MCP server with a name
mcp = FastMCP("MalloryAI")

malloryai_client = MalloryIntelligenceClient(api_key=settings.MALLORY_API_KEY)


def load_tools():
    """Dynamically load all tool modules in the tools package"""
    # Get the tools directory
    tools_dir = Path(__file__).resolve().parent.parent / "tools"

    # Find all Python modules in the tools directory
    for _, module_name, _ in pkgutil.iter_modules([str(tools_dir)]):
        # Skip the __init__ module
        if module_name != "__init__":
            # Import the module
            importlib.import_module(f"malloryai.mcp.tools.{module_name}")
            print(f"Loaded tool: {module_name}")


def initialize_server():
    """Initialize the server by loading all tools"""
    try:
        print("Starting tool loading...")
        load_tools()
        print("Tools loaded successfully")
        return mcp
    except Exception as e:
        print(f"Error during initialization: {str(e)}", file=sys.stderr)
        raise
