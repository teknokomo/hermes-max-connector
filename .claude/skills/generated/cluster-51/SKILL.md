---
name: cluster-51
description: "Skill for the Cluster_51 area of hermes-max-connector. 8 symbols across 2 files."
---

# Cluster_51

8 symbols | 2 files | Cohesion: 67%

## When to Use

- Understanding how from_config, is_dm_allowed, is_connected work
- Modifying cluster_51-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | from_config, is_dm_allowed, _bounded_int, _compile_mention_patterns, _truthy (+2) |
| `tests.py` | test_empty_allowlist_denies_and_allow_all_is_explicit |

## Entry Points

Start here when exploring this area:

- **`from_config`** (Function) — `adapter.py:628`
- **`is_dm_allowed`** (Function) — `adapter.py:692`
- **`is_connected`** (Function) — `adapter.py:3555`
- **`validate_config`** (Function) — `adapter.py:3551`
- **`test_empty_allowlist_denies_and_allow_all_is_explicit`** (Function) — `tests.py:53`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `from_config` | Function | `adapter.py` | 628 |
| `is_dm_allowed` | Function | `adapter.py` | 692 |
| `is_connected` | Function | `adapter.py` | 3555 |
| `validate_config` | Function | `adapter.py` | 3551 |
| `test_empty_allowlist_denies_and_allow_all_is_explicit` | Function | `tests.py` | 53 |
| `_bounded_int` | Function | `adapter.py` | 580 |
| `_compile_mention_patterns` | Function | `adapter.py` | 588 |
| `_truthy` | Function | `adapter.py` | 559 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Connect → Is_dm_allowed` | cross_community | 6 |
| `Test_poll_once_dispatches_and_advances_marker → Is_dm_allowed` | cross_community | 5 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 2 calls |
| Cluster_11 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "from_config"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_51"})` — find related execution flows
3. Read key files listed above for implementation details
