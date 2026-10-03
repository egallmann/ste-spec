<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: a6ec22ea449f83e2dd845ac18ef83867c204ab4218397b229f3ed99044fb1273
rendered_hash: 544c2cd9d1437e6a352b77973b3680f9400ca4dbccf59b87c10e96a9a179fa9d
-->

# ADR-L-1004: Architecture Freshness Model

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel, evidence<br>
**Tags:** freshness, staleness<br>
**Alias name:** architecture-freshness-model<br>

## Context

Freshness distinguishes whether integration-state (Architecture IR) and observational
state (evidence) are current enough for the decision at hand. IR freshness and evidence
freshness are distinct signals and MUST NOT be conflated.

Failure modes MUST align with ADR-031 and `execution/STE-Kernel-Execution-Model.md`:
invalid IR blocks boot; admission operates only on validated IR projections.








## Invariants

### INV-5031

**Statement:** IR validation failure MUST surface as boot/integration failure, not as a successful
admission ALLOW outcome.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Matches STE kernel execution model: invalid IR cannot underpin successful admission.




### INV-5032

**Statement:** Freshness interpretations for identical inputs MUST be stable for deterministic replay
of admission outcomes.
<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Deterministic replay and audit require stable freshness classification for identical inputs.






## Decisions

### DEC-6431: Define IR invalid as boot failure preventing operational kernel use

**Rationale:**
Unvalidated IR cannot be a trustworthy substrate for admission or orchestration.





### DEC-6432: Map IR stale to CONDITIONAL or DENY per posture and rules

**Rationale:**
Stale declared architecture may still be structurally valid but untrustworthy for action.





### DEC-6433: Map evidence stale to WARNING or CONDITIONAL default bands

**Rationale:**
Evidence lag may warn or gate without necessarily invalidating IR structure.





### DEC-6434: Map evidence missing to CONDITIONAL or DENY per required evidence classes

**Rationale:**
Missing required observations cannot be treated as silent assent.





### DEC-6435: Treat IR and evidence mismatch as drift classification input

**Rationale:**
Mismatch is not resolved by picking a winner; it is classified per ADR-L-1005.






## Gaps

### GAP-5031: Required evidence classes per action and environment

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-1004 by ADR Architecture Kit*