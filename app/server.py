from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any

@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    handler: Callable[..., Any]

class AuditLog:
    def __init__(self): self.events: list[dict] = []
    def record(self, actor: str, tool: str, allowed: bool):
        self.events.append({"actor": actor, "tool": tool, "allowed": allowed})

class ToolRegistry:
    def __init__(self, workspace: str = "."):
        self.root = Path(workspace).resolve(); self.audit = AuditLog(); self.tools = {}
        self.register(Tool("list_files", "List workspace files", self.list_files))
        self.register(Tool("read_file", "Read a bounded text file", self.read_file))

    def register(self, tool: Tool): self.tools[tool.name] = tool

    def _safe(self, path: str) -> Path:
        target = (self.root / path).resolve()
        if target != self.root and self.root not in target.parents: raise PermissionError("path outside workspace")
        return target

    def list_files(self, prefix: str = ""):
        base = self._safe(prefix)
        return [str(p.relative_to(self.root)) for p in base.rglob("*") if p.is_file()][:100]

    def read_file(self, path: str, max_chars: int = 12000):
        return self._safe(path).read_text(encoding="utf-8")[:max_chars]

    def call(self, name: str, actor: str = "agent", **kwargs):
        tool = self.tools[name]
        try:
            result = tool.handler(**kwargs); self.audit.record(actor, name, True); return result
        except Exception:
            self.audit.record(actor, name, False); raise

if __name__ == "__main__":
    registry = ToolRegistry(".")
    print(registry.call("list_files"))
