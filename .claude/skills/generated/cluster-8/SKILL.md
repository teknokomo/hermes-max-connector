---
name: cluster-8
description: "Skill for the Cluster_8 area of hermes-max-connector. 12 symbols across 1 files."
---

# Cluster_8

12 symbols | 1 files | Cohesion: 68%

## When to Use

- Understanding how answer_callback, consume_interactive, parse_message_callback work
- Modifying cluster_8-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | ParsedCallback, _ack_stale_callback, _consume_interactive, _dispatch_callback, answer_callback (+7) |

## Entry Points

Start here when exploring this area:

- **`answer_callback`** (Function) — `adapter.py:1785`
- **`consume_interactive`** (Function) — `adapter.py:386`
- **`parse_message_callback`** (Function) — `adapter.py:1256`
- **`ParsedCallback`** (Class) — `adapter.py:824`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ParsedCallback` | Class | `adapter.py` | 824 |
| `answer_callback` | Function | `adapter.py` | 1785 |
| `consume_interactive` | Function | `adapter.py` | 386 |
| `parse_message_callback` | Function | `adapter.py` | 1256 |
| `_ack_stale_callback` | Function | `adapter.py` | 2093 |
| `_consume_interactive` | Function | `adapter.py` | 2078 |
| `_dispatch_callback` | Function | `adapter.py` | 2141 |
| `_clarify_callback_message` | Function | `adapter.py` | 1831 |
| `_mark_clarify_awaiting_text` | Function | `adapter.py` | 1826 |
| `_model_picker_replacement` | Function | `adapter.py` | 1930 |
| `_resolve_clarify_choice` | Function | `adapter.py` | 1821 |
| `_resolve_exec_approval` | Function | `adapter.py` | 1942 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Connect → _connect` | cross_community | 7 |
| `_dispatch_callback → _max_ssl_context` | cross_community | 6 |
| `_dispatch_callback → _call` | cross_community | 6 |
| `Test_poll_once_dispatches_and_advances_marker → _connect` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 5 calls |
| Cluster_50 | 2 calls |
| Cluster_54 | 2 calls |
| Cluster_48 | 1 calls |
| Cluster_44 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "answer_callback"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_8"})` — find related execution flows
3. Read key files listed above for implementation details
