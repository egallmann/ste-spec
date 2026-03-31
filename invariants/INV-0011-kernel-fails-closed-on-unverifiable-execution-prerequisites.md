# INV-0011: Kernel Fails Closed on Unverifiable Execution Prerequisites

## Scope

Kernel execution eligibility boundary.

## Rule

The Kernel SHALL fail closed.

If required artifacts, lifecycle state, authority, or governance requirements
cannot be verified, the Kernel MUST refuse execution.

## Enforcement Expectation

Kernel returns denied or blocked outcomes when execution prerequisites cannot
be verified.

Unverifiable is treated as non-eligible, not deferred permissiveness.

## Related Artifacts

- `execution/STE-Kernel-Execution-Model.md`
- `adrs/published/ADR-031-runtime-kernel-responsibility-boundary.md`
- `adrs/published/ADR-032-fail-closed-enforcement-model.md`
- `invariants/INV-0002-kernel-final-admission-authority.md`
- `invariants/INV-0006-kernel-fails-closed-on-invalid-evidence.md`
