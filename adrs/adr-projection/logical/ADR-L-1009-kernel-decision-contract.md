<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: acd7484ed539b5c2eb2288581281ec4a90e361f1691bdd84242cd2dbd1794c1b
rendered_hash: 21fba516ce55a23d11cd9900d3fdeb1ebdbb76a709ac0bd620645b1131100668
-->

# ADR-L-1009: Kernel Decision Contract

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel, contract<br>
**Tags:** decision-contract, determinism<br>
**Alias name:** kernel-decision-contract<br>

## Context

This ADR-L defines the normative **inputs** and **outputs** of a kernel admission
decision and the invariants that make decisions auditable and reproducible. It is the
architectural predecessor to future schemas and integration contracts; it does not specify wire formats.

**requested_action** is a required input and MUST conform to ADR-L-1001. Assessment-only
flows follow ste-kernel ADR-PS for the assessment path and MUST NOT use this contract
for allow/deny semantics.

Repository roles and kernel fail-closed evidence gating are anchored by **ADR-L-0031** and
**ADR-L-0032** (migrated from published ADR-031 / ADR-032).








## Invariants

### INV-5081

**Statement:** Determinism — Given the same Architecture IR bundle, evidence bundle, governance
posture, active rules, and requested_action (plus fixed evaluation scope and
environment), the kernel MUST produce the same decision outcome and the same structured
explanation skeleton.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Enables audit, replay, and cross-environment parity for admission automation.




### INV-5082

**Statement:** Explainability — Every admission decision MUST cite the specific ADRs, IR elements,
rules, invariants, posture, or evidence observations that caused the outcome; vague
summaries without pointers are non-conformant.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Explanations without citations are indistinguishable from opaque denial of service.




### INV-5083

**Statement:** Fail-closed — Missing, invalid, or unverifiable required inputs MUST yield DENY or
CONDITIONAL outcomes that do not allow the requested_action; silent ALLOW is forbidden.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Prevents silent success when prerequisites are unknown or untrusted.






## Decisions

### DEC-6981: Require requested_action in the admission decision input closure

**Rationale:**
Admission without an action is undefined and fail-closed per invariants below.





### DEC-6982: Enumerate decision outputs including violations, drift, remediation, explanations

**Rationale:**
Consumers need both human and structured machine narratives tied to cited causes.






## Gaps

### GAP-5081: Formal schema for machine-readable explanation graph

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-1009 by ADR Architecture Kit*