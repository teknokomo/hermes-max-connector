---
name: cluster-11
description: "Skill for the Cluster_11 area of hermes-max-connector. 6 symbols across 1 files."
---

# Cluster_11

6 symbols | 1 files | Cohesion: 50%

## When to Use

- Understanding how config, test_adapter_forwards_dm_to_gateway_pairing_auth, test_config_env_precedence_and_safe_defaults work
- Modifying cluster_11-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `tests.py` | Client, config, test_adapter_forwards_dm_to_gateway_pairing_auth, test_config_env_precedence_and_safe_defaults, test_group_dispatch_injects_attribution_guard_without_observed_history (+1) |

## Entry Points

Start here when exploring this area:

- **`config`** (Function) — `tests.py:34`
- **`test_adapter_forwards_dm_to_gateway_pairing_auth`** (Function) — `tests.py:272`
- **`test_config_env_precedence_and_safe_defaults`** (Function) — `tests.py:38`
- **`test_group_dispatch_injects_attribution_guard_without_observed_history`** (Function) — `tests.py:118`
- **`test_poll_once_dispatches_and_advances_marker`** (Function) — `tests.py:297`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `Client` | Class | `tests.py` | 302 |
| `config` | Function | `tests.py` | 34 |
| `test_adapter_forwards_dm_to_gateway_pairing_auth` | Function | `tests.py` | 272 |
| `test_config_env_precedence_and_safe_defaults` | Function | `tests.py` | 38 |
| `test_group_dispatch_injects_attribution_guard_without_observed_history` | Function | `tests.py` | 118 |
| `test_poll_once_dispatches_and_advances_marker` | Function | `tests.py` | 297 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → Chunk_text` | cross_community | 6 |
| `Test_group_dispatch_injects_attribution_guard_without_observed_history → Chunk_text` | cross_community | 6 |
| `Test_poll_once_dispatches_and_advances_marker → _connect` | cross_community | 6 |
| `Test_poll_once_dispatches_and_advances_marker → _call` | cross_community | 6 |
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → PublicResolver` | cross_community | 5 |
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → _call` | cross_community | 5 |
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → Validate_inbound_cdn_url` | cross_community | 5 |
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → _document_store_module` | cross_community | 5 |
| `Test_adapter_forwards_dm_to_gateway_pairing_auth → _autosave_scope` | cross_community | 5 |
| `Test_group_dispatch_injects_attribution_guard_without_observed_history → PublicResolver` | cross_community | 5 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 6 calls |
| Cluster_51 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "config"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_11"})` — find related execution flows
3. Read key files listed above for implementation details
