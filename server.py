from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from server.math_tools import math_tools, mcp

math_mcp_app = mcp.http_app(path="/")


@asynccontextmanager
async def lifespan(app):
    async with math_mcp_app.lifespan(app):
        yield


app = FastAPI(
    title="MCP Server",
    description="MCP Server",
    version="1.0.0-rc.1",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "app_name": "mcp-server-example",
        "message": "It works on my machine!",
        "endpoints": {
            "docs": "/docs",
            "math_mcp": "/math-mcp",
        },
    }


# FastAPI routes
for tool_fn in math_tools:
    app.get(f"/{tool_fn.__name__.lstrip('_')}", tags=["math"])(tool_fn)

app.mount("/math-mcp", math_mcp_app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=58080)
