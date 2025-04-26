from fastmcp import FastMCP
from api import database

mcp = FastMCP(name="JetShift MCP Server", version="0.1.0", author="Md Obydullah")

# Databases
mcp.tool()(database.jetshift_databases)
mcp.tool()(database.create_database)
mcp.tool()(database.get_database)
mcp.tool()(database.update_database)
mcp.tool()(database.delete_database)

if __name__ == "__main__":
    mcp.run()
