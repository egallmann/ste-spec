# STE Spine State Model

## Purpose

This document is normative supporting doctrine for the STE Spine system
lifecycle state model.

It supports
[`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
and does not override the canonical Spine definition. It is a system lifecycle
framing, not a universal single-artifact state machine. Where accepted doctrine
already defines narrower lifecycle states, such as the Architecture IR record
states in
[`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md),
this document maps rather than replaces them.

## State List

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

## State Usage By Artifact Class

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

## Required Mapping Notes

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

## Transition Conditions

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

## Invalid or Undefined Transitions

- Any transition not listed as allowed is undefined at the Spine system
  lifecycle level.
- The model does not imply `Implemented -> Published` without `Verified`.
- The model does not imply `Observed -> Remediated` without `Assessed`.
- The model does not imply `Compiled -> Executed` without `Admitted`.
- The model does not imply `Drafted -> Superseded`.
- The model does not imply `Implemented -> Superseded`.

## Notes

- Detailed artifact placement and direct kernel input mapping are explained in
  [`STE-Spine-Artifact-Mapping.md`](./STE-Spine-Artifact-Mapping.md).
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
- [`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
