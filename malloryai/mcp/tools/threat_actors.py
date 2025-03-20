from typing import Any, Dict

from ..decorator.api import handle_api_errors
from ..server.server import mcp, malloryai_client


@mcp.tool()
@handle_api_errors
async def get_threat_actor(
    identifier: str = None,
) -> Dict[str, Any]:
    """Get threat actor by identifier
    Args:
        identifier (str): The identifier of the threat actor
    """
    return await malloryai_client.threat_actors.get_threat_actor(identifier)


@mcp.tool()
@handle_api_errors
async def list_threat_actors(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> Dict[str, Any]:
    """Get threat actors

    Args:
        filter (str, optional): A string used to filter threat actors. It can start with specific prefixes:
            * `name:`: Filter by Name.
            * `uuid:`: Filter by UUID.
            * If no prefix is provided, it defaults to a name filter.
            Defaults to "".
        offset (int, optional): The number of items to skip before starting to collect the result set.
            Defaults to 0.
        limit (int, optional): The maximum number of items to return. Minimum value is 1.
            Defaults to 10 (API default is 100).
        sort (str, optional): Field to sort by - either 'name', 'created_at', or 'updated_at'.
            Defaults to 'created_at'.
        order (str, optional): Sort order - either 'asc' or 'desc'.
            Defaults to 'desc'.

    Returns:
        Dict[str, Any]: Dictionary containing threat actors and metadata.
    """
    return await malloryai_client.threat_actors.list_threat_actors(
        filter=filter, offset=offset, limit=limit, sort=sort, order=order
    )


@mcp.tool()
@handle_api_errors
async def get_mentioned_threat_actors(
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> Dict[str, Any]:
    """Get mentioned threat actors

    Args:
        offset (int, optional): The number of items to skip before starting to collect the result set. Defaults to 0.
        limit (int, optional): The maximum number of items to return. Minimum value is 1. Defaults to 10.
        sort (str, optional): Field to sort by - either 'name', 'created_at', or 'updated_at'. Defaults to 'created_at'.
        order (str, optional): Sort order - either 'asc' or 'desc'. Defaults to 'desc'.

    Returns:
        Dict[str, Any]: Dictionary containing the threat actors and metadata.
    """
    return await malloryai_client.threat_actors.list_threat_actors_mentioned(
        offset=offset, limit=limit, sort=sort, order=order
    )
