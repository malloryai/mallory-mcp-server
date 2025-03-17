from typing import Any, Dict

from ..server.server import mcp, malloryai_client


@mcp.tool()
async def find_vulnerability(
    cve: str = None,
) -> Dict[str, Any]:
    """Find a vulnerability by CVE
    Args:
        cve (str): The CVE to search for
    """
    vulnerability = await malloryai_client.vulnerabilities.get_vulnerability(cve)
    return vulnerability
