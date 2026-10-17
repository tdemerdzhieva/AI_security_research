# Vulnerable MCP Server

Security assessment of a FastMCP server with three critical vulnerabilities: log disclosure exposing backend credentials and internals, SQL injection in resource templates, and OS command injection in a restricted tool.

## Findings
- Information disclosure via resource://logs - backend API URL, live Bearer token, and server version exposed
- SQL injection in price:// resource template - UNION-based SQLite injection with no input sanitization
- OS command injection in execute_server_command - validation incomplete against shell operators, execution as root

## Tools Used
- fastmcp client library - MCP protocol interaction
- Python asyncio - asynchronous tool and resource calls
- URL encoding - bypassing URI parser restrictions in SQLi payloads
- Basic shell commands - whoami, cat, etc. to confirm RCE

## Read the full writeup
[vulnerable_MCP_server.md](vulnerable_MCP_server.md)