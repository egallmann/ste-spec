# INV-0005: Unknown Freshness Is Explicit

## Scope

Runtime freshness signaling.

## Rule

If runtime cannot determine architecture-bundle freshness confidently, it emits
`stale-unknown`.

## Enforcement Expectation

Implementations do not substitute optimistic defaults for unknown freshness.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `adr/ADR-032-fail-closed-enforcement-model.md`
