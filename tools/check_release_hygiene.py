#!/usr/bin/env python3
"""Scan the indexed public tree or current project filesystem for release hazards."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "GitHub fine-grained token": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "GitLab token": re.compile(r"\bglpat-[A-Za-z0-9_-]{16,}\b"),
    "Multica token": re.compile(r"\bmul_[A-Za-z0-9]{16,}\b"),
    "VK token": re.compile(r"\bvk1\.a\.[A-Za-z0-9._-]{40,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "JWT": re.compile(r"\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}"),
    "private host path": re.compile(
        r"/home/" + r"[A-Za-z0-9_.-]+/|/" + r"root/|/opt/" + r"hermes-agent"
    ),
    "private network endpoint": re.compile(
        r"\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.(?:\d{1,3}\.){1,2}\d{1,3}|"
        r"172\.(?:1[6-9]|2\d|3[01])\.(?:\d{1,3}\.){1,2}\d{1,3})\b"
    ),
    "webhook URL with configured route": re.compile(r"https://[^\s\"'<>]+/max/webhook\b", re.I),
}
FORBIDDEN_PATHS = (
    ".local/",
    ".ontoindex/",
    ".venv/",
    "__pycache__/",
    ".pytest_cache/",
    ".ruff_cache/",
    "history/",
    "provenance/",
    "compat/",
    "unmerged/",
    "build/",
    "dist/",
)


def tracked_paths() -> list[Path]:
    raw = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    ).stdout
    return [ROOT / item.decode() for item in raw.split(b"\0") if item]


def filesystem_paths() -> list[Path]:
    ignored_dirs = {".local", ".ontoindex", ".git", ".venv", "__pycache__", ".pytest_cache", ".ruff_cache", "build", "dist"}
    return [
        path for path in ROOT.rglob("*")
        if path.is_file() and not any(
            part in ignored_dirs or part.endswith(".egg-info")
            for part in path.relative_to(ROOT).parts
        )
    ]


def scan(paths: list[Path], *, from_index: bool = False) -> list[str]:
    issues = []
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        if (relative.startswith(FORBIDDEN_PATHS) or path.suffix == ".bundle"
                or any(part.endswith(".egg-info") for part in path.relative_to(ROOT).parts)):
            issues.append(f"forbidden public path: {relative}")
            continue
        if path.name == ".env" or path.name.startswith(".env."):
            issues.append(f"environment file in public tree: {relative}")
            continue
        try:
            if from_index:
                content = subprocess.run(
                    ["git", "show", ":" + relative], cwd=ROOT, check=True,
                    capture_output=True, text=True, encoding="utf-8", errors="replace",
                ).stdout
            else:
                content = path.read_text(encoding="utf-8", errors="replace")
        except (OSError, subprocess.CalledProcessError):
            issues.append(f"cannot read public file: {relative}")
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                issues.append(f"{label}: {relative}")
        if relative in {"plugin.yaml", "config/example.yaml"}:
            for values in re.findall(
                r"(?:allowed_users|allow_admin_from|allowed_chats)\s*:\s*\[([^\]]*)\]",
                content,
            ):
                entries = [value.strip().strip("\"'") for value in values.split(",")]
                if any(value and not re.fullmatch(r"<[a-z0-9-]+>", value) for value in entries):
                    issues.append(f"non-placeholder account in public example: {relative}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--filesystem", action="store_true")
    args = parser.parse_args()
    paths = filesystem_paths() if args.filesystem else tracked_paths()
    if not paths:
        parser.error("no public files found to scan")
    problems = scan(paths, from_index=not args.filesystem)
    if problems:
        print("\n".join(f"FAIL: {problem}" for problem in problems), file=sys.stderr)
        return 1
    print(f"Release hygiene PASS: scanned {len(paths)} {'filesystem' if args.filesystem else 'tracked'} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
