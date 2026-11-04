---
name: cluster-10
description: "Skill for the Cluster_10 area of hermes-max-connector. 4 symbols across 1 files."
---

# Cluster_10

4 symbols | 1 files | Cohesion: 50%

## When to Use

- Understanding how ReplyLink work
- Modifying cluster_10-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | ReplyLink, _declared_size, _resolved_reply_link, _safe_inbound_filename |

## Entry Points

Start here when exploring this area:

- **`ReplyLink`** (Class) — `adapter.py:858`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ReplyLink` | Class | `adapter.py` | 858 |
| `_declared_size` | Function | `adapter.py` | 742 |
| `_resolved_reply_link` | Function | `adapter.py` | 914 |
| `_safe_inbound_filename` | Function | `adapter.py` | 725 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 2 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "ReplyLink"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_10"})` — find related execution flows
3. Read key files listed above for implementation details
