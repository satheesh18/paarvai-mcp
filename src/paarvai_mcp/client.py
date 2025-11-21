"""HTTP client for Paarvai API - matches backend implementation."""

import logging
from typing import Any, Dict, Optional

import httpx

from paarvai_mcp.config import Settings

logger = logging.getLogger(__name__)


class APIError(Exception):
    """Base exception for API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class PaarvaiClient:
    """HTTP client for interacting with Paarvai API."""

    def __init__(self, settings: Settings):
        """Initialize the client with settings."""
        self.settings = settings
        self.client = httpx.AsyncClient(
            base_url=settings.api_base_url,
            headers={
                "Authorization": f"Bearer {settings.api_key}",
                "User-Agent": "paarvai-mcp-server/0.1.0",
                "Content-Type": "application/json",
            },
            timeout=settings.timeout,
        )

    async def __aenter__(self):
        """Async context manager entry."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call an MCP tool on the backend.
        
        This is the main method that forwards all tool calls to the backend API.
        The backend handles all the logic - this is just a thin wrapper.
        
        Args:
            tool_name: Name of the tool to call
            arguments: Tool arguments
            
        Returns:
            Tool execution results
        """
        logger.info(f"Calling tool: {tool_name}")
        logger.debug(f"Arguments: {arguments}")
        
        try:
            response = await self.client.post(
                "/api/v1/mcp/tools/call",
                json={
                    "name": tool_name,
                    "arguments": arguments
                }
            )
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error: {e.response.status_code} - {e.response.text}")
            raise APIError(
                f"API request failed: {e.response.text}",
                status_code=e.response.status_code,
            )
        except httpx.RequestError as e:
            logger.error(f"Request error: {str(e)}")
            raise APIError(f"Failed to connect to Paarvai API: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise APIError(f"Unexpected error: {str(e)}")
