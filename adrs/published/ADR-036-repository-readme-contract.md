# ADR-036: Repository README Contract

## Migration status

| Field | Value |
| --- | --- |
| **Canonical record** | Machine ADR **ADR-L-0036** — [`adrs/logical/ADR-L-0036-repository-readme-contract.yaml`](../logical/ADR-L-0036-repository-readme-contract.yaml) |
| **Human projection** | [`adrs/rendered/ADR-L-0036.md`](../rendered/ADR-L-0036.md) (generated; do not edit by hand) |
| **This file** | Legacy published markdown; **not canonical** |
| **Disposition** | Migrated one-to-one |

Authority: treat **ADR-L-0036** as the source of truth for decisions and invariants.

---

## Status

Accepted

## Context

STE is a multi-repository system with explicit repository boundaries and
authority splits across intent, constraints, governance, evidence, decision,
and enforcement.

Those authority splits already live in normative ADRs, contracts, invariants,
and Architecture IR doctrine. What is still easy to lose is the
human-readable explanation of what each repository is for, what it is not for,
and how it fits into the STE pipeline.

`README.md` is the first document most readers open. If it behaves only as a
tutorial or local usage note, repository responsibility drift becomes likely
and authority boundaries become harder to understand.

STE therefore needs a standard contract for what every repository README must
communicate, while keeping README subordinate to the existing normative
surfaces.

## Decision

Every STE repository `README.md` **MUST** function as a human-readable
architectural boundary and responsibility document for that repository.

### Artifact role distinction

| Artifact | Purpose |
|---------|---------|
| ADRs | Normative architectural decisions |
| Contracts | Machine-readable and integration boundaries |
| Architecture IR | Canonical compiled system model |
| README | Human-readable boundary and responsibility explanation |

`README.md` is:

- the human-readable architectural boundary description for a repository
- the orientation and responsibility entry point
- the fastest way for a reader to understand a repository's role in STE

`README.md` is not:

- normative authority
- a replacement for ADRs
- a replacement for contracts
- a replacement for Architecture IR documentation

This ADR does not define system authority. It defines how repositories **MUST**
describe their authority and boundaries in `README.md`.

README content is subordinate to ADRs, contracts, schemas, invariants, and
Architecture IR doctrine.

When repository README content conflicts with a normative ADR, invariant,
schema, contract, or Architecture IR doctrine, the normative artifact governs.
`README.md` is a communication surface, not an authority surface.

### Standard STE system statement

Every STE repository README **MUST** include the following system statement, or
a semantically equivalent statement that preserves the same meaning:

> STE is an architecture decision system that compiles intent, constraints, and
> runtime evidence into a canonical Architecture IR and produces deterministic
> admission decisions.

### Canonical STE pipeline model

Each README **MUST** identify the repository's position in the STE pipeline
using the canonical layer model below.

| Layer | Responsibility |
|------|----------------|
| Intent | ADRs |
| Constraints | Spec and invariants |
| Governance | Rules |
| Evidence | Runtime |
| Decision | Kernel |
| Enforcement | Components assigned by `ste-spec` |

Each repository README **MUST** explicitly state which layer or layers it
serves.

### Required communicative content

The purpose of these sections is to ensure that a reader can understand a
repository's role, authority, limits, inputs, outputs, and integration
position without reconstructing the system from multiple repositories first.

Each STE repository README **MUST** communicate, at minimum, the following
sections or equivalent content:

1. `STE System Statement`
   - reader understands what STE is and what problem it solves
2. `Mental Model and Pipeline Position`
   - reader understands where the repository fits in the STE pipeline
3. `Inputs`
   - reader understands what the repository consumes and from whom
4. `Outputs`
   - reader understands what the repository produces and who consumes it
5. `Responsibilities`
   - reader understands what the repository is expected to do
6. `Non-Responsibilities`
   - reader understands what the repository explicitly does not do
7. `Authority Boundary`
   - reader understands what decisions the repository is allowed to make and
     what it cannot authoritatively decide
8. `Determinism and Guarantees` when applicable
   - reader understands what behavior is guaranteed and under what conditions
9. `Failure Behavior` when applicable
   - reader understands how the system behaves when the repository fails
10. `CLI / Usage` when applicable
   - reader understands how to exercise the repository's public operational
     surface
11. `Repository Boundary and Adapter Model`
   - reader understands integration boundaries and adapter relationships
12. `Canonical Documents and Contracts`
   - reader knows where the normative ADRs, schemas, invariants, and contracts
     live

These are communicative requirements, not formatting requirements. Repository
READMEs may choose headings and local ordering that fit their role so long as
the required understanding is present and easy to find.

### Applicability across repository roles

The communicative obligation defined by this ADR is universal across STE
repositories. The exact set of headings may vary by repository role, but the
required understanding must still be present.

Some sections are conditional and may be omitted only when they are genuinely
not applicable to the repository:

- `Determinism and Guarantees` is required only when the repository makes
  behavioral guarantees.
- `Failure Behavior` is required when repository failure materially affects
  integration or operational behavior.
- `CLI / Usage` is required when the repository exposes a user-facing or
  operator-facing operational surface.

This ADR is intended to support staged convergence of repository README files
across the STE system. Repositories may converge incrementally, but all future
README refactors should move toward this contract.

### Required authority-boundary communication

Every STE repository README **MUST** explicitly state:

- what the repository is responsible for
- what the repository is not responsible for
- what authority the repository holds, if any
- which repository is authoritative for:
  - intent
  - constraints
  - governance
  - evidence
  - decision
  - enforcement

This communication requirement exists to prevent responsibility drift and make
authority scarcity visible at the repository entry point.

### Existing authority surfaces this ADR defers to

This ADR standardizes README communication only. It explicitly defers to the
existing authority and integration surfaces in `ste-spec`, including:

- [`ADR-030-contract-authority-in-ste-spec.md`](ADR-030-contract-authority-in-ste-spec.md)
- [`ADR-031-runtime-kernel-responsibility-boundary.md`](ADR-031-runtime-kernel-responsibility-boundary.md)
- [`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
- [`../architecture/STE-System-Components-and-Responsibilities.md`](../architecture/STE-System-Components-and-Responsibilities.md)
- [`../architecture/STE-Integration-Model.md`](../architecture/STE-Integration-Model.md)

Those artifacts define system authority and repository boundaries. `ADR-036`
defines how each repository README must describe those decisions in
human-readable form.

### README conformance review standard

A repository README is conformant to this ADR when:

- the required communicative content is present and easy to find
- repository responsibilities and non-responsibilities are explicit
- authority boundaries are explicit
- repository pipeline position is explicit
- canonical documents and contracts are identified
- no README statement contradicts a normative ADR, contract, invariant, schema,
  or Architecture IR doctrine

### Reference implementation

The `ste-kernel` README is the current reference implementation of the STE
Repository README Contract.

It is the current reference implementation because it demonstrates the intended
depth, clarity, authority-boundary discipline, failure-model description, and
contract-oriented structure expected by this ADR. Other repositories should
converge their README content and structure to this contract according to their
role in the STE system.

This reference status is exemplary, not normative. This ADR does not copy
`ste-kernel` README content, does not make that README the normative source,
and does not require other repositories to copy it verbatim.

The checklist operationalizes this ADR for repository maintainers, but does not
create additional normative requirements beyond this ADR.

## Rationale

- Keeps repository entrypoints aligned with existing authority ADRs and
  integration contracts.
- Makes responsibility and non-responsibility visible without requiring readers
  to reconstruct repo boundaries from multiple documents first.
- Improves onboarding while preserving authority discipline.
- Reduces the chance that tutorials, examples, or implementation notes become
  mistaken for repository authority.

## Consequences

### Positive

- STE repositories gain consistent system entry points.
- Onboarding improves because repository role and boundary are easier to find.
- Responsibility drift is reduced.
- Authority communication becomes clearer.
- Repository README convergence becomes easier over time.

### Discipline obligations

- README maintenance must remain aligned with normative sources.
- Maintainers must update README content when repository authority or
  boundaries change.
- README refactors must preserve communicative completeness, not just
  formatting.

## Out of scope

This ADR does not:

- define adapter contracts
- define Architecture IR semantics
- define repository runtime behavior
- define conformance automation
- define CI enforcement

It defines only how repository README files must communicate already-defined
system boundaries and responsibilities.

## Related

- [`ADR-030-contract-authority-in-ste-spec.md`](ADR-030-contract-authority-in-ste-spec.md)
- [`ADR-031-runtime-kernel-responsibility-boundary.md`](ADR-031-runtime-kernel-responsibility-boundary.md)
- [`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
- [`../architecture/STE-System-Components-and-Responsibilities.md`](../architecture/STE-System-Components-and-Responsibilities.md)
- [`../architecture/STE-Integration-Model.md`](../architecture/STE-Integration-Model.md)
- [`../architecture/STE-Repository-README-Checklist.md`](../architecture/STE-Repository-README-Checklist.md)
