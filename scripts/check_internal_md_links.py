"""One-off / repeatable internal link check for ste-spec Markdown (repository-local)."""
from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
REF_DEF_RE = re.compile(r"^\s*\[([^\]]+)\]:\s*(\S+)", re.MULTILINE)


def should_skip_dir(dirpath: str) -> bool:
    parts = dirpath.replace("\\", "/").split("/")
    return ".git" in parts or ".pytest_cache" in parts


def main() -> int:
    broken: list[tuple[str, str, str]] = []
    checked = 0

    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not should_skip_dir(os.path.join(dirpath, d))]
        if should_skip_dir(dirpath):
            continue
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            try:
                text = open(path, encoding="utf-8").read()
            except OSError as e:
                broken.append((rel, f"<read error {e}>", "read"))
                continue

            for m in REF_DEF_RE.finditer(text):
                target = m.group(2).strip()
                if target.startswith("http") or target.startswith("mailto:"):
                    continue
                path_part = target.split("#", 1)[0].strip()
                if not path_part:
                    continue
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), path_part))
                checked += 1
                if not os.path.isfile(resolved):
                    broken.append((rel, target, "ref-def"))

            for m in LINK_RE.finditer(text):
                target = m.group(2).strip().strip('"').strip("'")
                if not target or target.startswith("#"):
                    continue
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                path_part = target.split("#", 1)[0].strip()
                if not path_part:
                    continue
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), path_part))
                checked += 1
                if not os.path.isfile(resolved):
                    broken.append((rel, target, "inline"))

    for rel, tgt, kind in sorted(broken):
        print(f"{kind}\t{rel}\t{tgt}")

    print(f"Total broken: {len(broken)}; internal path targets checked: {checked}", file=sys.stderr)
    return 0 if not broken else 1


if __name__ == "__main__":
    raise SystemExit(main())
