# ADR-031: Runtime and Kernel Responsibility Boundary

## Status

Accepted

## Context

The handoff requires a stable division between factual evidence production and
caller-facing decision authority.

## Decision

`ste-runtime` is an evidence producer only.

`ste-kernel` is the caller-facing admission authority.

## Lifecycle Placement in the STE Spine

This ADR defines the boundary between Runtime Execution and Observation
(Evidence) on the runtime side and Admission Decision on the kernel side.
Runtime-side lifecycle participation stops at Observation (Evidence);
caller-facing decision output appears at Admission Decision in `ste-kernel`.
Admission authority at that boundary includes deterministic execution
eligibility determination before caller-facing admission output is emitted.

## Rationale

Separating evidence from decision semantics keeps runtime factual and kernel
authoritative, while preserving repo boundaries.

## Consequences

- Runtime does not emit admission or caller-facing decision semantics.
- Kernel alone emits `KernelAdmissionAssessment`.
- Shared contracts do not collapse runtime and kernel roles.
