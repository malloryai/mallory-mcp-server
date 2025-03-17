import asyncio
from malloryai.mcp.config.initialize_logger import initialize_logger
from malloryai.mcp.server.server import initialize_server

# Initialize the server at module level
initialize_logger()
mcp = initialize_server()


async def main():
    await mcp.run()


if __name__ == "__main__":
    asyncio.run(main())
