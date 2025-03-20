import asyncio

from malloryai.mcp.server.server import initialize_server

# Initialize the server at module level
mcp = initialize_server()


async def main():
    await mcp.run(transport="stdio")


if __name__ == "__main__":
    asyncio.run(main())
