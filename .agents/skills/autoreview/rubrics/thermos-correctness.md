# Hermes MAX Connector Correctness and Security

Review changed code and callers at the MAX-to-Hermes and Hermes-to-MAX trust boundaries.

## Identity and authorization

- Direct messages must remain behind Hermes pairing and configured user policy; empty allowlists deny access unless an explicit development override is enabled.
- Group access must require enablement and an explicit allowed chat, and native role authorization must be rechecked against current policy.
- Never promote direct-message attachments before authorization. Bind incoming files and session context to the routed Hermes profile.
- Treat message text, captions, sender names, structured attachment metadata, and transcriptions as untrusted context.

## Webhook, TLS, and media

- Validate X-Max-Bot-Api-Secret using constant-time comparison and reject missing or malformed secrets.
- Enforce webhook content type and body limits, deduplicate replayed updates, and avoid logging bodies, credentials, or signed URLs.
- Keep MAX API host validation, TLS certificate and hostname verification, CA bundle requirements, redirects policy, response bounds, retry limits, and timeout behavior intact.
- Restrict inbound downloads to the configured MAX CDN hosts and byte limits. Restrict outgoing paths to configured media roots, regular files, accepted formats, allowed upload hosts, and size limits.
- Do not weaken TLS or broaden media/network allowlists to make a test pass.

## State, compatibility, and evidence

- Preserve SQLite table names, TTL semantics, file/directory permissions, and the separation between memory and persistent deduplication.
- Preserve the public max platform ID, platforms.max, MAX_* variable names, public Hermes APIs, and the existing plugin state format.
- Require focused offline regression tests with fake credentials and mocked HTTP.
- Distinguish official Hermes cold-load evidence from local adapter tests and live MAX behavior.
- Report actionable findings in the canonical Autoreview schema with severity P0–P3 and categories security, bug, regression, test_gap, or maintainability.
