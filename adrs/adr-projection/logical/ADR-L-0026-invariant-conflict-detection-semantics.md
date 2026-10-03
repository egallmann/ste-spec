<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 68423c4951bd0de961bc0e62769674fb2e4c6a0a6c2e04d67b84c5ee8df91048
rendered_hash: ecfd7743175432e5835b611ae0d528ea9b8cf86f239a7e2681798d6280c881d4
-->

# ADR-L-0026: Invariant Conflict Detection Semantics

**Status:** accepted<br>
**Created:** 2025-12-29<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** fabric, gateway<br>
**Tags:** invariants, conflicts<br>
**Alias name:** invariant-conflict-detection-semantics<br>

## Context

For v1, Fabric performs conflict detection when creating attestations and signs a
`conflict_status` field (`none` or `detected`). Gateway verifies the attestation and
enforces denial when conflicts are attested; Gateway MUST NOT implement independent
invariant content parsing for conflict detection.

Legacy: `adrs/published/ADR-026-invariant-conflict-detection-semantics.md`.

**Reconciliation vs ADR-L-0023:** **merge** — the normative Gateway obligation in
ADR-L-0023 is satisfied by **verifying Fabric-attested conflict status**, not by
recomputing conflicts from raw invariant payloads at Gateway.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — kernel IR may model
invariants separately; this ADR governs **STE eligibility attestation mechanics**.








## Invariants

### INV-2601

**Statement:** Gateway MUST NOT treat raw invariant payload comparison as authoritative for conflict
detection; authoritative conflict signal is the signed Fabric `conflict_status` field.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Aligns verifier-only boundary with deterministic enforcement.






## Decisions

### DEC-2601: Define v1 conflict as duplicate canonical invariant identifiers with differing content digests within one Fabric Attestation scope

**Rationale:**
Provides a mechanical, falsifiable conflict predicate without semantic theorem proving.



**Consequences:**

**Positive:**
- Deterministic detection in Fabric

**Negative:**
- Semantic contradictions without ID collision remain out of scope for v1


### DEC-2602: Require signed `conflict_status` on Fabric Attestations; Gateway denies with INVARIANT_CONFLICT when status is detected; missing or invalid status fails closed

**Rationale:**
Keeps Gateway in verifier-only posture while enforcing PREREQ-4 outcomes.



**Consequences:**

**Positive:**
- Stable denial category mapping

**Negative:**
- Fabric must publish consistent attestation fields


### DEC-2603: Forbid Gateway-side conflict algorithms that parse or compare invariant content beyond attestation verification

**Rationale:**
Prevents implementation divergence and hidden state discovery at the boundary.



**Consequences:**

**Positive:**
- Interoperable Gateway behavior

**Negative:**
- Fabric bears detection responsibility



## Gaps

### GAP-2601: Future ADR-L for semantic conflict classes or cross-attestation rules if required

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0026 by ADR Architecture Kit*