<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 06bd9adb7703bb4edc8b9779a1156ea7191a74dbf81907611f968c11ad8eb4ea
rendered_hash: 9b006409e8659e4ac815b6989920534b122fa15b720d625c90fa94fa5fad3ebb
-->

# ADR-L-0031: Runtime and Kernel Responsibility Boundary

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** kernel, runtime<br>
**Tags:** admission, evidence<br>
**Alias name:** runtime-and-kernel-responsibility-boundary<br>

## Context

**ste-runtime** produces factual evidence only. **ste-kernel** is the caller-facing
admission authority at the evaluated System Instance boundary (explicit environment and
evaluation scope).

Legacy: `adrs/published/ADR-031-runtime-kernel-responsibility-boundary.md`.

**Reconciliation vs ADR-L-100x:** **merge** — **ADR-L-1001** action model and
**ADR-L-1002** admission model formalize the same separation for kernel documentation;
this ADR names the **repository roles** (runtime vs kernel) that realize it.








## Invariants

### INV-3101

**Statement:** ste-runtime MUST NOT emit caller-facing admission or execution-eligibility decision
semantics; ste-kernel alone emits `KernelAdmissionAssessment` per published contracts.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Enforces the evidence versus decision split at the boundary.






## Decisions

### DEC-3101: Confine ste-runtime to evidence production; assign caller-facing admission to ste-kernel

**Rationale:**
Keeps runtime factual and kernel authoritative without collapsing shared contracts into
one role.



**Consequences:**

**Positive:**
- Clear handoff semantics

**Negative:**
- Runtime cannot emit admission outcomes



## Gaps

### GAP-3101: Wire-format examples live in contracts; keep ADR-L scoped to authority

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0031 by ADR Architecture Kit*