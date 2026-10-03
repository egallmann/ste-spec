<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: eae29272c74a5c4ad70f75ad7d2e35650722c5b54e363b7fb619add69c17dadb
rendered_hash: 760a89f335cf1041a6b046bc0db411fb0eefda408cbe2038f55997aa262e5c44
-->

# ADR-L-1007: Golden System Model

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel<br>
**Tags:** golden, promotion<br>
**Alias name:** golden-system-model<br>

## Context

A Golden system is a designated reference or production-grade posture with stricter
eligibility, evidence, and promotion gates. Golden status is not merely descriptive;
it changes what future promotions and dependent systems may assume.

Promotion to Golden MUST be auditable and MUST bind to explicit authority (human
governance decision and/or deterministic automated gates declared in policy), not to
informal convention.








## Invariants

### INV-5061

**Statement:** Promotion to Golden MUST be reproducibly justified from IR, evidence, posture, and
explicit promotion records; silent promotion MUST be forbidden.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Golden status must be evidence-backed and reviewable, not a cosmetic label.






## Decisions

### DEC-6761: Define Golden eligibility prerequisites

**Rationale:**
Golden without criteria becomes a hollow label.





### DEC-6762: Define who or what may promote to Golden

**Rationale:**
Separates governance authority from tooling automation boundaries.





### DEC-6763: State implications for downstream systems and templates

**Rationale:**
Golden systems act as reference baselines for stricter inheritance or copying rules.






## Gaps

### GAP-5061: Automated versus human-only promotion gates per environment

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-1007 by ADR Architecture Kit*