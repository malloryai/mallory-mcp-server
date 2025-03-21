from typing import Any, Dict

from ..decorator.api import handle_api_errors
from ..server.server import mcp, malloryai_client


@mcp.tool()
@handle_api_errors
async def get_threat_actor(
    identifier: str = None,
) -> Dict[str, Any]:
    """Get threat actor by identifier

    Use this tool when you need detailed intelligence about a specific threat actor or
    advanced persistent threat (APT) group. This information is valuable for:
    - Understanding the tactics, techniques, and procedures (TTPs) of threat actors
    - Researching who might be behind a security incident
    - Evaluating the sophistication level of potential adversaries
    - Gathering threat intelligence for security briefings
    - Understanding which sectors or regions a threat actor typically targets

    Args:
        identifier (str): The identifier of the threat actor - can be either:
            - UUID (e.g., "a9b46d37-42b8-4b27-8b69-583dbcb2f5e1")
            - Name (e.g., "dark_cloud_shield")

    Returns:
    Dict[str, Any]: Detailed threat actor information including:
        - uuid: Unique identifier for this threat actor
        - name: Machine-readable name (typically lowercase with underscores)
        - display_name: Human-readable name with proper formatting
        - created_at/updated_at/enriched_at: Timestamps for record management
        - gen_description: Generated description (if available)
        - mentions: List of references to this threat actor from various sources, each containing:
            - uuid: Unique identifier for this mention
            - overview: Summary of the threat actor's activities from this source
            - published_at: When the source material was published
            - collected_at: When this mention was collected
            - reference_url: URL of the source material
            - reference_source: Name of the source (e.g., "talos_intelligence_blog")
            - reference_user_generated_content: Whether this is user-generated content
            - Other metadata about the mention and reference

    These mentions provide valuable context about the threat actor's:
    - Known attack vectors and exploited vulnerabilities
    - Target sectors, regions, or organizations
    - Tools and malware used
    - Attribution confidence and alternate names
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

    Use this tool when you need to search, browse, or list multiple threat actors. This is
    particularly useful for:
    - Discovering recently added threat actors in the database
    - Searching for specific threat actors by name
    - Creating reports on threat actor landscapes
    - Building comprehensive threat intelligence briefings
    - Comparing multiple threat actors

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
        Dict[str, Any]: Dictionary containing:
            - total: Total number of threat actors matching the filter criteria
            - offset: Current pagination offset
            - limit: Number of items returned per page
            - message: Status message (usually null when successful)
            - data: List of threat actor records, each containing:
                - uuid: Unique identifier for the threat actor
                - name: Machine-readable name (typically lowercase with underscores)
                - display_name: Human-readable name with proper formatting
                - gen_description: Generated description (if available)
                - misp_uuid: Reference ID in MISP (Malware Information Sharing Platform)
                - created_at: Timestamp when this record was first added
                - updated_at: Timestamp when this record was last modified
                - enriched_at: Timestamp when this record was last enriched with additional data

    Note: This function returns summary information about threat actors. To get detailed
    information including mentions and intelligence sources for a specific threat actor,
    use the get_threat_actor() function with the uuid or name.
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

    Use this tool when you need to monitor recent threat actor activities mentioned in
    threat intelligence sources. This is especially valuable for:
    - Tracking emerging threats and active threat actors
    - Monitoring the latest threat intelligence reporting
    - Identifying which threat actors are currently active or trending
    - Building situational awareness of the current threat landscape
    - Obtaining recent summaries of threat actor tactics and campaigns

    Unlike list_threat_actors() which returns basic threat actor records, this function
    returns actual mentions with context from recent intelligence sources.

    Args:
        offset (int, optional): The number of items to skip before starting to collect the result set. Defaults to 0.
        limit (int, optional): The maximum number of items to return. Minimum value is 1. Defaults to 10.
        sort (str, optional): Field to sort by - either 'name', 'created_at', or 'updated_at'. Defaults to 'created_at'.
        order (str, optional): Sort order - either 'asc' or 'desc'. Defaults to 'desc'.

    Returns:
        Dict[str, Any]: Dictionary containing:
            - total: Total number of threat actor mentions available
            - offset: Current pagination offset
            - limit: Number of items returned per page
            - message: Status message (usually null when successful)
            - data: List of recent threat actor mentions, each containing:
                - uuid: Unique identifier for this mention
                - overview: Summary of the threat actor's recent activities or campaigns
                - created_at: Timestamp when this mention was first added to the system
                - updated_at: Timestamp when this mention was last updated
                - published_at: Original publication date of the source material
                - collected_at: When this intelligence was collected
                - reference_url: URL of the source article or report
                - reference_source: Name of the intelligence source (e.g., "securityaffairs")
                - reference_user_generated_content: Whether this is from user-generated content
                - threat_actor_uuid: UUID of the referenced threat actor
                - threat_actor_name: Name of the referenced threat actor

    This function provides timely intelligence about threat actors from recently published
    sources, making it ideal for staying current on the threat landscape.
    """
    return await malloryai_client.threat_actors.list_threat_actors_mentioned(
        offset=offset, limit=limit, sort=sort, order=order
    )
