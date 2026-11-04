---
name: cluster-52
description: "Skill for the Cluster_52 area of hermes-max-connector. 5 symbols across 1 files."
---

# Cluster_52

5 symbols | 1 files | Cohesion: 89%

## When to Use

- Understanding how _is_adts_aac, _is_m4a_audio_container, _is_mpeg_audio_frame work
- Modifying cluster_52-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | _is_adts_aac, _is_m4a_audio_container, _is_mpeg_audio_frame, _is_ogg_opus, _sniff_audio_format |

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `_is_adts_aac` | Function | `adapter.py` | 514 |
| `_is_m4a_audio_container` | Function | `adapter.py` | 524 |
| `_is_mpeg_audio_frame` | Function | `adapter.py` | 502 |
| `_is_ogg_opus` | Function | `adapter.py` | 480 |
| `_sniff_audio_format` | Function | `adapter.py` | 535 |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "_is_adts_aac"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "cluster_52"})` — find related execution flows
3. Read key files listed above for implementation details
