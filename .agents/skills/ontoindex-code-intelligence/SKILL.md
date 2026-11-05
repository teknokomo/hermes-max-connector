---
name: ontoindex-code-intelligence
description: Use the repository-specific OntoIndex graph for Hermes MAX Connector symbol search, impact analysis, and diff checks.
metadata:
  version: "1.0.0"
  scope: "hermes-max-connector"
---

# OntoIndex for Hermes MAX Connector

The project graph is generated locally in `.ontoindex/` and must never be copied from another repository. It supports Python symbol navigation; it does not prove security or live Hermes behavior.

## Setup and status

Use the CLI from this repository and verify the repository identity before relying on graph results:

~~~bash
ontoindex status --repo "$PWD"
~~~

Repository queries refresh stale indexes in the background, so normally rely on refresh-on-query. Only the coordinating agent may start a manual `ontoindex analyze` when an immediate refresh is required and status confirms that no analysis job is active; sub-agents must not start or duplicate analysis jobs. If a manual refresh is required before Git history exists, use `ontoindex analyze --skip-git --skip-agents-md --name hermes-max-connector "$PWD"`. Do not run `ontoindex setup` unless asked to change MCP client configuration.

## Safe use

- Check `ontoindex status` before graph-backed claims. Verify changed or uncommitted source directly.
- Search/context can locate callers and flows; inspect source and tests before concluding.
- Run impact analysis before code changes when the graph is current and includes the target function. Otherwise use direct source inspection and say graph impact was unavailable.
- Run diff verification after changes only when the graph identifies this repository and can represent the changed files.
- Treat webhook secrets, MAX identity, authorization, attachment provenance, TLS, and SQLite behavior as source-and-test review areas; the graph is supporting evidence only.
