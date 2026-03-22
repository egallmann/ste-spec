from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = REPO_ROOT / "contracts" / "architecture-ir" / "spec-ir-fragments.json"
DECISION_ID = "decision:c6ab3dd75821e8181aea60442b230e4cdb24d63ea5ebe6436448ba94caf6ef28"
COMPONENT_ID = "component:architecture_graph"
INVARIANT_ID = "invariant:kernel.boot.readiness.contract"
LAST_UPDATED = "2026-03-21T00:00:00.000Z"


def _canonical_json_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _publication_json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def _content_hash(fragment: dict) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json_bytes(fragment)).hexdigest()


def _provenance(record_id: str, record_kind: str, input_ref: str) -> dict:
    fragment = {
        "namespace": "repo:ste-workspace:boot",
        "record_id": record_id,
        "record_kind": record_kind,
        "source_contract": input_ref,
    }
    return {
        "source": {
            "adapter": "spec",
            "artifact_uri": "spec://contracts/architecture-ir/spec-ir-fragments.json",
            "artifact_kind": "spec-ir-fragment",
        },
        "last_updated": LAST_UPDATED,
        "derivation_chain": [
            {
                "step": 0,
                "adapter": "spec",
                "operation": "publish_spec_ir_fragment",
                "input_ref": input_ref,
                "adapter_schema_version": "1.0",
                "content_hash": _content_hash(fragment),
            }
        ],
    }


def build_spec_ir_records() -> list[dict]:
    records = [
        {
            "id": COMPONENT_ID,
            "kind": "component",
            "name": "architecture_graph",
            "type": "service",
            "boundary": "kernel",
            "owners": ["ste-spec"],
            "provenance": _provenance(
                COMPONENT_ID,
                "component",
                "spec://architecture/STE-Architecture.md#architecture-graph",
            ),
        },
        {
            "id": INVARIANT_ID,
            "kind": "invariant",
            "invariant_key": "kernel.boot.readiness.contract",
            "statement": "The kernel boot readiness contract must be published deterministically.",
            "scope": "kernel_boot",
            "enforcement_level": "must",
            "enforcement_mechanism": "governance",
            "verification_method": "manual",
            "rationale": "Boot orchestration must consume only published contract-backed artifacts.",
            "provenance": _provenance(
                INVARIANT_ID,
                "invariant",
                "spec://invariants/INV-0007-closed-object-contract-discipline",
            ),
        },
        {
            "id": "rel:component.implements.decision.architecture_graph.c6ab3dd75821",
            "type": "component_implements_decision",
            "from_id": COMPONENT_ID,
            "to_id": DECISION_ID,
            "provenance": _provenance(
                "rel:component.implements.decision.architecture_graph.c6ab3dd75821",
                "relationship",
                "spec://architecture/STE-Architecture.md#architecture-graph",
            ),
        },
        {
            "id": "rel:invariant.constrains.component.kernel.boot.readiness.contract.architecture_graph",
            "type": "invariant_constrains_component",
            "from_id": INVARIANT_ID,
            "to_id": COMPONENT_ID,
            "provenance": _provenance(
                "rel:invariant.constrains.component.kernel.boot.readiness.contract.architecture_graph",
                "relationship",
                "spec://invariants/INV-0007-closed-object-contract-discipline",
            ),
        },
    ]
    return sorted(records, key=lambda record: record["id"].encode("utf-8"))


def publish_architecture_ir_fragments(output_path: Path = OUTPUT_PATH) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(_publication_json_bytes(build_spec_ir_records()))
    return output_path


def main() -> int:
    output_path = publish_architecture_ir_fragments()
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
