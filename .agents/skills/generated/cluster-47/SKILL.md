---
name: cluster-47
description: "Skill for the Cluster_47 area of hermes-max-connector. 4 symbols across 1 files."
---

# Cluster_47

4 symbols | 1 files | Cohesion: 67%

## When to Use

- Understanding how delete_message, delete_message, edit_message work
- Modifying cluster_47-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | delete_message, delete_message, edit_message, _require_api_success |

## Entry Points

Start here when exploring this area:

- **`delete_message`** (Function) — `adapter.py:3528`
- **`delete_message`** (Function) — `adapter.py:1733`
- **`edit_message`** (Function) — `adapter.py:1716`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `delete_message` | Function | `adapter.py` | 3528 |
| `delete_message` | Function | `adapter.py` | 1733 |
| `edit_message` | Function | `adapter.py` | 1716 |
| `_require_api_success` | Function | `adapter.py` | 1809 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Delete_message → _max_ssl_context` | cross_community | 5 |
| `Delete_message → _call` | cross_community | 5 |
| `Edit_message → _max_ssl_context` | cross_community | 4 |
| `Edit_message → _call` | cross_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Cluster_48 | 2 calls |
| Tests | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "delete_message"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_47"})` — find related execution flows
3. Read key files listed above for implementation details
