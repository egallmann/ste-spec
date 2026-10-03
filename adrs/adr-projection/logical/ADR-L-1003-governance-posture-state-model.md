<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: c1b588e4be90df5b2c6d1ee38ec19aec25bfa6dd7aa0b3cfdd056ccce8b33b24
rendered_hash: ec39432accc17cd9786e1e277db90e13221fa282fef3caaad4973834904cec30
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

**Impact:** high<br>
**Blocking:** No






---

*Generated from ADR-L-1003 by ADR Architecture Kit*