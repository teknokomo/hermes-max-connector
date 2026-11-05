# Hermes MAX Connector Thermos Review

Review changed source, tests, package metadata, and deployment guidance for correctness, security, concurrency, and maintainability. Verify documentation claims against the connector code.

## Correctness and security

- Trace MAX updates through authentication, policy checks, profile routing, attachment caching, and Hermes dispatch.
- Verify pairing and static DM allowlists, group allowlists, reauthorization, and that unauthenticated DMs cannot trigger durable attachment promotion.
- Check webhook secret validation, request body/content-type bounds, replay deduplication, callback handling, and safe logging.
- Check profile-scoped CA configuration, certificate and hostname verification, API host restrictions, upload/download allowlists, size bounds, and redirects.
- Verify inbound and outbound media paths remain bound to the routed profile and configured roots.
- Review SQLite permissions, data minimization, TTL cleanup, retry behavior, and state compatibility.
- Preserve the public max platform ID, platforms.max key, MAX_* variables, Hermes registration surface, and SQLite format.
- Distinguish live delivery, API subscriptions, and runtime configuration from local source evidence.

## Maintainability and evidence

- Check module complexity, asynchronous lifecycle, Python 3.11+ support, error handling, tests, and dependency scope.
- Require fake credentials and mocked network calls for all offline tests.
- Check the package can be cold-loaded by the official Hermes PluginManager and that __init__.py exports register.
- Verify package metadata, checksums, wheel/sdist contents, bilingual README parity, and exclusion of .local and .ontoindex.
- Report actionable findings in the helper's canonical JSON result. Use P0–P3 severity and categories security, bug, regression, test_gap, or maintainability.
