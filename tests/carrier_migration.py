"""Structural snapshots for the authoring 1.6 carrier migration.

Compared values are parsed canonical ADR sources. The only allowlisted
difference is ``schema_version``.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
LOGICAL_DIR = REPO_ROOT / "adrs" / "logical"
FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "authoring-16-carrier"
B0_PATH = FIXTURE_DIR / "b0.json"
B1_PATH = FIXTURE_DIR / "b1.json"
ALLOWLIST = frozenset({"schema_version"})
ENCODING_ADR = "ADR-L-1010-canonical-adr-encoding-moves-to-authoring-1-6.yaml"
B0_REF = "e21b8409f09d01be419db09d979ce924a92e3777"
B1_REF = "f10abe05bdf74ece3e163757d087c2c3355e44eb"


def parse_adr_bytes(payload: bytes) -> dict[str, Any]:
    """Parse one canonical ADR YAML document."""
    document = yaml.safe_load(payload)
    if not isinstance(document, dict):
        raise TypeError("ADR source did not parse to a mapping")
    return document


def canonical_bytes(document: dict[str, Any]) -> bytes:
    """Return deterministic UTF-8 JSON for a parsed ADR document."""
    return json.dumps(
        document,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_sha256(document: dict[str, Any]) -> str:
    """Return the SHA-256 of one canonical ADR document."""
    return hashlib.sha256(canonical_bytes(document)).hexdigest()


def allowlisted(document: dict[str, Any]) -> dict[str, Any]:
    """Replace allowlisted fields so only those values may differ."""
    compared = copy.deepcopy(document)
    for key in ALLOWLIST:
        if key in compared:
            compared[key] = None
    return compared


def structural_diff(left: dict[str, Any], right: dict[str, Any]) -> str | None:
    """Return a mismatch description, or None when the allowlisted values match."""
    left_bytes = canonical_bytes(allowlisted(left))
    right_bytes = canonical_bytes(allowlisted(right))
    if left_bytes == right_bytes:
        return None
    return "allowlisted structural mismatch"


def load_logical_sources(root: Path = LOGICAL_DIR) -> dict[str, dict[str, Any]]:
    """Parse every canonical logical ADR in filename order."""
    documents: dict[str, dict[str, Any]] = {}
    for path in sorted(root.glob("*.yaml")):
        documents[path.name] = parse_adr_bytes(path.read_bytes())
    return documents


def load_snapshot(path: Path) -> dict[str, Any]:
    """Load one committed baseline snapshot."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"{path} did not contain a snapshot object")
    return payload


def snapshot_document_sha256(snapshot: dict[str, Any]) -> str:
    """Hash the ordered canonical documents stored in a snapshot."""
    digest = hashlib.sha256()
    documents = snapshot["documents"]
    for name in sorted(documents):
        digest.update(name.encode("utf-8"))
        digest.update(canonical_bytes(documents[name]))
    return digest.hexdigest()
