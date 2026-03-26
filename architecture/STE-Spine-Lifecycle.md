# STE Spine Lifecycle

## Purpose

This document is normative supporting doctrine for the STE Spine lifecycle.

It explains and maps the lifecycle defined canonically in
[`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md).
It uses ADR-040 for Spine-local terminology, does not override ADR-040, and
does not redefine artifact taxonomy, which remains canonical in
[`../adr/ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md).

## Canonical Spine Diagram

### How to read this diagram

- Read the stages from left to right in the exact lifecycle order defined by
  ADR-040.
- The figure shows lifecycle flow, not artifact taxonomy; the node labels are
  lifecycle stages, not artifact classes.
- Artifact classes are defined by ADR-038 and are not shown here as separate
  stages.
- The Spine shows how artifacts move through lifecycle boundaries, are
  evaluated, and influence downstream decisions.
- Authority shifts happen at named lifecycle boundaries defined by doctrine,
  not by diagram styling alone.
- Normative authority defines intent, implementation produces implementation
  truth, proof produces verification results, and governance decisions can feed
  the next cycle of intent change.
- `ste-kernel` performs deterministic validation, compilation, and
  caller-facing admission at the integration boundary.
- Runtime produces evidence only; it does not emit caller-facing admission
  decisions.
- `Publication` and `Projection` are overlays or postures in this model, not
  standalone artifact classes or lifecycle stages.
- Authority and canonicity are defined by the ADRs and doctrine text, not by
  this diagram.
- If this diagram and ADR-040 ever differ, ADR-040 governs and this diagram
  must be corrected.

```mermaid
flowchart LR
    intent["Intent Definition"] --> implementation["Implementation"]
    implementation --> proof["Proof / Verification"]
    proof --> publication["Publication / Integration Input"]
    publication --> compilation["Architecture IR Compilation"]
    compilation --> admission["Admission Decision"]
    admission --> runtime["Runtime Execution"]
    runtime --> observation["Observation (Evidence)"]
    observation --> assessment["Assessment (Reports)"]
    assessment --> governance["Governance Decision"]
    governance --> remediation["Intent Update / Remediation"]
    remediation --> intent

    publication_overlay["Publication overlay:<br/>Lifecycle role applied to canonical classes at the integration boundary.<br/>Not an artifact class or separate stage."]
    publication_overlay -.-> publication

    projection_overlay["Projection overlay:<br/>Derived representational posture.<br/>Fed by compiled, observed, and assessed material.<br/>Not a stage, state, or artifact class."]
    compilation -.-> projection_overlay
    observation -.-> projection_overlay
    assessment -.-> projection_overlay
```

Early lifecycle segments are dominated by authored normative intent,
implementation truth, and proof results. Later lifecycle segments include
derived integration-state, evidence, reports, and projections. This is a
posture distinction across the lifecycle, not a new lifecycle partition or
taxonomy.

This diagram is a projection of the canonical lifecycle defined in ADR-040. If
this figure and ADR-040 ever differ, ADR-040 is authoritative and this diagram
must be updated.

## Lifecycle Stages

| Stage | Description | Responsible repository | Artifact classes present | Authority type | Inputs | Outputs | Entry criteria | Exit criteria | Primary state result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Intent Definition | Normative intent is written and accepted through ADRs, invariants, contracts, and canonical doctrine. Doctrine often speaks of contract authority, invariant surfaces, and architecture decisions rather than "intent definition" as a stage label. | `ste-spec` | Normative, Orientation | Normative Authority | Prior doctrine, change need, accepted constraints | ADRs, invariants, contracts, doctrine updates | Need for new or revised intent is identified | Accepted authoritative intent exists in accepted doctrine or accepted contract shape | Accepted |
| Implementation | Executable behavior is realized in repository source. Doctrine defines this as versioned implementation truth rather than normative authority. | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` | Implementation | Implementation Truth | Accepted doctrine and repository-local implementation work | Source changes and executable logic | Accepted intent exists for the affected scope | Implementation exists as versioned source and is ready for proof / verification | Implemented |
| Proof / Verification | Proof logic verifies or certifies expected behavior. Doctrine uses "Proof Logic", validation, and deterministic baselines rather than one universal verification stage label. | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` | Proof Logic, Reports | Proof Authority | Accepted doctrine, implementation source, proof harnesses | Tests, deterministic baselines, proof outcomes, validation summaries | Implementation or doctrine requiring proof is present | Verification outcome exists and the verified scope is ready for publication / integration input | Verified |
| Publication / Integration Input | Contract-backed publication surfaces expose fragments and evidence to the integration boundary. Publication is a lifecycle role applied to canonical classes; it does not create a new artifact class. | `adr-architecture-kit`, `ste-spec`, `ste-runtime`, `ste-rules-library` | Derived, Evidence, Normative | Derived Artifact, Observational Authority | Published fragments, `ArchitectureEvidence`, contract-backed paths | Kernel-consumable fragments and evidence | Declared publication surfaces are available and required proof for the publication surface has completed | Required integration inputs are available to `ste-kernel` for downstream compilation | Published |
| Architecture IR Compilation | `ste-kernel` loads, merges, and validates a compiled IR candidate from publication inputs. Doctrine speaks of merge, validation, and `Compiled_IR_Document` semantics. | `ste-kernel` | Derived | Derived Artifact | Publication surfaces, merge policy, pinned IR contract references | Validated `Compiled_IR_Document` or fail-closed boot failure | Required inputs are loaded | Validated compiled integration-state exists or boot aborts fail-closed | Compiled |
| Admission Decision | `ste-kernel` projects the admission slice and emits the caller-facing admission decision. Doctrine uses "admission evaluation" and `KernelAdmissionAssessment`. | `ste-kernel` | Derived | Decision Authority (Admission) | Validated IR snapshot, projected admission slice, policy context | `KernelAdmissionAssessment` | Validated IR exists; admission has not yet run | Caller-facing admission output exists or execution is blocked | Admitted |
| Runtime Execution | Runtime performs execution work within its repository boundary. Doctrine places runtime as execution and evidence production only. | `ste-runtime` | Implementation, Evidence | Implementation Truth, Observational Authority | Runtime implementation, admitted or operative runtime path, runtime context | Runtime activity and factual observations | Runtime execution path is invoked from an admitted or operative path | Execution has occurred and runtime facts are ready to be emitted as evidence | Executed |
| Observation (Evidence) | Runtime produces factual evidence only. Doctrine uses `ArchitectureEvidence`, runtime evidence, bundle health, and freshness. | `ste-runtime` | Evidence | Observational Authority (Evidence) | Runtime execution facts, bundle health, freshness state | `ArchitectureEvidence` and related factual observations | Runtime has observable facts to report | Evidence exists without caller-facing decision semantics and is ready for assessment | Observed |
| Assessment (Reports) | Validation, review, and assessment outputs interpret evidence and compiled or projected material. Projection is a representational posture generated from compiled, observed, or assessed material; it is not a state-bearing class. | `ste-kernel`, `ste-rules-library`, governance-side consumers | Reports, Derived | Interpretive Output (Reports) | Evidence, compiled IR, projections, review inputs | Assessments, validation summaries, reviews, report outputs | Evidence or compiled/projected material is available | Interpretive outputs exist and are ready for governance consumption | Assessed |
| Governance Decision | Governance review, override, and remediation decide how unresolved issues are accepted, deferred, or corrected. Accepted doctrine is strongest in the Architecture IR governance model and does not promote draft governance-decision contracts in this tranche. | `ste-spec`, `ste-rules-library`, governance-side consumers | Normative, Reports, Internal | Governance Authority | Reviews, unresolved gaps, override and remediation inputs | Overrides, remediation records, accepted governance outcomes | Assessment or review has produced governance-relevant findings | Governance outcome is explicit and recorded for the next cycle | Remediated |
| Intent Update / Remediation | Governance feedback modifies authoritative intent or drives corrective implementation work for the next cycle. Doctrine uses the Architecture Index feedback loop and remediation ledger rather than one fixed title for this stage. | `ste-spec` with affected implementation repositories | Normative, Implementation, Proof Logic, Internal | Governance Authority leading back to Normative Authority | Governance outcome, remediation work, next-cycle architecture inputs | Updated doctrine, supersession, implementation follow-up | Governance outcome requires doctrine or implementation change | Next-cycle intent is re-entered in Drafted or Accepted form in the authoritative layer | Drafted or Accepted |

## Stage Notes

- `Publication` is a lifecycle role applied to canonical classes. It marks
  declared boundary material as available for integration input and downstream
  compilation.
- `Assessment (Reports)` includes report-like and review-like outputs already
  present in accepted doctrine. Those outputs remain interpretive rather than
  caller-facing admission artifacts.
- `Projection` is a derived representational posture generated from compiled,
  observed, or assessed material. It is not a state-bearing class or taxonomy
  class.
- `Governance Decision` is limited to accepted review, override, remediation,
  and governance-loop doctrine. Draft governance-decision contracts are not
  promoted here.

## Stage and State Interpretation

- Lifecycle stages describe ordered system segments.
- Spine lifecycle states describe readiness or result posture within that
  ordered system.
- Conformance states are an execution-eligibility overlay on top of the locked
  Spine lifecycle states. They do not replace those states.
- Stage completion does not change authority ownership. It changes what
  downstream work is eligible to occur.
- Evidence and lifecycle feedback use a conformance-state overlay on top of the
  locked Spine states. That overlay affects execution eligibility without
  replacing the canonical Spine lifecycle.
- The same System may occupy different lifecycle and conformance postures in
  different Environments because evaluation is instance-scoped.

## Related Documents

- [`STE-Spine-Extracted-Doctrine.md`](./STE-Spine-Extracted-Doctrine.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`STE-Spine-Artifact-Mapping.md`](./STE-Spine-Artifact-Mapping.md)
- [`STE-Spine-State-Model.md`](./STE-Spine-State-Model.md)
- [`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
