# INV-0012 — Evidence Must Reference Evaluated Subjects

## Scope

Runtime-emitted `ArchitectureEvidence`.

## Rule

`ArchitectureEvidence` payloads **MUST** reference the subject or subjects they
validate or invalidate.

## Enforcement Expectation

Subject-linked evidence is required for conformance evaluation. Evidence that
omits referenced subjects is invalid for conformance evaluation and must not be
treated as sufficient kernel evidence for execution eligibility.

## Related Artifacts

- `contracts/architecture-evidence.schema.json`
- `architecture/STE-Spine-State-Model.md`
- `execution/STE-Kernel-Execution-Model.md`
- `contracts/README.md`
