# ADR-031: Runtime and Kernel Responsibility Boundary

## Migration status

| Field | Value |
| --- | --- |
| **Canonical record** | Machine ADR **ADR-L-0031** — [`adrs/logical/ADR-L-0031-runtime-kernel-responsibility-boundary.yaml`](../logical/ADR-L-0031-runtime-kernel-responsibility-boundary.yaml) |
| **Human projection** | [`adrs/rendered/ADR-L-0031.md`](../rendered/ADR-L-0031.md) (generated; do not edit by hand) |
| **This file** | Legacy published markdown; **not canonical** |
| **Disposition** | Migrated one-to-one |

Authority: treat **ADR-L-0031** as the source of truth for decisions and invariants.

---

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
