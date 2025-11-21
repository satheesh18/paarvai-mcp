"""Entry point for running paarvai_mcp as a module."""

import asyncio
from paarvai_mcp.server import main

if __name__ == "__main__":
    asyncio.run(main())
