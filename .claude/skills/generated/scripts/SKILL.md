---
name: scripts
description: "Skill for the Scripts area of hermes-max-connector. 170 symbols across 5 files."
---

# Scripts

170 symbols | 5 files | Cohesion: 91%

## When to Use

- Working with code in `.agents/`
- Understanding how redact_sensitive_content, test_compact_json_credentials_are_redacted, test_diff_replacement_multiline_sensitive_assignment_keeps_sides_isolated work
- Modifying scripts-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | test_compact_json_credentials_are_redacted, test_diff_replacement_multiline_sensitive_assignment_keeps_sides_isolated, test_double_quoted_python_literal_redaction_preserves_escaped_quotes, test_json_private_key_fields_are_redacted, test_multiline_diff_redaction_tracks_old_and_new_sides_independently (+102) |
| `.agents/skills/autoreview/scripts/autoreview` | redact_sensitive_content, git_bounded, git_paths, local_bundle, review_paths (+25) |
| `.agents/skills/autoreview/scripts/autoreview_runtime.py` | ReviewError, executable_for_engine, preflight_review, resolve_state_dir, validate_extra_prompt (+23) |
| `tests/test_release_gates.py` | test_readme_parity_checker, test_release_hygiene_checker, test_example_config_is_parseable_and_uses_placeholders_only, test_manifest_declares_public_identity_and_required_interfaces |
| `tests/test_qa_regressions.py` | test_publication_scan_reads_index_bytes_not_worktree |

## Entry Points

Start here when exploring this area:

- **`redact_sensitive_content`** (Function) — `.agents/skills/autoreview/scripts/autoreview:906`
- **`test_compact_json_credentials_are_redacted`** (Function) — `.agents/skills/autoreview/scripts/test-autoreview-reliability.py:743`
- **`test_diff_replacement_multiline_sensitive_assignment_keeps_sides_isolated`** (Function) — `.agents/skills/autoreview/scripts/test-autoreview-reliability.py:560`
- **`test_double_quoted_python_literal_redaction_preserves_escaped_quotes`** (Function) — `.agents/skills/autoreview/scripts/test-autoreview-reliability.py:680`
- **`test_json_private_key_fields_are_redacted`** (Function) — `.agents/skills/autoreview/scripts/test-autoreview-reliability.py:737`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `ReviewError` | Class | `.agents/skills/autoreview/scripts/autoreview_runtime.py` | 49 |
| `redact_sensitive_content` | Function | `.agents/skills/autoreview/scripts/autoreview` | 906 |
| `test_compact_json_credentials_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 743 |
| `test_diff_replacement_multiline_sensitive_assignment_keeps_sides_isolated` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 560 |
| `test_double_quoted_python_literal_redaction_preserves_escaped_quotes` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 680 |
| `test_json_private_key_fields_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 737 |
| `test_multiline_diff_redaction_tracks_old_and_new_sides_independently` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 625 |
| `test_multiline_sensitive_assignment_literals_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 533 |
| `test_multiline_sensitive_assignment_with_opener_comment_is_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 547 |
| `test_multiline_sensitive_redaction_preserves_diff_markers` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 607 |
| `test_prefixed_and_triple_quoted_inline_mapping_credentials_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 758 |
| `test_prefixed_sensitive_environment_assignments_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 483 |
| `test_private_key_pem_block_is_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 509 |
| `test_python_config_literals_redact_without_breaking_source` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 663 |
| `test_python_sensitive_boolean_expressions_keep_their_logic` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 411 |
| `test_python_sensitive_code_references_are_preserved_but_literals_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 427 |
| `test_python_sensitive_field_annotations_are_preserved_and_defaults_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 394 |
| `test_sensitive_assignment_redaction_preserves_code_delimiters` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 519 |
| `test_sensitive_assignments_with_env_suffix_are_redacted` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 497 |
| `test_sensitive_mapping_redaction_has_bounded_backtracking` | Function | `.agents/skills/autoreview/scripts/test-autoreview-reliability.py` | 646 |

## Execution Flows

| Flow | Type | Steps |
|------|------|-------|
| `Test_bounded_capture_preserves_split_utf8_and_suppresses_display → Flush` | cross_community | 5 |
| `Test_bounded_capture_preserves_split_utf8_and_suppresses_display → Terminal_safe_text` | cross_community | 5 |
| `Test_engine_output_is_bounded_without_stream_display → Flush` | cross_community | 5 |
| `Test_engine_output_is_bounded_without_stream_display → Terminal_safe_text` | cross_community | 5 |
| `Test_preflight_allows_codex_without_tools → _call` | cross_community | 5 |
| `Test_preflight_allows_missing_primary_when_configured_fallback_exists → _call` | cross_community | 5 |
| `Test_preflight_rejects_invalid_canonical_schema → _call` | cross_community | 5 |
| `Test_preflight_rejects_missing_fallback_executable → _call` | cross_community | 5 |
| `Test_preflight_rejects_missing_primary_without_fallback → _call` | cross_community | 5 |
| `Test_preflight_still_rejects_copilot_without_tools → _call` | cross_community | 5 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 5 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "redact_sensitive_content"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "scripts"})` — find related execution flows
3. Read key files listed above for implementation details
