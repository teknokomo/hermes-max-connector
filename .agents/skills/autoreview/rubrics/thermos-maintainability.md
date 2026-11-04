# Hermes MAX Connector Maintainability and Code Quality

Review focused Python modules and packaging boundaries for the Hermes MAX platform adapter.

## Structure and clarity

- Keep Hermes platform ID, config key, environment variable names, and SQLite schema stable.
- Check asynchronous lifecycle, error translation, bounded retries, and safe diagnostics.
- Keep Python 3.11+ compatibility and runtime dependencies minimal.
- Check that optional document-store integration fails soft when the module is absent.

## Tests and packaging

- Require offline regression coverage for webhook authentication and body limits, pairing/group authorization, persistent deduplication, group cron delivery, media roots, and actual PluginManager package loading.
- Confirm tests use synthetic IDs, fake credentials, and mocked HTTP; they must not send live MAX requests or launch another Gateway.
- Verify plugin.yaml, wheel/sdist contents, manifest checksums, installation path, and README claims against the implementation.
- Check English/Russian headings, examples, links, technical tokens, and code blocks for parity.
- Keep .local, .ontoindex, caches, credentials, and build artifacts out of public archives.

Report concrete maintainability findings through the canonical Autoreview schema.
