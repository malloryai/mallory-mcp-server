from malloryai.mcp.server.server import initialize_server

# Initialize the server at module level
mcp = initialize_server()

if __name__ == "__main__":
    mcp.run(transport="stdio")
