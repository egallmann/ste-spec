# INV-0008: Invalid Bundle Requires Error Diagnostics

## Scope

Runtime bundle diagnostics.

## Rule

`bundle.status: "invalid"` is accompanied by at least one error entry that
explains why the required bundle is unusable.

## Enforcement Expectation

Schema-valid evidence without required invalid-bundle diagnostics is treated as
semantically invalid.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- [`ADR-L-0032`](../adrs/adr-projection/logical/ADR-L-0032-fail-closed-enforcement-model.md)
