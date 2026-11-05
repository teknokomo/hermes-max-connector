---
name: cluster-45
description: "Skill for the Cluster_45 area of hermes-max-connector. 8 symbols across 2 files."
---

# Cluster_45

8 symbols | 2 files | Cohesion: 67%

## When to Use

- Understanding how send, send_text, chunk_text work
- Modifying cluster_45-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | _send_text_chunked, send, send_text, _is_internal_compression_failure_notice, chunk_text (+1) |
| `tests.py` | test_chunk_text_prefers_boundaries_and_never_loses_content, test_send_chunks_all_text_and_returns_last_message_id |

## Entry Points

Start here when exploring this area:

- **`send`** (Function) — `adapter.py:3176`
- **`send_text`** (Function) — `adapter.py:1744`
- **`chunk_text`** (Function) — `adapter.py:1343`
- **`send_chunked`** (Function) — `adapter.py:1952`
- **`test_chunk_text_prefers_boundaries_and_never_loses_content`** (Function) — `tests.py:172`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `send` | Function | `adapter.py` | 3176 |
| `send_text` | Function | `adapter.py` | 1744 |
| `chunk_text` | Function | `adapter.py` | 1343 |
| `send_chunked` | Function | `adapter.py` | 1952 |
| `test_chunk_text_prefers_boundaries_and_never_loses_content` | Function | `tests.py` | 172 |
| `test_send_chunks_all_text_and_returns_last_message_id` | Function | `tests.py` | 256 |
| `_send_text_chunked` | Function | `adapter.py` | 3140 |
| `_is_internal_compression_failure_notice` | Function | `adapter.py` | 91 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `_handle_autosave_command → _max_ssl_context` | cross_community | 7 |
| `_handle_autosave_command → _call` | cross_community | 7 |
| `Send → _max_ssl_context` | cross_community | 7 |
| `Send → _call` | cross_community | 7 |
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → Chunk_text` | cross_community | 6 |
| `Test_group_dispatch_injects_attribution_guard_without_observed_history → Chunk_text` | cross_community | 6 |
| `Test_send_chunks_all_text_and_returns_last_message_id → _max_ssl_context` | cross_community | 6 |
| `Test_send_chunks_all_text_and_returns_last_message_id → _call` | cross_community | 6 |
| `Send → Chunk_text` | intra_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Cluster_11 | 1 calls |
| Cluster_48 | 1 calls |
| Cluster_43 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "send"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_45"})` — find related execution flows
3. Read key files listed above for implementation details
