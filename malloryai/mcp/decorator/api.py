import functools
from typing import Dict, Any, Callable

from malloryai.sdk.api.v1.exceptions.exception import APIError


def handle_api_errors(func: Callable) -> Callable:
    """Decorator to handle API errors consistently across tool functions"""

    @functools.wraps(func)
    async def wrapper(*args, **kwargs) -> Dict[str, Any]:
        try:
            return await func(*args, **kwargs)
        except APIError as e:
            if e.status_code == 401:
                return {
                    "error": str(e),
                    "status_code": 401,
                    "type": "authentication_error",
                }
            return {
                "error": e.message,
                "status_code": e.status_code,
                "type": "api_error",
            }
        except Exception as e:
            # Optionally handle other unexpected exceptions
            return {"error": str(e), "type": "general_error"}

    return wrapper
