# mcp-server-example

[![Build](https://github.com/jecklgamis/mcp-server-example/actions/workflows/build.yaml/badge.svg)](https://github.com/jecklgamis/mcp-server-example/actions/workflows/build.yaml)

A FastAPI MCP (Model Context Protocol) server built with [FastMCP](https://github.com/jlowin/fastmcp). Exposes math tools over streamable-http transport.

## MCP Tools

### Math (`/math-mcp`)

| Tool        | Description                                    |
|-------------|------------------------------------------------|
| `add`       | Add two numbers                                |
| `subtract`  | Subtract b from a                              |
| `multiply`  | Multiply two numbers                           |
| `divide`    | Divide a by b                                  |
| `power`     | Raise base to the power of exponent            |
| `sqrt`      | Calculate the square root of a number          |
| `modulo`    | Calculate a mod b                              |
| `factorial` | Calculate the factorial of a non-negative integer |
| `discriminant` | Calculate the discriminant `b² - 4ac` of `ax² + bx + c` |
| `solve_quadratic` | Solve `ax² + bx + c = 0`; returns the discriminant, number of real roots, and the roots (complex roots as strings like `"-1.0+2.0i"`) |

## Project Structure

```
server.py                — FastAPI app entry point with REST routes and MCP mount
server/                  — MCP server definitions
  math_tools.py          — Math MCP server with tool definitions
client/                  — LangChain agent clients
  math_client.py         — Interactive LangChain agent client (math)
  llm_factory.py         — LLM provider factory (ollama, openai, gemini)
requirements.txt         — Python dependencies
Dockerfile               — Container image definition
Makefile                 — Build and run shortcuts
deployment/              — Helm chart for Kubernetes deployment
```

## Getting Started

### Requirements

* Python 3.13+

### Run Locally

```bash
pip install -r requirements.txt
python server.py
```

The server starts on `http://localhost:58080` with:
- Root endpoint at `/` listing available endpoints
- Math MCP endpoint at `/math-mcp` (streamable-http transport)
- REST API endpoints at `/add`, `/subtract`, `/multiply`, `/divide`, `/power`, `/sqrt`, `/modulo`, `/factorial`, `/discriminant`, `/solve_quadratic`
- API docs at `/docs`

### Run Client

The client uses a LangChain agent to interact with the MCP server via an interactive REPL. Configure the LLM provider via the `LLM_PROVIDER` env var and the server URL via `MCP_SERVER_URL`.

| Env Var          | Description              | Default                   |
|------------------|--------------------------|---------------------------|
| `LLM_PROVIDER`  | LLM provider to use      | `ollama`                  |
| `MCP_SERVER_URL` | MCP server base URL      | `http://localhost:58080`   |

Supported LLM providers:

| Provider | Model              |
|----------|--------------------|
| `ollama` | `llama3.1`         |
| `openai` | `gpt-4.1`          |
| `gemini` | `gemini-2.5-flash` |

> **Known issue:** `fastmcp` requires `mcp` 2.x, while `langchain-mcp-adapters` 0.3.2 requires `mcp<2`, so the adapters are pinned to 0.3.1. That version still imports the mcp 1.x layout (`mcp.server.fastmcp`), so the LangChain client (`python -m client.*`) fails to import until an adapters release supports mcp 2.x. The server is unaffected.

```bash
python -m client.math_client
```

```bash
LLM_PROVIDER=openai python -m client.math_client
```

### Run with Docker

```bash
docker build -t mcp-server-example .
docker run -p 58080:58080 mcp-server-example
```

### Deploy with Helm

```bash
cd deployment/k8s/helm
helm install mcp-server-example ./mcp-server-example
```

### Upgrade with Helm

```bash
cd deployment/k8s/helm
make upgrade
```

## Makefile Targets

| Target              | Description                        |
|---------------------|------------------------------------|
| `install-deps`      | Install Python dependencies        |
| `image`             | Build Docker image                 |
| `run`               | Run Docker container               |
| `run-shell`         | Start a shell in a new container   |
| `exec-shell`        | Exec into a running container      |
| `check`             | Run tests with pytest              |
| `clean`             | Remove generated files             |
| `up`                | Build and run (`check` + `image` + `run`) |

## CI/CD

The GitHub Actions [workflow](.github/workflows/build.yaml) runs on pushes to `main` and on pull requests. It builds the project with Python 3.13 and pushes a Docker image to Docker Hub on non-PR events.
