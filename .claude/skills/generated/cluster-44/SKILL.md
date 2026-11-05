---
name: cluster-44
description: "Skill for the Cluster_44 area of hermes-max-connector. 10 symbols across 1 files."
---

# Cluster_44

10 symbols | 1 files | Cohesion: 69%

## When to Use

- Understanding how send_audio, send_image_file, send_video work
- Modifying cluster_44-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | _send_media, send_audio, send_image_file, send_video, send_voice (+5) |

## Entry Points

Start here when exploring this area:

- **`send_audio`** (Function) — `adapter.py:3492`
- **`send_image_file`** (Function) — `adapter.py:3464`
- **`send_video`** (Function) — `adapter.py:3496`
- **`send_voice`** (Function) — `adapter.py:3487`
- **`init_upload`** (Function) — `adapter.py:1626`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `send_audio` | Function | `adapter.py` | 3492 |
| `send_image_file` | Function | `adapter.py` | 3464 |
| `send_video` | Function | `adapter.py` | 3496 |
| `send_voice` | Function | `adapter.py` | 3487 |
| `init_upload` | Function | `adapter.py` | 1626 |
| `send_attachment` | Function | `adapter.py` | 1684 |
| `resolve` | Function | `adapter.py` | 1426 |
| `attachment_payload` | Function | `adapter.py` | 1396 |
| `_send_media` | Function | `adapter.py` | 3406 |
| `_resolve_slash_confirmation` | Function | `adapter.py` | 1947 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Send_audio → _max_ssl_context` | cross_community | 6 |
| `Send_audio → _call` | cross_community | 6 |
| `Send_image_file → _max_ssl_context` | cross_community | 6 |
| `Send_image_file → _call` | cross_community | 6 |
| `Send_video → _max_ssl_context` | cross_community | 6 |
| `Send_video → _call` | cross_community | 6 |
| `Send_voice → _max_ssl_context` | cross_community | 6 |
| `Send_voice → _call` | cross_community | 6 |
| `Send_audio → Validate_upload_url` | cross_community | 4 |
| `Send_image_file → Validate_upload_url` | cross_community | 4 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 2 calls |
| Cluster_48 | 2 calls |
| Cluster_49 | 1 calls |
| Cluster_43 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "send_audio"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_44"})` — find related execution flows
3. Read key files listed above for implementation details
