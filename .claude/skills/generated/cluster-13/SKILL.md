---
name: cluster-13
description: "Skill for the Cluster_13 area of hermes-max-connector. 4 symbols across 2 files."
---

# Cluster_13

4 symbols | 2 files | Cohesion: 55%

## When to Use

- Understanding how get_me, test_api_client_auth_updates_marker_and_send, FakeResponse work
- Modifying cluster_13-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `tests.py` | FakeResponse, FakeSession, test_api_client_auth_updates_marker_and_send |
| `adapter.py` | get_me |

## Entry Points

Start here when exploring this area:

- **`get_me`** (Function) — `adapter.py:1560`
- **`test_api_client_auth_updates_marker_and_send`** (Function) — `tests.py:231`
- **`FakeResponse`** (Class) — `tests.py:191`
- **`FakeSession`** (Class) — `tests.py:210`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `FakeResponse` | Class | `tests.py` | 191 |
| `FakeSession` | Class | `tests.py` | 210 |
| `get_me` | Function | `adapter.py` | 1560 |
| `test_api_client_auth_updates_marker_and_send` | Function | `tests.py` | 231 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Test_api_client_auth_updates_marker_and_send → _max_ssl_context` | cross_community | 5 |
| `Test_api_client_auth_updates_marker_and_send → _call` | cross_community | 5 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 2 calls |
| Cluster_45 | 1 calls |
| Cluster_48 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "get_me"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_13"})` — find related execution flows
3. Read key files listed above for implementation details
