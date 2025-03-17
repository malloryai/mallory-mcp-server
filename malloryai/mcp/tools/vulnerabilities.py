from typing import Any, Coroutine

from ..server.server import mcp, malloryai_client


@mcp.tool()
async def find_vulnerability(
    cve: str = None,
) -> Coroutine[Any, Any, dict[str, Any]]:
    """Find a vulnerability by CVE
    Args:
        cve (str): The CVE to search for
    """
    return malloryai_client.vulnerabilities.get_vulnerability(cve)
