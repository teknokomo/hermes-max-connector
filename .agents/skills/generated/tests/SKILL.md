---
name: tests
description: "Skill for the Tests area of hermes-max-connector. 115 symbols across 6 files."
---

# Tests

115 symbols | 6 files | Cohesion: 72%

## When to Use

- Working with code in `tests/`
- Understanding how connect, get_updates, list_subscriptions work
- Modifying tests-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `adapter.py` | InboundAttachment, ParsedMessage, ParsedMessageLifecycle, _classify_subscription, _dispatch_lifecycle_update (+64) |
| `tests/test_release_gates.py` | test_plugin_manager_cold_loads_public_package, test_inbound_media_home_uses_routed_profile, test_rejected_profile_route_has_no_media_home, _Request, config (+13) |
| `tests/test_qa_regressions.py` | test_optional_document_store_absence_preserves_profile_cache, Client, test_outgoing_media_inside_root_reaches_mock_upload, Request, test_passive_group_store_failure_can_be_retried (+8) |
| `tests.py` | _call, get, post, test_env_enablement_and_yaml_bridge_do_not_expose_token, test_parse_message_created_and_ignore_other_or_malformed_updates (+3) |
| `tests/conftest.py` | build_source, BasePlatformAdapter, __init__, PlatformRegistry, _install_hermes_boundary (+1) |
| `tools/check_release_hygiene.py` | scan |

## Entry Points

Start here when exploring this area:

- **`connect`** (Function) — `adapter.py:2619`
- **`get_updates`** (Function) — `adapter.py:1611`
- **`list_subscriptions`** (Function) — `adapter.py:1606`
- **`parse_message_created`** (Function) — `adapter.py:1199`
- **`parse_message_lifecycle`** (Function) — `adapter.py:1296`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `InboundAttachment` | Class | `adapter.py` | 708 |
| `ParsedMessage` | Class | `adapter.py` | 810 |
| `ParsedMessageLifecycle` | Class | `adapter.py` | 837 |
| `PublicResolver` | Class | `adapter.py` | 1425 |
| `MaxAdapter` | Class | `adapter.py` | 1976 |
| `BasePlatformAdapter` | Class | `tests/conftest.py` | 43 |
| `Client` | Class | `tests/test_qa_regressions.py` | 190 |
| `GroupMetadata` | Class | `adapter.py` | 850 |
| `Request` | Class | `tests/test_qa_regressions.py` | 166 |
| `MaxApiClient` | Class | `adapter.py` | 1491 |
| `InboundMediaDownloader` | Class | `adapter.py` | 1412 |
| `MaxPersistentState` | Class | `adapter.py` | 314 |
| `PlatformRegistry` | Class | `tests/conftest.py` | 59 |
| `connect` | Function | `adapter.py` | 2619 |
| `get_updates` | Function | `adapter.py` | 1611 |
| `list_subscriptions` | Function | `adapter.py` | 1606 |
| `parse_message_created` | Function | `adapter.py` | 1199 |
| `parse_message_lifecycle` | Function | `adapter.py` | 1296 |
| `parse_reply_link` | Function | `adapter.py` | 867 |
| `subscription_is_healthy` | Function | `adapter.py` | 299 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `_handle_autosave_command → _max_ssl_context` | cross_community | 7 |
| `_handle_autosave_command → _call` | cross_community | 7 |
| `Connect → _connect` | cross_community | 7 |
| `Send → _call` | cross_community | 7 |
| `_dispatch_callback → _call` | cross_community | 6 |
| `Connect → ParsedMessageLifecycle` | intra_community | 6 |
| `Connect → _call` | intra_community | 6 |
| `Connect → Validate_inbound_cdn_url` | cross_community | 6 |
| `Connect → Is_dm_allowed` | cross_community | 6 |
| `Connect → Is_group_allowed` | cross_community | 6 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Cluster_10 | 4 calls |
| Cluster_48 | 4 calls |
| Cluster_50 | 3 calls |
| Cluster_51 | 3 calls |
| Cluster_45 | 3 calls |
| Scripts | 2 calls |
| Cluster_11 | 1 calls |
| Cluster_55 | 1 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "connect"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "tests"})` — find related execution flows
3. Read key files listed above for implementation details
