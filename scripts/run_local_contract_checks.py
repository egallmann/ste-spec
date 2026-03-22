from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_step(label: str, command: list[str]) -> int:
    print(f"== {label} ==")
    completed = subprocess.run(command, cwd=REPO_ROOT)
    return completed.returncode


def main() -> int:
    failures = 0

    failures |= run_step("internal markdown links", [sys.executable, "scripts/check_internal_md_links.py"])
    failures |= run_step("publication tests", [sys.executable, "-m", "pytest", "tests", "-q"])

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
