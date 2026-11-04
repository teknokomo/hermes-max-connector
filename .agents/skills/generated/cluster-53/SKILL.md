---
name: cluster-53
description: "Skill for the Cluster_53 area of hermes-max-connector. 4 symbols across 1 files."
---

# Cluster_53

4 symbols | 1 files | Cohesion: 75%

## When to Use

- Understanding how _log_webhook_shape, _safe_webhook_category, _safe_webhook_keys work
- Modifying cluster_53-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | _log_webhook_shape, _safe_webhook_category, _safe_webhook_keys, _webhook_json_category |

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `_log_webhook_shape` | Function | `adapter.py` | 248 |
| `_safe_webhook_category` | Function | `adapter.py` | 218 |
| `_safe_webhook_keys` | Function | `adapter.py` | 223 |
| `_webhook_json_category` | Function | `adapter.py` | 234 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "_log_webhook_shape"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_53"})` — find related execution flows
3. Read key files listed above for implementation details
