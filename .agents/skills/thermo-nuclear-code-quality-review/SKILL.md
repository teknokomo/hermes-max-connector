---
name: thermo-nuclear-code-quality-review
description: Review Python maintainability, tests, packaging, and documentation for Hermes MAX Connector.
metadata:
  version: "1.0.0"
  scope: "hermes-max-connector"
---

# Hermes MAX Connector maintainability review

Review module boundaries, Python 3.11 compatibility, asynchronous lifecycle, error handling, stable plugin interfaces, tests, wheel/source distribution contents, and the English/Russian documentation pair.

Check that `plugin.yaml` matches the actual transport and environment behavior; `__init__.py` exports `register`; package installation places the complete runtime plugin in the expected directory; optional document-store integration fails soft; and `.local`, `.ontoindex`, caches, and credentials stay out of public artifacts.

Prefer small changes to the existing connector over broad refactors. Confirm that review claims have direct source or test evidence.
