# ADR-031: Runtime and Kernel Responsibility Boundary

## Status

Accepted

## Context

The handoff requires a stable division between factual evidence production and
caller-facing decision authority.

## Decision

`ste-runtime` is an evidence producer only.

`ste-kernel` is the caller-facing admission authority.

## Rationale

Separating evidence from decision semantics keeps runtime factual and kernel
authoritative, while preserving repo boundaries.

## Consequences

- Runtime does not emit admission or caller-facing decision semantics.
- Kernel alone emits `KernelAdmissionAssessment`.
- Shared contracts do not collapse runtime and kernel roles.
