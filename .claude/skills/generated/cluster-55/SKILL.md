---
name: cluster-55
description: "Skill for the Cluster_55 area of hermes-max-connector. 4 symbols across 2 files."
---

# Cluster_55

4 symbols | 2 files | Cohesion: 89%

## When to Use

- Understanding how generate_webhook_secret, is_valid_webhook_secret, verify_webhook_secret work
- Modifying cluster_55-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | generate_webhook_secret, is_valid_webhook_secret, verify_webhook_secret |
| `tests.py` | test_webhook_secret_helpers |

## Entry Points

Start here when exploring this area:

- **`generate_webhook_secret`** (Function) — `adapter.py:1364`
- **`is_valid_webhook_secret`** (Function) — `adapter.py:1372`
- **`verify_webhook_secret`** (Function) — `adapter.py:1376`
- **`test_webhook_secret_helpers`** (Function) — `tests.py:180`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `generate_webhook_secret` | Function | `adapter.py` | 1364 |
| `is_valid_webhook_secret` | Function | `adapter.py` | 1372 |
| `verify_webhook_secret` | Function | `adapter.py` | 1376 |
| `test_webhook_secret_helpers` | Function | `tests.py` | 180 |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "generate_webhook_secret"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_55"})` — find related execution flows
3. Read key files listed above for implementation details
