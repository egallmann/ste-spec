# INV-0009: Degraded Bundle Requires Diagnostic Context

## Scope

Runtime degraded-bundle reporting.

## Rule

`bundle.status: "degraded"` carries warning or error context when a degradative
condition is known.

## Enforcement Expectation

Empty diagnostics are reserved for cases where no degradative context applies.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `adr/ADR-032-fail-closed-enforcement-model.md`
