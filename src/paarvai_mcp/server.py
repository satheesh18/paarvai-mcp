"""Main MCP server implementation for Paarvai."""

import json
import logging
import sys
from typing import Any, Dict

from mcp.server import Server
from mcp.types import TextContent

from paarvai_mcp.client import APIError, PaarvaiClient
from paarvai_mcp.config import get_settings
from paarvai_mcp.tools import TOOLS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)


def format_response(data: Dict[str, Any]) -> str:
    """Format API response for display."""
    try:
        return json.dumps(data, indent=2)
    except Exception:
        return str(data)


def create_server() -> Server:
    """Create and configure the MCP server."""
    # Load settings
    try:
        settings = get_settings()
        # Update log level from settings
        logging.getLogger().setLevel(settings.log_level.upper())
        logger.info("Paarvai MCP Server starting...")
        logger.debug(f"API URL: {settings.api_base_url}")
    except Exception as e:
        logger.error(f"Failed to load settings: {e}")
        logger.error("Make sure PAARVAI_API_KEY environment variable is set")
        sys.exit(1)

    # Create MCP server
    server = Server("paarvai")

    # Create API client
    client = PaarvaiClient(settings)

    @server.list_tools()
    async def list_tools():
        """List available tools."""
        logger.debug("Listing tools")
        return TOOLS

    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        """Handle tool calls - forwards everything to backend API."""
        logger.info(f"Tool called: {name}")
        logger.debug(f"Arguments: {arguments}")

        try:
            # Forward the tool call to the backend
            # The backend handles all the logic - we're just a thin wrapper
            result = await client.call_tool(name, arguments)
            
            # Extract the text content from the backend response
            if isinstance(result, dict) and "content" in result:
                content = result["content"]
                if isinstance(content, list) and len(content) > 0:
                    text = content[0].get("text", str(result))
                else:
                    text = str(result)
            else:
                text = format_response(result)
            
            logger.debug(f"Tool result: {text[:200]}...")
            return [TextContent(type="text", text=text)]

        except APIError as e:
            error_msg = f"API Error: {e.message}"
            if e.status_code:
                error_msg += f" (Status: {e.status_code})"
            logger.error(error_msg)
            return [TextContent(type="text", text=error_msg)]

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg, exc_info=True)
            return [TextContent(type="text", text=error_msg)]

    return server


async def async_main():
    """Async main entry point for the MCP server."""
    from mcp.server.stdio import stdio_server
    
    try:
        server = create_server()
        logger.info("Paarvai MCP Server ready")
        
        async with stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                server.create_initialization_options()
            )
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)


def main():
    """Synchronous entry point that runs the async main."""
    import asyncio
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
