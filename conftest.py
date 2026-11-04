"""Provide a minimal Hermes boundary for the Python-version unit-test matrix.

The official PluginManager integration runs separately against pinned Hermes
source trees. The Python matrix exercises connector logic without requiring
Hermes' runtime dependency lock (which currently targets Python 3.14+).
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from enum import Enum
from types import ModuleType, SimpleNamespace


def _module(name: str, *, package: bool = False) -> ModuleType:
    module = ModuleType(name)
    if package:
        module.__path__ = []
    sys.modules[name] = module
    return module


def _install_hermes_boundary() -> None:
    gateway = _module("gateway", package=True)
    config = _module("gateway.config")
    platforms = _module("gateway.platforms", package=True)
    base = _module("gateway.platforms.base")
    registry = _module("gateway.platform_registry")

    class Platform(str):
        pass

    class MessageType(str, Enum):
        TEXT = "text"
        COMMAND = "command"
        DOCUMENT = "document"
        PHOTO = "photo"
        VOICE = "voice"
        AUDIO = "audio"
        VIDEO = "video"

    class BasePlatformAdapter:
        def __init__(self, *, config, platform):
            self.config = config
            self.platform = platform
            self.gateway_runner = None

        def build_source(self, **values):
            values.setdefault("platform", self.platform)
            return SimpleNamespace(**values)

    @dataclass
    class SendResult:
        success: bool
        message_id: str | None = None
        error: str | None = None

    class PlatformRegistry:
        def __init__(self):
            self.entries = []

        def register(self, entry):
            self.entries.append(entry)

    class PlatformEntry:
        def __init__(self, source: str = "plugin", **values):
            self.source = source
            self.__dict__.update(values)

    config.Platform = Platform
    base.BasePlatformAdapter = BasePlatformAdapter
    base.MessageEvent = SimpleNamespace
    base.MessageType = MessageType
    base.SendResult = SendResult
    base.cache_document_from_bytes = lambda *_args, **_kwargs: "cached-document"
    base.cache_image_from_bytes = lambda *_args, **_kwargs: "cached-image"
    registry.PlatformEntry = PlatformEntry
    registry.platform_registry = PlatformRegistry()
    gateway.config = config
    gateway.platforms = platforms
    gateway.platform_registry = registry
    platforms.base = base


if not os.environ.get("HERMES_SOURCE_DIR"):
    _install_hermes_boundary()
