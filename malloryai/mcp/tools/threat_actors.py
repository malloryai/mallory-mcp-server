from typing import Any, Dict

from ..server.server import mcp, malloryai_client


@mcp.tool()
async def get_threat_actor(
    identifier: str = None,
) -> Dict[str, Any]:
    """Get threat actor by identifier
    Args:
        identifier (str): The identifier of the threat actor
    """
    actor = await malloryai_client.threat_actors.get_threat_actor(identifier)
    return actor
