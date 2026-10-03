<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: df532745760eb8aa6b05f75097d4f9210fc733d02ffba6c6a833364517dae07f
rendered_hash: 82e4bdf0a9d0b53f52d82ed13b74ecd2ed295181a96c184f33edf34de43c0e2a
-->

# ADR-L-0028: AI-DOC Fabric and Gateway Authority Boundaries

**Status:** accepted<br>
**Created:** 2025-12-29<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** fabric, gateway, runtime<br>
**Tags:** authority, boundaries<br>
**Alias name:** ai-doc-fabric-and-gateway-authority-boundaries<br>

## Context

Fabric is the sole canonical state authority, invariant resolver, conflict detector for
attested bundles, and signer of Fabric Attestations. Gateway is a pure verifier that does
not query Fabric during eligibility evaluation. Runtime assembles and transports bundles
and attestations without substituting Fabric authority.

Legacy: `adrs/published/ADR-028-fabric-gateway-authority-boundaries.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — kernel governance ADRs
describe documentation-state admission; this ADR pins **runtime STE component roles**
for canonical truth vs enforcement.








## Invariants

### INV-2801

**Statement:** During execution eligibility evaluation, Gateway MUST rely on signed attestations and
authoritative reference resolution rules in ADR-L-0024, not live Fabric queries, to
obtain canonical claims.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Separates Fabric publication time from Gateway verification time.






## Decisions

### DEC-2801: Require one-way knowledge flow Human or Agent to Runtime to Fabric to Runtime to Gateway to model provider; Gateway must not query Fabric synchronously on the eligibility hot path

**Rationale:**
Prevents cache, network, and availability variance from changing eligibility outcomes.



**Consequences:**

**Positive:**
- Deterministic eligibility given the same signed inputs

**Negative:**
- Runtime must prefetch attestations


### DEC-2802: Prohibit Gateway from recomputing Fabric conflict determinations or enriching attestations from external knowledge sources during evaluation

**Rationale:**
Preserves verifier-only posture and minimal attack surface for probing canonical state.



**Consequences:**

**Positive:**
- Consistent cross-vendor Gateway behavior

**Negative:**
- No best-effort gap filling at Gateway


### DEC-2803: Prohibit Runtime from signing Fabric Attestations or overriding Fabric canonical claims

**Rationale:**
Keeps canonical publisher boundary singular.



**Consequences:**

**Positive:**
- Clear accountability for attestations

**Negative:**
- Runtime cannot self-attest canonical slices



## Gaps

### GAP-2801: Physical deployment patterns for Fabric availability belong in ADR-PS when authored

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0028 by ADR Architecture Kit*