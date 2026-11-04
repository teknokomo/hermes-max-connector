---
name: thermos
description: Orchestrate correctness/security and maintainability review for Hermes MAX Connector.
metadata:
  version: "1.0.0"
  scope: "hermes-max-connector"
---

# Thermos review

Use Thermos for connector code changes, explicit code review, and final QA.

## Required checks

1. Read the changed code, its callers, tests, `SECURITY.md`, and relevant deployment guidance.
2. Run the focused offline tests and static checks independently of the reviewer.
3. Run `.agents/skills/autoreview/scripts/autoreview --mode local --prompt-file .agents/skills/autoreview/rubrics/thermos.md`.
4. Verify findings against source and tests, fix accepted actionable issues, and repeat affected checks and review.
5. Report reviewed scope, commands/evidence, accepted or rejected findings, and the helper's terminal status.

Critical correctness or security findings block a clean recommendation. A local pass does not prove live MAX delivery, production credentials, webhook subscription health, or systemd configuration.
