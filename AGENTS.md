# Project instructions

This repository contains the Hermes MAX platform connector. Treat the Hermes platform ID max, platforms.max configuration, MAX_* environment variables, public plugin registration and SQLite state format as compatibility contracts.

## Before changing code

- Read README.md, README-RU.md, SECURITY.md, and relevant sections of deploy/README.md.
- Inspect the current diff and preserve unrelated changes.
- Keep webhook authentication, DM pairing, group allowlists and reauthorization, profile-aware media handling, TLS verification, attachment limits, and SQLite state boundaries intact unless a scoped change explicitly requires otherwise.
- Use Python 3.11+ and avoid runtime dependencies beyond aiohttp without a concrete need.
- Keep public user documentation in Russian and English with matching headings and examples. Keep source comments and docstrings in English.

## Security and operations

- Treat MAX_BOT_TOKEN, MAX_WEBHOOK_SECRET, CA bundles, real chat/user IDs, signed media URLs, profile state, and private server details as sensitive.
- Offline tests must use fake credentials and mocked HTTP. Do not contact MAX or install/restart a live Hermes service during ordinary code work.
- Do not change the production Hermes plugin, profiles, allowlists, subscriptions, or Gateway from this repository task.
- Do not include production identifiers or the ignored .local handoff archive in Git.

## Verification

Run the checks documented in README.md and the release workflow. When testing PluginManager loading, use an official Hermes source tree selected through HERMES_SOURCE_DIR and verify the exact upstream version in the result. Report offline tests separately from any live runtime evidence.

## OntoIndex

- The project graph is local in ignored .ontoindex/; never copy it from another repository.
- Check OntoIndex status before graph-backed claims. For a new or unindexed project, use direct source inspection until a fresh project-specific graph is generated.
- Run impact analysis before changing functions when the current graph supports the source; use direct inspection if it does not.
- Keep .ontoindex/, generated caches, and build output out of Git.

Edit-gate fallback: if OntoIndex tools or a usable current graph are unavailable, inspect the relevant source, callers, and tests directly to establish impact before editing; record that graph-backed impact analysis was unavailable. Commit-gate fallback: manually reconcile changed files and expected symbols with executed tests; do not report `verify_diff` as passing.

<!-- ontoindex:start -->
# OntoIndex — Code Intelligence

This project is indexed by OntoIndex as **hermes-max-connector** (1869 symbols, 3801 relationships, 161 execution flows). Use the OntoIndex MCP tools to understand code, assess impact, and navigate safely.

> Always query OntoIndex first. Repo queries refresh stale indexes in the background; dirty edits use the automatic overlay. Use stale/refreshing results with freshness labels; verify edited or new code from source. Never fall back to grep-only because the index is stale. Manual `ontoindex analyze` is only for immediate refresh with no active job. Sub-agents never start reindex jobs; refresh-on-query covers them.

## Always Do

Use OntoIndex in this order:

1. **Explore/search** — MCP `search({action: "semantic", repo: "hermes-max-connector", query: "concept"})` to find execution flows instead of grepping.
2. **Inspect context** — MCP `inspect({action: "context", repo: "hermes-max-connector", target: "symbolName"})` for a symbol's callers, callees, and execution flows.
3. **Impact before edits** — MCP `impact({action: "symbol", repo: "hermes-max-connector", target: "symbolName", direction: "upstream"})` or CLI `ontoindex impact --repo hermes-max-connector <symbol>`; report the blast radius and MUST warn on HIGH or CRITICAL risk before editing.
4. **Verify scope before commit** — use MCP `audit({action: "verify_diff", repo: "hermes-max-connector", scope: "all", changedFiles: [...], expectedFiles: [...], expectedSymbols: [...], executedTests: [...]})` with actual paths, symbols, and test commands from this change. `scope: "all"` alone does not define the expected scope.

## Never Do

- NEVER edit a function, class, or method without first running MCP `impact` or CLI `ontoindex impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- For symbol renames, use MCP `refactor({action: "rename", ...})` to preview candidates; review them, then apply the rename through manual file edits. The tool does not apply changes.
- NEVER commit changes without step 4 verification.

## Resources

| Resource | Use for |
|----------|---------|
| `ontoindex://repo/hermes-max-connector/context` | Codebase overview, check index freshness |
| `ontoindex://repo/hermes-max-connector/clusters` | All functional areas |
| `ontoindex://repo/hermes-max-connector/processes` | All execution flows |
| `ontoindex://repo/hermes-max-connector/process/{name}` | Step-by-step execution trace |

## CLI

| Task | Read this skill file |
|------|---------------------|
| Start here, any task | `.claude/skills/ontoindex/ontoindex-navigation/SKILL.md` |
| Understand architecture / "How does X work?" | `.claude/skills/ontoindex/ontoindex-exploring/SKILL.md` |
| Blast radius / "What breaks if I change X?" | `.claude/skills/ontoindex/ontoindex-impact-analysis/SKILL.md` |
| Trace bugs / "Why is X failing?" | `.claude/skills/ontoindex/ontoindex-debugging/SKILL.md` |
| Rename / extract / split / refactor | `.claude/skills/ontoindex/ontoindex-refactoring/SKILL.md` |
| Tools, resources, schema reference | `.claude/skills/ontoindex/ontoindex-guide/SKILL.md` |
| Index, status, clean, wiki CLI commands | `.claude/skills/ontoindex/ontoindex-cli/SKILL.md` |
| Work in the Scripts area (170 symbols) | `.claude/skills/generated/scripts/SKILL.md` |
| Work in the Tests area (115 symbols) | `.claude/skills/generated/tests/SKILL.md` |
| Work in the Tools area (13 symbols) | `.claude/skills/generated/tools/SKILL.md` |
| Work in the Cluster_8 area (12 symbols) | `.claude/skills/generated/cluster-8/SKILL.md` |
| Work in the Cluster_43 area (11 symbols) | `.claude/skills/generated/cluster-43/SKILL.md` |
| Work in the Cluster_44 area (10 symbols) | `.claude/skills/generated/cluster-44/SKILL.md` |
| Work in the Cluster_45 area (8 symbols) | `.claude/skills/generated/cluster-45/SKILL.md` |
| Work in the Cluster_51 area (8 symbols) | `.claude/skills/generated/cluster-51/SKILL.md` |
| Work in the Cluster_11 area (6 symbols) | `.claude/skills/generated/cluster-11/SKILL.md` |
| Work in the Cluster_48 area (6 symbols) | `.claude/skills/generated/cluster-48/SKILL.md` |
| Work in the Cluster_52 area (5 symbols) | `.claude/skills/generated/cluster-52/SKILL.md` |
| Work in the Cluster_54 area (5 symbols) | `.claude/skills/generated/cluster-54/SKILL.md` |
| Work in the Cluster_10 area (4 symbols) | `.claude/skills/generated/cluster-10/SKILL.md` |
| Work in the Cluster_12 area (4 symbols) | `.claude/skills/generated/cluster-12/SKILL.md` |
| Work in the Cluster_13 area (4 symbols) | `.claude/skills/generated/cluster-13/SKILL.md` |
| Work in the Cluster_47 area (4 symbols) | `.claude/skills/generated/cluster-47/SKILL.md` |
| Work in the Cluster_49 area (4 symbols) | `.claude/skills/generated/cluster-49/SKILL.md` |
| Work in the Cluster_50 area (4 symbols) | `.claude/skills/generated/cluster-50/SKILL.md` |
| Work in the Cluster_53 area (4 symbols) | `.claude/skills/generated/cluster-53/SKILL.md` |
| Work in the Cluster_55 area (4 symbols) | `.claude/skills/generated/cluster-55/SKILL.md` |

<!-- ontoindex:end -->
