# INV-0001: Runtime Evidence Is Factual Only

## Scope

Runtime-emitted `ArchitectureEvidence`.

## Rule

Runtime evidence is limited to factual bundle health, freshness, warnings,
errors, and allowed timestamps.

Runtime evidence excludes admission outcomes, eligibility semantics,
acknowledgement semantics, and caller-facing decision intent.

## Enforcement Expectation

Contract conformance rejects undeclared or policy-bearing evidence fields.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- [`ADR-L-0030`](../adrs/adr-projection/logical/ADR-L-0030-contract-authority-in-ste-spec.md)
- [`ADR-L-0031`](../adrs/adr-projection/logical/ADR-L-0031-runtime-and-kernel-responsibility-boundary.md)
