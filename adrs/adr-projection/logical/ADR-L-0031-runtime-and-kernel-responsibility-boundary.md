<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: ffa4dd0a23774998cdd301c26fa4fe7b4bbcfcb9b2580db5f1ad2b5833dc19a2
rendered_hash: c8f435b5b39780e3d5027dc858c05c47f74ce28d72fc064afc93300d8d0f198e
-->

# ADR-L-0031: Runtime and Kernel Responsibility Boundary

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-10-04<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** kernel, runtime<br>
**Tags:** admission, evidence<br>
**Alias name:** runtime-and-kernel-responsibility-boundary<br>

## Context

**ste-runtime** owns bounded observation and evidence-backed embodiment
reconstruction, including Runtime embodiment identity, semantic relationships, and
the governed resolution, support derivation, assessment, Runtime-semantic admission,
and Snapshot qualification assigned by Runtime authority. It is not architectural-intent
authority. **ste-kernel** is the caller-facing admission authority at the evaluated
System Instance boundary (explicit environment and evaluation scope) and alone emits
`KernelAdmissionAssessment`. Runtime semantic admission of reconstructed Runtime state
is not that caller-facing decision.

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
Enforces the caller-facing admission boundary. It does not confine ste-runtime
to raw observation, transfer architectural-intent authority to ste-runtime, or
treat Runtime semantic admission as `KernelAdmissionAssessment`.






## Decisions

### DEC-3101: Preserve ste-runtime embodiment reconstruction authority while assigning caller-facing admission and execution-eligibility decisions to ste-kernel

**Rationale:**
ste-runtime retains evidence-backed observation, embodiment reconstruction,
and the governed resolution, support derivation, assessment, Runtime-semantic
admission, and Snapshot qualification assigned by Runtime authority. That authority
is not architectural intent, and it does not include caller-facing admission or
execution-eligibility decisions. ste-kernel alone emits `KernelAdmissionAssessment`.
Runtime semantic admission is not `KernelAdmissionAssessment`.



**Consequences:**

**Positive:**
- Runtime reconstruction authority and kernel caller-facing admission remain distinct

**Negative:**
- Runtime cannot emit caller-facing admission or execution-eligibility decision semantics



## Gaps

### GAP-3101: Wire-format examples live in contracts; keep ADR-L scoped to authority

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0031 by ADR Architecture Kit*