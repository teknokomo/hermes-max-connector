---
name: thermo-nuclear-review
description: Deep correctness and security review for Hermes MAX Connector.
metadata:
  version: "1.0.0"
  scope: "hermes-max-connector"
---

# Hermes MAX Connector correctness and security review

Review the trust boundary from MAX update to Hermes event and from Hermes output to the MAX API. Trace callers and state transitions instead of relying on names or comments.

Check webhook secret validation and response behavior; allowlist and pairing gates; group grant reauthorization; routing to the correct Hermes profile; untrusted message and attachment context; CDN host, path, size, and media-root restrictions; TLS certificate and hostname validation; retry/dedup semantics; SQLite TTL and permissions; and logs/errors for token, URL, ID, body, or path disclosure.

Require offline regression tests with fake credentials and mocked HTTP. Do not use live MAX credentials or a second Gateway as review fixtures. Distinguish source-level conclusions from tests, Hermes compatibility runs, and live runtime evidence.
