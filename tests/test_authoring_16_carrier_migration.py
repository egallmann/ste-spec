"""Historical evidence for the authoring 1.6 carrier migration.

B0 and B1 are immutable snapshots of the logical corpus before the migration.
They are compared only with each other; the live corpus is not frozen to them.
The live check below enforces only the encoding that ADR-L-1010 requires.
"""

from __future__ import annotations

from tests.carrier_migration import (
    ALLOWLIST,
    B0_PATH,
    B0_REF,
    B1_PATH,
    B1_REF,
    ENCODING_ADR,
    load_logical_sources,
    load_snapshot,
    snapshot_document_sha256,
    structural_diff,
)


B0_DOCUMENTS_SHA256 = "d49247cf20ab22e8e1e030c577a9c377505d862c8404ac17b4fa892398806bbd"
B1_DOCUMENTS_SHA256 = "9ecbbd4198fba334ac7249d5a3d4a70f9ab00be4ee91bb4785aace01e272c717"
PRE_MIGRATION_SCHEMA = "1.3"


def test_allowlist_is_schema_version_only() -> None:
    assert ALLOWLIST == frozenset({"schema_version"})


def test_baselines_are_unchanged_historical_snapshots() -> None:
    b0 = load_snapshot(B0_PATH)
    b1 = load_snapshot(B1_PATH)

    assert b0["ref"] == B0_REF
    assert b1["ref"] == B1_REF
    assert b0["count"] == len(b0["documents"])
    assert b1["count"] == len(b1["documents"])
    assert snapshot_document_sha256(b0) == B0_DOCUMENTS_SHA256
    assert snapshot_document_sha256(b1) == B1_DOCUMENTS_SHA256


def test_b0_is_the_corpus_before_the_encoding_adr() -> None:
    documents = load_snapshot(B0_PATH)["documents"]

    assert ENCODING_ADR not in documents
    assert {document["schema_version"] for document in documents.values()} == {
        PRE_MIGRATION_SCHEMA
    }


def test_b1_is_b0_plus_only_the_encoding_adr() -> None:
    b0 = load_snapshot(B0_PATH)["documents"]
    b1 = load_snapshot(B1_PATH)["documents"]

    assert set(b1) - set(b0) == {ENCODING_ADR}
    assert set(b0) - set(b1) == set()
    mismatches = sorted(name for name in b0 if structural_diff(b0[name], b1[name]) is not None)
    assert mismatches == []


def test_b1_is_the_accepted_pre_migration_authority_state() -> None:
    documents = load_snapshot(B1_PATH)["documents"]

    assert documents[ENCODING_ADR]["alias_id"] == "ADR-L-1010"
    assert documents[ENCODING_ADR]["status"] == "accepted"
    assert {document["schema_version"] for document in documents.values()} == {
        PRE_MIGRATION_SCHEMA
    }


def test_baselines_carry_no_normative_propositions() -> None:
    for path in (B0_PATH, B1_PATH):
        documents = load_snapshot(path)["documents"]
        assert all("normative_propositions" not in document for document in documents.values())


def test_live_logical_corpus_is_authoring_16() -> None:
    sources = load_logical_sources()

    assert sources
    versions = {name: document["schema_version"] for name, document in sources.items()}
    assert {name: version for name, version in versions.items() if version != "1.6"} == {}
