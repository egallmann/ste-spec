<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 46a3f006a63f68c9628bd9925267b2667c471a8110a753254995710cdd1f5889
rendered_hash: e572e43af97ebf8a976c0f3af975a5de1d2840107c7b457fd5465cc36fc2e56b
-->

# ADR-L-0024: Cross-Component Contracts and Execution Eligibility Interface

**Status:** accepted<br>
**Created:** 2025-12-23<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** gateway, runtime<br>
**Tags:** contracts, context-bundle<br>
**Alias name:** cross-component-contracts-and-execution-eligibility-interface<br>

## Context

Gateway is a pure validator over a complete Context Bundle; Runtime (with ADF-produced
artifacts) supplies completeness. Requests use references and integrity bindings; responses
are structured with stable reason codes. Execution blocks synchronously until ALLOW.

Legacy: `adrs/published/ADR-024-cross-component-contracts.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1009** shapes
kernel-facing decision vocabulary; this ADR defines **Runtime–Gateway** eligibility
envelopes and reason-code stability for the STE system model.








## Invariants

### INV-2401

**Statement:** Execution MUST NOT begin until Gateway returns ALLOW; optimistic or asynchronous
eligibility patterns that proceed before ALLOW are forbidden for authoritative execution.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Prevents time-of-check to time-of-use gaps.






## Decisions

### DEC-2401: Gateway MUST NOT modify, enrich, infer, or complete eligibility requests; incomplete input fails closed

**Rationale:**
Preserves deterministic evaluation and audit reconstruction from submitted bundles alone.



**Consequences:**

**Positive:**
- Reproducible eligibility decisions

**Negative:**
- Callers must supply complete envelopes


### DEC-2402: Runtime or Runtime-plus-ADF constructs the complete Context Bundle; Gateway resolves references from authoritative stores and verifies independently

**Rationale:**
Separates construction from verification and prevents blind trust in upstream validation summaries.



**Consequences:**

**Positive:**
- Independent verification at the boundary

**Negative:**
- Duplicate verification work at Gateway


### DEC-2403: Require structured eligibility responses with ALLOW, DENY, or INDETERMINATE; map INDETERMINATE to denial for execution; use stable reason codes

**Rationale:**
Enables machine-actionable handling and aligns with normalized outcomes (ADR-L-0023).



**Consequences:**

**Positive:**
- Deterministic client behavior

**Negative:**
- Reason-code taxonomy must evolve carefully



## Gaps

### GAP-2401: Transport and serialization formats remain implementation-specific if contract semantics are preserved

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0024 by ADR Architecture Kit*