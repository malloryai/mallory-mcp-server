from mcp.server.fastmcp import FastMCP
from typing import Literal
import aiohttp
import os

# Get API endpoint from environment variable
MALLORY_API = os.getenv('MALLORY_API', 'https://ics-api.mallory.ai')
# Retrieve the API key from the environment variable once
MALLORY_API_KEY = os.getenv('MALLORY_API_KEY', '')

# Create MCP server with a name and dependencies
mcp = FastMCP(
    "Mallory Intelligence",
    dependencies=["mcp>=1.2.0rc1", "aiohttp"]
)


@mcp.tool()
async def search_vulnerabilities(
    sort: Literal["created_at"] = "created_at",
    order: Literal["desc"] = "desc",
    search: str = ""
) -> dict:
    """Search for vulnerabilities in the Mallory database
    
    Args:
        sort: Field to sort by (only created_at supported)
        order: Sort order (only desc supported)
        search: Search term to filter vulnerabilities
    """
    async with aiohttp.ClientSession() as session:
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': MALLORY_API_KEY
        }
        url = f"{MALLORY_API.rstrip('/')}/v1/entities/vulnerabilities?sort={sort}&order={order}&search={search}"
        async with session.get(url, headers=headers) as response:
            return await response.json()

@mcp.tool()
async def search_threat_actors(
    sort: Literal["created_at"] = "created_at",
    order: Literal["desc"] = "desc",
    search: str = ""
) -> dict:
    """Search for threat actors in the Mallory database
    
    Args:
        sort: Field to sort by (only created_at supported)
        order: Sort order (only desc supported)
        search: Search term to filter threat actors
    """
    async with aiohttp.ClientSession() as session:
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': MALLORY_API_KEY
        }
        url = f"{MALLORY_API.rstrip('/')}/v1/entities/threat_actors?sort={sort}&order={order}&search={search}"
        async with session.get(url, headers=headers) as response:
            return await response.json()

@mcp.tool()
async def recent_vulnerability_mentions(
    sort: Literal["created_at"] = "created_at",
    order: Literal["desc"] = "desc"
) -> dict:
    """Get recent mentions of vulnerabilities from the Mallory API
    
    Args:
        sort: Field to sort by (only created_at supported)
        order: Sort order (only desc supported)
    """
    async with aiohttp.ClientSession() as session:
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': MALLORY_API_KEY
        }
        url = f"{MALLORY_API.rstrip('/')}/v1/mentions/vulnerabilities?sort={sort}&order={order}"
        async with session.get(url, headers=headers) as response:
            return await response.json()