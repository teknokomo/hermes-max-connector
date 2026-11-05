---
name: cluster-50
description: "Skill for the Cluster_50 area of hermes-max-connector. 4 symbols across 1 files."
---

# Cluster_50

4 symbols | 1 files | Cohesion: 50%

## When to Use

- Understanding how interactive_status, is_update_claimed work
- Modifying cluster_50-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | __init__, _connect, interactive_status, is_update_claimed |

## Entry Points

Start here when exploring this area:

- **`interactive_status`** (Function) — `adapter.py:394`
- **`is_update_claimed`** (Function) — `adapter.py:368`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `interactive_status` | Function | `adapter.py` | 394 |
| `is_update_claimed` | Function | `adapter.py` | 368 |
| `__init__` | Function | `adapter.py` | 321 |
| `_connect` | Function | `adapter.py` | 336 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Connect → _connect` | cross_community | 7 |
| `Test_poll_once_dispatches_and_advances_marker → _connect` | cross_community | 6 |
| `Send_choice_picker → _connect` | cross_community | 4 |
| `Send_clarify → _connect` | cross_community | 4 |
| `Send_exec_approval → _connect` | cross_community | 4 |
| `Send_model_picker → _connect` | cross_community | 4 |
| `Send_slash_confirm → _connect` | cross_community | 4 |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "interactive_status"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_50"})` — find related execution flows
3. Read key files listed above for implementation details
