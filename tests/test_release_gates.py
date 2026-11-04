from __future__ import annotations

import asyncio
import os
import subprocess
import sys
import textwrap
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

import adapter


def config(**extra):
    return SimpleNamespace(extra=extra)


class _Response:
    def __init__(self, status: int = 200, payload: dict | None = None):
        self.status = status
        self.headers = {}
        self._payload = payload or {}

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_args):
        return None

    async def json(self):
        return self._payload

    async def text(self):
        return ""


class _Session:
    def __init__(self):
        self.calls = []

    def post(self, url, **kwargs):
        self.calls.append((url, kwargs))
        return _Response(payload={"message": {"body": {"mid": "m-test"}}})

    async def close(self):
        return None


class _Request:
    def __init__(self, *, headers=None, content_length=2, content_type="application/json", payload=None):
        self.headers = headers or {}
        self.content_length = content_length
        self.content_type = content_type
        self.payload = payload or {}

    async def json(self):
        return self.payload

    async def read(self):
        return b"{}"


def test_inbound_media_home_uses_routed_profile(monkeypatch, tmp_path):
    profiles = SimpleNamespace(get_profile_dir=lambda profile: tmp_path / profile)
    monkeypatch.setitem(sys.modules, "hermes_cli.profiles", profiles)

    home = adapter._profile_home_for_source(SimpleNamespace(), SimpleNamespace(profile="test-profile"))

    assert home == (tmp_path / "test-profile").resolve()


def test_rejected_profile_route_has_no_media_home():
    source = SimpleNamespace(profile="test-profile", profile_route_rejected=True)

    assert adapter._profile_home_for_source(SimpleNamespace(), source) is None


@pytest.mark.asyncio
async def test_webhook_secret_header_missing_and_invalid_are_rejected(monkeypatch):
    monkeypatch.setenv("MAX_BOT_TOKEN", "fake-token")
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "expected-secret")
    instance = adapter.MaxAdapter(config(webhook=True))
    missing = await instance._handle_webhook(_Request())
    invalid = await instance._handle_webhook(
        _Request(headers={"X-Max-Bot-Api-Secret": "wrong-secret"})
    )
    assert missing.status == 401
    assert invalid.status == 401


@pytest.mark.asyncio
async def test_webhook_accepts_body_at_limit_and_rejects_over_limit(monkeypatch):
    monkeypatch.setenv("MAX_BOT_TOKEN", "fake-token")
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "expected-secret")
    instance = adapter.MaxAdapter(config(webhook=True))
    headers = {"X-Max-Bot-Api-Secret": "expected-secret"}
    exact = await instance._handle_webhook(
        _Request(headers=headers, content_length=adapter.MAX_WEBHOOK_BODY, payload={})
    )
    over = await instance._handle_webhook(
        _Request(headers=headers, content_length=adapter.MAX_WEBHOOK_BODY + 1, payload={})
    )
    assert exact.status == 200
    assert over.status == 413


@pytest.mark.asyncio
async def test_webhook_handler_failure_returns_retryable_status_and_releases_dedup(
    monkeypatch, tmp_path
):
    monkeypatch.setenv("MAX_BOT_TOKEN", "fake-token")
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "expected-secret")
    instance = adapter.MaxAdapter(config(webhook=True))
    instance._persistent_state = adapter.MaxPersistentState(tmp_path / "reliability.db")
    attempts = 0

    async def handler(_update):
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise RuntimeError("synthetic transient dispatch failure")

    monkeypatch.setattr(instance, "_dispatch_update", handler)
    request = _Request(
        headers={"X-Max-Bot-Api-Secret": "expected-secret"},
        payload={
            "update_type": "message_created",
            "message": {"body": {"mid": "m-retry"}},
        },
    )

    failed = await instance._handle_webhook(request)
    assert failed.status == 503
    assert instance._persistent_state.is_update_claimed("message_created:m-retry") is False

    retried = await instance._handle_webhook(request)
    assert retried.status == 200
    assert instance._persistent_state.is_update_claimed("message_created:m-retry") is True

    duplicate = await instance._handle_webhook(request)
    assert duplicate.status == 200
    assert attempts == 2


@pytest.mark.asyncio
async def test_webhook_duplicate_during_processing_gets_retryable_status(monkeypatch):
    monkeypatch.setenv("MAX_BOT_TOKEN", "fake-token")
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "expected-secret")
    instance = adapter.MaxAdapter(config(webhook=True))
    entered = asyncio.Event()
    release = asyncio.Event()
    attempts = 0

    async def handler(_update):
        nonlocal attempts
        attempts += 1
        entered.set()
        await release.wait()

    monkeypatch.setattr(instance, "_dispatch_update", handler)
    request = _Request(
        headers={"X-Max-Bot-Api-Secret": "expected-secret"},
        payload={
            "update_type": "message_created",
            "message": {"body": {"mid": "m-inflight"}},
        },
    )

    first = asyncio.create_task(instance._handle_webhook(request))
    await entered.wait()
    duplicate_inflight = await instance._handle_webhook(request)
    assert duplicate_inflight.status == 503

    release.set()
    assert (await first).status == 200
    assert (await instance._handle_webhook(request)).status == 200
    assert attempts == 1


@pytest.mark.asyncio
async def test_webhook_handler_timeout_releases_update_for_max_retry(monkeypatch):
    monkeypatch.setenv("MAX_BOT_TOKEN", "fake-token")
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "expected-secret")
    monkeypatch.setattr(adapter, "MAX_WEBHOOK_HANDLER_TIMEOUT_SECONDS", 0.01)
    instance = adapter.MaxAdapter(config(webhook=True))
    entered = asyncio.Event()
    release = asyncio.Event()

    async def slow_handler(_update):
        entered.set()
        await release.wait()

    monkeypatch.setattr(instance, "_dispatch_update", slow_handler)
    request = _Request(
        headers={"X-Max-Bot-Api-Secret": "expected-secret"},
        payload={
            "update_type": "message_created",
            "message": {"body": {"mid": "m-timeout"}},
        },
    )

    timed_out = await instance._handle_webhook(request)
    assert entered.is_set()
    assert timed_out.status == 503
    assert instance._webhook_inflight == set()

    async def retry_handler(_update):
        return None

    monkeypatch.setattr(instance, "_dispatch_update", retry_handler)
    retried = await instance._handle_webhook(request)
    assert retried.status == 200


def test_persistent_dedup_survives_state_object_restart(tmp_path):
    path = tmp_path / "profile" / "max" / "reliability.db"
    first = adapter.MaxPersistentState(path, now_ms=lambda: 1_000_000)
    assert first.claim_update("message_created:opaque-test-id") is True
    restarted = adapter.MaxPersistentState(path, now_ms=lambda: 1_000_001)
    assert restarted.claim_update("message_created:opaque-test-id") is False
    assert path.stat().st_mode & 0o777 == 0o600
    assert path.parent.stat().st_mode & 0o777 == 0o700


@pytest.mark.asyncio
async def test_standalone_group_send_preserves_group_destination(monkeypatch):
    monkeypatch.setenv("MAX_BOT_TOKEN", "fake-token")
    monkeypatch.setenv("MAX_CA_BUNDLE", "/unused/test-ca.pem")
    captured = {}

    class Client:
        def __init__(self, *_args, **_kwargs):
            self.session = _Session()

        async def send_text(self, chat_id, text, *, chat_type="dm", **_kwargs):
            captured.update(chat_id=chat_id, text=text, chat_type=chat_type)
            return {"message": {"body": {"mid": "m-test"}}}

        async def close(self):
            return None

    monkeypatch.setattr(adapter, "MaxApiClient", Client)
    result = await adapter._standalone_send(
        config(allowed_chats=["-123456"]),
        "-123456",
        "scheduled test",
    )
    assert result["success"] is True
    assert captured == {
        "chat_id": "-123456",
        "text": "scheduled test",
        "chat_type": "group",
    }


@pytest.mark.asyncio
async def test_group_api_send_uses_chat_id_parameter():
    session = _Session()
    client = adapter.MaxApiClient("fake-token", session=session)
    await client.send_text("-123456", "group message", chat_type="group")
    assert session.calls[0][1]["params"] == {"chat_id": "-123456"}


@pytest.mark.asyncio
async def test_outgoing_media_outside_media_roots_is_rejected(tmp_path):
    allowed = tmp_path / "allowed"
    outside = tmp_path / "outside.txt"
    allowed.mkdir()
    outside.write_text("synthetic file", encoding="utf-8")
    instance = adapter.MaxAdapter(config(media_roots=[str(allowed)]))
    instance._client = object()
    result = await instance.send_document("123", str(outside))
    assert result.success is False
    assert "outside allowed media roots" in result.error


def test_manifest_declares_public_identity_and_required_interfaces():
    manifest = yaml.safe_load(Path("plugin.yaml").read_text(encoding="utf-8"))
    assert manifest["name"] == "hermes-max-connector"
    assert manifest["version"] == "0.1.0"
    assert manifest["kind"] == "platform"
    assert manifest["requires_hermes"] == ">=0.22.4"
    required = [entry["name"] for entry in manifest["requires_env"]]
    optional = [entry["name"] for entry in manifest["optional_env"]]
    assert required == ["MAX_BOT_TOKEN"]
    assert set(optional) == {
        "MAX_ALLOWED_USERS",
        "MAX_ALLOW_ALL_USERS",
        "MAX_POLLING_DEV",
        "MAX_POLL_TIMEOUT",
        "MAX_CA_BUNDLE",
        "MAX_HOME_CHANNEL",
        "MAX_WEBHOOK_SECRET",
    }


def test_example_config_is_parseable_and_uses_placeholders_only():
    example = yaml.safe_load(Path("config/example.yaml").read_text(encoding="utf-8"))
    max_config = example["platforms"]["max"]
    assert max_config["groups"]["allowed_chats"] == ["<max-chat-id>"]
    assert max_config["allowed_users"] == ["<max-user-id>"]
    assert max_config["ca_bundle"] == "<path-to-ca-bundle>"
    assert max_config["webhook_host"] == "127.0.0.1"


def test_readme_parity_checker():
    result = subprocess.run(
        [sys.executable, "tools/check_readme_parity.py"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_release_hygiene_checker():
    result = subprocess.run(
        [sys.executable, "tools/check_release_hygiene.py", "--filesystem"],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_plugin_manager_cold_loads_public_package(tmp_path):
    hermes_source = os.environ.get("HERMES_SOURCE_DIR")
    if not hermes_source:
        pytest.skip("set HERMES_SOURCE_DIR to an official Hermes checkout for PluginManager cold-load")
    repo_root = Path(__file__).resolve().parents[1]
    child = textwrap.dedent(
        """
        import json
        import os
        import sys
        from pathlib import Path

        hermes_source = Path(os.environ["HERMES_SOURCE_DIR"])
        sys.path.insert(0, str(hermes_source))
        from hermes_cli.plugins import PluginManager
        from hermes_cli.plugins_manifest import parse_manifest_file

        plugin_dir = Path(sys.argv[1]).resolve()
        manifest = parse_manifest_file(
            plugin_dir / "plugin.yaml", plugin_dir, "user", ""
        )
        assert manifest is not None, "manifest parsing failed"
        assert manifest.name == "hermes-max-connector"
        manager = PluginManager(scope_key=os.environ["HERMES_HOME"])
        manager._load_plugin(manifest)
        loaded = manager._plugins.get("hermes-max-connector")
        details = {
            "enabled": bool(loaded and loaded.enabled),
            "error": loaded.error if loaded else "missing manager record",
            "registered_max": "max" in manager._plugin_platform_names,
        }
        print(json.dumps(details, sort_keys=True))
        assert details["enabled"], details
        assert details["registered_max"], details
        """
    )
    env = os.environ.copy()
    env["HERMES_HOME"] = str(tmp_path / "hermes-home")
    env["PYTHONPATH"] = str(hermes_source) + os.pathsep + env.get("PYTHONPATH", "")
    result = subprocess.run(
        [sys.executable, "-c", child, str(repo_root)],
        check=False,
        capture_output=True,
        text=True,
        env=env,
        timeout=60,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert '"registered_max": true' in result.stdout
