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
    # Get the threat actor data - await the coroutine
    actor = await malloryai_client.threat_actors.get_threat_actor(identifier)

    # Format the response
    response = {
        "actor_id": actor.get("uuid"),
        "name": actor.get("display_name") or actor.get("name"),
        "created_at": actor.get("created_at"),
        "updated_at": actor.get("updated_at"),
        "mentions": [],
    }

    # Process mentions if available
    if actor.get("mentions"):
        for mention in actor.get("mentions"):
            response["mentions"].append(
                {
                    "overview": mention.get("overview"),
                    "source": mention.get("reference_source"),
                    "url": mention.get("reference_url"),
                    "published_at": mention.get("published_at"),
                }
            )

    return response
