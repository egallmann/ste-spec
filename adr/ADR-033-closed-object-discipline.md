# ADR-033: Closed-Object Discipline

## Status

Accepted

## Context

Open-ended contract objects allow silent extension fields to become hidden
semantic or policy channels across repositories.

## Decision

The runtime/kernel handoff uses closed objects by default.

## Rationale

Explicitly bounded objects prevent semantic drift and force contract evolution
through deliberate spec revision and versioning.

## Consequences

- Ad hoc extension fields are not contract-valid.
- Future expansion requires explicit spec updates.
- Producer and consumer conformance can reject drift deterministically.
