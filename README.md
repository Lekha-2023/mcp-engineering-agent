# MCP Engineering Agent

An engineering-focused agent architecture demonstrating how an LLM agent can safely use typed tools through an MCP-style interface. The project emphasizes explicit schemas, authorization boundaries, audit events, and deterministic local tools.

## Architecture

`User -> Agent -> Tool Registry -> Authorization -> Tool -> Audit Log`

## Tools

- `list_files` — inspect an allowed workspace
- `read_file` — read a bounded text file
- `query_sql` — execute an allowlisted read-only query pattern
- `create_ticket` — generate a structured engineering task

The tool layer is deliberately framework-light so the security and orchestration concepts are easy to explain in an interview.

## Run

```bash
pip install -e '.[dev]'
python -m app.server
pytest -q
```
