# STE Spine Artifact Mapping

## Purpose and Scope

This document is normative supporting doctrine for applying ADR-038 canonical
artifact classes to the STE Spine lifecycle.

## Authority Boundary

This document supports
[`../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`](../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md)
and explicitly defers taxonomy and versioning authority to
[`../adrs/published/ADR-038-artifact-classification-and-versioning.md`](../adrs/published/ADR-038-artifact-classification-and-versioning.md).

It does not redefine artifact taxonomy. Spine-local term meanings follow
ADR-040. In this document:

- `Publication` = lifecycle role applied to some canonical classes
- `Projection` = derived representational posture
- `Report` = canonical `Reports` class

## Core Model

| Artifact class | What it is | Primary Spine stages | Authority / posture | Can directly produce | Can influence / constrain | Direct kernel input? |
| --- | --- | --- | --- | --- | --- | --- |
| Normative | Accepted doctrine, contracts, schemas, invariants, and other accepted authoritative intent surfaces. | Intent Definition, Governance Decision, Intent Update / Remediation | Authoritative for intent and constraints | Accepted intent, contract surfaces, schema rules, governance outcomes | Implementation, proof, publication, compilation, admission, and governance by defining what is allowed | Yes, when exposed through accepted contract-backed publication surfaces or other accepted normative boundary inputs |
| Implementation | Executable source truth in implementation repositories. | Implementation, Runtime Execution | Authoritative for executable behavior, not normative | Runtime behavior, repository-local execution behavior, attributable observed effects | Proof readiness, evidence production, governance review, and remediation planning | No |
| Proof Logic | Versioned proof inputs, deterministic baselines, and expected outcomes. | Proof / Verification | Authoritative for proof inputs and expected outcomes | Verification outcomes, deterministic baselines, validation summaries | Publication readiness, governance review, and conformance assessment | No |
| Derived | Generated outputs produced from authoritative inputs through declared processes. | Publication / Integration Input, Architecture IR Compilation, Admission Decision, Assessment (Reports) | Non-authoritative by default; may be designated for specific boundary roles without changing class posture | Declared publication inputs, compiled integration-state, `KernelAdmissionAssessment`, generated indices, projections | Compilation, admission, assessment, and governance review without becoming authority by default | Yes, when the derived artifact is the declared integration input, compiled integration-state, or caller-facing admission artifact used at the boundary |
| Evidence | Factual runtime observations emitted within the evidence boundary. | Observation (Evidence) | Authoritative as factual observation within its boundary | `ArchitectureEvidence`, freshness observations, bundle health observations | Admission freshness/evidence checks, assessment, and governance input | Yes |
| Reports | Interpretive outputs derived from authoritative or observed inputs. | Proof / Verification, Assessment (Reports), Governance Decision | Non-authoritative interpretive output | Reviews, validation summaries, certification reports, diff reports | Governance review, remediation prioritization, and human understanding | No |
| Orientation | Navigation and explanatory material that helps readers find or understand authoritative surfaces. | Intent Definition, Assessment (Reports), Intent Update / Remediation | Non-authoritative and indirect | Overviews, manifests, README-like navigation surfaces | Reader understanding and discoverability only | No |
| Internal | Local planning and remediation material that is not public authority. | Governance Decision, Intent Update / Remediation | Non-authoritative | Plans, gap assessments, local design notes | Local remediation work and next-cycle preparation | No |

## Direct vs Indirect Participation

Direct kernel inputs are limited to the boundary-relevant Normative, Derived,
and Evidence artifacts already allowed by accepted doctrine.

Implementation, Proof Logic, Reports, Orientation, and Internal artifacts can
influence or constrain boundary behavior indirectly, but they are not direct
kernel handoff inputs in this model.

Normative, Implementation, Proof Logic, Derived, Evidence, and Reports directly
produce downstream artifacts or outputs in this model. Orientation and Internal
artifacts constrain, explain, or prepare work without acting as direct
boundary outputs.

## Control Loop Mapping

| Lifecycle segment | Primary artifact classes | Primary outputs | Constrains next segment? | Validated by runtime evidence? | Feeds back to intent? |
| --- | --- | --- | --- | --- | --- |
| Intent Definition | Normative, Orientation | Accepted intent, contracts, invariants, doctrine updates | Yes | Indirectly | Yes |
| Implementation | Implementation | Executable behavior and attributable observed effects | Yes | Indirectly | Indirectly |
| Proof / Verification | Proof Logic, Reports | Verification outcomes, baselines, validation summaries | Yes | Indirectly | Indirectly |
| Publication / Integration Input | Normative, Derived, Evidence | Declared publication inputs and boundary evidence surfaces | Yes | Where evidence participates directly | Indirectly |
| Architecture IR Compilation / Admission Decision | Derived | Compiled integration-state and caller-facing admission output | Yes | Indirectly, through later observation and assessment | Indirectly |
| Runtime Execution | Implementation, Evidence | Runtime activity and observable runtime facts | Yes | Directly, through observation | Indirectly |
| Observation (Evidence) | Evidence | `ArchitectureEvidence` and related factual observations | Yes | Directly | Yes |
| Assessment (Reports) | Reports, Derived | Interpretive outputs, reviews, validation summaries | Yes | Yes, through evidence inputs | Yes |
| Governance Decision / Intent Update | Normative, Reports, Internal | Governance outcomes, remediation records, updated intent inputs | Yes | Indirectly, through assessed evidence | Yes |

This loop maps the accepted Spine sequence without adding new stage labels.
When readers use terms such as `Design`, that participation is carried here by
accepted intent definition surfaces and Architecture IR semantics rather than
by a separate Spine stage.

Rule declarations and published rule inputs participate in this model through
the existing taxonomy rather than through a separate `Rules` artifact class.
Accepted rule declarations are part of normative or published boundary
material where doctrine says so. Rule projections and rule-evaluation result
envelopes remain derived and draft/interface-only unless separately promoted.

`Canonical` names the governing source for a subject area, such as ADR-038 for
taxonomy or ADR-040 for the Spine. `Derived` names an artifact class and
posture; it does not mean "less important."

## Interpretation Notes

### Publication

Accepted doctrine uses `publication artifacts` and `publication surfaces` as
role or posture labels, not as top-level artifact classes.

In the Spine, publication is a lifecycle role applied to canonical classes. It
marks declared boundary material as available for integration input and does
not change the underlying canonical class.

### Projection

Accepted doctrine treats projection as a derived representational posture.

In the Spine, projection is generated from compiled, observed, or assessed
material. It is not a lifecycle state, not a taxonomy class, and not an
authoritative surface. A projection is a representational output, not a new
authority surface.

## Related Documents

- [`STE-Spine-Lifecycle.md`](./STE-Spine-Lifecycle.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`](../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md)
