# INV-0006: Kernel Fails Closed on Invalid Evidence

## Scope

Kernel evidence consumption boundary.

## Rule

Malformed, unavailable, schema-invalid, semantically invalid, or
version-unsupported runtime evidence does not produce permissive admission
outcomes.

## Enforcement Expectation

Kernel rejects invalid evidence and returns blocked outcomes only.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
- `adrs/published/ADR-032-fail-closed-enforcement-model.md`
