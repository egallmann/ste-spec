# INV-0002: Kernel Is Final Admission Authority

## Scope

Caller-facing `KernelAdmissionAssessment`.

## Rule

Kernel is the only participant in this handoff that emits caller-facing
admission and eligibility semantics.

## Enforcement Expectation

Runtime evidence remains non-decision-bearing. Assessment payloads are emitted
by kernel only.

## Related Artifacts

- `contracts/kernel-admission-assessment.schema.json`
- `adrs/published/ADR-031-runtime-kernel-responsibility-boundary.md`
