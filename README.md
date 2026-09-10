# MCP Engineering Agent

A security-first engineering agent demonstrating an **MCP-style JSON-RPC tool boundary**. It separates model orchestration from typed tools, authorization, and audit events.

## Architecture

```text
User -> Agent -> JSON-RPC/MCP Boundary -> Tool Registry -> Authorization -> Tool
                                                    `-> Audit Event
```

## What this demonstrates

- `tools/list` and `tools/call` JSON-RPC methods
- Typed tool registration and discovery
- Role-based authorization before tool execution
- Read-only vs write-capable tool separation
- UTC audit events for every authorization decision
- Framework-light design that is easy to extend to a full MCP server

## Why it matters

Agentic systems become risky when an LLM can directly execute arbitrary actions. This project treats tools as a privileged interface with explicit schemas and authorization boundaries.

## Run

```bash
pip install -e '.[dev]'
python -m app.server
pytest -q
```

No real credentials or external systems are required for the demo.
