---
name: cluster-43
description: "Skill for the Cluster_43 area of hermes-max-connector. 11 symbols across 1 files."
---

# Cluster_43

11 symbols | 1 files | Cohesion: 81%

## When to Use

- Understanding how send_choice_picker, send_clarify, send_exec_approval work
- Modifying cluster_43-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | _interactive_scope, _new_interactive_state, _send_inline_keyboard, send_choice_picker, send_clarify (+6) |

## Entry Points

Start here when exploring this area:

- **`send_choice_picker`** (Function) — `adapter.py:3363`
- **`send_clarify`** (Function) — `adapter.py:3275`
- **`send_exec_approval`** (Function) — `adapter.py:3235`
- **`send_model_picker`** (Function) — `adapter.py:3317`
- **`send_slash_confirm`** (Function) — `adapter.py:3200`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `send_choice_picker` | Function | `adapter.py` | 3363 |
| `send_clarify` | Function | `adapter.py` | 3275 |
| `send_exec_approval` | Function | `adapter.py` | 3235 |
| `send_model_picker` | Function | `adapter.py` | 3317 |
| `send_slash_confirm` | Function | `adapter.py` | 3200 |
| `send_inline_keyboard` | Function | `adapter.py` | 1766 |
| `record_interactive` | Function | `adapter.py` | 378 |
| `_interactive_scope` | Function | `adapter.py` | 2055 |
| `_new_interactive_state` | Function | `adapter.py` | 2068 |
| `_send_inline_keyboard` | Function | `adapter.py` | 2116 |
| `_message_id` | Function | `adapter.py` | 1800 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Send_choice_picker → _max_ssl_context` | cross_community | 6 |
| `Send_choice_picker → _call` | cross_community | 6 |
| `Send_clarify → _max_ssl_context` | cross_community | 6 |
| `Send_clarify → _call` | cross_community | 6 |
| `Send_exec_approval → _max_ssl_context` | cross_community | 6 |
| `Send_exec_approval → _call` | cross_community | 6 |
| `Send_model_picker → _max_ssl_context` | cross_community | 6 |
| `Send_model_picker → _call` | cross_community | 6 |
| `Send_slash_confirm → _max_ssl_context` | cross_community | 6 |
| `Send_slash_confirm → _call` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 4 calls |
| Cluster_54 | 2 calls |
| Cluster_50 | 1 calls |
| Cluster_48 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "send_choice_picker"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_43"})` — find related execution flows
3. Read key files listed above for implementation details
