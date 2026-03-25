# CLAUDE.md

## Project Overview

This is a FastAPI MCP (Model Context Protocol) math server built with FastMCP. It exposes math tools (add, subtract, multiply, divide, power, sqrt, modulo, factorial) over SSE transport on port 8080.

## Tech Stack

- Python 3.13+
- FastMCP
- FastAPI / Uvicorn

## Project Structure

- `server.py` — MCP server entry point with all tool definitions
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
