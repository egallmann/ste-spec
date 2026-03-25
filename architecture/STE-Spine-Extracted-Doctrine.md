# STE Spine Extracted Doctrine

## Purpose

This file reconstructs the implicit STE Spine from accepted doctrine only.

It is analysis-only. It does not introduce new runtime behavior, repository
responsibilities, or artifact taxonomy changes.

Primary source set for this extraction:

- [`STE-Manifest.md`](./STE-Manifest.md)
- [`STE-Architecture.md`](./STE-Architecture.md)
- [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)
- [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)
- [`STE-Integration-Model.md`](./STE-Integration-Model.md)
- [`../execution/STE-Kernel-Execution-Model.md`](../execution/STE-Kernel-Execution-Model.md)
- [`../adr/ADR-030-contract-authority-in-ste-spec.md`](../adr/ADR-030-contract-authority-in-ste-spec.md)
- [`../adr/ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md)
- [`../adr/ADR-032-fail-closed-enforcement-model.md`](../adr/ADR-032-fail-closed-enforcement-model.md)
- [`../adr/ADR-033-closed-object-discipline.md`](../adr/ADR-033-closed-object-discipline.md)
- [`../adr/ADR-035-architecture-ir-ontology-authority.md`](../adr/ADR-035-architecture-ir-ontology-authority.md)
- [`../adr/ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md)
- [`../adr/ADR-039-structured-diagram-format-mermaid.md`](../adr/ADR-039-structured-diagram-format-mermaid.md)
- [`../invariants/INV-0001-runtime-evidence-factual-only.md`](../invariants/INV-0001-runtime-evidence-factual-only.md)
- [`../invariants/INV-0002-kernel-final-admission-authority.md`](../invariants/INV-0002-kernel-final-admission-authority.md)

## Doctrine Precedence Used For Extraction

This reconstruction applies the Spine consolidation precedence required for this
tranche:

1. Accepted ADRs
2. Accepted invariants
3. Canonical doctrine documents in `architecture/`
4. Contracts marked normative
5. Execution model documents
6. Integration model documents
7. Orientation documents

Where accepted sources use different terms for the same part of the lifecycle,
this file records the mismatch instead of silently reconciling it.

## Lifecycle Stages Already Described

### Explicitly stated in doctrine

- Normative intent and authority surfaces are declared in
  [`STE-Manifest.md`](./STE-Manifest.md),
  [`ADR-030-contract-authority-in-ste-spec.md`](../adr/ADR-030-contract-authority-in-ste-spec.md),
  and
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md).
- Implementation and proof logic are defined as artifact classes in
  [`ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md)
  and
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md).
- Publication surfaces and integration inputs are defined in
  [`STE-Integration-Model.md`](./STE-Integration-Model.md).
- IR compilation, IR validation, and admission evaluation are defined in
  [`../execution/STE-Kernel-Execution-Model.md`](../execution/STE-Kernel-Execution-Model.md).
- Runtime evidence production is defined in
  [`ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md),
  [`../invariants/INV-0001-runtime-evidence-factual-only.md`](../invariants/INV-0001-runtime-evidence-factual-only.md),
  and
  [`STE-Integration-Model.md`](./STE-Integration-Model.md).
- The Architecture IR control loop explicitly names declared intent, compiled
  model, evidence, validation, gap detection, review, override/remediation, and
  Architecture Index publication in
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md).

### Reconstructed from multiple accepted sources

The following end-to-end Spine can be reconstructed without adding new stages:

1. Intent definition
2. Implementation
3. Proof / verification
4. Publication / integration input
5. Architecture IR compilation
6. Admission decision
7. Runtime execution
8. Observation through evidence
9. Assessment through reports, review, and validation outputs
10. Governance decision
11. Intent update / remediation

This reconstruction is grounded jointly in
[`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md),
[`STE-Integration-Model.md`](./STE-Integration-Model.md),
[`../execution/STE-Kernel-Execution-Model.md`](../execution/STE-Kernel-Execution-Model.md),
and
[`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md).

## Artifact Classes Already Defined

### Explicitly stated in doctrine

Canonical artifact classes are defined by
[`ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md)
and
[`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md):

- Normative
- Implementation
- Proof Logic
- Derived
- Evidence
- Reports
- Orientation
- Internal

### Reconstructed from multiple accepted sources

- Publication is not a top-level artifact class in accepted doctrine. It is an
  exception posture or lifecycle role applied to some derived or contract-backed
  outputs in
  [`ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md),
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md),
  and
  [`STE-Integration-Model.md`](./STE-Integration-Model.md).
- Projection is not a top-level artifact class in accepted doctrine. It is a
  derived representational posture defined in
  [`ADR-039-structured-diagram-format-mermaid.md`](../adr/ADR-039-structured-diagram-format-mermaid.md)
  and
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md).

## Authority Types Already Defined

### Explicitly stated in doctrine

- Contract authority in `ste-spec`:
  [`ADR-030-contract-authority-in-ste-spec.md`](../adr/ADR-030-contract-authority-in-ste-spec.md)
- Runtime evidence versus kernel admission authority:
  [`ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md)
- Fail-closed enforcement at the kernel boundary:
  [`ADR-032-fail-closed-enforcement-model.md`](../adr/ADR-032-fail-closed-enforcement-model.md)
- Architecture IR semantic authority in `ste-spec` with mechanical compiled IR
  authority referenced to `ste-kernel`:
  [`ADR-035-architecture-ir-ontology-authority.md`](../adr/ADR-035-architecture-ir-ontology-authority.md)
- Artifact authority versus versioning posture:
  [`ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md)
- Runtime evidence is factual only:
  [`../invariants/INV-0001-runtime-evidence-factual-only.md`](../invariants/INV-0001-runtime-evidence-factual-only.md)
- Kernel is final caller-facing admission authority:
  [`../invariants/INV-0002-kernel-final-admission-authority.md`](../invariants/INV-0002-kernel-final-admission-authority.md)

### Reconstructed from multiple accepted sources

Accepted doctrine supports these authority categories across the Spine:

- Normative authority
- Implementation truth
- Proof authority
- Derived artifact, non-authoritative by default
- Observational authority for evidence
- Interpretive outputs for reports
- Decision authority for admission
- Governance authority for review, override, and remediation

These categories are distributed across
[`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md),
[`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md),
[`STE-Integration-Model.md`](./STE-Integration-Model.md),
and the accepted ADR and invariant set above.

## Runtime vs Kernel Boundary

### Explicitly stated in doctrine

- `ste-runtime` is an evidence producer only:
  [`ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md)
- `ste-kernel` is the caller-facing admission authority:
  [`ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md),
  [`../invariants/INV-0002-kernel-final-admission-authority.md`](../invariants/INV-0002-kernel-final-admission-authority.md)
- `ste-kernel` is the sole integration orchestrator for merge, IR validation,
  and admission evaluation at the boundary:
  [`STE-Integration-Model.md`](./STE-Integration-Model.md)
- `ste-kernel` alone compiles merged `Compiled_IR_Document` semantics at the
  integration boundary:
  [`../execution/STE-Kernel-Execution-Model.md`](../execution/STE-Kernel-Execution-Model.md)

### Reconstructed from multiple accepted sources

The Spine boundary between runtime and kernel is:

- runtime executes and observes
- kernel loads, compiles, validates, projects, and decides

That reconstruction is directly consistent across
[`ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md),
[`STE-Integration-Model.md`](./STE-Integration-Model.md),
and
[`../execution/STE-Kernel-Execution-Model.md`](../execution/STE-Kernel-Execution-Model.md).

## Evidence vs Decision Boundary

### Explicitly stated in doctrine

- Evidence is factual only and excludes caller-facing decision semantics:
  [`../invariants/INV-0001-runtime-evidence-factual-only.md`](../invariants/INV-0001-runtime-evidence-factual-only.md)
- Kernel alone emits `KernelAdmissionAssessment`:
  [`ADR-031-runtime-kernel-responsibility-boundary.md`](../adr/ADR-031-runtime-kernel-responsibility-boundary.md),
  [`../invariants/INV-0002-kernel-final-admission-authority.md`](../invariants/INV-0002-kernel-final-admission-authority.md)
- Evidence informs freshness and bundle health projection but must not carry
  admission semantics:
  [`STE-Integration-Model.md`](./STE-Integration-Model.md)

### Reconstructed from multiple accepted sources

In the Spine, observation and decision are adjacent but distinct:

- evidence is the observational input
- admission assessment is the caller-facing decision output

Accepted doctrine does not permit those roles to collapse into a single
artifact family.

## Derived vs Authoritative Posture

### Explicitly stated in doctrine

- Derived artifacts are not authoritative by default:
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)
- Evidence may be authoritative as factual observation within its boundary:
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)
- Reports are non-authoritative interpretive outputs:
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)
- `Compiled_IR_Document` is integration-state and must not substitute for
  declared documentation-state:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)

### Reconstructed from multiple accepted sources

The Spine supports a forward authority transition:

- authoritative intent
- executable implementation and proof truth
- derived integration-state
- observational evidence
- interpretive report and review outputs
- governance response feeding back into authoritative intent

## Governance Feedback Loop

### Explicitly stated in doctrine

- The Architecture IR control loop explicitly closes from Architecture Index
  back into the next cycle:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)
- Governance artifacts include review, override, remediation, unresolved
  registry, and Architecture Index publication:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)
- `STE-Architecture.md` describes canonization flow, governance surfaces, and
  invariant lifecycle flow:
  [`STE-Architecture.md`](./STE-Architecture.md)

### Reconstructed from multiple accepted sources

Governance feedback exists as a loop from:

- evidence and validation
- to gaps, review, override, and remediation
- to updated intent and doctrine

Accepted doctrine makes the loop real, but distributed across multiple sources
rather than one Spine definition.

## Architecture IR Role

### Explicitly stated in doctrine

- Architecture IR semantics are canonical in `ste-spec`:
  [`ADR-035-architecture-ir-ontology-authority.md`](../adr/ADR-035-architecture-ir-ontology-authority.md)
- Architecture IR is the single conceptual graph that authoritative ADR
  material, implementation attribution, and runtime observations compile into:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)

### Reconstructed from multiple accepted sources

In the Spine, Architecture IR is the canonical semantic model that bridges:

- intent
- implementation attribution
- evidence
- governance state

It is not identical to any single compiled document instance.

## Compiled IR Role

### Explicitly stated in doctrine

- `ste-kernel` compiles publication surfaces into `Compiled_IR_Document`:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md),
  [`../execution/STE-Kernel-Execution-Model.md`](../execution/STE-Kernel-Execution-Model.md)
- Mechanical schema, merge order, identity, and compiled enums remain referenced
  to `ste-kernel`:
  [`ADR-035-architecture-ir-ontology-authority.md`](../adr/ADR-035-architecture-ir-ontology-authority.md)
- Compiled IR is derived integration-state:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)

### Reconstructed from multiple accepted sources

Compiled IR occupies the integration and admission segment of the Spine. It is:

- required for kernel validation and admission
- derived from published inputs
- not itself the documentation-state source of truth

## Reports Role

### Explicitly stated in doctrine

- Reports are summaries, diffs, assessments, and other analysis outputs:
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)
- Reports are non-authoritative and not routinely versioned:
  [`ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md)
- Reviews and validation outputs are governance inputs inside the Architecture
  IR control loop:
  [`STE-Architecture-Intermediate-Representation.md`](./STE-Architecture-Intermediate-Representation.md)

### Reconstructed from multiple accepted sources

The Spine assessment layer consists of report-like and review-like outputs that
interpret evidence, validation, and projection material without becoming
normative authority.

## Projection Role

### Explicitly stated in doctrine

- Canonical diagrams are structured projection artifacts and representational
  views only:
  [`ADR-039-structured-diagram-format-mermaid.md`](../adr/ADR-039-structured-diagram-format-mermaid.md)
- Projections are derived artifacts, not authoritative architecture intent:
  [`ADR-039-structured-diagram-format-mermaid.md`](../adr/ADR-039-structured-diagram-format-mermaid.md),
  [`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)

### Reconstructed from multiple accepted sources

Projection sits in the Spine as a Derived representational posture used for:

- explanation
- review
- governance
- human-readable lifecycle and architecture views

Projection does not introduce new Spine semantics.

## Conflicts / Terminology Mismatches

- Accepted doctrine defines canonical artifact classes in ADR-038 and does not
  define `Publication` or `Projection` as top-level classes. Spine lifecycle
  modeling therefore treats them as role or posture labels only.
- `STE-Architecture-Intermediate-Representation.md` defines a lifecycle model
  for architecture records with states such as `proposed`, `active`,
  `deprecated`, and `superseded`. The broader Spine state vocabulary used in
  this tranche is a system lifecycle framing and is not already stated in one
  accepted source as a universal artifact state machine.
- Governance decision storage beyond accepted review, override, and remediation
  surfaces is only partially formalized in accepted doctrine. Draft projection
  and governance-decision contracts exist, but they are not promoted by this
  extraction.

## Extraction Summary

Accepted doctrine already defines the major parts of the STE Spine:

- intent and authority surfaces
- implementation and proof truth
- publication and integration inputs
- Architecture IR semantic meaning
- compiled IR as derived integration-state
- kernel admission authority
- runtime evidence production
- reports and projections as non-authoritative outputs
- governance feedback into the next cycle

What is missing prior to this tranche is not the underlying doctrine, but a
single canonical document that makes the full lifecycle and authority-transition
model explicit.

## Related Documents

- [`STE-Spine-Lifecycle.md`](./STE-Spine-Lifecycle.md)
- [`STE-Spine-Authority.md`](./STE-Spine-Authority.md)
- [`STE-Spine-Artifact-Mapping.md`](./STE-Spine-Artifact-Mapping.md)
- [`STE-Spine-State-Model.md`](./STE-Spine-State-Model.md)
- [`../adr/ADR-040-ste-spine-lifecycle-and-authority.md`](../adr/ADR-040-ste-spine-lifecycle-and-authority.md)
