# MAX webhook deployment

Run the MAX webhook listener behind a trusted reverse proxy. MAX sends webhook requests to an HTTPS endpoint on port 443. The proxy terminates public TLS and forwards only the configured path to the adapter bound to a loopback address. Keep the proxy route, the adapter path, and the MAX subscription URL aligned. See the [official MAX subscription requirements](https://dev.max.ru/docs-api/methods/POST/subscriptions).

Configure the adapter with webhook transport enabled, the expected webhook secret, and the listener host, port, and path. The adapter listens on loopback; it does not bind a public interface and does not create a MAX subscription. Create and manage the subscription through the MAX Bot API and verify that it includes message_created, message_callback, message_edited, and message_removed.

MAX expects a successful HTTP 200 response within 30 seconds. The connector bounds handler processing to 25 seconds, returns 503 when processing fails or is still in progress, and returns 200 only after successful dispatch or for an already completed duplicate. MAX retries unsuccessful responses up to 10 times and removes a subscription after 8 hours without a successful delivery. Monitor the subscription and adapter logs without recording request bodies, tokens, webhook secrets, or signed media URLs.

Provide a profile-scoped CA bundle through MAX_CA_BUNDLE or platforms.max.ca_bundle. The connector requires certificate validation and hostname checking for MAX API requests. Do not disable TLS verification and do not install an untrusted or unrelated root certificate into the operating system trust store.

Long polling is an opt-in development and testing transport. Do not run it alongside webhook transport for the same bot. The adapter rejects that configuration.
