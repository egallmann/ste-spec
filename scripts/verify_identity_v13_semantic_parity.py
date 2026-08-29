"""Verify v1.3 identity migration preserves ste-spec ADR semantics."""
from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
REPRESENTATION_FIELDS = {"alias_id", "alias_name", "schema_version"}
LEGACY_PUNCTUATION_NORMALIZATIONS = {
    "â€”": "—",
    "â€“": "–",
    "Â§": "§",
}


def git_show(ref: str, relative_path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"{ref}:{relative_path}"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return result.stdout


def git_paths(ref: str, prefix: str) -> list[str]:
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref, prefix],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    return [path for path in result.stdout.splitlines() if path.endswith((".yaml", ".yml"))]


def normalize(value: Any, uuid_to_alias: dict[str, str]) -> Any:
    if isinstance(value, dict):
        return {
            key: normalize(item, uuid_to_alias)
            for key, item in sorted(value.items())
            if key not in REPRESENTATION_FIELDS
        }
    if isinstance(value, list):
        return [normalize(item, uuid_to_alias) for item in value]
    if isinstance(value, str):
        for legacy, normalized in LEGACY_PUNCTUATION_NORMALIZATIONS.items():
            value = value.replace(legacy, normalized)
        return uuid_to_alias.get(value, value)
    return value


def source_documents(ref: str, uuid_to_alias: dict[str, str], *, current: bool) -> dict[str, Any]:
    paths = git_paths(ref, "adrs/logical") if not current else [
        path.relative_to(REPO_ROOT).as_posix()
        for path in sorted((REPO_ROOT / "adrs" / "logical").glob("*.yaml"))
    ]
    result: dict[str, Any] = {}
    for path in paths:
        text = (REPO_ROOT / path).read_text(encoding="utf-8") if current else git_show(ref, path)
        result[path] = normalize(yaml.safe_load(text), uuid_to_alias)
    return result


def relationship_triples(payload: dict[str, Any], uuid_to_alias: dict[str, str]) -> list[tuple[str, str, str]]:
    triples = [
        (
            str(item["relationship_type"]),
            uuid_to_alias.get(str(item["from_entity_id"]), str(item["from_entity_id"])),
            uuid_to_alias.get(str(item["to_entity_id"]), str(item["to_entity_id"])),
        )
        for item in payload.get("relationships", [])
    ]
    return sorted(triples)


def document_counts(documents: dict[str, Any]) -> dict[str, int | dict[str, int]]:
    values = list(documents.values())
    return {
        "adr_count": len(values),
        "statuses": dict(sorted(Counter(str(document.get("status")) for document in values).items())),
        "decisions": sum(len(document.get("decisions", [])) for document in values),
        "invariants": sum(len(document.get("invariants", [])) for document in values),
        "gaps": sum(len(document.get("gaps", [])) for document in values),
        "constraints": sum(len(document.get("constraints", [])) for document in values),
        "capabilities": sum(len(document.get("capabilities", [])) for document in values),
        "components": sum(len(document.get("components", [])) for document in values),
        "boundaries": sum(len(document.get("boundaries", [])) for document in values),
    }


def first_difference(left: Any, right: Any, path: str = "$") -> str:
    if type(left) is not type(right):
        return f"{path}: type {type(left).__name__} != {type(right).__name__}"
    if isinstance(left, dict):
        if set(left) != set(right):
            return f"{path}: keys {sorted(left)} != {sorted(right)}"
        for key in sorted(left):
            difference = first_difference(left[key], right[key], f"{path}.{key}")
            if difference:
                return difference
        return ""
    if isinstance(left, list):
        if len(left) != len(right):
            return f"{path}: length {len(left)} != {len(right)}"
        for index, (left_item, right_item) in enumerate(zip(left, right)):
            difference = first_difference(left_item, right_item, f"{path}[{index}]")
            if difference:
                return difference
        return ""
    if left != right:
        return f"{path}: {left!r} != {right!r}"
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before-ref", required=True)
    parser.add_argument("--identity-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    identity_map = yaml.safe_load(args.identity_map.read_text(encoding="utf-8"))
    uuid_to_alias = {entry["uuid"]: entry["legacy_alias_id"] for entry in identity_map["entries"]}
    before_documents = source_documents(args.before_ref, {}, current=False)
    after_documents = source_documents(args.before_ref, uuid_to_alias, current=True)
    before_relationships = relationship_triples(
        yaml.safe_load(git_show(args.before_ref, "adrs/index/relationship-registry.yaml")), {}
    )
    after_relationships = relationship_triples(
        yaml.safe_load((REPO_ROOT / "adrs/index/relationship-registry.yaml").read_text(encoding="utf-8")),
        uuid_to_alias,
    )

    errors: list[str] = []
    if before_documents != after_documents:
        changed = sorted(
            path
            for path in set(before_documents) | set(after_documents)
            if before_documents.get(path) != after_documents.get(path)
        )
        differences = {
            path: first_difference(before_documents.get(path), after_documents.get(path))
            for path in changed
        }
        errors.append(
            "Source semantic documents differ after inverse identity substitution: "
            + json.dumps(differences, sort_keys=True)
        )
    if before_relationships != after_relationships:
        errors.append("Relationship type/source/target multiset differs after inverse identity substitution")

    evidence = {
        "type": "identity_v13_semantic_parity",
        "before_ref": args.before_ref,
        "identity_map_fingerprint": identity_map["seal"]["map_fingerprint"],
        "counts": {
            "before": document_counts(before_documents),
            "after": document_counts(after_documents),
            "relationships_before": len(before_relationships),
            "relationships_after": len(after_relationships),
        },
        "representational_deltas": [
            "schema_version",
            "id",
            "alias_id",
            "alias_name",
            "YAML serializer normalization of legacy double-encoded dash punctuation",
        ],
        "semantic_parity_verified": not errors,
        "errors": errors,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
