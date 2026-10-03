<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 7e6ef3a942c2a67c478545f6713bdb2820f3694f533332de6c62e3c122e4bf5d
rendered_hash: 0a5a604d9306a9c96d4f7de445341b1e098f65c72f8de94eaa2eccbfb1ffa61c
-->

# ADR-L-0021: Gateway Trust Verification Model

**Status:** accepted<br>
**Created:** 2025-12-23<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, gateway<br>
**Tags:** trust-registry, fail-closed<br>
**Alias name:** gateway-trust-verification-model<br>

## Context

Gateway is not a trust-registry principal; trust checks run per eligibility evaluation;
registry outages fail execution closed; bootstrap material only anchors registry
verification; cached trust cannot authorize execution.

Legacy: `adrs/published/ADR-021-gateway-trust-verification.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1009** states
kernel fail-closed posture; this ADR specializes **Gateway trust verification** mechanics.








## Invariants

### INV-2101

**Statement:** Cached trust material MUST NOT be used to approve execution eligibility; if used for
read-only paths, outputs MUST be marked non-authoritative and canonical promotion MUST
be blocked.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Mitigates revocation and staleness attacks.






## Decisions

### DEC-2101: Gateway is not a Trust Registry principal and performs per-request trust verification

**Rationale:**
Avoids self-referential trust entries and ensures revocations and expirations are
respected at evaluation time.



**Consequences:**

**Positive:**
- Contemporaneous trust decisions

**Negative:**
- Higher verification load per request


### DEC-2102: Fail closed when the Trust Registry is unavailable; bootstrap keys only verify the registry; cache cannot authorize execution

**Rationale:**
Prevents stale or offline trust from authorizing execution; read-only degraded modes
must be explicitly non-authoritative.



**Consequences:**

**Positive:**
- Stronger security posture

**Negative:**
- Availability coupling to registry health



## Gaps

### GAP-2101: Physical deployment patterns for registry HA belong in ADR-PS when authored

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0021 by ADR Architecture Kit*