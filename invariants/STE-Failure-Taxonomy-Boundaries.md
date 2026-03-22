# STE Failure Taxonomy Boundaries

## Purpose

`ste-spec` classifies failures in **non-overlapping** layers. This document maps
each layer to responsibilities so engineers do not mix cognitive divergence,
integration boot failures, and admission policy outcomes.

---

## Layer 1 — Cognitive / documentation-state divergence

**Source:** `invariants/STE-Divergence-Taxonomy.md`

**Describes:** Drift and inconsistency during **workspace cognition** (AI-DOC,
inventories, framework sync, RECON completeness, artifact structure).

**Characteristics:** Taxonomy types (for example `RECON-Incomplete`,
`Doc-State-Staleness`); gate types; reconvergence obligations.

**MUST NOT:** Use this taxonomy alone to classify `ste-kernel` boot or IR schema
failures—those belong to Layer 2.

---

## Layer 2 — Kernel integration failures

**Source:** `ste-kernel/documentation/BOOT_SEQUENCE.md` (stable class names)

**Describes:** Failures before **`kernel_ready`** or before valid merged IR is
available.

**Stable classes (normative names):**

- `adapter_unavailable`
- `invalid_artifacts`
- `ir_validation_failure`

**MUST:** Boot failures abort; no success **`KernelAdmissionAssessment`** alongside boot failure.

**MUST NOT:** Treat these as “divergence types” in the cognitive taxonomy; they
are **integration failures**.

---

## Layer 3 — Admission outcomes

**Source:** `contracts/kernel-admission-assessment.schema.json`; admission
evaluation in `ste-kernel`.

**Describes:** Policy-bearing **`KernelAdmissionAssessment`** after successful
boot and valid IR projection inputs.

**Characteristics:** `blocking`, `readyForAction`, `requiresAcknowledgement`,
`decision`, advisories.

**MUST NOT:** Conflate policy denial (`readyForAction: false`) with boot or IR
validation failure.

---

## Mapping Table

| Symptom example | Layer | Primary reference |
|-----------------|-------|-------------------|
| Stale AI-DOC inventory | 1 | Divergence Taxonomy |
| Missing adapter publication file | 2 | `adapter_unavailable` / `invalid_artifacts` |
| Merged IR fails schema | 2 | `ir_validation_failure` |
| Evidence valid but policy blocks action | 3 | `KernelAdmissionAssessment` |

---

## Related

- `execution/STE-Kernel-Execution-Model.md`
- `adr/ADR-032-fail-closed-enforcement-model.md`

## Canon Status

This file is **canonical** for failure-layer separation in `ste-spec`.
