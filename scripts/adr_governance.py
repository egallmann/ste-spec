"""Fail-closed ADR governance entrypoint for the ste-spec repository.

Validation uses the published ``adr_kit.api`` seam. The v1.3
``adrs/adr-projection/`` layout remains in the generated-document freshness check.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from adr_kit.api import (
    Diagnostic,
    GeneratedDocsValidationRequest,
    OperationError,
    ProjectMetadataValidationRequest,
    ValidationRequest,
    validate_architecture,
    validate_generated_docs,
    validate_project_metadata,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_local_checks() -> int:
    """Run ste-spec checks that are not ADR-Kit operations."""
    print("\n== repository contract, Markdown-link, and pytest checks ==", flush=True)
    print(f"{sys.executable} scripts/run_local_contract_checks.py", flush=True)
    return subprocess.run(
        [sys.executable, "scripts/run_local_contract_checks.py"],
        cwd=REPO_ROOT,
    ).returncode


def print_diagnostics(diagnostics: tuple[Diagnostic, ...]) -> None:
    """Print public-seam diagnostics without treating warnings as failure."""
    for diagnostic in diagnostics:
        location = diagnostic.path or diagnostic.source_ref or ""
        prefix = f"{location}: " if location else ""
        print(
            f"{diagnostic.severity.upper()}: {prefix}{diagnostic.code}: {diagnostic.message}",
            flush=True,
        )


def validate_metadata() -> int:
    """Validate PROJECT.yaml through the public metadata operation."""
    print("\n== ADR project metadata validation ==", flush=True)
    print("adr_kit.api.validate_project_metadata", flush=True)
    try:
        result = validate_project_metadata(ProjectMetadataValidationRequest(REPO_ROOT))
    except OperationError as exc:
        print(f"ERROR: {exc}", flush=True)
        return 1
    print_diagnostics(result.diagnostics)
    if result.success:
        print("PROJECT.yaml valid", flush=True)
        return 0
    return 1


def validate_sources() -> int:
    """Validate the ADR corpus in complete mode, including cross-references."""
    print("\n== ADR complete-scope and cross-reference validation ==", flush=True)
    print("adr_kit.api.validate_architecture mode=complete cross_references=true", flush=True)
    try:
        result = validate_architecture(
            ValidationRequest(REPO_ROOT, mode="complete", cross_references=True)
        )
    except OperationError as exc:
        print(f"ERROR: {exc}", flush=True)
        return 1
    print_diagnostics(result.diagnostics)
    if not result.success:
        return 1
    print(f"All {len(result.validated_files)} files valid", flush=True)
    print("Cross-references valid", flush=True)
    return 0


def validate_generated() -> int:
    """Validate generated-document freshness through the public operation."""
    print("\n== ADR generated-document freshness validation ==", flush=True)
    print("adr_kit.api.validate_generated_docs", flush=True)
    try:
        result = validate_generated_docs(GeneratedDocsValidationRequest(REPO_ROOT))
    except OperationError as exc:
        print(f"ERROR: {exc}", flush=True)
        return 1
    for artifact in result.artifacts:
        print(
            f"  {artifact.status}: {artifact.artifact_path} ({artifact.reason_code})",
            flush=True,
        )
    print_diagnostics(result.diagnostics)
    return 0 if result.success else 1


def main() -> int:
    failures = validate_metadata()
    failures |= validate_sources()
    failures |= validate_generated()
    failures |= run_local_checks()
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
