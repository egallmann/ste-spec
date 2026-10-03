<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 8c890f0759ad1badf88e5b125e4fa73753df1b1648d36093e4691d92722554d5
rendered_hash: a70dbb202908a3790af8fe6c59fc1c77e727db29bce8626cbcb33825e3abae0e
-->

# ADR-L-0037: Repository README Conformance and Reference Implementation

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, documentation<br>
**Tags:** readme, conformance<br>
**Alias name:** repository-readme-conformance-and-reference-implementation<br>

## Context

Every STE repository MUST provide a README conforming to ADR-L-0036. README is an
Orientation artifact per ADR-L-0038: non-authoritative, should be versioned, cannot
introduce doctrine, and must cite normative sources for authority claims.

Legacy: `adrs/published/ADR-037-repository-readme-conformance-and-reference-implementation.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — orthogonal to kernel
admission contracts; governs **multi-repo human surfaces** only.








## Invariants

### INV-3701

**Statement:** Repository README files MUST remain subordinate to normative artifacts; they MUST NOT
introduce new normative rules, invariants, or contract shapes without an ADR-L or contract change.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Aligns Orientation posture with ADR-L-0038.






## Decisions

### DEC-3701: Treat ste-spec README as the reference implementation pattern for ADR-L-0036 conformance

**Rationale:**
Provides a concrete converged example after ste-spec refactor.



**Consequences:**

**Positive:**
- System-wide README convergence anchor

**Negative:**
- Reference may lag if ste-spec README changes without updating cross-links



## Gaps

### GAP-3701: Automated linting for README sections is optional tooling outside this ADR-L

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0037 by ADR Architecture Kit*