"""Fail until the logical corpus is homogeneous authoring 1.6.

The proposition key must already be absent, and every document must match the
accepted pre-migration baseline except ``schema_version``.
"""

from __future__ import annotations

from tests.carrier_migration import (
    ALLOWLIST,
    B1_PATH,
    ENCODING_ADR,
    load_logical_sources,
    load_snapshot,
    structural_diff,
)


def test_authoring_16_carrier_migration() -> None:
    sources = load_logical_sources()
    baseline = load_snapshot(B1_PATH)
    expected = baseline["documents"]

    assert len(sources) == 41
    assert set(sources) == set(expected)
    assert all("normative_propositions" not in document for document in sources.values())

    mismatches = {
        name: structural_diff(sources[name], expected[name])
        for name in sorted(sources)
        if structural_diff(sources[name], expected[name]) is not None
    }
    assert mismatches == {}
    assert ALLOWLIST == frozenset({"schema_version"})

    histogram: dict[str, int] = {}
    for document in sources.values():
        version = document["schema_version"]
        histogram[version] = histogram.get(version, 0) + 1
    assert histogram == {"1.6": 41}, (
        f"schema histogram {histogram} != {{'1.6': 41}}; "
        f"encoding ADR status is {sources[ENCODING_ADR]['status']}"
    )
