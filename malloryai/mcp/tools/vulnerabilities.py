from typing import Any, Dict

from ..decorator.api import handle_api_errors
from ..server.server import mcp, malloryai_client


@mcp.tool()
@handle_api_errors
async def find_vulnerability(
    cve: str = None,
) -> Dict[str, Any]:
    """Find a vulnerability by CVE identifier

    Use this tool when you need detailed information about a specific vulnerability,
    including its severity scores, description, and whether it has been exploited in the wild.
    This is particularly useful for threat assessment, prioritizing patching, or
    understanding the technical details of a specific CVE.

    Args:
        cve (str): The CVE to search for

    Returns:
        Dict[str, Any]: Dictionary containing vulnerability details including:
            - uuid: Unique identifier for this vulnerability record
            - cve_id: The CVE identifier
            - description: Detailed description of the vulnerability
            - created_at/updated_at: Timestamps for record creation and updates
            - cvss_base_score: Severity score (0.0-10.0, higher is more severe)
            - cvss_version: Version of the CVSS scoring system used
            - cvss_vector: Detailed scoring vector showing attack characteristics
            - cvss_data: List of all available CVSS scores from different sources
            - epss_score: Exploit Prediction Scoring System score (probability of exploitation)
            - epss_percentile: Percentile ranking of the EPSS score
            - cisa_kev_added_at: When CISA added this to Known Exploited Vulnerabilities catalog (if applicable)
            - weaknesses: List of CWE identifiers associated with this vulnerability
            - mentions_count: Number of references to this vulnerability
            - detection_signatures_count: Number of detection signatures available
            - exploits_count: Number of known exploit implementations
            - exploitations_count: Number of recorded instances of exploitation in the wild
            - vulnerable_configurations_count: Number of affected system configurations
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

    Use this tool when you need to search or browse multiple vulnerabilities, such as when:
    - Discovering recently added vulnerabilities in the database
    - Searching for vulnerabilities by keywords in their descriptions
    - Finding all vulnerabilities related to a specific technology
    - Creating reports on vulnerability trends or statistics
    - Looking for high-severity vulnerabilities based on CVSS or EPSS scores

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
        Dict[str, Any]: Dictionary containing:
            - total: Total number of vulnerabilities matching the filter criteria
            - offset: Current pagination offset
            - limit: Number of items returned per page
            - message: Status message (usually null when successful)
            - data: List of vulnerability records, each containing:
                - uuid: Unique identifier for the vulnerability
                - cve_id: The CVE identifier
                - description: Detailed description of the vulnerability
                - created_at/updated_at: Timestamps for record creation and updates
                - cvss_base_score: Severity score (if available)
                - cvss_version: Version of the CVSS scoring system used
                - cvss_vector: Detailed scoring vector
                - cvss_data: Additional CVSS scoring information
                - epss_score: Exploit Prediction Scoring System score
                - epss_percentile: Percentile ranking of the EPSS score
                - cisa_kev_added_at: Date added to CISA's Known Exploited Vulnerabilities catalog
                - gen_description/gen_name: Generated content (if available)
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

    Use this tool when you need to understand how a specific vulnerability can be detected
    in your environment. Detection signatures provide technical indicators that can help
    security teams identify if they're exposed to or being targeted by a particular
    vulnerability. This is particularly useful for:
    - Building detection rules for security monitoring tools
    - Understanding the technical indicators of compromise
    - Verifying if detection capabilities exist for a specific vulnerability
    - Determining which sources (vendors, researchers) have published detection methods

    Args:
        identifier (str): The unique CVE ID or UUID of the vulnerability to retrieve.
            Example formats: "CVE-2023-1234" or "123e4567-e89b-12d3-a456-426614174000"

    Returns:
        Dict[str, Any]: List of detection signatures for the specified vulnerability,
        where each signature contains:
            - uuid: Unique identifier for this detection signature
            - source: Origin of the detection signature (e.g., "cisa_kev", "snort", "yara")
            - method: How the signature was created (e.g., "manual", "automated")
            - description: Human-readable description of what the signature detects
            - upstream_id: Original identifier from the source system
            - created_at: Timestamp when this signature was first added
            - updated_at: Timestamp when this signature was last modified
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

    Use this tool when you need to determine if a vulnerability has been actively exploited
    in the wild. This information is critical for risk assessment, incident response, and
    prioritization of remediation efforts. Exploitation data can help you:
    - Validate that a vulnerability is being actively used by threat actors
    - Understand when exploitation began and if it's ongoing
    - Identify which detection mechanisms observed the exploitation
    - Determine the frequency or prevalence of exploitation (count)
    - Make data-driven decisions about patching priorities

    Args:
        identifier (str): The unique CVE ID or UUID of the vulnerability to retrieve.
            Example formats: "CVE-2023-1234" or "123e4567-e89b-12d3-a456-426614174000"

    Returns:
        Dict[str, Any]: List of exploitation records for the specified vulnerability,
        where each record contains:
            - uuid: Unique identifier for this exploitation record
            - begins_at: Timestamp when exploitation was first observed
            - ends_at: Timestamp when exploitation activity ended
            - count: Number of exploitation occurrences detected
            - created_at: Timestamp when this record was first added
            - updated_at: Timestamp when this record was last modified
            - detection_signature_uuid: UUID of the signature that detected this exploitation
            - detection_signature_name: Name of the detection signature
            - detection_signature_source: Source of the detection (e.g., "cisa_kev")
            - detection_signature_method: Method used for detection (e.g., "manual")

        An empty list indicates no known exploitation events for this vulnerability.
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

    Use this tool when you need to understand exactly which systems, products, or versions
    are affected by a vulnerability. This information is essential for:
    - Determining if your specific product versions are vulnerable
    - Planning targeted remediation efforts
    - Conducting accurate asset vulnerability mapping
    - Filtering out false positives in vulnerability scanning
    - Understanding the scope of affected software/hardware configurations

    The configuration data follows CPE (Common Platform Enumeration) standards to precisely
    identify affected systems.

    Args:
        identifier (str): The unique CVE ID or UUID of the vulnerability to retrieve.
            Example formats: "CVE-2023-1234" or "123e4567-e89b-12d3-a456-426614174000"

    Returns:
        Dict[str, Any]: List of vulnerable configurations for the specified vulnerability,
        where each configuration contains:
            - uuid: Unique identifier for this configuration record
            - cpe_id: Identifier for this CPE configuration
            - set_id: Identifier for the set this configuration belongs to
            - is_vulnerable: Boolean indicating if this configuration is vulnerable
            - vendor/vendor_display_name: The vendor of the affected product
            - product/product_display_name: The affected product name
            - product_type: Type of product (e.g., "application", "os")
            - Version range indicators:
                - versionStartIncluding/versionStartExcluding: Minimum affected version
                - versionEndIncluding/versionEndExcluding: Maximum affected version
                - updateStartIncluding/updateEndIncluding: Update version specifiers
            - Platform details:
                - edition: Edition of the product
                - language: Language of the product
                - sw_edition: Software edition information
                - target_sw: Target software environment (e.g., "wordpress")
                - target_hw: Target hardware environment
                - other: Additional targeting information
            - created_at/updated_at: Timestamps for record management
            - cve_id: The CVE identifier associated with this configuration

        An empty list indicates no specific configuration information is available.
    """
    return await malloryai_client.vulnerabilities.get_vulnerability_configurations(
        identifier=identifier
    )
