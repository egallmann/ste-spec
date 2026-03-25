# STE Spine Lifecycle

## Purpose

This document is normative supporting doctrine for the STE Spine lifecycle.

It explains and maps the lifecycle defined canonically in
[`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md).
It does not override ADR-040, and it does not redefine artifact taxonomy,
which remains canonical in
[`../adr/ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md).

## Lifecycle Stages

| Stage | Description | Responsible repository | Artifact classes present | Authority type | Inputs | Outputs | Entry criteria | Exit criteria |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Intent Definition | Normative intent is written and accepted through ADRs, invariants, contracts, and canonical doctrine. Doctrine often speaks of contract authority, invariant surfaces, and architecture decisions rather than "intent definition" as a stage label. | `ste-spec` | Normative, Orientation | Normative Authority | Prior doctrine, change need, accepted constraints | ADRs, invariants, contracts, doctrine updates | Need for new or revised intent is identified | Authoritative intent exists in accepted doctrine or accepted contract shape |
| Implementation | Executable behavior is realized in repository source. Doctrine defines this as versioned implementation truth rather than normative authority. | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` | Implementation | Implementation Truth | Accepted doctrine and repository-local implementation work | Source changes and executable logic | Accepted intent exists for the affected scope | Implementation exists as versioned source |
| Proof / Verification | Proof logic verifies or certifies expected behavior. Doctrine uses "Proof Logic", validation, and deterministic baselines rather than one universal verification stage label. | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` | Proof Logic, Reports | Proof Authority | Accepted doctrine, implementation source, proof harnesses | Tests, deterministic baselines, proof outcomes, validation summaries | Implementation or doctrine requiring proof is present | Required proof inputs and checks exist; verification outcome is available |
| Publication / Integration Input | Contract-backed publication surfaces expose fragments and evidence to the integration boundary. Doctrine uses "publication surfaces" and "adapter" language here. | `adr-architecture-kit`, `ste-spec`, `ste-runtime`, `ste-rules-library` | Derived, Evidence, Normative | Derived Artifact, Observational Authority | Published fragments, `ArchitectureEvidence`, contract-backed paths | Kernel-consumable fragments and evidence | Declared publication surfaces are available | Required integration inputs are loadable by `ste-kernel` |
| Architecture IR Compilation | `ste-kernel` loads, merges, and validates a compiled IR candidate from publication inputs. Doctrine speaks of merge, validation, and `Compiled_IR_Document` semantics. | `ste-kernel` | Derived | Derived Artifact | Publication surfaces, merge policy, pinned IR contract references | Validated `Compiled_IR_Document` or fail-closed boot failure | Required inputs are loaded | IR is validated or boot aborts fail-closed |
| Admission Decision | `ste-kernel` projects the admission slice and emits the caller-facing admission decision. Doctrine uses "admission evaluation" and `KernelAdmissionAssessment`. | `ste-kernel` | Derived, Reports | Decision Authority (Admission) | Validated IR snapshot, projected admission slice, policy context | `KernelAdmissionAssessment` | Validated IR exists; admission has not yet run | Caller-facing admission output is emitted or blocked |
| Runtime Execution | Runtime performs execution work within its repository boundary. Doctrine does not redefine runtime behavior here; it places runtime as execution and evidence production only. | `ste-runtime` | Implementation, Evidence | Implementation Truth, Observational Authority | Runtime implementation, runtime context, admitted or operative work | Runtime activity and factual observations | Runtime execution path is invoked | Runtime has produced only factual outputs for the handoff boundary |
| Observation (Evidence) | Runtime produces factual evidence only. Doctrine uses `ArchitectureEvidence`, runtime evidence, bundle health, and freshness. | `ste-runtime` | Evidence | Observational Authority (Evidence) | Runtime execution facts, bundle health, freshness state | `ArchitectureEvidence` and related factual observations | Runtime has observable facts to report | Evidence is emitted without caller-facing decision semantics |
| Assessment (Reports) | Validation, review, and assessment outputs interpret evidence and compiled or projected material. Doctrine uses reports, validation summary, review, and Architecture Index support rather than a single report pipeline. | `ste-kernel`, `ste-rules-library`, governance-side consumers | Reports, Derived, Orientation | Interpretive Output (Reports) | Evidence, compiled IR, projections, review inputs | Assessments, validation summaries, reviews, report outputs | Evidence or compiled/projected material is available | Interpretive outputs exist for governance or review consumption |
| Governance Decision | Governance review, override, and remediation decide how unresolved issues are accepted, deferred, or corrected. Accepted doctrine is strongest in the Architecture IR governance model and does not promote draft governance-decision contracts in this tranche. | `ste-spec`, `ste-rules-library`, governance-side consumers | Normative, Reports, Internal | Governance Authority | Reviews, unresolved gaps, override and remediation inputs | Overrides, remediation records, accepted governance outcomes | Assessment or review has produced governance-relevant findings | Governance outcome is explicit, attributable, and suitable to feed the next cycle |
| Intent Update / Remediation | Governance feedback modifies authoritative intent or drives corrective implementation work. Doctrine uses the Architecture Index feedback loop and remediation ledger rather than one fixed title for this stage. | `ste-spec` with affected implementation repositories | Normative, Implementation, Proof Logic, Internal | Governance Authority leading back to Normative Authority | Governance outcome, remediation work, next-cycle architecture inputs | Updated doctrine, supersession, implementation follow-up | Governance outcome requires doctrine or implementation change | Updated intent, supersession, or remediation work is recorded in the authoritative layer |

## Stage Notes

- `Publication` is treated here as a lifecycle role applied to canonical classes,
  not as a new artifact class.
- `Assessment (Reports)` includes report-like and review-like outputs already
  present in accepted doctrine.
- `Governance Decision` is limited to accepted review, override, remediation,
  and governance-loop doctrine. Draft governance-decision contracts are not
  promoted here.

## Related Documents

- [`STE-Spine-Extracted-Doctrine.md`](./STE-Spine-Extracted-Doctrine.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`STE-Spine-Artifact-Mapping.md`](./STE-Spine-Artifact-Mapping.md)
- [`STE-Spine-State-Model.md`](./STE-Spine-State-Model.md)
- [`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
