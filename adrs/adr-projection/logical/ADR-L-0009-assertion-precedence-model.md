<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 98a137bae350f0abcb0e240be66b79186cbb4cf4b097149c8f9f853df9ff58e5
rendered_hash: 21d73c59c59391f8a22f58a0dd73a6b55f52a9f2ab777d6e32eacf57e46f0758
-->

# ADR-L-0009: Assertion Precedence Model

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** documentation-state, extraction, queries<br>
**Tags:** assertions, provenance, conflicts<br>
**Alias name:** assertion-precedence-model<br>

## Context

Manual assertions and deterministic extraction can describe the same elements. The model
preserves both with provenance, surfaces contradictions, requires evidence for human
claims, and supports time-bounded validity.

Legacy: `adrs/published/ADR-009-assertion-precedence-model.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — refines provenance and
conflict surfacing for Fabric queries (**ADR-L-0008**); kernel admission contracts
(**ADR-L-1002**, **ADR-L-1009**) govern the kernel boundary when both apply.








## Invariants

### INV-0901

**Statement:** Manual assertions MUST carry provenance sufficient to identify the asserting party,
scope, and evidentiary reference before admission into authoritative query surfaces.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Prevents unattested human overrides from masquerading as canonical facts.




### INV-0902

**Statement:** When extracted and asserted facts contradict, query responses MUST surface the
conflict with both provenances unless a superseding ADR-L defines automatic precedence.
<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Aligns with transparency commitments in ADR-L-0008.






## Decisions

### DEC-0901: Coexist extracted and asserted facts with explicit conflict surfacing

**Rationale:**
Store both sources with provenance; default queries return both; contradictions
appear in a dedicated conflicts section; users resolve disputes—no silent automatic
winner between extractor and human in the general case.



**Consequences:**

**Positive:**
- Auditable dual sources of truth

**Negative:**
- Requires client handling of conflicts


### DEC-0902: Require evidence, actor, scope, and optional expiry for manual assertions

**Rationale:**
Assertions without evidence are rejected; optional `valid_until` excludes stale
claims from default query results while preserving history when explicitly requested.



**Consequences:**

**Positive:**
- Governance and auditability for human overrides

**Negative:**
- Higher submission friction for assertions



## Gaps

### GAP-0901: Machine schema for assertion payloads and conflict records in Architecture IR

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0009 by ADR Architecture Kit*