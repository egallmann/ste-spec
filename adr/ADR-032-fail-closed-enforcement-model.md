# ADR-032: Fail-Closed Enforcement Model

## Status

Accepted

## Context

The handoff becomes unsafe if unsupported or semantically invalid evidence can
still reach permissive kernel outcomes.

## Decision

Invalid runtime evidence is fail-closed at the kernel boundary.

## Rationale

The contract is only trustworthy if invalid, unavailable, malformed, or
semantically inconsistent evidence cannot produce action-eligible results.

## Consequences

- Version failures, shape failures, and semantic invariant failures are blocking conditions.
- Schema validity alone is insufficient for conformance.
- Evidence diagnostics become part of semantic validity expectations.
