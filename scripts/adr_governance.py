"""Fail-closed ADR governance entrypoint for the ste-spec repository.

The v1.3 ``adrs/adr-projection/`` layout is included in the generated-document
freshness check.
"""
from __future__ import annotations

import os
import subprocess
import sys
import sysconfig
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def adr_cli() -> str:
    """Locate the installed public ADR-Kit CLI for the active Python environment."""
    executable_name = "adr.exe" if os.name == "nt" else "adr"
    executable = Path(sysconfig.get_path("scripts")) / executable_name
    return str(executable) if executable.is_file() else executable_name


def run_step(label: str, command: list[str]) -> int:
    print(f"\n== {label} ==", flush=True)
    print(" ".join(command), flush=True)
    return subprocess.run(command, cwd=REPO_ROOT).returncode


def main() -> int:
    adr = adr_cli()
    steps = [
        (
            "ADR project metadata validation",
            [adr, "validate-project-metadata", "--scope", "."],
        ),
        (
            "ADR complete-scope and cross-reference validation",
            [adr, "validate", "--scope", ".", "--cross-references", "--mode", "complete"],
        ),
        (
            "ADR generated-document freshness validation",
            [adr, "validate-generated-docs", "--scope", "."],
        ),
        (
            "repository contract, Markdown-link, and pytest checks",
            [sys.executable, "scripts/run_local_contract_checks.py"],
        ),
    ]

    failures = 0
    for label, command in steps:
        failures |= run_step(label, command)
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
