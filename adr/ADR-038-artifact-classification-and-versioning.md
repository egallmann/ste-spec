# ADR-038: Artifact Classification and Versioning

## Status

Accepted

## Context

Existing `ste-spec` doctrine already distinguishes documentation-state,
integration-state, runtime evidence, repository boundaries, contract authority,
and Architecture IR authority.

This ADR establishes a binding system decision for artifact classification and
version-control posture across STE repositories. Without that decision,
repositories could drift in what they treat as source truth, regenerable
output, runtime evidence, and reports.

## Decision

STE formally classifies artifacts according to
`architecture/STE-Artifact-Classification-and-Versioning.md`.

Version-control posture is defined by artifact class, not by repository, tool,
or team preference.

STE artifact classes include at minimum:

- Normative
- Implementation
- Proof Logic
- Derived
- Evidence
- Reports
- Orientation
- Internal

Repositories MUST use the doctrine in
`architecture/STE-Artifact-Classification-and-Versioning.md` when determining
version-control posture.

This ADR defines artifact classification posture, the
authority-versus-versioning distinction, and the reproducibility expectation.
It does not redefine contract authority or Architecture IR authority. The
architecture document is the detailed doctrine model.

## Authority and Precedence

This ADR is the canonical authority for STE artifact taxonomy and versioning
posture.

Spine doctrine may map these classes into lifecycle stages, authority
categories, and state transitions, but it must not redefine the taxonomy or
change class posture established here.

If a supporting Spine document appears to imply a new artifact class, altered
class boundary, or different versioning posture, this ADR controls.

## Lifecycle Placement in the STE Spine

This ADR applies across the full STE Spine by classifying which artifact
families participate in Intent Definition, Implementation, Proof /
Verification, Publication / Integration Input, Architecture IR Compilation,
Admission Decision, Observation (Evidence), Assessment (Reports), and
Governance Decision without defining the lifecycle sequence or state machine
itself.

## Relationship to the STE Spine

ADR-040 is the canonical definition of the STE Spine lifecycle and
authority-transition model. This ADR remains the canonical taxonomy and
versioning posture authority that the Spine uses.

## Terminology Boundary

In this ADR, `artifact` means a member of the STE artifact taxonomy.

`derived` means the canonical `Derived` artifact class and posture defined by
this taxonomy. It is not a loose synonym for any produced output.

`publication artifact` remains an exception label or posture applied by
doctrine. It does not create a new top-level artifact class.

`projection` and `view` are not artifact classes in this ADR.

## Rules

- Normative artifacts MUST be versioned.
- Implementation artifacts MUST be versioned.
- Proof Logic artifacts MUST be versioned.
- Deterministic baselines MUST be versioned as Proof Logic.
- Derived artifacts MUST NOT be routinely versioned if reproducible.
- Evidence artifacts MUST NOT be routinely versioned.
- Reports MUST NOT be routinely versioned.
- Orientation artifacts SHOULD be versioned.
- Internal artifacts MAY be versioned but are not normative.

Version-control status does not determine authority.
Authority is defined by doctrine, ADRs, and contracts.
Committing a generated artifact does not make it authoritative.
Some authoritative artifacts, such as runtime evidence within its boundary, are
not routine repository source truth.
Some versioned artifacts, such as README, are not normative authority.

## Reproducibility Requirement

A clean clone of authoritative STE repositories plus documented build and proof
commands MUST be sufficient to regenerate intentionally unversioned derived
artifacts, runtime evidence artifacts, and reports.

## Exceptions

The primary explicit exceptions are:

- publication artifacts
- deterministic proof baselines

These are versioned by deliberate designation, not by default derivation
status. They are versioned because doctrine or contract treats them as
designated outputs or proof inputs, not because they are merely derived.

## Non-Goals

This ADR does not:

- define CI enforcement
- define `.gitignore` contents
- define build pipelines
- define runtime behavior
- define Architecture IR schema
- define contract formats
- restructure repositories

## Compliance Interpretation

A repository aligned with this ADR should be able to answer "yes" to questions
such as:

- are normative artifacts versioned?
- is implementation source versioned?
- is proof logic versioned?
- are compiled or other regenerable derived artifacts excluded from routine
  version control?
- are runtime evidence and reports excluded from routine version control?
- can a clean clone regenerate intended unversioned derived artifacts and
  reports?

## Rationale

This decision separates source truth from compiled and observed outputs,
supports reproducibility and certification discipline, and preserves existing
authority boundaries instead of collapsing them into version-control status.

## Consequences

- Future repository cleanup can align to this doctrine.
- Publication artifacts and deterministic baselines remain explicit exceptions.
- Generated outputs do not become authoritative by being committed.
- No runtime or contract behavior changes are introduced.

## Related Documents

- [`ADR-030-contract-authority-in-ste-spec.md`](ADR-030-contract-authority-in-ste-spec.md)
- [`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
- [`../architecture/STE-Artifact-Classification-and-Versioning.md`](../architecture/STE-Artifact-Classification-and-Versioning.md)
- [`../architecture/STE-Canonical-Project-Artifacts.md`](../architecture/STE-Canonical-Project-Artifacts.md)
- [`../architecture/STE-Determinism-and-Canonical-Identity.md`](../architecture/STE-Determinism-and-Canonical-Identity.md)
- [`../architecture/STE-System-Components-and-Responsibilities.md`](../architecture/STE-System-Components-and-Responsibilities.md)
- [`../contracts/README.md`](../contracts/README.md)
