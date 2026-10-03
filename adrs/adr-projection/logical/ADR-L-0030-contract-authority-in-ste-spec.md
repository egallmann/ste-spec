<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 2759e1aba067c30516e0fbd252f83bdf2bd4a4f8578d2ca6821abf53ac313ee2
rendered_hash: 82b275bd77c3a71df038a56baef9ab061360f528d561937337ba0c09a31aecc6
-->

# ADR-L-0030: Contract Authority in ste-spec

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** contracts, governance<br>
**Tags:** contracts, ste-spec<br>
**Alias name:** contract-authority-in-ste-spec<br>

## Context

Cross-repository handoff contracts are governed in **ste-spec**: shape in `contracts/`,
rules in `invariants/`, rationale in ADRs. Runtime and kernel repos remain subordinate
implementation surfaces.

Legacy: `adrs/published/ADR-030-contract-authority-in-ste-spec.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1002** defines
admission semantics at the kernel documentation layer; this ADR asserts **ste-spec
ownership of interchange contracts** that admission consumes.








## Invariants

### INV-3001

**Statement:** Runtime and kernel repositories MUST NOT treat repo-local types, tests, or informal
prose as authoritative over ste-spec `contracts/` and published invariants for the
same handoff surfaces.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves ADR-L-0030 as the contract authority anchor.






## Decisions

### DEC-3001: Govern cross-repository handoff contract shape in ste-spec `contracts/` and rules in `invariants/`

**Rationale:**
Single normative source for payload structure, semantic rules, and architectural intent
at the runtime/kernel boundary.



**Consequences:**

**Positive:**
- No parallel shadow contract authority in consumer repos

**Negative:**
- Contract evolution requires coordinated ste-spec changes



## Gaps

### GAP-3001: Enumerate every handoff contract family in Architecture IR when catalogs mature

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0030 by ADR Architecture Kit*