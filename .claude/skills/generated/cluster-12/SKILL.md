---
name: cluster-12
description: "Skill for the Cluster_12 area of hermes-max-connector. 4 symbols across 2 files."
---

# Cluster_12

4 symbols | 2 files | Cohesion: 86%

## When to Use

- Understanding how register, register_platform, test_register_exposes_standalone_sender_and_security_hooks work
- Modifying cluster_12-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `tests.py` | Ctx, register_platform, test_register_exposes_standalone_sender_and_security_hooks |
| `adapter.py` | register |

## Entry Points

Start here when exploring this area:

- **`register`** (Function) — `adapter.py:3646`
- **`register_platform`** (Function) — `tests.py:11`
- **`test_register_exposes_standalone_sender_and_security_hooks`** (Function) — `tests.py:324`
- **`Ctx`** (Class) — `tests.py:325`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `Ctx` | Class | `tests.py` | 325 |
| `register` | Function | `adapter.py` | 3646 |
| `register_platform` | Function | `tests.py` | 11 |
| `test_register_exposes_standalone_sender_and_security_hooks` | Function | `tests.py` | 324 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "register"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_12"})` — find related execution flows
3. Read key files listed above for implementation details
