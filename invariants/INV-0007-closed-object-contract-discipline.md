# INV-0007: Closed-Object Contract Discipline

## Scope

All handoff contract objects.

## Rule

Contract objects are explicitly bounded. Additional undeclared fields are not
part of the contract.

## Enforcement Expectation

Producer and consumer conformance rejects ad hoc extension fields unless the
contract is explicitly revised.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
- `adrs/published/ADR-033-closed-object-discipline.md`
