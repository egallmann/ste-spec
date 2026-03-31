# Freshness fields across handoff contracts

## Normative scope

This note is **normative** for how **`ArchitectureEvidence`** freshness relates
to **`KernelAdmissionAssessment`** snapshot and decision fields. It does not
change runtime or kernel algorithms; it removes vocabulary ambiguity at the
contract boundary.

## Layers

| Layer | Contract location | Field | Vocabulary |
|-------|-------------------|-------|------------|
| Runtime evidence | `architecture-evidence.schema.json` | `freshness.status` | `current`, `stale-unknown`, `stale-confirmed` |
| Admission snapshot | `kernel-admission-assessment.schema.json` | `snapshot.freshnessStatus` | `fresh`, `partial`, `stale`, `unknown` |
| Admission decision | `kernel-admission-assessment.schema.json` | `decision.freshnessClass` | `current`, `stale-unknown`, `stale-confirmed` |

## Mapping rules

1. **`ArchitectureEvidence.freshness.status`** is the **authoritative runtime
   statement** of evidence freshness for conforming **`ArchitectureEvidence`**
   payloads (version `2`).

2. **`KernelAdmissionAssessment.decision.freshnessClass`** **MUST** carry the same
   three-valued semantics as evidence freshness for assessments produced from
   that evidence (it is the decision trace of the same concept).

3. **`KernelAdmissionAssessment.snapshot.freshnessStatus`** is a **caller-facing
   summary** vocabulary. For assessments driven from **`ArchitectureEvidence`**
   version `2`, implementations **SHOULD** map:

   - `current` → `fresh`
   - `stale-confirmed` → `stale`
   - `stale-unknown` → `unknown`

4. The value **`partial`** in `snapshot.freshnessStatus` is **reserved** for
   non–`ArchitectureEvidence-v2` sources or future extensions that require a
   distinct partial-freshness summary. It **MUST NOT** be required for v2
   runtime-sourced assessments.

## Reference implementation

The **`ste-kernel`** mapping for runtime-sourced evidence is implemented in
`src/admission/runtime-evidence.ts` (`snapshotFromRuntimeEvidence`) and legacy
compat paths in `src/adapters/runtime/runtime-ir-adapter.ts`. Those files are
**informative** as examples; this document is the **normative** vocabulary and
layering definition.
