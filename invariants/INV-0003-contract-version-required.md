# INV-0003: Contract Version Is Required

## Scope

Runtime evidence contract versioning.

## Rule

Every successful runtime evidence payload includes a supported contract
version.

Unsupported, missing, or malformed contract versions are invalid.

## Enforcement Expectation

Consumers reject unsupported or absent versions and fail closed.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `adr/ADR-030-contract-authority-in-ste-spec.md`
- `adr/ADR-032-fail-closed-enforcement-model.md`
