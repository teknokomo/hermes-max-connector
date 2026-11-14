# Changelog

## 0.1.0

- First public release of the Hermes MAX platform connector.
- Includes production webhook ingress, opt-in development long polling, message and media handling, group policy reauthorization, profile-aware inbound media storage, and group-aware standalone delivery.
- Marks webhook updates as processed only after handler success; failures and in-progress duplicate deliveries return a retryable response to MAX.
- Marks passive group observations as seen only after transcript storage succeeds, preserving retries after a failed write.
- Enforces the inclusive webhook body limit consistently across supported aiohttp versions, including chunked requests.
- Declares the actual transport, TLS, environment, and Hermes compatibility requirements in the plugin manifest.
- Adds a source distribution and a wheel package artifact, bilingual user documentation, security guidance, and offline release checks; installation copies the runtime files into the Hermes profile or uses the Hermes plugin installer.
- Documents that the MAX chat action endpoint, and therefore the typing indicator, applies to group chats: personal dialogs accept the call but do not display an indicator in MAX clients.
