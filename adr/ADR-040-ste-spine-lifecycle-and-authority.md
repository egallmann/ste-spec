# ADR-040: STE Spine Lifecycle and Authority

## Status

Accepted

## Context

Accepted `ste-spec` doctrine already defines the major parts of the STE
lifecycle and authority model across multiple surfaces:

- normative intent and contract authority in `ste-spec`
- implementation and proof truth in implementation repositories
- publication surfaces into the integration boundary
- Architecture IR semantic authority in `ste-spec`
- compiled IR as kernel-derived integration-state
- kernel admission authority
- runtime evidence production
- reports and projections as non-authoritative outputs
- governance review, override, remediation, and feedback loops

What is missing is one explicit canonical statement of the end-to-end Spine.
Readers can reconstruct the lifecycle from accepted doctrine, but they must join
multiple viewpoints to do so.

This ADR consolidates that implicit model into one canonical lifecycle and
authority-transition definition. It does not redefine:

- artifact taxonomy from ADR-038
- Architecture IR ontology from ADR-035
- runtime versus kernel boundary from ADR-031
- contract authority from ADR-030
- runtime or kernel behavior
- repository responsibilities
- draft governance artifacts as normative status

## Authority and Precedence

This ADR is the canonical definition of the STE Spine lifecycle and
authority-transition model.

ADR-038 remains the canonical artifact taxonomy and versioning posture
authority used by the Spine.

The supporting Spine documents in `architecture/` are normative supporting
doctrine where they explain, map, or summarize this ADR. They do not override
this ADR, and they do not redefine ADR-038 taxonomy.

Analysis-oriented Spine material is non-normative and does not define doctrine.

If wording appears to conflict:

- ADR-040 controls for Spine lifecycle and authority-transition definition
- ADR-038 controls for artifact taxonomy and versioning posture
- supporting Spine doctrine follows those ADRs
- analysis-only material yields to accepted doctrine and supporting doctrine

## Decision

STE defines the **Spine** as the canonical lifecycle and authority-transition
model connecting:

- normative intent
- implementation
- proof / verification
- publication / integration input
- Architecture IR compilation
- admission decision
- runtime execution
- observation through evidence
- assessment through reports and review
- governance decision
- intent update / remediation

### 1. Lifecycle stages

The canonical Spine lifecycle stages are:

1. Intent Definition
2. Implementation
3. Proof / Verification
4. Publication / Integration Input
5. Architecture IR Compilation
6. Admission Decision
7. Runtime Execution
8. Observation (Evidence)
9. Assessment (Reports)
10. Governance Decision
11. Intent Update / Remediation

These stage names provide one explicit end-to-end vocabulary for the lifecycle.
Where accepted source doctrine uses narrower or different terminology, those
source terms remain valid within their original documents.

### 2. Authority model

The Spine uses the following authority categories:

- **Normative Authority**: accepted doctrine, contracts, invariants, and other
  authoritative intent published in `ste-spec`
- **Implementation Truth**: executable source truth in implementation
  repositories
- **Proof Authority**: versioned proof inputs and expected outcomes
- **Derived Artifact (Non-Authoritative)**: generated outputs derived from
  authoritative inputs
- **Observational Authority (Evidence)**: factual runtime observations
- **Interpretive Output (Reports)**: assessments, summaries, diffs, and review
  outputs
- **Decision Authority (Admission)**: caller-facing admission semantics emitted
  by `ste-kernel`
- **Governance Authority**: explicit review, override, remediation, and
  next-cycle steering

Normative authority remains in `ste-spec` doctrine. Implementation truth does
not override normative authority. Runtime evidence is authoritative only as
factual observation within its boundary. Kernel admission output is final
caller-facing decision authority at the runtime/kernel handoff. Compiled IR is
derived integration-state. Reports and projections are non-authoritative.

### 3. Artifact participation in the lifecycle

ADR-038 artifact classes remain canonical:

- Normative
- Implementation
- Proof Logic
- Derived
- Evidence
- Reports
- Orientation
- Internal

This ADR does not add or rename artifact classes.

For Spine modeling:

- `Publication` is a lifecycle role or posture applied to some canonical
  classes, especially Derived outputs and declared boundary surfaces
- `Projection` is a derived representational posture
- `Report` maps to the canonical `Reports` class

Artifact participation is:

- Normative artifacts define intent, governance outcomes, and supersession
- Implementation artifacts realize executable behavior
- Proof Logic verifies behavior and defines deterministic expected outcomes
- Derived artifacts carry publication, compiled integration-state, and some
  admission outputs without becoming authoritative by default
- Evidence artifacts record factual runtime observations
- Reports interpret evidence, validation, and projection material
- Orientation artifacts explain and navigate
- Internal artifacts support local planning and remediation without becoming
  public authority

### 4. State transitions

The Spine system lifecycle states are:

- Drafted
- Accepted
- Implemented
- Verified
- Published
- Compiled
- Admitted
- Executed
- Observed
- Assessed
- Remediated
- Superseded

This is a system lifecycle model, not a universal single-artifact state machine.

| State | Meaning | Applicable artifact classes or lifecycle segment | Authority effect | Generation / derivation effect |
| --- | --- | --- | --- | --- |
| Drafted | Normative intent or corrective intent has been written but is not yet authoritative for its scope. | Normative intent work and next-cycle remediation outputs | Does not assign or change authority ownership. | Does not authorize downstream implementation, proof, or publication as accepted Spine output. |
| Accepted | Normative intent is authoritative for its scope. | Normative artifacts | Makes the accepted normative intent authoritative for its scope without changing repository authority ownership. | Authorizes downstream implementation, proof, and publication work against the accepted intent. |
| Implemented | Executable logic exists in implementation repositories for the accepted scope. | Implementation artifacts | Does not elevate implementation to normative authority. | Makes the implementation eligible for proof / verification. |
| Verified | Proof output exists for the implementation or publication surface under review. | Proof Logic and the implementation segment it verifies | Does not elevate implementation to normative authority. | Makes the verified scope eligible for publication / integration input. |
| Published | Declared integration inputs are available through the required publication surfaces. | Derived publication outputs and other declared integration inputs | Does not make Derived artifacts authoritative. | Makes the published inputs eligible for compilation. |
| Compiled | Validated compiled integration-state exists. | Derived compiled integration-state | Does not replace Architecture IR semantic authority or change authority ownership. | Makes the validated compiled state eligible for admission evaluation and downstream projection. |
| Admitted | Caller-facing admission output exists. | Admission decision segment | Does not change normative authority ownership; it establishes the caller-facing decision result at the kernel boundary. | Makes the admitted or operative runtime path eligible for execution. |
| Executed | Runtime execution has occurred for the relevant admitted or operative path. | Runtime execution segment | Does not change authority ownership. | Makes runtime facts eligible to be emitted as evidence. |
| Observed | Factual evidence exists. | Evidence artifacts | Does not change authority ownership; it establishes observational authority within the evidence boundary. | Makes evidence eligible for assessment and governance input. |
| Assessed | Interpretive outputs exist. | Reports and assessment outputs | Does not create normative authority. | Makes assessment results eligible for governance decision. |
| Remediated | Corrective action or governance disposition has been explicitly recorded for the next cycle. | Governance outputs and internal remediation tracking | Does not by itself create new normative authority. | Makes next-cycle intent update eligible to re-enter Drafted or Accepted. |
| Superseded | Earlier accepted normative intent is no longer the current authoritative intent. | Normative artifacts | Ends current applicability of the earlier accepted normative intent without changing authority ownership. | Prevents superseded intent from acting as the current accepted basis for new downstream work. |

Allowed transition constraints are:

- `Drafted -> Accepted`
- `Accepted -> Implemented`
- `Implemented -> Verified`
- `Verified -> Published`
- `Published -> Compiled`
- `Compiled -> Admitted`
- `Admitted -> Executed`
- `Executed -> Observed`
- `Observed -> Assessed`
- `Assessed -> Remediated`
- `Accepted -> Superseded`
- `Remediated -> Drafted`
- `Remediated -> Accepted`

Transitions not named by the Spine are invalid or undefined at this lifecycle
level.

No state change by itself changes canonical authority ownership.

State constrains readiness and eligibility to generate downstream artifacts. It
does not reassign ownership of truth.

Where narrower accepted doctrine already defines local lifecycle states, such as
Architecture IR record states, those local vocabularies remain valid in their
own scope.

### 5. Enforcement points

Enforcement in the Spine occurs primarily at the kernel boundary.

- `ste-kernel` loads required publication-surface inputs
- `ste-kernel` merges and validates IR
- invalid runtime evidence is fail-closed at the kernel boundary
- admission evaluation must run only on validated IR
- closed-object discipline prevents undeclared semantic channels across the
  runtime/kernel handoff

This ADR does not add new enforcement behavior. It consolidates the accepted
enforcement locations already defined by ADR-031, ADR-032, ADR-033, and the
kernel execution model.

### 6. Observation points

Observation occurs in the runtime evidence layer.

- `ste-runtime` produces `ArchitectureEvidence`
- evidence is factual only
- evidence informs freshness, bundle health, and subsequent evaluation
- evidence must not embed caller-facing admission decision semantics

### 7. Assessment points

Assessment occurs after compiled or observed material is available for
interpretation.

Assessment outputs include:

- validation summaries
- reviews
- report outputs
- Architecture Index snapshots and related governance summaries

Assessment outputs are interpretive. They inform governance and review but do
not become normative authority by themselves.

### 8. Governance decision points

Governance decision points occur where accepted doctrine records:

- unresolved gaps
- review outcomes
- overrides
- remediation work
- next-cycle updates to intent

The strongest accepted governance model for this stage is in the Architecture IR
governance loop. Draft governance-decision contracts and draft rule-projection
envelopes remain draft and are not promoted by this ADR.

### 9. Architecture IR role

Architecture IR is the canonical semantic model of the Spine.

- `ste-spec` owns what Architecture IR means
- Architecture IR is the single conceptual graph into which authoritative ADR
  material, implementation attribution, and runtime observations compile
- Architecture IR is broader than any single compiled document instance

### 10. Compiled IR role

Compiled IR is the derived integration-state used by `ste-kernel` for
validation, orchestration, projection, and admission evaluation.

- `ste-kernel` remains the compiler of record for merged, validated
  `Compiled_IR_Document` semantics at the integration boundary
- compiled IR is not the documentation-state source of truth
- mechanical schema, merge order, identity, and compiled enums remain kernel
  authority per the pinned contract references

### 11. Evidence role

Evidence is the observational layer of the Spine.

- evidence is factual only
- evidence is authoritative within its observational boundary
- evidence is input to evaluation, not itself the caller-facing decision

### 12. Report role

Reports are the interpretive layer of the Spine.

- reports summarize, assess, compare, or review
- reports consume authoritative or observed inputs
- reports do not become authoritative because they are useful or versioned

### 13. Projection role

Projection is the representational layer of the Spine.

- canonical diagrams and similar projection artifacts are derived views
- projections are generated from compiled, observed, or assessed material to
  explain lifecycle, authority, flow, and governance state
- projection is a representational posture, not a state family or artifact
  class
- projection generation does not affect authority or canonicity
- projections do not introduce semantics absent from accepted authoritative
  sources

### 14. Feedback loop into intent

The Spine is a loop, not only a one-way pipeline.

Governance feedback from:

- evidence
- validation
- review
- override
- remediation
- Architecture Index publication

feeds the next cycle of intent definition, implementation, proof, and
publication.

### 15. Change categories

The Spine distinguishes these change categories:

- **Normative change**: modifies accepted intent, doctrine, contracts,
  invariants, or other normative authority
- **Implementation change**: modifies executable behavior without by itself
  changing normative authority
- **Proof change**: modifies proof logic, deterministic baselines, or
  verification harnesses
- **Runtime change**: modifies execution or observation behavior within runtime
  responsibilities
- **Projection change**: modifies derived representational views without
  changing authoritative meaning
- **Report change**: modifies interpretive or assessment outputs without
  changing authoritative meaning

## Consequences

- The STE Spine now has one canonical lifecycle and authority definition.
- Supporting Spine documents explain and map this ADR but do not override it.
- ADR-038 remains the canonical taxonomy and versioning authority for Spine
  artifact classes.
- Readers no longer need to reconstruct the full model only by joining multiple
  accepted doctrine sources.
- ADR-038 artifact taxonomy remains unchanged.
- ADR-035 semantic versus mechanical Architecture IR split remains unchanged.
- ADR-030 and ADR-031 boundary authority remains unchanged.
- Runtime and kernel responsibilities remain unchanged.
- Draft governance artifacts remain draft unless separately promoted.

## Related

Supporting doctrine:
- [`../architecture/STE-Spine-Extracted-Doctrine.md`](../architecture/STE-Spine-Extracted-Doctrine.md)
- [`../architecture/STE-Spine-Lifecycle.md`](../architecture/STE-Spine-Lifecycle.md)
- [`../architecture/STE-Spine-Authority.md`](../architecture/STE-Spine-Authority.md)
- [`../architecture/STE-Spine-Artifact-Mapping.md`](../architecture/STE-Spine-Artifact-Mapping.md)
- [`../architecture/STE-Spine-State-Model.md`](../architecture/STE-Spine-State-Model.md)
Canonical related ADRs:
- [`ADR-030-contract-authority-in-ste-spec.md`](./ADR-030-contract-authority-in-ste-spec.md)
- [`ADR-031-runtime-kernel-responsibility-boundary.md`](./ADR-031-runtime-kernel-responsibility-boundary.md)
- [`ADR-032-fail-closed-enforcement-model.md`](./ADR-032-fail-closed-enforcement-model.md)
- [`ADR-033-closed-object-discipline.md`](./ADR-033-closed-object-discipline.md)
- [`ADR-035-architecture-ir-ontology-authority.md`](./ADR-035-architecture-ir-ontology-authority.md)
- [`ADR-038-artifact-classification-and-versioning.md`](./ADR-038-artifact-classification-and-versioning.md)
- [`ADR-039-structured-diagram-format-mermaid.md`](./ADR-039-structured-diagram-format-mermaid.md)
