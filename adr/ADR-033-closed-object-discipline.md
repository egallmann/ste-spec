# ADR-033: Closed-Object Discipline

## Status

Accepted

## Context

Open-ended contract objects allow silent extension fields to become hidden
semantic or policy channels across repositories.

## Decision

The runtime/kernel handoff uses closed objects by default.

## Lifecycle Placement in the STE Spine

This ADR governs Publication / Integration Input and the admission-boundary
handoff by constraining the allowed shape of material presented at the boundary.
It also affects Architecture IR Compilation and Admission Decision by
preventing undeclared fields from becoming hidden semantic channels in
downstream processing.

## Relationship to Enforcement Model

This ADR supplies the Object Shape step in the chain `Doctrine -> Object Shape
-> IR Semantics -> Enforcement -> Admission` by constraining what encoded
handoff objects are allowed at the boundary. Its allowed-shape discipline is
interpreted through
[`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
and enforced fail-closed through
[`ADR-032-fail-closed-enforcement-model.md`](ADR-032-fail-closed-enforcement-model.md).

## Rationale

Explicitly bounded objects prevent semantic drift and force contract evolution
through deliberate spec revision and versioning.

## Consequences

- Ad hoc extension fields are not contract-valid.
- Future expansion requires explicit spec updates.
- Producer and consumer conformance can reject drift deterministically.
