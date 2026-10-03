<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 19870268bb3a7ee3c19953ed6027f7ae95c9f08158154ae027ad6ab92b8174ce
rendered_hash: be3bf3773c932343a1713f8b1fd90b34984bfb61833cd3d3a86f14bf5c09c66f
-->

# ADR-L-0033: Closed-Object Discipline

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** contracts, kernel<br>
**Tags:** schema, handoff<br>
**Alias name:** closed-object-discipline<br>

## Context

Runtime/kernel handoff objects are **closed by default**: undeclared fields are not
contract-valid and cannot become hidden semantic or policy channels across repositories.

Legacy: `adrs/published/ADR-033-closed-object-discipline.md`.

**Reconciliation vs ADR-L-1002:** **coexist-with-precedence** — admission consumes typed
inputs; closed objects prevent undeclared side channels that would undermine admission
predicates.








## Invariants

### INV-3301

**Statement:** Ad hoc extension fields on closed handoff objects MUST NOT be treated as contract-valid
without an explicit ste-spec contract and invariant update.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Prevents silent semantic extension.






## Decisions

### DEC-3301: Require closed-object discipline for encoded handoff payloads at the runtime/kernel boundary

**Rationale:**
Bounded objects force explicit contract evolution and deterministic rejection of drift.



**Consequences:**

**Positive:**
- Deterministic producer/consumer conformance

**Negative:**
- Extension requires spec revision



## Gaps

### GAP-3301: Per-contract closedness flags belong in schema metadata and invariants indexes

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0033 by ADR Architecture Kit*