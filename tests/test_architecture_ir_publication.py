from __future__ import annotations

import json
from pathlib import Path

import jsonschema

from scripts.publish_architecture_ir_fragments import OUTPUT_PATH, publish_architecture_ir_fragments


REPO_ROOT = Path(__file__).resolve().parents[1]
KERNEL_SCHEMA_PATH = (
    REPO_ROOT.parent / "ste-kernel" / "architecture-ir" / "architecture-ir.schema.json"
)
DECISION_ID = "decision:c6ab3dd75821e8181aea60442b230e4cdb24d63ea5ebe6436448ba94caf6ef28"


def _load_kernel_schema() -> dict:
    return json.loads(KERNEL_SCHEMA_PATH.read_text(encoding="utf-8"))


def _build_compiled_document(records: list[dict]) -> dict:
    entities = [record for record in records if "kind" in record]
    relationships = [record for record in records if "type" in record]
    return {
        "ir_version": "0.1.0",
        "schema_id": "https://ste-kernel.local/schema/architecture-ir/0.1.0/architecture-ir.schema.json",
        "document_id": "sha256:" + "e" * 64,
        "assembled_at": "2026-03-21T00:00:00.000Z",
        "namespace": "repo:ste-workspace:boot",
        "entities": {
            "capabilities": [],
            "decisions": [
                {
                    "id": DECISION_ID,
                    "kind": "decision",
                    "adr_id": "ADR-L-9000\u001fDEC-9000",
                    "status": "promoted",
                    "authority_tier": "promoted",
                    "summary": "Publish a deterministic logical ADR fragment for boot readiness.",
                    "provenance": entities[0]["provenance"],
                }
            ],
            "components": [record for record in entities if record["kind"] == "component"],
            "invariants": [record for record in entities if record["kind"] == "invariant"],
            "rules": [],
            "evidences": [],
        },
        "relationships": {
            "decision_supports_capability": [],
            "component_implements_decision": [
                record for record in relationships if record["type"] == "component_implements_decision"
            ],
            "invariant_constrains_component": [
                record for record in relationships if record["type"] == "invariant_constrains_component"
            ],
            "rule_evaluates_decision": [],
            "evidence_supports_component": [],
        },
    }


def test_publish_architecture_ir_fragments_writes_conventional_artifact() -> None:
    output_path = publish_architecture_ir_fragments()

    assert output_path == OUTPUT_PATH
    assert output_path.exists()
    assert output_path.read_bytes()[:3] != b"\xef\xbb\xbf"

    records = json.loads(output_path.read_text(encoding="utf-8"))
    assert isinstance(records, list)
    assert {record.get("kind", record.get("type")) for record in records} == {
        "component",
        "invariant",
        "component_implements_decision",
        "invariant_constrains_component",
    }
    assert all(
        record["provenance"]["source"]["adapter"] == "spec"
        for record in records
    )

    jsonschema.validate(instance=_build_compiled_document(records), schema=_load_kernel_schema())


def test_publish_architecture_ir_fragments_is_deterministic() -> None:
    first_path = publish_architecture_ir_fragments()
    first_bytes = first_path.read_bytes()

    second_path = publish_architecture_ir_fragments()
    second_bytes = second_path.read_bytes()

    assert second_path == first_path
    assert first_bytes == second_bytes
