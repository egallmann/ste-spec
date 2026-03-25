# ADR-037: Repository README Conformance and Reference Implementation

## Status

Accepted

## Context

[`ADR-036`](ADR-036-repository-readme-contract.md) defined the communicative and
structural contract for repository `README.md` files across the STE system.

STE is a multi-repository architecture with explicit authority splits across
intent, constraints, governance, evidence, decision, and enforcement.
Repository entrypoints therefore affect architectural correctness: when README
content is underspecified, stale, or inconsistent, readers infer the wrong
authority boundary, misunderstand inputs and outputs, and lose the repository's
place in the multi-repository system.

README quality is therefore an architectural concern in STE, not merely a
documentation style preference. README files are the human-readable boundary
surface for repositories that participate in a larger system with governed
handoffs and explicit responsibility boundaries.

`ste-spec` has now been refactored to satisfy `ADR-036`. That makes its current
README the first full implementation of the README contract in practice and the
natural reference point for system-wide README convergence.

## Decision

1. [`ADR-036`](ADR-036-repository-readme-contract.md) is the governing README
   contract for STE repositories.

2. Every STE repository **MUST** provide a `README.md` that conforms to
   `ADR-036`.

3. In ADR-038 artifact posture, `README.md` is an **Orientation** artifact: it
   is non-authoritative, should be versioned, cannot introduce doctrine, and
   must reference normative sources when describing authority, contracts, or
   invariants.

4. A conformant README **MUST** accurately communicate the repository's:

   - authority
   - responsibilities
   - non-responsibilities
   - inputs
   - outputs
   - boundaries
   - lifecycle position

5. README content is subordinate to normative artifacts, including:

   - ADRs
   - contracts
   - schemas
   - invariants
   - Architecture IR doctrine

   When README content conflicts with a normative artifact, the normative
   artifact governs.

6. A conformant README must communicate, in substance:

   - what the repository is
   - why it exists
   - where it sits in the STE lifecycle
   - what it consumes
   - what it produces
   - what it is responsible for
   - what it is not responsible for
   - what authority it holds and does not hold
   - how it relates to adjacent repositories
   - where readers should go for normative artifacts

   `ADR-036` remains the source of truth for the exact README contract and
   expected communicative section responsibilities.

7. The current `ste-spec` README is the reference implementation of
   `ADR-036` for the STE system.

   It is the reference implementation because it demonstrates:

   - ADR-036-compliant structure
   - explicit authority-boundary communication
   - explicit responsibilities and non-responsibilities
   - explicit inputs and outputs
   - a clear distinction between normative and explanatory surfaces
   - practical navigation across the multi-repository STE system

   This reference status is exemplary, not normative. The `ste-spec` README is
   not itself the rule source. Other repositories should converge toward it
   according to their role, and **MUST NOT** treat it as text to copy verbatim.

8. New repositories entering the STE ecosystem **MUST** treat README creation
   as part of repository architectural definition from day one.

   A new repository should define its README alongside its authority boundary,
   contract surfaces, and role in the STE system. README work is not a later
   polish step.

9. README conformance supports multi-repository navigation by making the
   relationships among `adr-architecture-kit`, `ste-spec`, `ste-runtime`,
   `ste-rules-library`, and `ste-kernel` visible at each repository entrypoint.

10. README conformance may later become reviewable or machine-checkable.
   This ADR does not define CI checks, schema checks, or conformance tooling.
   Any future enforcement mechanism must remain subordinate to `ADR-036` and to
   the normative authority surfaces it references.

## Rationale

- Makes repository entrypoints part of the governed Orientation surface rather
  than an informal prose layer.
- Prevents authority drift by requiring repository boundaries to be described
  explicitly and accurately.
- Gives new repositories a clear starting posture for boundary communication.
- Improves multi-repository navigation without collapsing authority into a
  single repo or a single document type.
- Uses a real, current repository example (`ste-spec`) to demonstrate that the
  README contract is practical and implementable.

## Consequences

- STE repositories must treat README content as a maintained Orientation
  communication surface.
- README refactors must preserve conformance to `ADR-036` and remain aligned
  with the repository's normative artifacts.
- New repository creation now includes README boundary definition from the
  beginning.
- `ste-spec` becomes the convergence target for README structure and quality,
  while `ADR-036` remains the governing contract.
- Future review or automation work may use this ADR as the conformance posture
  decision, but such tooling is outside the scope of this decision.

## Related

- [`ADR-030-contract-authority-in-ste-spec.md`](ADR-030-contract-authority-in-ste-spec.md)
- [`ADR-031-runtime-kernel-responsibility-boundary.md`](ADR-031-runtime-kernel-responsibility-boundary.md)
- [`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
- [`ADR-036-repository-readme-contract.md`](ADR-036-repository-readme-contract.md)
- [`../README.md`](../README.md)
- [`../architecture/STE-System-Components-and-Responsibilities.md`](../architecture/STE-System-Components-and-Responsibilities.md)
- [`../architecture/STE-Integration-Model.md`](../architecture/STE-Integration-Model.md)
