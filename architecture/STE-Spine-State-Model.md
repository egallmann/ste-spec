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

| State | Meaning |
| --- | --- |
| Drafted | Intent is written but not yet authoritative. |
| Accepted | Intent is authoritative for its scope. |
| Implemented | Executable logic exists in implementation repositories. |
| Verified | Proof logic has produced a verification outcome. |
| Published | Integration artifacts are available through declared publication surfaces. |
| Compiled | Architecture IR inputs have been merged into compiled integration-state. |
| Admitted | Kernel caller-facing admission decision has been produced. |
| Executed | Runtime execution has occurred. |
| Observed | Runtime evidence has been produced. |
| Assessed | Report, validation, or review outputs have been produced. |
| Remediated | Governance outcome has required or recorded corrective action. |
| Superseded | Earlier authoritative intent has been replaced. |

## State Usage By Artifact Class

| Artifact class | Applicable states |
| --- | --- |
| Normative | Drafted, Accepted, Superseded |
| Implementation | Implemented |
| Proof Logic | Verified |
| Derived | Published, Compiled, Admitted |
| Evidence | Observed |
| Reports | Assessed |
| Orientation | Drafted, Accepted, Superseded when tied to the surrounding doctrine cycle, but not as a primary authoritative driver |
| Internal | Remediated and local planning states only; not part of the public authority chain |

## Required Mapping Notes

- Normative: Drafted -> Accepted -> Superseded
- Implementation: Implemented -> Verified
- Derived: Published -> Compiled
- Runtime: Executed -> Observed
- Reports: Assessed
- Governance: Remediated -> Intent Update

The state list is broader than the accepted Architecture IR record lifecycle.
Accepted IR record states map approximately as:

- `proposed` -> Drafted
- `active` -> Accepted
- `deprecated` -> transitional retirement posture prior to Superseded
- `superseded` -> Superseded

## Transition Conditions

| Transition | Requires governance | Requires kernel validation | Requires proof | Produces evidence |
| --- | --- | --- | --- | --- |
| Drafted -> Accepted | Yes | No | No | No |
| Accepted -> Implemented | No | No | No | No |
| Implemented -> Verified | No | No | Yes | No |
| Verified -> Published | No | No | Usually yes, because publication follows implementation and proof discipline, but accepted doctrine does not require one universal proof gate for every published artifact | No |
| Published -> Compiled | No | Yes | No | No |
| Compiled -> Admitted | No | Yes, because admission must run on validated IR only | No | No |
| Admitted -> Executed | No | No | No | Runtime may later produce evidence, but execution alone is not the evidence artifact |
| Executed -> Observed | No | No | No | Yes |
| Observed -> Assessed | Sometimes, when review or governance mechanisms are invoked; not for every report | No | No | No |
| Assessed -> Remediated | Yes | No | No | No |
| Remediated -> Drafted or Accepted | Yes, because remediation feeds back into authoritative intent or accepted corrective work | No | Sometimes, depending on the corrective change | No |
| Accepted -> Superseded | Yes | No | No | No |

## Notes

- Not every artifact class traverses every state.
- `Published`, `Compiled`, and `Admitted` are integration and admission states,
  not states of every repository artifact.
- `Assessed` covers report, validation, and review outputs already present in
  accepted doctrine.
- `Remediated` names the governance-response segment of the loop. It does not
  imply that all remediation is complete; it means corrective action is
  explicitly recorded and feeding the next cycle.

## Related Documents

- [`STE-Spine-Lifecycle.md`](./STE-Spine-Lifecycle.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`STE-Spine-Extracted-Doctrine.md`](./STE-Spine-Extracted-Doctrine.md)
- [`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
