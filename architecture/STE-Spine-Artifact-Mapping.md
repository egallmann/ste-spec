# STE Spine Artifact Mapping

## Purpose

This document is normative supporting doctrine for applying ADR-038 canonical
artifact classes to the STE Spine lifecycle.

It supports
[`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
and explicitly defers taxonomy and versioning authority to
[`../adr/ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md).
It does not redefine artifact taxonomy. `Publication` and `Projection` are used
here only as helper labels for Spine modeling:

- `Publication` = lifecycle role applied to some canonical classes
- `Projection` = derived representational posture
- `Report` = canonical `Reports` class

## Artifact Mapping

| Artifact class | Lifecycle stages | Authority level | Versioning posture | Admissible to kernel | Used for governance decisions | Example artifacts |
| --- | --- | --- | --- | --- | --- | --- |
| Normative | Intent Definition, Governance Decision, Intent Update / Remediation | Authoritative | Must be versioned | Yes, when exposed through contract-backed publication surfaces or normative inputs consumed at the boundary | Yes | ADRs, invariants, contracts, schemas, canonical doctrine |
| Implementation | Implementation, Runtime Execution | Authoritative for executable behavior, not normative | Must be versioned | No, not as direct kernel admission input at this boundary | Indirectly, through attribution, proof, and governance review | kernel source, runtime source, rules-engine source, toolkit source |
| Proof Logic | Proof / Verification | Authoritative for proof inputs and expected outcomes | Must be versioned | No, not as direct admission input | Yes, as proof basis and validation input | tests, scenarios, certification logic, deterministic baselines |
| Derived | Publication / Integration Input, Architecture IR Compilation, Admission Decision, Assessment (Reports) | Non-authoritative by default | Must not be routinely versioned unless explicitly designated | Yes, when the derived artifact is the declared integration input or compiled integration-state used by `ste-kernel` | Sometimes, as input to assessment or governance review, but not as authority by itself | compiled IR, merged IR, generated indices, generated docs, projections, designated publication artifacts |
| Evidence | Observation (Evidence) | Authoritative as factual observation within its boundary | Must not be routinely versioned | Yes, `ArchitectureEvidence` is a kernel-consumed handoff artifact | Yes, as factual governance input | `ArchitectureEvidence`, runtime freshness observations, runtime bundle health observations |
| Reports | Assessment (Reports), Governance Decision | Non-authoritative interpretive output | Must not be routinely versioned | No, reports are not the kernel handoff contract for admission | Yes, as interpretive input to review, override, and remediation | assessments, certification reports, diff reports, coverage outputs |
| Orientation | Intent Definition, Assessment (Reports), Intent Update / Remediation | Non-authoritative unless another doctrine explicitly says otherwise | Should be versioned | No | Indirectly, for navigation and explanation only | README, overviews, status docs, manifests |
| Internal | Governance Decision, Intent Update / Remediation | Non-authoritative | May be versioned | No | Yes, for local planning and remediation work, but not as public authority | plans, gap assessments, internal design notes |

## Publication and Projection Notes

### Publication

Accepted doctrine uses `publication artifacts` and `publication surfaces` as
role or posture labels, not as top-level artifact classes.

In the Spine:

- publication most often applies to some Derived outputs
- some Normative contract-backed surfaces also participate in publication or
  integration input
- publication does not change the underlying canonical class

### Projection

Accepted doctrine treats projections as derived representational artifacts.

In the Spine:

- projections are typically a Derived posture rather than a separate artifact
  class
- canonical diagrams are projection artifacts
- projections support explanation, assessment, and governance review
- projections do not become authoritative by being versioned

## Related Documents

- [`STE-Spine-Lifecycle.md`](./STE-Spine-Lifecycle.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
