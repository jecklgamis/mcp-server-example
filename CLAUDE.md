# CLAUDE.md

## Project Overview

This is a FastAPI MCP (Model Context Protocol) math server built with FastMCP. It exposes math tools (add, subtract, multiply, divide, power, sqrt, modulo, factorial) over streamable-http transport on port 8080. Includes a LangChain-based client for interacting with the server via an LLM agent.

## Tech Stack

- Python 3.13+
- FastMCP
- FastAPI / Uvicorn
- LangChain / LangGraph (client)
- langchain-mcp-adapters (client)

## Project Structure

- `server.py` — MCP server entry point with all tool definitions
- `client.py` — LangChain agent client that connects to the MCP server
- `llm_factory.py` — LLM provider factory (ollama, openai, gemini)
- `requirements.txt` — Pinned Python dependencies
- `Dockerfile` — Container image definition (port 8080)
- `.github/workflows/build.yaml` — CI/CD pipeline (build, test, Docker push)
- `deployment/k8s/helm/mcp-server-example/` — Helm chart for Kubernetes deployment

## Running

```bash
pip install -r requirements.txt
python server.py
```

## Docker

```bash
docker build -t mcp-server-example .
docker run -p 8080:8080 mcp-server-example
```
