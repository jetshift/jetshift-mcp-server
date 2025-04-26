<p align="center">
  <a href="https://github.com/mdobydullah/jetshift-core">
    <img src="https://cdn.shouts.dev/media/435/jetshift-github.png" alt="JefShift" width="100">
    <img src="https://cdn.shouts.dev/media/438/mcp.png" alt="JefShift" width="120">
  </a>
</p>

<p align="center">
<strong>JetShift MCP Server</strong>
</p>

> JetShift MCP Server allows communication with JetShift. It lets you manage all aspects of JetShift.

## Server

[FastMCP Doc](https://gofastmcp.com/getting-started/welcome)

```bash
uv pip install .
```

```bash
fastmcp dev main.py
# or,
mcp dev main.py
```

```bash
# add mcp to claude desktop
fastmcp install jsmcp/main.py
```

## Clients

[Claude Desktop](https://claude.ai/download)

```bash
{
  "mcpServers": {
    "JetShift MCP Server": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "E:\\Python\\jetshift-mcp-server\\main.py"
      ]
    }
  }
}
```

[5ire](https://github.com/nanbingxyz/5ire)

```bash
uv run --with fastmcp fastmcp run "E:\Python\jetshift-mcp-server\main.py"
```

[fast-agent](https://github.com/evalstate/fast-agent)

```bash
@fast.agent(
    instruction="You are a helpful AI Agent",
    servers=["jetshift_mcp_server"],
)
  
cp fastagent.secrets.example.yaml fastagent.secrets.yaml

cd fast-agent
uv run agent.py
```

## MCP prompts

Create a database:

```bash
create a JetShift database from this connection mysql://obydul:123456@localhost:3306/test_db
```

Update database info:

```bash
Rename database (5) title to "Test MCP database".
```

Get database info:

```bash
Show me the DB info. id = 5
```

Delete database:

```bash
Delete database id = 5
```
