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
- `adr/ADR-030-contract-authority-in-ste-spec.md`
- `adr/ADR-031-runtime-kernel-responsibility-boundary.md`
