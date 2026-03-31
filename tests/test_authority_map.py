from __future__ import annotations

from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
AUTHORITY_MAP_PATH = REPO_ROOT / "architecture" / "authority-map.md"


def test_authority_map_exists_and_names_core_authority_locations() -> None:
    content = AUTHORITY_MAP_PATH.read_text(encoding="utf-8")

    assert "## Public Contracts" in content
    assert "ste-spec/contracts/architecture-ir/architecture-ir.schema.json" in content
    assert "ste-spec/contracts/architecture-evidence.schema.json" in content
    assert "ste-spec/contracts/kernel-admission-assessment.schema.json" in content
    assert "## Kernel-private Contracts" in content
    assert "boot-result.schema.json" in content
    assert "admission-context.schema.json" in content
    assert "ADR | `adr-architecture-kit`" in content
    assert "IR bundle | `ste-spec`" in content
    assert "Evidence | `ste-runtime`" in content
    assert "Admission | `ste-kernel`" in content


def test_public_contract_mirror_paths_are_absent_when_workspace_siblings_exist() -> None:
    sibling_roots = {
        "adr_kit": REPO_ROOT.parent / "adr-architecture-kit",
        "rules": REPO_ROOT.parent / "ste-rules-library",
    }
    if not all(path.exists() for path in sibling_roots.values()):
        pytest.skip("Sibling workspace repositories are not available in this environment.")

    forbidden_paths = [
        sibling_roots["adr_kit"] / "tests" / "fixtures" / "kernel" / "architecture-ir.schema.json",
        sibling_roots["rules"] / "tests" / "fixtures" / "kernel" / "architecture-ir.schema.json",
    ]

    for forbidden_path in forbidden_paths:
        assert not forbidden_path.exists(), f"Forbidden public schema mirror still exists: {forbidden_path}"


def test_public_ir_docs_use_canonical_spec_schema_id() -> None:
    content = (REPO_ROOT / "contracts" / "architecture-ir" / "ARCHITECTURE_IR.md").read_text(encoding="utf-8")

    assert "https://github.com/egallmann/ste-spec/contracts/architecture-ir/architecture-ir.schema.json" in content
    assert "https://ste-kernel.local/schema/architecture-ir/0.1.0/architecture-ir.schema.json" not in content


def test_contract_examples_are_present_for_public_handoffs() -> None:
    examples_root = REPO_ROOT / "contracts" / "examples"

    evidence_example = examples_root / "architecture-evidence.valid.json"
    admission_example = examples_root / "kernel-admission-assessment.valid.json"
    compiled_ir_example = examples_root / "compiled-ir-document.reference.json"

    assert evidence_example.exists()
    assert admission_example.exists()
    assert compiled_ir_example.exists()

    evidence_content = evidence_example.read_text(encoding="utf-8")
    compiled_ir_content = compiled_ir_example.read_text(encoding="utf-8")

    assert '"version": "2"' in evidence_content
    assert '"subjects"' in evidence_content
    assert '"schema_id": "https://github.com/egallmann/ste-spec/contracts/architecture-ir/architecture-ir.schema.json"' in compiled_ir_content
