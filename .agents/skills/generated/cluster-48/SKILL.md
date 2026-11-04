---
name: cluster-48
description: "Skill for the Cluster_48 area of hermes-max-connector. 6 symbols across 1 files."
---

# Cluster_48

6 symbols | 1 files | Cohesion: 38%

## When to Use

- Understanding how send_typing, get_messages_by_ids, get_video_details work
- Modifying cluster_48-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | send_typing, _json, get_messages_by_ids, get_video_details, send_chat_action (+1) |

## Entry Points

Start here when exploring this area:

- **`send_typing`** (Function) — `adapter.py:3500`
- **`get_messages_by_ids`** (Function) — `adapter.py:1563`
- **`get_video_details`** (Function) — `adapter.py:1585`
- **`send_chat_action`** (Function) — `adapter.py:1706`
- **`update_commands`** (Function) — `adapter.py:1592`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `send_typing` | Function | `adapter.py` | 3500 |
| `get_messages_by_ids` | Function | `adapter.py` | 1563 |
| `get_video_details` | Function | `adapter.py` | 1585 |
| `send_chat_action` | Function | `adapter.py` | 1706 |
| `update_commands` | Function | `adapter.py` | 1592 |
| `_json` | Function | `adapter.py` | 1537 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `_handle_autosave_command → _max_ssl_context` | cross_community | 7 |
| `_handle_autosave_command → _call` | cross_community | 7 |
| `Send → _max_ssl_context` | cross_community | 7 |
| `Send → _call` | cross_community | 7 |
| `_dispatch_callback → _max_ssl_context` | cross_community | 6 |
| `_dispatch_callback → _call` | cross_community | 6 |
| `Send_audio → _max_ssl_context` | cross_community | 6 |
| `Send_audio → _call` | cross_community | 6 |
| `Send_choice_picker → _max_ssl_context` | cross_community | 6 |
| `Send_choice_picker → _call` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 3 calls |
| Cluster_49 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "send_typing"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_48"})` — find related execution flows
3. Read key files listed above for implementation details
