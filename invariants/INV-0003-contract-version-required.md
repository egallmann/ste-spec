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
- [`ADR-L-0030`](../adrs/adr-projection/logical/ADR-L-0030-contract-authority-in-ste-spec.md)
- [`ADR-L-0032`](../adrs/adr-projection/logical/ADR-L-0032-fail-closed-enforcement-model.md)
