# Security policy

## Trust boundaries

The MAX adapter runs inside the Hermes Gateway process and has the authority of the Hermes profile that loads it. Install and enable it only when you trust the source and its maintainers.

The adapter validates incoming webhook requests with the configured MAX_WEBHOOK_SECRET using a constant-time comparison. The secret arrives in the X-Max-Bot-Api-Secret header. The webhook listener binds to a loopback address; place it behind a TLS-terminating reverse proxy and expose only the configured webhook path.

Webhook identities are marked complete only after the connector handler succeeds. Failures and concurrent in-progress duplicates receive HTTP 503 for MAX retry; request handling is capped at 25 seconds within MAX's documented 30-second response window.

Direct messages use Hermes pairing and configured user allowlists. Group access is disabled by default and requires the group feature to be enabled plus an explicit allowed chat. Reauthorization checks the group grant again for native role actions. MAX_ALLOW_ALL_USERS is an unsafe broad override and should remain disabled.

Incoming media is downloaded only from the connector's allowlisted MAX media hosts, with byte limits and profile-aware caching. Outgoing media must resolve under a configured media_roots directory, use an allowed format, and remain within the size limit. Treat attachment names, captions, transcription, and structured attachment metadata as untrusted input.

MAX API traffic uses a profile-scoped CA bundle with hostname and certificate verification. The connector rejects missing or unreadable bundles. Never use verify=False or add an unrelated root certificate to the operating system trust store to work around a TLS failure.

Optional SQLite reliability state stores opaque webhook deduplication identities and short-lived interactive tokens. It does not store message bodies, chat IDs, user IDs, bot tokens, or webhook secrets. Keep the profile directory private and back it up according to the profile owner's policy.

## Reporting a vulnerability

Report security issues privately to the project maintainers before opening a public issue. Include the affected version, a minimal reproduction, and the impact. Do not include live credentials, private chat data, or unredacted webhook requests. Rotate any credential that may have been exposed.
