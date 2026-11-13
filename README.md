🇬🇧 **English** | 🇷🇺 [Русский](README-RU.md)

[![Version](https://img.shields.io/github/v/release/teknokomo/hermes-max-connector?label=version&color=blue&sort=semver)](https://github.com/teknokomo/hermes-max-connector/releases/latest)
[![License: Omsk Open License](https://img.shields.io/badge/license-Omsk%20Open%20License-green)](LICENSE.md)

![Teknokomo — 73rd Meridian](docs/assets/teknokomo-om73-en.jpg)

# Important! Grave! Важно!

- Workers of the world, unite!
- Proletoj el ĉiuj landoj, unuiĝu!
- Пролетарии всех стран, соединяйтесь!

# Hermes MAX Connector

**Attention: version 0.1.0 is the first public release. Review the security and transport settings before enabling this connector.**

## Developers

Developed by [Teknokomo](https://universo.pro/).<br>
Made with the support of the [73rd Meridian Consortium](https://om73.ru).

## Overview

Hermes MAX Connector adds MAX messenger as a platform adapter for Hermes Agent. It receives messages from MAX through a production webhook or an opt-in development long-polling transport, applies profile policy, and sends replies through the MAX Bot API.

The public package name is hermes-max-connector. The registered Hermes platform and configuration key remain max, so settings continue to live under platforms.max.

## Features

- Direct messages use Hermes pairing and configured user allowlists.
- Groups require explicit enablement and an allowed chat ID; group grants are rechecked for native role actions.
- Webhook requests require the configured shared secret and are deduplicated in memory, with optional profile-local SQLite persistence.
- Incoming attachments use an allowlisted MAX media host and are cached under the routed Hermes profile.
- Outgoing files are restricted to configured media_roots and checked for type and size.
- Replies longer than 4,000 characters are split without dropping text.

## Installation

Install the project files in the `plugins` directory under the active profile's Hermes home. With the default profile and no custom HERMES_HOME, this is ~/.hermes; a named profile uses `<Hermes root>/profiles/<name>`. Set HERMES_PROFILE_HOME to that profile home before copying; for a named profile, do not leave it at the default path:

```bash
# For a named profile, set this to that profile's Hermes home.
HERMES_PROFILE_HOME="${HERMES_HOME:-$HOME/.hermes}"
mkdir -p "$HERMES_PROFILE_HOME/plugins/hermes-max-connector"
cp adapter.py __init__.py plugin.yaml "$HERMES_PROFILE_HOME/plugins/hermes-max-connector/"
```

After publication, Hermes can also install from the public repository; select the same profile for installation and activation.

Install aiohttp in the Python environment used by Hermes. Configure MAX_BOT_TOKEN and a trusted CA bundle, then enable hermes-max-connector with hermes plugins enable hermes-max-connector. For a named profile, use `hermes -p <name> plugins enable hermes-max-connector`. Keep the platform key max in config.yaml.

## Configuration

| Setting | Required | Purpose and default |
|---|---|---|
| MAX_BOT_TOKEN | Yes | MAX Bot API credential; required. |
| MAX_ALLOWED_USERS | No | Comma-separated MAX user IDs allowed to start direct-message turns; empty by default. |
| MAX_ALLOW_ALL_USERS | No | Allows every direct-message sender when true; defaults to false. |
| MAX_POLLING_DEV | No | Enables development long polling when true; defaults to false. |
| MAX_POLL_TIMEOUT | No | Long-poll wait in seconds; defaults to 30 and is bounded to 1–90. |
| MAX_CA_BUNDLE | No | Profile-scoped PEM CA bundle for verified MAX API TLS; required for API connections unless platforms.max.ca_bundle supplies the path. |
| MAX_HOME_CHANNEL | No | MAX user or chat destination for Hermes cron delivery; unset by default. |
| MAX_WEBHOOK_SECRET | Conditional | Shared secret checked against X-Max-Bot-Api-Secret when webhook transport is enabled. |

Non-secret settings belong under platforms.max. The adapter also supports allowed_users, allow_all_users, webhook, webhook_host, webhook_port, webhook_path, media_roots, persistent_state, markdown, and group policy settings. See config/example.yaml for a placeholder-only example.

Direct messages use Hermes pairing. MAX_ALLOWED_USERS adds a static user allowlist; the default policy does not allow every user. Group conversations are off by default. To enable a group, set groups.enabled and list its chat ID in groups.allowed_chats. Keep require_mention enabled unless the group has a clear reason to allow unaddressed messages. Passive observation of unmentioned messages and documents is off by default; set groups.observe_unmentioned_group_messages to true only when you explicitly want them saved in the session transcript. Use MAX_ALLOW_ALL_USERS only for a controlled development setup.

## Transports

Webhook is the production transport. Set platforms.max.webhook to true, configure MAX_WEBHOOK_SECRET, and expose the loopback listener through a trusted HTTPS reverse proxy on port 443. The adapter does not create a MAX subscription; create it through the MAX Bot API and include message_created, message_callback, message_edited, and message_removed. Set the subscription's `secret` to the same value as `MAX_WEBHOOK_SECRET` (5–256 letters, digits, underscores, or hyphens, as required by MAX); MAX sends it in `X-Max-Bot-Api-Secret` only when configured, and the connector rejects a missing or mismatched header.

Follow the [MAX webhook subscription requirements](https://dev.max.ru/docs-api/methods/POST/subscriptions) when creating and operating the subscription.

The connector returns HTTP 200 after the update handler completes. Handler failures, duplicate deliveries that are still processing, and handler timeouts return HTTP 503 so MAX can retry; processing is bounded to 25 seconds to stay within the 30-second response window.

Long polling is development-only and disabled by default. Set MAX_POLLING_DEV=true for a controlled test bot. Webhook and polling cannot be enabled together.

## TLS and media

MAX API requests require certificate and hostname verification with a trusted profile-scoped CA bundle. Set MAX_CA_BUNDLE or platforms.max.ca_bundle. The connector does not fall back to disabled verification. Do not use verify=False or install an unrelated root certificate into the system trust store.

Incoming media is fetched from configured MAX CDN hosts with a 20 MiB limit and cached for the routed Hermes profile. Outgoing media requires a media_roots entry; files outside those roots are rejected. Image uploads are limited to 50 MiB and other outgoing files to 50 MiB. Only the configured supported media types and MAX upload hosts are accepted.

The optional document-store integration — the `document-store` component of [hermes-document-platform](https://github.com/teknokomo/hermes-document-platform), published as the `omisa-document-store` plugin — provides profile-aware document autosave when installed. Without it the MAX connector still registers and handles ordinary platform traffic; only document autosave is unavailable. Autosave applies only to group chats. Documents sent in direct messages are cached but not saved durably.

## State and limits

The optional persistent_state setting stores webhook deduplication and interactive-token state in the profile-local max/reliability.db SQLite database. In-memory deduplication retains up to 4,096 recent webhook identities. Persistent entries expire after 7 days. The webhook body limit is 1 MiB.

MAX messages are limited to 4,000 characters per outgoing message and are chunked automatically. Typing notifications are best-effort. Long polling is intended for development, and MAX API behavior may vary by bot permissions and supported update types.

## Verification

From the repository or an unpacked source distribution, install the locked development environment and run the offline checks:

```bash
uv sync --locked --group dev
uv run pytest -q
uv run python -m compileall -q adapter.py __init__.py conftest.py tests.py tests tools
uv run ruff check adapter.py __init__.py conftest.py tests.py tests tools
uv run bandit -r adapter.py __init__.py -c pyproject.toml
uv run python tools/check_readme_parity.py
uv run python tools/check_release_hygiene.py --filesystem
sha256sum -c MANIFEST.sha256
uv run python -m build
uv run twine check dist/*
```

Tests use fake credentials and mocked MAX API calls; HTTP ingress tests use a temporary loopback listener. The Python 3.11–3.14 unit matrix supplies a minimal Hermes boundary. The separate CI compatibility jobs cold-load the plugin on official Hermes v0.22.4 and v0.22.5 using their required Python runtime; without HERMES_SOURCE_DIR that integration test is explicitly skipped. See .github/workflows/ci.yml for the pinned upstream commits and compatibility commands.

Before committing, stage the intended files and run `uv run python tools/check_release_hygiene.py` to scan the actual Git index. The filesystem scan checks current source files; neither scan replaces manual review of names, identifiers, or private context.

## Security and project files

Read [SECURITY.md](SECURITY.md) for trust boundaries and vulnerability reporting, [CHANGELOG.md](CHANGELOG.md) for release history, and [LICENSE.md](LICENSE.md) for the license text. Webhook deployment guidance is in [deploy/README.md](deploy/README.md).
