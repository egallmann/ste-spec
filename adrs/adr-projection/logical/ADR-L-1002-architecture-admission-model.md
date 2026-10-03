<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: a48531da42d2749d3772a9b7028df53899f3fa04d4d141018b377b424f34bf9d
rendered_hash: b97bd7d9814f5f73f080210a650f2ef736b0f586bd87b774ffe168210153444b
-->

# ADR-L-1002: Architecture Admission Model

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel, admission<br>
**Tags:** admission, allow, deny<br>
**Alias name:** architecture-admission-model<br>

## Context

Admission decides whether a **requested action** may proceed under declared
architecture truth (IR), factual evidence, governance posture, and active rules.
This ADR-L defines the semantic meaning of allowed, denied, conditional, and warned
admission postures and the **input closure** required to reach a decision.

IR validation versus admission evaluation follows ADR-031 and the STE kernel execution
model: invalid IR is a boot/integration failure surface, not a disguised policy waiver.








## Invariants

### INV-5011

**Statement:** Admission input closure MUST include validated Architecture IR slice (or compiled IR
handle), evidence bundle reference, governance posture, active ruleset identity,
requested_action, environment, and evaluation scope sufficient to reproduce the decision.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Reproducible admission requires explicit inputs aligned with ADR-L-1009 determinism invariant.




### INV-5012

**Statement:** DENY and CONDITIONAL outcomes MUST NOT be represented as successful boot or successful
unvalidated IR consumption.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Preserves separation between IR validation/boot integrity and policy-layer admission outcomes.






## Decisions

### DEC-6211: Treat admission as evaluation of requested_action in context

**Rationale:**
Aligns all admission semantics with ADR-L-1001; forbids abstract system-only checks.





### DEC-6212: Separate IR validation failure semantics from policy denial semantics

**Rationale:**
Preserves fail-closed boot while keeping admission outcomes honest for policy layers.







---

*Generated from ADR-L-1002 by ADR Architecture Kit*