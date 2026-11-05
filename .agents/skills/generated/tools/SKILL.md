---
name: tools
description: "Skill for the Tools area of hermes-max-connector. 13 symbols across 3 files."
---

# Tools

13 symbols | 3 files | Cohesion: 70%

## When to Use

- Working with code in `tools/`
- Understanding how links, main, normalize_number work
- Modifying tools-related functionality

## Key Files

| File | Symbols |
|------|---------|
| `tools/check_readme_parity.py` | links, main, normalize_number, numbers, technical_tokens (+3) |
| `tools/check_release_hygiene.py` | filesystem_paths, main, tracked_paths |
| `tests/test_qa_regressions.py` | test_filesystem_scan_does_not_skip_an_ignored_name_in_root_ancestors, test_parity_rejects_unclosed_backtick_fence |

## Entry Points

Start here when exploring this area:

- **`links`** (Function) — `tools/check_readme_parity.py:47`
- **`main`** (Function) — `tools/check_readme_parity.py:80`
- **`normalize_number`** (Function) — `tools/check_readme_parity.py:102`
- **`numbers`** (Function) — `tools/check_readme_parity.py:105`
- **`technical_tokens`** (Function) — `tools/check_readme_parity.py:112`

## Key Symbols

| Symbol | Type | File | Line |
|--------|------|------|------|
| `links` | Function | `tools/check_readme_parity.py` | 47 |
| `main` | Function | `tools/check_readme_parity.py` | 80 |
| `normalize_number` | Function | `tools/check_readme_parity.py` | 102 |
| `numbers` | Function | `tools/check_readme_parity.py` | 105 |
| `technical_tokens` | Function | `tools/check_readme_parity.py` | 112 |
| `test_filesystem_scan_does_not_skip_an_ignored_name_in_root_ancestors` | Function | `tests/test_qa_regressions.py` | 88 |
| `filesystem_paths` | Function | `tools/check_release_hygiene.py` | 53 |
| `main` | Function | `tools/check_release_hygiene.py` | 100 |
| `tracked_paths` | Function | `tools/check_release_hygiene.py` | 46 |
| `test_parity_rejects_unclosed_backtick_fence` | Function | `tests/test_qa_regressions.py` | 41 |
| `code_blocks` | Function | `tools/check_readme_parity.py` | 76 |
| `headings` | Function | `tools/check_readme_parity.py` | 42 |
| `markdown_parts` | Function | `tools/check_readme_parity.py` | 51 |

## Connected Areas

| Area | Connections |
|------|-------------|
| Tests | 3 calls |
| Scripts | 2 calls |

## How to Explore

1. `inspect({action: "context", repo: "<repo>", target: "links"})` — see callers and callees
2. `search({action: "semantic", repo: "<repo>", query: "tools"})` — find related execution flows
3. Read key files listed above for implementation details
