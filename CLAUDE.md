# CLAUDE.md

## Project Overview

This is a FastAPI MCP (Model Context Protocol) server built with FastMCP. It exposes math tools over streamable-http transport on port 58080. Includes LangChain-based clients for interacting with the server via an LLM agent.

## Tech Stack

- Python 3.13+
- FastMCP
- FastAPI / Uvicorn
- LangChain / LangGraph (client)
- langchain-mcp-adapters (client)

## Project Structure

- `server.py` — FastAPI app entry point with REST routes and MCP mount
- `server/` — MCP server definitions
  - `math_tools.py` — Math MCP server with tool definitions (arithmetic, factorial, discriminant, quadratic solver)
- `client/` — LangChain agent clients
  - `math_client.py` — LangChain agent client for math MCP
  - `llm_factory.py` — LLM provider factory (ollama, openai, gemini)
- `requirements.txt` — Pinned Python dependencies
- `Dockerfile` — Container image definition (port 58080)
- `.github/workflows/build.yaml` — CI/CD pipeline (build, test, Docker push)
- `deployment/k8s/helm/mcp-server-example/` — Helm chart for Kubernetes deployment

## Known Issues

- `fastmcp` needs `mcp` 2.x but `langchain-mcp-adapters` 0.3.2 needs `mcp<2`, so adapters stay at 0.3.1. That version fails to import with mcp 2.x (`mcp.server.fastmcp` missing), so `client/` is broken until an adapters release supports mcp 2.x. The server works.
- Perf tools were split out into the separate `~/workspace/perf-mcp-server` repo.

## Running

```bash
pip install -r requirements.txt
python server.py
```

## Docker

```bash
docker build -t mcp-server-example .
docker run -p 58080:58080 mcp-server-example
```
