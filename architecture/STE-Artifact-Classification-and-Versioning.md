# STE Artifact Classification and Versioning

## Purpose

This document is the canonical doctrine in `ste-spec` for STE artifact
classification, authority posture, version-control posture, and reproducibility
expectations.

It complements existing STE doctrine and does not replace repository-boundary,
contract-authority, or Architecture IR authority documents.

## Scope Boundary

This document defines artifact classification and version-control posture only.
It does not define:

- repository ownership
- contract formats
- Architecture IR schema
- runtime behavior
- build pipelines
- CI enforcement
- publication workflows

Those concerns are governed by other STE doctrine and ADRs. This document
defines artifact classes, authority posture, and versioning posture only.

## Why Artifact Classification Exists in STE

STE requires a clear distinction between source truth and generated state.
Without that distinction, repositories drift toward treating compiled state,
runtime observations, or reports as if they were authority surfaces.

Artifact classification exists in STE to preserve:

- separation of source truth from generated state
- reproducibility without committing routine outputs
- determinism and certification support
- clean-clone reconstruction from authoritative inputs
- stable authority boundaries across repositories

## Definitions

### Authoritative

An artifact that serves as a source of truth for a defined aspect of the
system.

### Normative

An artifact that defines intended behavior, rules, constraints, or doctrine.

### Canonical

The designated primary representation of a concept within a given plane.

### Derived

An artifact generated from authoritative sources through a defined process.
Derived artifacts are not authoritative by default. Some derived artifacts may
be deliberately designated as publication artifacts or deterministic proof
baselines and therefore versioned by explicit doctrine or contract.

### Versioned

Stored in repository source control as part of the system's persistent source
of truth.

### Reproducible

Able to be regenerated deterministically from versioned authoritative inputs and
documented commands.

## Doctrine Precedence

- ADRs define binding governance decisions.
- Architecture documents define doctrinal models and classification.
- Contract documents define canonical handoff formats and surfaces.
- Orientation documents summarize but do not override doctrine.

This document governs artifact classification and version-control posture, but
does not override `ADR-030` or `ADR-035`.

If there is any perceived conflict between this document and another `ste-spec`
document or ADR, the conflict must be resolved through a new ADR. This document
does not silently override existing authority surfaces such as `ADR-030` or
`ADR-035`.

## Relationship to Existing Authority Surfaces

This document is additive and deferential:

- `STE-Canonical-Project-Artifacts.md` remains the documentation-state and
  publication-surface map by repository.
- `STE-Determinism-and-Canonical-Identity.md` remains the determinism and
  canonical identity doctrine for the integration plane.
- `STE-System-Components-and-Responsibilities.md` remains the canonical
  repository-boundary and role-responsibility view.
- `contracts/README.md` remains the canonical summary of cross-component
  contract surfaces and canonical versus derived handoff examples.
- `ADR-030` remains the contract-authority decision.
- `ADR-035` remains the Architecture IR semantic authority decision.

This document does not redefine those surfaces. It classifies artifact classes
and establishes their authority and versioning posture.

## Relationship to STE Planes

STE operates across multiple planes:

- documentation-state
- integration-state
- runtime evidence
- reporting and analysis

The artifact classes defined here apply across those planes. The classification
model defines authority and versioning posture. It does not define where an
artifact is generated.

## Artifact Flow Overview

```text
Normative -> Derived -> Evidence -> Reports
                ^
            Proof Logic
                ^
            Implementation
```

This diagram is conceptual only. It explains why different artifact classes
have different versioning rules. It is not a build pipeline or runtime
sequence.

## Artifact Classes

| Class | Authoritative | Must Be Versioned | Must Be Reproducible | Typical Examples | Primary Producers |
| --- | --- | --- | --- | --- | --- |
| Normative | Yes | Yes | Not primarily a regeneration class | ADRs, invariants, contracts, schemas, canonical doctrine | `ste-spec`, repository authority surfaces |
| Implementation | Yes, for executable behavior | Yes | Yes | kernel source, runtime source, rules-engine source, tooling source | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` |
| Proof Logic | Yes, for proof inputs and expected outcomes | Yes | Yes | tests, scenarios, certification logic, deterministic expected baselines | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` |
| Derived | No by default | No, unless explicitly designated as a publication artifact or proof baseline | Yes | compiled IR, merged IR, generated indices, generated docs, projections | all repositories, depending on workflow |
| Evidence | Yes, as factual observation within its boundary | No | Yes | `ArchitectureEvidence`, runtime observations, freshness snapshots | `ste-runtime` and other evidence-producing systems |
| Reports | No | No | Yes | diffs, assessments, certification reports, coverage outputs | proof and execution tooling |
| Orientation | No, unless another doctrine explicitly says otherwise | Should be versioned | Not necessarily | README, architecture overviews, status docs, navigational manifests | all repositories |
| Internal | No | May be versioned | Not necessarily | plans, gap assessments, internal design notes | repository-local maintainers |

### Normative

Normative artifacts define intended behavior, rules, constraints, or doctrine.
They are authoritative and must be versioned.

Typical examples:

- ADRs
- invariants
- contracts
- schemas
- canonical doctrine documents

Primary producers:

- `ste-spec`
- any repository surface explicitly designated as normative in its own doctrine

### Implementation

Implementation artifacts carry executable or operational logic. They are not
normative doctrine, but they are versioned source truth for implementation
behavior.

Typical examples:

- kernel source code
- runtime source code
- rules-engine source code
- toolkit and validator source code

Primary producers:

- `ste-kernel`
- `ste-runtime`
- `ste-rules-library`
- `adr-architecture-kit`

### Proof Logic

Proof Logic artifacts define how behavior is verified, replayed, or certified.
They must be versioned and reproducible.

Typical examples:

- tests
- scenario definitions
- proof harnesses
- certification logic
- deterministic expected baselines

Primary producers:

- `ste-kernel`
- `ste-runtime`
- `ste-rules-library`
- `adr-architecture-kit`

### Derived

Derived artifacts are generated from authoritative sources through a defined
process. They are not authoritative by default and must not be versioned when
they can be regenerated from versioned source, except where explicit doctrine
or contract designates them as publication artifacts or deterministic proof
baselines.

Typical examples:

- compiled IR
- merged IR
- generated registries and indices
- generated markdown views
- projections

Primary producers:

- repositories that compile or project authoritative inputs

### Evidence

Evidence artifacts are factual observations or runtime-state outputs. They may
be authoritative as observations within their defined boundary, but they are not
routine repository source truth and must not be routinely versioned.

Typical examples:

- `ArchitectureEvidence`
- runtime freshness observations
- runtime bundle health observations

Primary producers:

- `ste-runtime`
- other factual observation systems where defined by contract

### Reports

Reports are summaries, diffs, assessments, or other analysis outputs produced
from authoritative or observed inputs. They are not authoritative and must not
be routinely versioned.

Typical examples:

- certification reports
- diff reports
- assessment outputs
- coverage reports

Primary producers:

- proof tooling
- validation tooling
- execution tooling

### Orientation

Orientation artifacts help readers navigate the system and understand repository
boundaries. They should be versioned, but they do not override normative
surfaces.

Typical examples:

- README
- architecture overviews
- status documents
- navigational manifests

Primary producers:

- all repositories

### Internal

Internal artifacts support planning or local design work. They may be versioned
by repository policy, but they are not normative and must not be treated as
external compatibility authority.

Typical examples:

- plans
- gap assessments
- internal design notes

Primary producers:

- repository-local maintainers

## Authority and Versioning Are Distinct

- Authoritative does not always mean versioned.
- Versioned does not always mean authoritative.
- A derived, evidence, or report artifact does not become authoritative merely
  because it is committed to version control.
- Authority must be explicitly defined by doctrine, ADR, or contract.

Examples:

- Runtime evidence may be authoritative as factual observation, but it is not
  routine repository source truth.
- README is usually versioned, but it is orientation material rather than
  normative authority.
- Kernel and runtime source are versioned implementation truth, but not
  normative doctrine.
- A generated publication artifact is versioned only when explicit doctrine or
  contract assigns it that posture.

## Source of Truth Rule

In STE, repository history must primarily record:

- decisions
- intent
- constraints
- contracts
- implementation logic
- proof logic

Repository history must not primarily record:

- compiled state
- runtime observations
- reports
- transient execution outputs

This is why derived artifacts, runtime evidence, and reports are not routinely
version-controlled.

## Versioning Rules

- Normative artifacts MUST be versioned.
- Implementation artifacts MUST be versioned.
- Proof Logic artifacts and deterministic baselines MUST be versioned.
- Derived artifacts MUST NOT be versioned if they can be regenerated from
  versioned source.
- Evidence artifacts MUST NOT be versioned as routine repository content.
- Reports MUST NOT be versioned.
- Orientation artifacts SHOULD be versioned.
- Internal artifacts MAY be versioned but are not normative.

Deterministic expected baselines used for proof, replay, or certification are
classified as Proof Logic and must be versioned. Although baselines may be
generated artifacts, they are authoritative proof inputs because they define the
expected deterministic outcome that future runs must match. They are versioned
as proof inputs, not as runtime evidence.

A derived artifact may be versioned when doctrine or contract deliberately
designates it as:

- a publication artifact
- a deterministic proof baseline

## Reproducibility Rule

A clean clone of authoritative STE repositories plus documented build and proof
commands must be sufficient to regenerate intentionally unversioned derived
artifacts, runtime evidence artifacts, and reports.

Reproducibility in this doctrine means versioning the authoritative inputs,
implementation logic, and proof logic required to recreate those outputs. It
does not require routine version control of the outputs themselves.

## Repository Responsibilities

### `ste-spec`

`ste-spec` versions normative doctrine, ADRs, invariants, contracts, schemas,
and orientation material. It does not treat runtime evidence, reports, or
routine derived state as repository truth.

### `ste-kernel`

`ste-kernel` versions implementation logic, proof logic, and contract-backed
inputs. It must not treat compiled integration-state, proof outputs, or reports
as routine repository truth, except where explicit doctrine designates a
publication artifact or proof baseline.

### `ste-runtime`

`ste-runtime` versions implementation logic, proof logic, fixtures, and
contract-backed surfaces. Runtime evidence and generated runtime state are not
routine version-controlled truth.

### `ste-rules-library`

`ste-rules-library` versions implementation logic, rule and governance-source
surfaces, proof logic, and any explicit contract-backed publication artifacts.
Routine generated reports and local run outputs are not repository truth.

### `adr-architecture-kit`

`adr-architecture-kit` versions authoring schemas, validators, generators,
implementation logic, and proof logic. Generated outputs are not versioned by
default unless explicitly designated as publication artifacts or compatibility
surfaces.

## Relationship to Determinism and Certification

Proof outputs are not versioned because they are run results, not proof logic.
Reports are not versioned because they are reproducible summaries rather than
source truth.

Compiled IR is not versioned because it is derived integration-state rather
than repository-authored documentation-state. Expected baselines and scenarios
are versioned because they are Proof Logic inputs and determinism anchors for
replay and certification.

This preserves certification as a reproducible discipline: version the logic,
baselines, and source inputs needed to recreate outcomes, not every generated
outcome.

## Non-Goals

This document does not define:

- CI enforcement
- `.gitignore` patterns
- build pipelines
- publication workflows
- runtime behavior
- Architecture IR schema
- contract formats

This document defines classification and doctrine only.

## Doctrine Consistency Test

The classification model defined here must support these outcomes
unambiguously:

- ADRs -> Normative -> Authoritative -> Versioned
- Kernel and runtime source -> Implementation -> Versioned -> Not normative
  doctrine
- Compiled IR -> Derived -> Not versioned
- Runtime evidence -> Evidence -> Not versioned
- Certification reports -> Reports -> Not versioned
- Expected baselines -> Proof Logic -> Versioned
- README -> Orientation -> Versioned -> Not normative
- Plans -> Internal -> May be versioned -> Not normative

## Canon Status

This file is canonical for STE artifact classification and version-control
posture in `ste-spec`.
