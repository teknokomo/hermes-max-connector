#!/usr/bin/env python3
"""Check structural parity of the English and Russian public README files."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = (ROOT / "README.md").read_text(encoding="utf-8")
RU = (ROOT / "README-RU.md").read_text(encoding="utf-8")
EXPECTED_EN = [
    "# Important! Grave! Important!",
    "# Hermes MAX Connector",
    "## Developers",
    "## Overview",
    "## Features",
    "## Installation",
    "## Configuration",
    "## Transports",
    "## TLS and media",
    "## State and limits",
    "## Verification",
    "## Security and project files",
]
EXPECTED_RU = [
    "# Важно! Grave! Important!",
    "# Hermes MAX Connector",
    "## Разработчики",
    "## Обзор",
    "## Возможности",
    "## Установка",
    "## Настройка",
    "## Транспорт",
    "## TLS и вложения",
    "## Состояние и ограничения",
    "## Проверка",
    "## Безопасность и файлы проекта",
]


def headings(text: str) -> list[str]:
    prose, _blocks = markdown_parts(text)
    return [line for line in prose if line.startswith("#")]


def links(text: str) -> list[str]:
    return re.findall(r"\]\(([^)]+)\)", text)


def markdown_parts(text: str) -> tuple[list[str], list[str]]:
    """Separate prose and fenced examples, retaining their language tags."""
    prose, blocks = [], []
    fence = ""
    current = []
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if (match and match[1][0] == fence[0]
                    and len(match[1]) >= len(fence) and not match[2].strip()):
                blocks.append("\n".join(current))
                current = []
                fence = ""
            else:
                current.append(line)
        elif match:
            fence = match[1]
            current = [match[2].strip()]
        else:
            prose.append(line)
    if fence:
        raise ValueError("unclosed fenced code block")
    return prose, blocks


def code_blocks(text: str) -> list[str]:
    return markdown_parts(text)[1]


def main() -> int:
    failures = []
    try:
        en_blocks, ru_blocks = code_blocks(EN), code_blocks(RU)
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    if headings(EN) != EXPECTED_EN:
        failures.append("English heading structure differs from the release contract")
    if headings(RU) != EXPECTED_RU:
        failures.append("Russian heading structure differs from the release contract")
    if len(EN.splitlines()) != len(RU.splitlines()):
        failures.append(f"README line counts differ: EN={len(EN.splitlines())} RU={len(RU.splitlines())}")
    if en_blocks != ru_blocks:
        failures.append("fenced code blocks differ")
    en_links, ru_links = links(EN), links(RU)
    # Language switchers and localized README banners intentionally differ.
    localized_links = {
        ("LICENSE.md", "LICENSE-RU.md"),
        ("README-RU.md", "README.md"),
        ("docs/assets/teknokomo-om73-en.jpg", "docs/assets/teknokomo-om73-ru.jpg"),
    }
    if len(en_links) != len(ru_links):
        failures.append("link counts differ")
    else:
        for index, (en_link, ru_link) in enumerate(zip(en_links, ru_links, strict=True)):
            if en_link != ru_link and (en_link, ru_link) not in localized_links:
                failures.append(f"link target differs at position {index + 1}: {en_link} != {ru_link}")
    def normalize_number(value: str) -> str:
        return re.sub(r"[, ]", "", value)

    def numbers(value: str) -> list[str]:
        return re.findall(r"(?<![A-Za-z])\d[\d, ]*(?:\.\d+)?", value)
    token_pattern = (
        r"\b(?:MAX_[A-Z0-9_]+|platforms\.max|media_roots|persistent_state|webhook_host|"
        r"webhook_port|webhook_path|allowed_users|allow_all_users|require_mention|"
        r"groups\.enabled|groups\.allowed_chats|verify=False|aiohttp)\b"
    )
    def technical_tokens(value: str) -> list[str]:
        return sorted(re.findall(token_pattern, value))
    for line_number, (en_line, ru_line) in enumerate(zip(EN.splitlines(), RU.splitlines()), 1):
        if [normalize_number(n) for n in numbers(en_line)] != [
            normalize_number(n) for n in numbers(ru_line)
        ]:
            failures.append(f"numeric values differ on line {line_number}")
        if technical_tokens(en_line) != technical_tokens(ru_line):
            failures.append(f"technical tokens differ on line {line_number}")
        if re.findall(r"`([^`]+)`", en_line) != re.findall(r"`([^`]+)`", ru_line):
            failures.append(f"inline code differs on line {line_number}")
    if failures:
        print("\n".join(f"FAIL: {item}" for item in failures), file=sys.stderr)
        return 1
    print(
        f"README parity PASS: {len(EXPECTED_EN)} headings, "
        f"{len(EN.splitlines())} lines, {len(en_links)} links, "
        f"{len(en_blocks)} identical code blocks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
