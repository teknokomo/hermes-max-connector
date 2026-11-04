# Project skills and review tools

This directory contains the review workflow for the standalone Hermes MAX Connector.

- `autoreview/` contains the local review helper, its reliability checks, and MAX specific review rubrics.
- `thermos/` coordinates correctness/security and maintainability reviews.
- `thermo-nuclear-review/` focuses on webhook authentication, authorization, media provenance, TLS, state, and concurrency.
- `thermo-nuclear-code-quality-review/` focuses on Python maintainability, tests, packaging, and public documentation.
- `ontoindex-code-intelligence/` documents project-scoped OntoIndex use. The index itself is generated separately under the ignored `.ontoindex/` directory.
- `.claude/skills/ontoindex/` contains the general CLI navigation instructions for OntoIndex.

Start with the repository-root `AGENTS.md`. Run the local review helper with `.agents/skills/autoreview/rubrics/thermos.md`. If it reports `UNAVAILABLE` or `INCOMPLETE`, report that status instead of calling the review clean.
