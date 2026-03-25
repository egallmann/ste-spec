# ADR-032: Fail-Closed Enforcement Model

## Status

Accepted

## Context

The handoff becomes unsafe if unsupported or semantically invalid evidence can
still reach permissive kernel outcomes.

## Decision

Invalid runtime evidence is fail-closed at the kernel boundary.

## Lifecycle Placement in the STE Spine

This ADR operates at the enforcement point between Observation (Evidence),
Architecture IR Compilation, and Admission Decision by requiring invalid
boundary evidence or other invalid publication inputs to block downstream
compilation and admission outcomes.

## Relationship to Enforcement Model

This ADR supplies the Enforcement step in the chain `Doctrine -> Object Shape ->
IR Semantics -> Enforcement -> Admission`. It relies on
[`ADR-033-closed-object-discipline.md`](ADR-033-closed-object-discipline.md)
for allowed encoded object shape and on
[`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
for semantic meaning authority before admission proceeds.

## Rationale

The contract is only trustworthy if invalid, unavailable, malformed, or
semantically inconsistent evidence cannot produce action-eligible results.

## Consequences

- Version failures, shape failures, and semantic invariant failures are blocking conditions.
- Schema validity alone is insufficient for conformance.
- Evidence diagnostics become part of semantic validity expectations.
