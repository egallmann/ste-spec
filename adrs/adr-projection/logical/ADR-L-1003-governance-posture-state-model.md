<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 6984a2f4bcfbda01e05ad752a484c692711dd448f01c7910245c38fa1d3d36f3
rendered_hash: 94530e7638636d789ea479aeb6534d289403a8f3eceba762821a82cff639792d
-->

# ADR-L-1003: Governance Posture State Model

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel<br>
**Tags:** posture, golden, experimental<br>
**Alias name:** governance-posture-state-model<br>

## Context

Governance posture constrains what is allowed, what requires explicit approval, what is
restricted, and what is denied independent of any single rule. This model composes with
active rules and promotion flows defined elsewhere (ADR-040 Spine, ste-rules-library).

Posture states are not a substitute for architecture truth; they modulate enforcement
strictness and approval requirements on top of IR and evidence.








## Invariants

### INV-5021

**Statement:** Posture MUST modulate admission outcomes only through declared, deterministic rules;
posture MUST NOT override normative architecture authority in ste-spec.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Normative architecture remains authoritative; posture only modulates enforcement strictness.




### INV-5022

**Statement:** Golden and locked postures MUST impose stricter or equal constraints compared to
governed baseline for the same action class unless explicitly documented exceptions exist.
<br>
**Scope:** global<br>
**Enforcement:** should (design)<br>
**Verification:** manual

**Rationale:**
Golden and locked names imply elevated assurance; weakening defaults would mislead consumers.






## Decisions

### DEC-6321: Define posture states experimental, governed, restricted, locked, golden

**Rationale:**
Provides a shared vocabulary for progressive assurance and promotion.





### DEC-6322: Bind posture transitions to auditable authority and evidence

**Rationale:**
Prevents silent escalation or relaxation of enforcement posture.






## Gaps

### GAP-5021: Exact matrix of posture x action class defaults

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-1003 by ADR Architecture Kit*