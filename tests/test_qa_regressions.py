"""Regressions for publication gates and realistic connector ingress."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import aiohttp
import pytest

import adapter

ROOT = Path(__file__).resolve().parents[1]


def load_tool(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("english,russian", [
    ("\n```bash\necho alpha\n```\n", "\n```bash\necho beta\n```\n"),
    ("\n```bash\necho same\n```\n", "\n```python\necho same\n```\n"),
    ("\nMAX_POLL_TIMEOUT=30\nMAX_WEBHOOK_BODY=90\n",
     "\nMAX_POLL_TIMEOUT=90\nMAX_WEBHOOK_BODY=30\n"),
    ("\nMAX_BOT_TOKEN MAX_BOT_TOKEN\n", "\nMAX_BOT_TOKEN\n"),
])
def test_parity_rejects_changed_examples_and_technical_meaning(monkeypatch, english, russian):
    module = load_tool("check_readme_parity")
    monkeypatch.setattr(module, "EN", module.EN + english)
    monkeypatch.setattr(module, "RU", module.RU + russian)
    assert module.main() == 1


def test_parity_rejects_unclosed_backtick_fence():
    module = load_tool("check_readme_parity")
    with pytest.raises(ValueError, match="unclosed"):
        module.code_blocks("```bash\necho incomplete\n")


@pytest.fixture
def publication_repo(monkeypatch, tmp_path):
    module = load_tool("check_release_hygiene")
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    monkeypatch.setattr(module, "ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_release_hygiene.py"])
    return module, tmp_path


@pytest.mark.parametrize("unsafe_index", [True, False])
def test_publication_scan_reads_index_bytes_not_worktree(publication_repo, unsafe_index):
    module, root = publication_repo
    path = root / "sample.txt"
    synthetic = "ghp_" + "A" * 36
    path.write_text(synthetic if unsafe_index else "safe staged content", encoding="utf-8")
    subprocess.run(["git", "add", "sample.txt"], cwd=root, check=True)
    path.write_text("safe working copy" if unsafe_index else synthetic, encoding="utf-8")
    assert module.main() == int(unsafe_index)


def test_empty_publication_index_is_not_a_pass(publication_repo):
    module, _root = publication_repo
    with pytest.raises(SystemExit) as exc:
        module.main()
    assert exc.value.code == 2


def test_publication_scan_fails_closed_for_unreadable_file(monkeypatch, tmp_path):
    module = load_tool("check_release_hygiene")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    assert module.scan([tmp_path / "missing.txt"])


def test_public_example_rejects_non_placeholder_account(monkeypatch, tmp_path):
    module = load_tool("check_release_hygiene")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    path = tmp_path / "plugin.yaml"
    path.write_text('# allowed_users: ["example-person"]\n', encoding="utf-8")
    assert module.scan([path])


def test_filesystem_scan_does_not_skip_an_ignored_name_in_root_ancestors(monkeypatch, tmp_path):
    module = load_tool("check_release_hygiene")
    root = tmp_path / ".local" / "source-distribution"
    root.mkdir(parents=True)
    public = root / "sample.txt"
    public.write_text("synthetic source", encoding="utf-8")
    ignored = root / ".local" / "private.txt"
    ignored.parent.mkdir()
    ignored.write_text("local fixture", encoding="utf-8")
    monkeypatch.setattr(module, "ROOT", root)
    assert module.filesystem_paths() == [public]


@pytest.mark.parametrize("relative", ["legacy.bundle", "dist/release.whl", "sample.egg-info/PKG-INFO"])
def test_release_scan_rejects_legacy_bundle_and_build_outputs(monkeypatch, tmp_path, relative):
    module = load_tool("check_release_hygiene")
    monkeypatch.setattr(module, "ROOT", tmp_path)
    path = tmp_path / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("synthetic artifact", encoding="utf-8")
    assert module.scan([path])


@pytest.mark.asyncio
@pytest.mark.parametrize("chunked", [False, True])
@pytest.mark.parametrize("extra_byte", [0, 1])
async def test_real_webhook_listener_enforces_body_limit(monkeypatch, chunked, extra_byte):
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "synthetic-secret")
    instance = adapter.MaxAdapter(SimpleNamespace(extra={"webhook": True}))
    instance.settings = replace(instance.settings, webhook_port=0)
    await instance._start_webhook_listener()
    try:
        port = instance._webhook_runner.addresses[0][1]
        prefix, suffix = b'{"padding":"', b'"}'
        payload = prefix + b"x" * (adapter.MAX_WEBHOOK_BODY + extra_byte
                                   - len(prefix) - len(suffix)) + suffix

        async def stream():
            for offset in range(0, len(payload), 32768):
                yield payload[offset:offset + 32768]

        async with aiohttp.ClientSession() as client:
            async with client.post(
                f"http://127.0.0.1:{port}{instance.settings.webhook_path}",
                data=stream() if chunked else payload,
                headers={"Content-Type": "application/json",
                         "X-Max-Bot-Api-Secret": "synthetic-secret"},
            ) as response:
                assert response.status == (413 if extra_byte else 200)
    finally:
        await instance._stop_webhook_listener()


@pytest.mark.asyncio
async def test_passive_group_store_failure_can_be_retried(monkeypatch, tmp_path):
    monkeypatch.setenv("MAX_WEBHOOK_SECRET", "synthetic-secret")
    monkeypatch.setattr(adapter, "_profile_home_for_source", lambda *_: tmp_path)
    instance = adapter.MaxAdapter(SimpleNamespace(extra={
        "groups_enabled": True, "allowed_chats": ["-123456"],
        "require_mention": True, "observe_unmentioned_group_messages": True,
    }))
    attempts, saved = [], []

    def append(_session, entry):
        attempts.append(entry)
        if len(attempts) == 1:
            raise RuntimeError("synthetic transaction failure")
        saved.append(entry)

    instance._session_store = SimpleNamespace(
        get_or_create_session=lambda _source: SimpleNamespace(session_id="synthetic-session"),
        append_to_transcript=append,
    )
    update = {"update_type": "message_created", "chat_id": -123456,
              "user": {"user_id": 42, "name": "Test User"},
              "message": {"recipient": {"chat_type": "chat", "chat_id": -123456},
                          "body": {"mid": "passive-retry", "text": "passive context"}}}

    class Request:
        headers = {"X-Max-Bot-Api-Secret": "synthetic-secret"}
        content_length = 1024
        content_type = "application/json"

        async def json(self):
            return update

        async def read(self):
            return b"{}"

    assert (await instance._handle_webhook(Request())).status == 503
    assert "passive-retry" not in instance._observed_message_ids
    assert (await instance._handle_webhook(Request())).status == 200
    assert (await instance._handle_webhook(Request())).status == 200
    assert len(saved) == 1


@pytest.mark.asyncio
async def test_outgoing_media_inside_root_reaches_mock_upload(tmp_path):
    path = tmp_path / "synthetic.txt"
    path.write_text("synthetic file", encoding="utf-8")
    uploaded, sent = [], []

    class Client:
        async def init_upload(self, _kind):
            return {"url": "https://fu.oneme.ru/synthetic"}

        async def upload_binary(self, _url, upload_path, **_kwargs):
            uploaded.append(upload_path)
            return {"token": "synthetic-upload-token"}

        async def send_attachment(self, *args, **_kwargs):
            sent.append(args)
            return {"message": {"body": {"mid": "synthetic-result"}}}

    instance = adapter.MaxAdapter(SimpleNamespace(extra={"media_roots": [str(tmp_path)]}))
    instance._client = Client()
    result = await instance.send_document("42", str(path))
    assert result.success
    assert uploaded == [path.resolve()]
    assert len(sent) == 1


@pytest.mark.skipif(not os.environ.get("HERMES_SOURCE_DIR"), reason="requires official Hermes cache API")
def test_optional_document_store_absence_preserves_profile_cache(monkeypatch, tmp_path):
    from hermes_constants import get_hermes_home

    def unavailable():
        raise ModuleNotFoundError("synthetic optional plugin absence")

    monkeypatch.setattr(adapter, "_document_store_module", unavailable)
    prior = get_hermes_home()
    routed = tmp_path / "routed-profile"
    with adapter._profile_storage_scope(routed):
        cached = Path(adapter.cache_document_from_bytes(b"synthetic attachment", "synthetic.txt"))
        assert cached.is_relative_to(routed)
        assert cached.read_bytes() == b"synthetic attachment"
    assert get_hermes_home() == prior
