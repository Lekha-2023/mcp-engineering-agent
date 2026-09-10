from dataclasses import dataclass
from datetime import datetime, timezone


READ_ONLY_TOOLS = {"list_files", "read_file", "query_sql"}
WRITE_TOOLS = {"create_ticket"}


@dataclass(frozen=True)
class AuditEvent:
    actor: str
    tool: str
    allowed: bool
    timestamp: str


def authorize(tool: str, role: str) -> bool:
    if tool in READ_ONLY_TOOLS:
        return role in {"developer", "admin"}
    if tool in WRITE_TOOLS:
        return role == "developer"
    return False


def audit(actor: str, tool: str, allowed: bool) -> AuditEvent:
    return AuditEvent(actor, tool, allowed, datetime.now(timezone.utc).isoformat())
