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

This ADR operates at Admission Decision by assigning caller-facing admission
output to `ste-kernel`. It also affects Observation (Evidence) by confining
`ste-runtime` to factual evidence production before the kernel boundary.

At that boundary, `ste-kernel` determines caller-facing admission and execution
eligibility for the active System Instance: the evaluated System in one
explicit Environment under the active evaluation scope.

## Rationale

Separating evidence from decision semantics keeps runtime factual and kernel
authoritative, while preserving repo boundaries.

## Consequences

- Runtime does not emit admission or caller-facing decision semantics.
- Kernel alone emits `KernelAdmissionAssessment`.
- Shared contracts do not collapse runtime and kernel roles.
