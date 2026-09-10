from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ToolResult:
    tool: str
    ok: bool
    data: Any


class ToolRegistry:
    def __init__(self):
        self._tools: dict[str, tuple[Callable[..., Any], str]] = {}

    def register(self, name: str, description: str, fn: Callable[..., Any]) -> None:
        self._tools[name] = (fn, description)

    def describe(self) -> list[dict[str, str]]:
        return [{"name": n, "description": d} for n, (_, d) in sorted(self._tools.items())]

    def call(self, name: str, arguments: dict[str, Any]) -> ToolResult:
        if name not in self._tools:
            raise KeyError(f"Unknown tool: {name}")
        fn, _ = self._tools[name]
        return ToolResult(name, True, fn(**arguments))
