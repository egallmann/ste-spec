"""Decision and invariant lifecycle must follow the declaring ADR status.

ADR-Kit 0.12.1 projected every authoring-1.6 child entity as ``active``, so the
children of a proposed ADR read as in force. This check compiles a temporary
authoring-1.6 project through the published compile operation.
"""

from __future__ import annotations

from pathlib import Path

import yaml
from adr_kit.api import CompilationRequest, compile_architecture


PROJECT = {
    "schema_version": "1.0",
    "type": "project_metadata",
    "project": {"name": "lifecycle-fixture", "description": "Fixture", "type": "specification"},
    "architecture_documentation": {
        "adr_directory": "adrs/",
        "manifest_path": "adrs/manifest.yaml",
        "architecture_namespace": "lifecycle-fixture",
    },
}

CASES = {
    "proposed": (
        "ADR-L-0001",
        "019a0000-0000-7000-8000-000000000001",
        "019a0000-0000-7000-8000-000000000011",
        "019a0000-0000-7000-8000-000000000021",
    ),
    "accepted": (
        "ADR-L-0002",
        "019a0000-0000-7000-8000-000000000002",
        "019a0000-0000-7000-8000-000000000012",
        "019a0000-0000-7000-8000-000000000022",
    ),
}
EXPECTED = {"proposed": "proposed", "accepted": "active"}


def _adr(status: str, alias: str, adr_id: str, decision_id: str, invariant_id: str) -> dict:
    number = alias[-4:]
    return {
        "schema_version": "1.6",
        "adr_type": "logical",
        "id": adr_id,
        "title": f"Fixture {status} ADR",
        "status": status,
        "created_date": "2026-01-01",
        "authors": ["ste-spec"],
        "domains": ["governance"],
        "context": "Fixture context.",
        "decisions": [
            {
                "id": decision_id,
                "summary": f"Fixture {status} decision",
                "rationale": "Fixture rationale.",
                "alias_id": f"DEC-{number}",
                "alias_name": f"fixture-{status}-decision",
            }
        ],
        "invariants": [
            {
                "id": invariant_id,
                "statement": f"Fixture {status} invariant MUST hold.",
                "scope": "global",
                "enforcement_level": "must",
                "enforcement_mechanism": "policy",
                "verification_method": "audit",
                "rationale": "Fixture rationale.",
                "upheld_by_decisions": [decision_id],
                "alias_id": f"INV-{number}",
                "alias_name": f"inv-{number}",
            }
        ],
        "gaps": [],
        "alias_id": alias,
        "alias_name": f"fixture-{status}-adr",
    }


def test_child_lifecycle_follows_declaring_adr_status(tmp_path: Path) -> None:
    logical = tmp_path / "adrs" / "logical"
    logical.mkdir(parents=True)
    (tmp_path / "PROJECT.yaml").write_text(yaml.safe_dump(PROJECT, sort_keys=False), encoding="utf-8")
    for status, (alias, *ids) in CASES.items():
        document = _adr(status, alias, *ids)
        path = logical / f"{alias}-fixture-{status}-adr.yaml"
        path.write_text(yaml.safe_dump(document, sort_keys=False), encoding="utf-8")

    result = compile_architecture(
        CompilationRequest(
            project_root=tmp_path,
            artifact_groups=("registries",),
            write=True,
            timestamp="2026-01-01T00:00:00Z",
            include_system_overview=False,
        )
    )
    assert result.success, [item.message for item in result.diagnostics]

    registry = yaml.safe_load(
        (tmp_path / "adrs" / "index" / "entity-registry.yaml").read_text(encoding="utf-8")
    )
    lifecycle = {entity["id"]: entity["lifecycle_stage"] for entity in registry["entities"]}
    for status, (_, adr_id, decision_id, invariant_id) in CASES.items():
        expected = EXPECTED[status]
        assert lifecycle[adr_id] == expected, f"{status} ADR"
        assert lifecycle[decision_id] == expected, f"{status} ADR decision"
        assert lifecycle[invariant_id] == expected, f"{status} ADR invariant"
