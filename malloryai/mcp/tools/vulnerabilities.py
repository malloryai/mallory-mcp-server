from typing import Any, Dict

from ..decorator.api import handle_api_errors
from ..server.server import mcp, malloryai_client


@mcp.tool()
@handle_api_errors
async def find_vulnerability(
    cve: str = None,
) -> Dict[str, Any]:
    """Find a vulnerability by CVE identifier
    Args:
        cve (str): The CVE to search for
    Returns:
        Dict[str, Any]: Dictionary containing vulnerability details or error information
    """
    return await malloryai_client.vulnerabilities.get_vulnerability(cve)


@mcp.tool()
@handle_api_errors
async def get_vulnerabilities(
    filter: str = "",
    offset: int = 0,
    limit: int = 10,
    sort: str = "created_at",
    order: str = "desc",
) -> Dict[str, Any]:
    """Get vulnerabilities

    Args:
        filter (str, optional): A string used to filter vulnerabilities. It can start with specific prefixes:
            * `cve:`: Filter by CVE ID.
            * `uuid:`: Filter by UUID.
            * `desc:`: Filter by description.
            * If the filter string matches the pattern `CVE-` or a UUID pattern, it will be treated as a specific filter.
            * If no prefix is provided, it defaults to a description filter.
            Defaults to "".
        offset (int, optional): The number of items to skip before starting to collect the result set.
            Defaults to 0.
        limit (int, optional): The maximum number of items to return. Minimum value is 1.
            Defaults to 10 (API default is 100).
        sort (str, optional): Field to sort by - either 'cve_id', 'created_at', 'updated_at',
            'cvss_3_base_score', 'epss_score', or 'epss_percentile'.
            Defaults to 'created_at'.
        order (str, optional): Sort order - either 'asc' or 'desc'.
            Defaults to 'desc'.

    Returns:
        Dict[str, Any]: Dictionary containing vulnerabilities and metadata.
    """
    return await malloryai_client.vulnerabilities.list_vulnerabilities(
        filter=filter, offset=offset, limit=limit, sort=sort, order=order
    )


@mcp.tool()
@handle_api_errors
async def get_vulnerability_detection_signatures(
    identifier: str,
) -> Dict[str, Any]:
    """Get detection signatures for a specific vulnerability

    Args:
        identifier (str): The unique CVE ID or UUID of the vulnerability to retrieve.
            Example formats: "CVE-2023-1234" or "123e4567-e89b-12d3-a456-426614174000"

    Returns:
        Dict[str, Any]: Dictionary containing vulnerability detection signatures and metadata.
    """
    return (
        await malloryai_client.vulnerabilities.get_vulnerability_detection_signatures(
            identifier=identifier
        )
    )


@mcp.tool()
@handle_api_errors
async def get_vulnerability_exploitations(
    identifier: str,
) -> Dict[str, Any]:
    """Get exploitation data for a specific vulnerability

    Args:
        identifier (str): The unique CVE ID or UUID of the vulnerability to retrieve.
            Example formats: "CVE-2023-1234" or "123e4567-e89b-12d3-a456-426614174000"

    Returns:
        Dict[str, Any]: Dictionary containing vulnerability exploitation data and metadata.
    """
    return await malloryai_client.vulnerabilities.get_vulnerability_exploitations(
        identifier=identifier
    )


@mcp.tool()
@handle_api_errors
async def get_vulnerability_configurations(
    identifier: str,
) -> Dict[str, Any]:
    """Get configuration information for a specific vulnerability

    Args:
        identifier (str): The unique CVE ID or UUID of the vulnerability to retrieve.
            Example formats: "CVE-2023-1234" or "123e4567-e89b-12d3-a456-426614174000"

    Returns:
        Dict[str, Any]: Dictionary containing vulnerability configuration information and metadata.
    """
    return await malloryai_client.vulnerabilities.get_vulnerability_configurations(
        identifier=identifier
    )
