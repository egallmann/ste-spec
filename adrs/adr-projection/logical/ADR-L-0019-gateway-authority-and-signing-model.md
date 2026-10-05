<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 9314ccdbdbdd1abb80c47d0b2d1842edb4e60c3a6dd50edce8488f2992e77749
rendered_hash: 038f0c0b6879624793c409df500a08d3dd7e64546a9f4903cbe5efbeaec1b4e6
-->

# ADR-L-0019: Gateway Authority and Signing Model

**Status:** accepted<br>
**Created:** 2025-12-23<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, gateway<br>
**Tags:** signing, enforcement, gateway<br>
**Alias name:** gateway-authority-and-signing-model<br>

## Context

STE Gateway verifies ORG-signed inputs and enforces eligibility; it does **not** attest
canonical truth or sign canonical artifacts. Eligibility outcomes are ephemeral and
unsigned.

Legacy: `adrs/published/ADR-019-gateway-authority-signing.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1009** kernel
decision contract and **ADR-L-1002** admission semantics govern STE-wide kernel
narratives; this ADR pins **gateway signing and attestation boundaries** for the STE
system model. On overlap, document precedence in consuming specs (e.g. execution model).








## Invariants

### INV-1901

**Statement:** The Gateway MUST NOT sign canonical artifacts or eligibility outcomes as substitutes
for ORG attestation of canonical truth.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves authority scarcity and non-repudiation semantics for canonical publishers.






## Decisions

### DEC-1901: Gateway holds ORG-scoped enforcement authority, not ORG attestation authority

**Rationale:**
Gateway verifies signatures and enforces constraints using ORG-signed canonical
material; it does not mint canonical artifacts, populate trust registries, or sign
eligibility decisions as durable truth.



**Consequences:**

**Positive:**
- Clear separation of verification vs attestation

**Negative:**
- Implementations cannot use Gateway keys as ORG signing keys


### DEC-1902: Treat execution eligibility outcomes as ephemeral, unsigned enforcement results

**Rationale:**
Eligibility answers are short-lived, derived deterministically from signed inputs, and
logged for audit without becoming canonical attestations.



**Consequences:**

**Positive:**
- Avoids false equivalence with immutable canonical state

**Negative:**
- Consumers cannot treat eligibility receipts as long-lived proofs without context



## Gaps

### GAP-1901: Map STE-System section references to machine cross-links in handbook/runtime

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0019 by ADR Architecture Kit*