# INV-0004: Required Arrays Are Explicit

## Scope

Runtime evidence and kernel assessment payloads.

## Rule

Warnings and errors in runtime evidence are always explicit arrays.

Blocking reasons, advisories, and preconditions in kernel assessment are always
explicit arrays.

## Enforcement Expectation

Payloads do not omit these surfaces to imply absence.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
