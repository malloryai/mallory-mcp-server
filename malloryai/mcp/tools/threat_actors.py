from typing import Any, Coroutine

from ..server.server import mcp, malloryai_client


@mcp.tool()
async def get_threat_actor(
    identifier: str = None,
) -> Coroutine[Any, Any, dict[str, Any]]:
    """Get threat actor by identifier
    Args:
        identifier (str): The identifier of the threat actor
    """
    return malloryai_client.threat_actors.get_threat_actor(identifier)
