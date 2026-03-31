# STE Spine State Model

## Purpose and Scope

This document is normative supporting doctrine for the STE Spine system
lifecycle state model.

## Authority Boundary

This document supports
[`../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`](../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md)
and uses ADR-040 for Spine-local terminology.

ADR-040 remains canonical for the Spine lifecycle and authority-transition
model. This document is a system lifecycle framing, not a universal
single-artifact state machine. Where accepted doctrine
already defines narrower lifecycle states, such as the Architecture IR record
states in
[`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md),
this document maps rather than replaces them.

## Core Model

### State List

| State | Meaning | Affects authority? | Affects canonicity? | Permits downstream generation / derivation? |
| --- | --- | --- | --- | --- |
| Drafted | Intent or corrective intent is written but not yet authoritative. | No. State never reassigns repository authority ownership. | No. Draft material is not current accepted intent. | No. Drafted intent does not authorize downstream implementation, proof, or publication as accepted Spine output. |
| Accepted | Intent is authoritative for its scope. | No. It does not change who owns normative authority. | Yes, for current normative applicability within that scope. | Yes. Accepted intent authorizes downstream implementation, proof, and publication work. |
| Implemented | Executable logic exists in implementation repositories. | No. | No. | Yes. Implemented scope is ready for proof / verification. |
| Verified | Proof logic has produced a verification outcome. | No. | No. | Yes. Verified scope is ready for publication / integration input. |
| Published | Integration artifacts are available through declared publication surfaces. | No. | No. Published material remains non-authoritative unless separately designated by doctrine. | Yes. Published inputs are ready for compilation. |
| Compiled | Architecture IR inputs have been merged into validated compiled integration-state. | No. | No. Compiled state does not replace canonical semantic authority. | Yes. Compiled state is ready for admission evaluation and downstream projection. |
| Admitted | Kernel caller-facing admission decision has been produced. | No. | No. | Yes. Admitted or operative runtime path is ready for execution. |
| Executed | Runtime execution has occurred. | No. | No. | Yes. Executed runtime facts are ready to be emitted as evidence. |
| Observed | Runtime evidence has been produced. | No. Observational authority exists within the evidence boundary, but ownership does not change. | No. | Yes. Evidence is ready for assessment and governance input. |
| Assessed | Report, validation, or review outputs have been produced. | No. Reports remain interpretive and non-authoritative. | No. | Yes. Assessment outputs are ready for governance decision. |
| Remediated | Governance outcome has required or recorded corrective action. | No. | No. | Yes. Remediation is ready to feed the next cycle into Drafted or Accepted intent. |
| Superseded | Earlier authoritative intent has been replaced. | No. | Yes, by ending current normative applicability of the earlier accepted intent. | No. Superseded intent does not act as the current accepted basis for new downstream work. |

### State Applicability By Artifact Class

| Artifact class or lifecycle segment | Valid states | Invalid / not used |
| --- | --- | --- |
| Normative | Drafted, Accepted, Superseded | Implemented, Verified, Published, Compiled, Admitted, Executed, Observed, Assessed, Remediated |
| Implementation | Implemented | Drafted, Accepted, Verified, Published, Compiled, Admitted, Executed, Observed, Assessed, Remediated, Superseded |
| Proof Logic | Verified | Drafted, Accepted, Implemented, Published, Compiled, Admitted, Executed, Observed, Assessed, Remediated, Superseded |
| Derived | Published, Compiled, Admitted | Drafted, Accepted, Implemented, Verified, Executed, Observed, Assessed, Remediated, Superseded |
| Runtime execution segment | Executed | Drafted, Accepted, Implemented, Verified, Published, Compiled, Admitted, Observed, Assessed, Remediated, Superseded |
| Evidence | Observed | Drafted, Accepted, Implemented, Verified, Published, Compiled, Admitted, Executed, Assessed, Remediated, Superseded |
| Reports | Assessed | Drafted, Accepted, Implemented, Verified, Published, Compiled, Admitted, Executed, Observed, Remediated, Superseded |
| Internal governance / remediation material | Remediated | Drafted, Accepted, Implemented, Verified, Published, Compiled, Admitted, Executed, Observed, Assessed, Superseded |
| Orientation | Not a primary state driver in the public authority chain | All lifecycle states as authoritative progression markers |

### Required Mapping Notes

- Normative: Drafted -> Accepted -> Superseded
- Implementation: Implemented -> Verified
- Derived: Published -> Compiled
- Runtime: Executed -> Observed
- Reports: Assessed
- Governance: Remediated -> Intent Update

The state list is broader than the accepted Architecture IR record lifecycle.
Accepted IR record states map at this lifecycle level as follows:

- `proposed` -> Drafted
- `active` -> Accepted
- `deprecated` -> transitional retirement posture prior to Superseded
- `superseded` -> Superseded

### Transition Conditions

| Transition | Allowed? | Preconditions | Result | Notes |
| --- | --- | --- | --- | --- |
| Drafted -> Accepted | Yes | Governance or acceptance process has established authoritative intent for scope. | Intent becomes authoritative for its scope. | This is the normative acceptance transition. |
| Accepted -> Implemented | Yes | Accepted intent exists for the affected scope. | Implementation exists as executable source. | This does not change normative authority ownership. |
| Implemented -> Verified | Yes | Required proof / verification has been run on the implemented scope. | Verification outcome exists. | Proof output exists but does not elevate implementation to normative authority. |
| Verified -> Published | Yes | Relevant publication surface is declared and required proof for that publication surface has completed. | Declared integration inputs are available. | Publication is a lifecycle role, not a new artifact class. |
| Published -> Compiled | Yes | Required published inputs are available and kernel validation runs on them. | Validated compiled integration-state exists. | Invalid inputs fail closed before a compiled state is established. |
| Compiled -> Admitted | Yes | Validated compiled integration-state exists and admission evaluation is run on it. | Caller-facing admission output exists. | Admission must run only on validated compiled state. |
| Admitted -> Executed | Yes | An admitted or operative runtime path is invoked. | Runtime execution occurs. | Execution does not itself produce evidence until `Observed`. |
| Executed -> Observed | Yes | Runtime has factual observations to emit. | Evidence exists. | This is the evidence-production transition. |
| Observed -> Assessed | Yes | Assessment is invoked on available evidence or compiled/projected material. | Interpretive outputs exist. | Assessment remains non-authoritative. |
| Assessed -> Remediated | Yes | Governance records a corrective action or explicit disposition. | Remediation or governance outcome is recorded. | This is the governance-response transition. |
| Remediated -> Drafted | Yes | Next-cycle corrective intent is recorded but not yet accepted. | New intent re-enters the lifecycle as drafted. | This starts the next cycle without immediate acceptance. |
| Remediated -> Accepted | Yes | Corrective or updated intent is accepted directly into authoritative doctrine. | New accepted intent exists. | This starts the next cycle in accepted form. |
| Accepted -> Superseded | Yes | Later accepted intent has replaced the earlier accepted intent for that scope. | Earlier accepted intent is no longer current. | Supersession applies to normative intent, not implementation state. |

### Conformance State Overlay

These conformance states apply to execution-eligible scope. They do not replace
the canonical Spine lifecycle states in ADR-040.

| Conformance state | Meaning | Execution allowed? | Remediation required? | Relationship to Spine state |
| --- | --- | --- | --- | --- |
| Accepted | Accepted intent exists for the scope. | No. | No. | Aligns to accepted normative intent, not runtime readiness. |
| Implemented | Implementation exists for the scope but conformance is not yet verified. | No. | No. | Aligns to the existing `Implemented` Spine state. |
| Verified | Required proof and/or evidence confirms conformance for the active scope. | Yes. | No. | Aligns to the existing `Verified` Spine readiness plus current valid evidence where required by the execution path. |
| Divergent | Evidence or event indicates drift from accepted or previously verified expectations for a known subject. | No. | Yes. | Overlays `Observed` / `Assessed`; it does not create a new Spine state. |
| Non-conformant | Assessed divergence is confirmed as violating an accepted requirement, invariant, rule, or architecture constraint. | No. | Yes. | Overlays `Assessed` / `Remediated`; it does not create a new Spine state. |
| Suspended | Execution is explicitly blocked pending remediation and re-verification. | No. | Yes. | Overlays governance-enforced blocking status; it does not create a new Spine state. |
| Retired | The scope is no longer intended for execution because it has been superseded or formally retired. | No. | No, to remain retired. | Overlays governance retirement or supersession; return requires a new accepted scope, not a direct state flip back into active execution. |

These conformance states are distinct from `Drafted`, `Accepted`,
`Implemented`, `Verified`, `Published`, `Compiled`, `Admitted`, `Executed`,
`Observed`, `Assessed`, `Remediated`, and `Superseded` as Spine lifecycle
states. They are also distinct from the canonical cognitive divergence taxonomy
in `invariants/STE-Divergence-Taxonomy.md`.

### Lifecycle Feedback Transition Table

| Current conformance state | Evidence or event | Resulting conformance state | Underlying Spine feedback stage | Execution allowed in resulting state? |
| --- | --- | --- | --- | --- |
| Accepted | Implementation is realized for the scope. | Implemented | Implementation | No |
| Implemented | Required proof and/or conformant evidence validates the scope. | Verified | Proof / Verification, then Observation (Evidence) / Assessment (Reports) as applicable | Yes |
| Verified | Current conformant evidence remains valid for the scope. | Verified | Observation (Evidence) / Assessment (Reports) | Yes |
| Verified | Drift is detected from accepted or previously verified expectation. | Divergent | Observation (Evidence) / Assessment (Reports) | No |
| Divergent | Assessment clears the issue and conformant evidence is present. | Verified | Assessment (Reports) | Yes |
| Divergent | Assessment confirms a violation. | Non-conformant | Assessment (Reports) | No |
| Non-conformant | Governance or enforcement blocks active execution. | Suspended | Remediated | No |
| Non-conformant | Remediation completes and proof/evidence reconfirms conformance. | Verified | Remediated, then next-cycle verification completes | Yes |
| Suspended | Remediation is accepted and proof/evidence reconfirms conformance. | Verified | Remediated, then next-cycle verification completes | Yes |
| Accepted, Implemented, Verified, Divergent, Non-conformant, Suspended | Retirement or supersession event occurs. | Retired | Governance Decision / Intent Update / Remediation | No |

## Interpretation Notes

### Escalation Definitions

- `Drift` is a detectable mismatch, staleness signal, or evidence conflict
  against expected state. It is an event or signal, not a conformance state.
- `Divergence` is classified drift affecting a known subject and requiring
  assessment. It is represented in this model by the `Divergent` conformance
  state.
- `Non-conformance` is assessed divergence confirmed as violating accepted
  doctrine, proof, rule, or constraint. It is represented in this model by the
  `Non-conformant` conformance state.
- `Suspension` is an execution-blocking disposition applied after
  non-conformance or equivalent blocking governance disposition. It is
  represented in this model by the `Suspended` conformance state.

This escalation model applies to runtime/kernel evidence and lifecycle
feedback. It does not replace or rename the cognitive/documentation-state
divergence taxonomy in `invariants/STE-Divergence-Taxonomy.md`.

### Invalid or Undefined Transitions

- Any transition not listed as allowed is undefined at the Spine system
  lifecycle level.
- The model does not imply `Implemented -> Published` without `Verified`.
- The model does not imply `Observed -> Remediated` without `Assessed`.
- The model does not imply `Compiled -> Executed` without `Admitted`.
- The model does not imply `Drafted -> Superseded`.
- The model does not imply `Implemented -> Superseded`.
- Any conformance transition not listed in the Lifecycle Feedback Transition
  Table is undefined.
- Conformance transitions do not replace the underlying Spine transitions.
- A scope does not move directly from `Divergent` to `Suspended` without
  `Non-conformant`.
- A `Retired` scope does not return to execution eligibility without a new
  accepted scope entering the lifecycle.

### Notes

- Detailed artifact placement and direct kernel input mapping are explained in
  [`STE-Spine-Artifact-Mapping.md`](./STE-Spine-Artifact-Mapping.md).
- `Lifecycle stage`, `Spine lifecycle state`, and `conformance state` are
  distinct terms in this model.
- Lifecycle state affects readiness and applicability within the Spine model.
- Conformance overlay state affects execution eligibility for evaluated scope.
- Authority ownership determines who governs truth and accepted transitions.
- Canonical status is orthogonal to state; a state change does not by itself
  make a surface canonical or derived.
- Spine lifecycle state and conformance overlay state apply to the evaluated
  System Instance or evaluated scope, not to an abstract System detached from
  Environment.
- Not every artifact class traverses every state.
- `Published`, `Compiled`, and `Admitted` are integration and admission states,
  not states of every repository artifact.
- `Assessed` covers report, validation, and review outputs already present in
  accepted doctrine.
- `Admitted` names the state of the derived caller-facing admission output.
  Interpretive reports about admission remain in `Assessed`.
- Evidence-driven non-conformance and incident outcomes are enforcement
  statuses and governance triggers layered on this state model. They are not
  additional lifecycle states.
- State changes do not reassign repository authority ownership.
- `Remediated` names the governance-response segment of the loop. It does not
  imply that all remediation is complete; it means corrective action is
  explicitly recorded and feeding the next cycle.

## Related Documents

- [`STE-Spine-Lifecycle.md`](./STE-Spine-Lifecycle.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`STE-Spine-Extracted-Doctrine.md`](./STE-Spine-Extracted-Doctrine.md)
- [`../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`](../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md)
