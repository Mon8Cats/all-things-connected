# MCP

## Building an MCP Server:

- Resources
  - https://github.com/modelcontextprotocol/python-sdk
  - https://modelcontextprotocol.io/introduction
  - https://github.com/modelcontextprotocol/servers
- Why build my own server
- The template to get me started
- Basics of an MCP server
- Using AI to create an MCP server
- MCP server template deep dive
  

## MCP Clients

- Windsurf
- Cursor
- n8n
- Claude Desktop 
- my own AI agents
  

## Configuration 

- Claude Desktop configuration: 


## Prerequisites

- Python 3.12+
- Supabase or any PostgreSQL database (for vector storage of memories)
- API keys for your chosen LLM provider (OpenAI, OpenRouter, or Ollama)
- Docker if running the MCP server as a container (recommended)

## Installation 

```bash
pip install uv
get clone ...
cd my-dir
uv pip install -e .
cp .env.example .env
docker build -t mcp/mem0 --build-arg PORT=8050 .  
uv run src/main.py
docker run --env-file .env -p:8050:8050 mcp/mem0

```

## Transport Protocol 

- sse
- io