import json
from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class ToolCall:
    name: str
    arguments: dict[str, Any]


class MCPProtocol:
    """Small JSON-RPC adapter illustrating an MCP-compatible tool boundary."""

    def __init__(self, registry):
        self.registry = registry

    def handle(self, payload: str) -> str:
        request = json.loads(payload)
        method = request.get("method")
        params = request.get("params", {})
        if method == "tools/list":
            result = {"tools": self.registry.describe()}
        elif method == "tools/call":
            call = ToolCall(params["name"], params.get("arguments", {}))
            result = {"content": [asdict(self.registry.call(call.name, call.arguments))]}
        else:
            raise ValueError(f"Unsupported method: {method}")
        return json.dumps({"jsonrpc": "2.0", "id": request.get("id"), "result": result})
