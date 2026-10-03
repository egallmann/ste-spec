<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: b3fe310283e7c96a98e51260fdf79637ee167803c5b3a6076e4e6b9b85c50052
rendered_hash: da17fc81a70b9b5ef5cc09b5430e4e4ba5d19a4b4047d560e1a583d86cf3f88e
-->

# ADR-L-0032: Fail-Closed Enforcement Model

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** kernel, enforcement<br>
**Tags:** fail-closed, admission<br>
**Alias name:** fail-closed-enforcement-model<br>

## Context

Invalid, unavailable, malformed, or semantically inconsistent runtime evidence and
related publication inputs are fail-closed at the **kernel** boundary before permissive
admission outcomes. Schema validity alone is insufficient for conformance.

Legacy: `adrs/published/ADR-032-fail-closed-enforcement-model.md`.

**Reconciliation vs ADR-L-1009:** **merge** — **ADR-L-1009** states determinism and
fail-closed kernel decision contracts; this ADR applies the same posture specifically to
**runtime evidence and publication inputs** at merge/admission.

**Reconciliation vs ADR-L-0022:** **coexist-with-precedence** — ADR-L-0022 defines STE
Gateway and promotion fail-closed triggers in the broader STE-System model; this ADR
governs the **kernel documentation-state / IR** enforcement chain.








## Invariants

### INV-3201

**Statement:** Version failures, closed-object shape failures, and semantic invariant failures at the
documented handoff MUST be fail-closed conditions for downstream compilation and
admission per ADR-L-0033 and ADR-L-0035.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Implements the enforcement link between shape, semantics, and admission.






## Decisions

### DEC-3201: Treat invalid boundary evidence and invalid publication inputs as blocking for compilation and admission

**Rationale:**
Unsupported or semantically invalid evidence must not yield action-eligible admission.



**Consequences:**

**Positive:**
- Trustworthy handoff contract

**Negative:**
- Stricter gating on partial failures



## Gaps

### GAP-3201: Diagnostic richness for denial paths is contract-defined; keep schemas aligned

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0032 by ADR Architecture Kit*