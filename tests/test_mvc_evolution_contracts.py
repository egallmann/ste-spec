from __future__ import annotations

import copy
import json
from pathlib import Path

import jsonschema
import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_DIR = REPO_ROOT / "contracts"
EXAMPLES_DIR = CONTRACTS_DIR / "examples"


VALID_FIXTURES = [
    (
        CONTRACTS_DIR / "graph-domain" / "graph-domain-definition.schema.json",
        EXAMPLES_DIR / "graph-domain-definition.valid.json",
    ),
    (
        CONTRACTS_DIR / "linkage-surface" / "linkage-surface.schema.json",
        EXAMPLES_DIR / "linkage-surface.valid.json",
    ),
    (
        CONTRACTS_DIR / "context-domain" / "context-domain-definition.schema.json",
        EXAMPLES_DIR / "context-domain-definition.valid.json",
    ),
    (
        CONTRACTS_DIR / "context-domain" / "context-domain-bundle.schema.json",
        EXAMPLES_DIR / "context-domain-bundle.valid.json",
    ),
    (
        CONTRACTS_DIR / "persona" / "persona-definition.schema.json",
        EXAMPLES_DIR / "persona-definition.valid.json",
    ),
    (
        CONTRACTS_DIR / "mvc" / "mvc-definition.schema.json",
        EXAMPLES_DIR / "mvc-definition.valid.json",
    ),
    (
        CONTRACTS_DIR / "mvc" / "mvc-snapshot.schema.json",
        EXAMPLES_DIR / "mvc-snapshot.valid.json",
    ),
    (
        CONTRACTS_DIR / "mvc" / "mvc-materialization-result.schema.json",
        EXAMPLES_DIR / "mvc-materialization-result.valid.json",
    ),
]


INVALID_FIXTURES = [
    (
        CONTRACTS_DIR / "context-domain" / "context-domain-definition.schema.json",
        EXAMPLES_DIR / "context-domain-definition.invalid-materialized.json",
        "selected_entities",
    ),
    (
        CONTRACTS_DIR / "linkage-surface" / "linkage-surface.schema.json",
        EXAMPLES_DIR / "linkage-surface.invalid-raw-signal-authority.json",
        "ticket",
    ),
    (
        CONTRACTS_DIR / "mvc" / "mvc-snapshot.schema.json",
        EXAMPLES_DIR / "mvc-snapshot.invalid-admission.json",
        "admitted",
    ),
]


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _validator(schema_path: Path) -> jsonschema.Draft202012Validator:
    return jsonschema.Draft202012Validator(_load_json(schema_path))


def _assert_valid(schema_path: Path, instance: dict) -> None:
    _validator(schema_path).validate(instance)


def _assert_invalid(schema_path: Path, instance: dict, expected_message_part: str) -> None:
    errors = sorted(_validator(schema_path).iter_errors(instance), key=lambda error: list(error.path))
    assert errors, "Expected fixture to fail schema validation"
    assert any(expected_message_part in error.message for error in errors), [
        error.message for error in errors
    ]


@pytest.mark.parametrize(("schema_path", "fixture_path"), VALID_FIXTURES)
def test_mvc_evolution_valid_fixtures_validate(schema_path: Path, fixture_path: Path) -> None:
    _assert_valid(schema_path, _load_json(fixture_path))


@pytest.mark.parametrize(("schema_path", "fixture_path", "expected_message_part"), INVALID_FIXTURES)
def test_mvc_evolution_invalid_fixtures_fail_for_expected_boundary(
    schema_path: Path,
    fixture_path: Path,
    expected_message_part: str,
) -> None:
    _assert_invalid(schema_path, _load_json(fixture_path), expected_message_part)


def test_context_domain_definition_is_declarative_only() -> None:
    schema_path = CONTRACTS_DIR / "context-domain" / "context-domain-definition.schema.json"
    base = _load_json(EXAMPLES_DIR / "context-domain-definition.valid.json")

    forbidden_payloads = {
        "selected_entities": [],
        "selected_relationships": [],
        "materialized_graph": {"nodes": [], "edges": []},
        "admission_outcome": {"admitted": True},
        "rendered_context_payload": "rendered context is not definition state",
    }

    _assert_valid(schema_path, base)
    for field, value in forbidden_payloads.items():
        candidate = copy.deepcopy(base)
        candidate[field] = value
        _assert_invalid(schema_path, candidate, field)


def test_graph_domain_definition_is_not_graph_instance() -> None:
    schema_path = CONTRACTS_DIR / "graph-domain" / "graph-domain-definition.schema.json"
    base = _load_json(EXAMPLES_DIR / "graph-domain-definition.valid.json")

    forbidden_payloads = {
        "nodes": [],
        "edges": [],
        "materialized_topology": {"node_count": 0, "edge_count": 0},
        "runtime_graph_snapshot": {"snapshot_id": "runtime-graph:fixture"},
    }

    _assert_valid(schema_path, base)
    for field, value in forbidden_payloads.items():
        candidate = copy.deepcopy(base)
        candidate[field] = value
        _assert_invalid(schema_path, candidate, field)


def test_mvc_d_is_not_materialized() -> None:
    schema_path = CONTRACTS_DIR / "mvc" / "mvc-definition.schema.json"
    base = _load_json(EXAMPLES_DIR / "mvc-definition.valid.json")

    assert "traversal_policy_ref" in base
    assert "projection_policy_ref" in base
    assert "admission_policy_ref" in base
    assert "context_domain_requirements" in base

    forbidden_payloads = {
        "assembled_context": [],
        "selected_entities": [],
        "admitted_payload": {"admitted": True},
    }

    _assert_valid(schema_path, base)
    for field, value in forbidden_payloads.items():
        candidate = copy.deepcopy(base)
        candidate[field] = value
        _assert_invalid(schema_path, candidate, field)


def test_mvc_s_is_not_admitted() -> None:
    schema_path = CONTRACTS_DIR / "mvc" / "mvc-snapshot.schema.json"
    base = _load_json(EXAMPLES_DIR / "mvc-snapshot.valid.json")

    assert "candidate_entities" in base
    assert "candidate_relationships" in base
    assert "inclusion_rationale" in base
    assert "exclusion_rationale" in base
    assert "topology_metrics" in base

    forbidden_payloads = {
        "admission_decision": {"admitted": True},
        "caller_facing_eligibility": "eligible",
        "kernel_assessment_state": {"assessment_id": "kernel-admission-assessment:fixture"},
    }

    _assert_valid(schema_path, base)
    for field, value in forbidden_payloads.items():
        candidate = copy.deepcopy(base)
        candidate[field] = value
        _assert_invalid(schema_path, candidate, field)


def test_mvc_m_preserves_provenance_and_integrity_requirements() -> None:
    schema_path = CONTRACTS_DIR / "mvc" / "mvc-materialization-result.schema.json"
    base = _load_json(EXAMPLES_DIR / "mvc-materialization-result.valid.json")

    for required_field in [
        "provenance",
        "integrity",
        "inclusion_rationale",
        "exclusion_rationale",
        "freshness",
    ]:
        candidate = copy.deepcopy(base)
        candidate.pop(required_field)
        _assert_invalid(schema_path, candidate, required_field)

    authority_elevation_payloads = {
        "authority_status": "authoritative",
        "creates_architectural_authority": True,
        "derived_content_authority": "canonical",
    }

    _assert_valid(schema_path, base)
    for field, value in authority_elevation_payloads.items():
        candidate = copy.deepcopy(base)
        candidate[field] = value
        _assert_invalid(schema_path, candidate, field)
