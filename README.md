# System of Thought Engineering (STE)
## `ste-spec` — Publishable Architectural Specification

`ste-spec` is the publishable architectural specification for the STE system.
STE is an architecture decision system that compiles intent, constraints, and
runtime evidence into a canonical Architecture IR and produces deterministic
admission decisions.

## Purpose

`ste-spec` exists to publish the normative architectural definitions that other
STE repositories and implementations rely on. It is the repository where STE
publishes:

- cross-repository contract shape
- normative invariants and semantic constraints
- architectural decisions and rationale
- semantic Architecture IR doctrine
- multi-repository responsibility and integration boundary guidance

This repository is an authority surface for specification and boundary
definition. It is not an implementation repository.

## Mental Model and Pipeline Position

In the canonical STE pipeline, `ste-spec` primarily serves the `Constraints`
layer and defines parts of the enforcement boundary assignment used by the rest
of the system.

| Layer | Responsibility | Primary Repository |
|------|----------------|--------------------|
| Intent | ADRs and architectural intent | `adr-architecture-kit` and repo-local ADR surfaces |
| Constraints | Spec and invariants | `ste-spec` |
| Governance | Rules and governance artifacts | `ste-rules-library` |
| Evidence | Runtime evidence | `ste-runtime` |
| Decision | Admission and orchestration decisions | `ste-kernel` |
| Enforcement | Components assigned by `ste-spec` | assigned by system design, executed outside `ste-spec` |

`ste-spec` defines what must be true, what boundaries must be preserved, and
how repository and handoff authority is described. It does not itself execute
kernel decisions, runtime evidence generation, or rules-engine behavior.

## Inputs

`ste-spec` primarily consumes architectural authoring and review work rather
than runtime evidence or kernel internals. In practice, that means it takes in:

- converged architectural decisions published under `adr/`
- contract definitions and schema work for cross-repository handoffs
- invariant definitions and semantic rule definitions
- orientation and viewpoint material that explains the published specification
- referenced mechanical Architecture IR pointers where the mechanical contract
  is owned by `ste-kernel`

`ste-spec` does not consume `ArchitectureEvidence` as an operational input and
does not depend on `ste-kernel` internals to function as the specification
authority.

## Outputs

`ste-spec` publishes the following artifact families today:

- `contracts/`
  - normative cross-repository contract shape
  - runtime/kernel handoff schemas
  - spec adapter IR fragments under
    [`contracts/architecture-ir/spec-ir-fragments.json`](contracts/architecture-ir/spec-ir-fragments.json)
- `invariants/`
  - normative semantic constraints and cross-component rules
- `adr/`
  - architectural decisions and rationale
- `architecture/`, `execution/`, `governance/`
  - orientation and viewpoint material
- root specification entrypoints such as `README.md`, `status.md`,
  `scope-and-non-goals.md`, and `glossary.md`

These outputs are intended to be consumed by adjacent STE repositories,
contributors, architectural reviewers, and downstream implementations seeking
the published STE contract and doctrine.

## Responsibilities

`ste-spec` is responsible for:

- normative contract authority for published cross-repository handoff shape
- normative invariant and semantic constraint publication
- architectural decision publication and rationale
- semantic Architecture IR ontology authority
- multi-repository responsibility and integration boundary doctrine
- publication of spec-owned adapter IR fragments consumed by `ste-kernel`

## Non-Responsibilities

`ste-spec` is not responsible for:

- kernel orchestration or admission execution
- runtime extraction or evidence generation
- rules-engine execution or governance adjudication implementation
- repository runtime behavior, deployment procedures, or operator runbooks
- owning the mechanical `Compiled_IR_Document` schema bundle versioned in
  `ste-kernel`
- acting as a tutorial, SDK, or implementation framework

## Authority Boundary

`ste-spec` is authoritative for specification-layer constraints and doctrine. It
defines contracts, invariants, architectural decisions, and semantic
Architecture IR meaning where those authorities have been assigned to this
repository.

`ste-spec` is not authoritative for runtime evidence, admission decisions, or
implementation execution behavior.

Authority split across the STE system:

- Intent
  - authoritative in ADR artifacts and their authoring/publication surfaces,
    including `adr-architecture-kit` and repository-local ADR corpora
- Constraints
  - authoritative in `ste-spec`
- Governance
  - authoritative on the rules-engine side in `ste-rules-library` and related
    governance artifacts, subject to published contracts
- Evidence
  - authoritative in `ste-runtime`
- Decision
  - authoritative in `ste-kernel`
- Enforcement
  - assigned by `ste-spec`, executed by the components that own those
    enforcement responsibilities

Precedence rule:

- README content is subordinate to ADRs, contracts, schemas, invariants, and
  Architecture IR doctrine
- when README content conflicts with a normative artifact, the normative
  artifact governs
- this README is a communication surface, not an authority surface

## Determinism and Guarantees

`ste-spec` does not claim runtime determinism in the way `ste-kernel` does. Its
guarantees are narrower and tied to publication discipline:

- normative artifact families are published in stable authority locations
- internal Markdown references can be checked with
  `python scripts/check_internal_md_links.py`
- repo-local contract publication checks can be run with
  `python scripts/run_local_contract_checks.py`
- draft surfaces are explicitly labeled as draft or pre-normative where the
  specification has not yet stabilized them

This repository does not currently prove broad behavioral determinism beyond
those publication and consistency checks, and this README should not imply that
it does.

## Failure Behavior

Failure in `ste-spec` means specification drift, broken references, or broken
published contract surfaces, not failed runtime admission.

Examples:

- broken internal Markdown links indicate documentation drift
- failing local contract checks indicate broken publication or contract
  integrity within this repository
- draft surfaces remaining unstable means they must not be treated as fully
  normative

`ste-spec` publishes constraints and doctrine. It does not itself execute
admission, runtime extraction, or operational enforcement logic, so its failure
behavior is about specification integrity rather than runtime availability.

## CLI / Usage

`ste-spec` is not a product CLI repository, but it does provide repo-local
validation commands for maintainers and reviewers.

Repeatable checks:

```bash
python scripts/check_internal_md_links.py
python scripts/run_local_contract_checks.py
```

Use these commands when changing normative or orientation surfaces so internal
links and published contract artifacts do not drift.

## Repository Boundary and Adjacent Repositories

`ste-spec` participates in a multi-repository architecture and must describe
its role relative to adjacent repositories without collapsing their authority.

| Repository | Relationship to `ste-spec` |
|------------|-----------------------------|
| `adr-architecture-kit` | Publishes ADR authoring and generation surfaces; consumes STE doctrine and may publish ADR IR fragments consumed downstream. |
| `ste-runtime` | Produces `ArchitectureEvidence`; consumes published STE contracts where applicable; does not emit caller-facing admission decisions. |
| `ste-rules-library` | Owns rules and governance-side artifacts; publishes rules-related surfaces and may participate in future projection contracts. |
| `ste-kernel` | Consumes adapter publication surfaces and executes merge, validation, and admission decisions; owns the mechanical `Compiled_IR_Document` bundle referenced by `ste-spec`. |

This repository must not redefine those repositories' implementation behavior.
It documents and constrains their shared boundaries.

## Normative vs Orientation vs Illustrative Surfaces

Use the following authority split when reading this repository:

- Normative
  - `contracts/` for contract shape
  - `invariants/` for semantic rules and constraints
  - binding ADRs in `adr/`
  - semantic Architecture IR doctrine in
    [`architecture/STE-Architecture-Intermediate-Representation.md`](architecture/STE-Architecture-Intermediate-Representation.md)
    as assigned by
    [`adr/ADR-035-architecture-ir-ontology-authority.md`](adr/ADR-035-architecture-ir-ontology-authority.md)
- Orientation
  - `architecture/`, `execution/`, and `governance/`
  - `status.md`
  - `scope-and-non-goals.md`
  - `glossary.md`
- Illustrative
  - `architecture/STE-Worked-Example-Walkthrough.md`
  - figure conventions and explanatory diagrams where explicitly informative

For the canonical artifact map, start with
[`architecture/STE-Manifest.md`](architecture/STE-Manifest.md).

## Canonical Documents and Where to Start

Start here based on your goal:

- Understand the repo and navigate the specification
  - [`architecture/STE-Manifest.md`](architecture/STE-Manifest.md)
- Inspect normative contract surfaces
  - [`contracts/README.md`](contracts/README.md)
- Understand repository boundaries and authority splits
  - [`architecture/STE-System-Components-and-Responsibilities.md`](architecture/STE-System-Components-and-Responsibilities.md)
- Understand multi-repo integration
  - [`architecture/STE-Integration-Model.md`](architecture/STE-Integration-Model.md)
- Understand semantic Architecture IR
  - [`architecture/STE-Architecture-Intermediate-Representation.md`](architecture/STE-Architecture-Intermediate-Representation.md)
- Understand repo status and maturity
  - [`status.md`](status.md)
- Understand scope limits and non-goals
  - [`scope-and-non-goals.md`](scope-and-non-goals.md)
  - [`NON-GOALS.md`](NON-GOALS.md)
- Understand architectural decisions
  - [`adr/README.md`](adr/README.md)

## Status and Maturity

Current repo status, per [`status.md`](status.md):

- stable handoff contracts and core doctrine are under review
- core invariants, execution semantics, and authority boundaries are stable
- broader governance extension surfaces remain explicitly draft or
  pre-normative

Draft / pre-normative surfaces currently called out by the repo include:

- `contracts/rule-projection/`
- `contracts/governance-decision-record/`
- `adr/ADR-034-rule-projection-envelope-authority.md`
- `invariants/INV-0010-rule-projection-envelope-discipline.md`

## Contribution and Maintenance Guidance

When changing this repository:

- update the correct authority surface
  - `contracts/` for shape
  - `invariants/` for rules
  - `adr/` for rationale
  - orientation docs only when navigation or explanation must change
- keep README subordinate to normative sources
- run the local checks
- preserve the distinction between normative, orientation, and illustrative
  material

This repository is an architectural specification, not a general-purpose how-to
guide or implementation repo. Changes should improve contract clarity, not blur
boundary responsibility.

## License

Copyright 2024-present Erik Gallmann
