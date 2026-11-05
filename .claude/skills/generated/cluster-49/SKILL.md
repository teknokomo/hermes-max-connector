---
name: cluster-49
description: "Skill for the Cluster_49 area of hermes-max-connector. 4 symbols across 1 files."
---

# Cluster_49

4 symbols | 1 files | Cohesion: 67%

## When to Use

- Understanding how upload_binary, validate_upload_url work
- Modifying cluster_49-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | _get_session, upload_binary, _max_ssl_context, validate_upload_url |

## Entry Points

Start here when exploring this area:

- **`upload_binary`** (Function) — `adapter.py:1634`
- **`validate_upload_url`** (Function) — `adapter.py:413`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `upload_binary` | Function | `adapter.py` | 1634 |
| `validate_upload_url` | Function | `adapter.py` | 413 |
| `_get_session` | Function | `adapter.py` | 1519 |
| `_max_ssl_context` | Function | `adapter.py` | 1383 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `_handle_autosave_command → _max_ssl_context` | cross_community | 7 |
| `Send → _max_ssl_context` | cross_community | 7 |
| `_dispatch_callback → _max_ssl_context` | cross_community | 6 |
| `Send_audio → _max_ssl_context` | cross_community | 6 |
| `Send_choice_picker → _max_ssl_context` | cross_community | 6 |
| `Send_clarify → _max_ssl_context` | cross_community | 6 |
| `Send_exec_approval → _max_ssl_context` | cross_community | 6 |
| `Send_image_file → _max_ssl_context` | cross_community | 6 |
| `Send_model_picker → _max_ssl_context` | cross_community | 6 |
| `Send_slash_confirm → _max_ssl_context` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "upload_binary"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_49"})` — find related execution flows
3. Read key files listed above for implementation details
