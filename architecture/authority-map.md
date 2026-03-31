# Authority Map

This file is the human-readable authority reference for cross-repository STE contracts and artifact ownership.

## Public Contracts

These are public cross-repo contracts and are authoritative only in `ste-spec/contracts/`.

| Contract | Authoritative location | Producers | Consumers |
| --- | --- | --- | --- |
| Architecture IR schema | `ste-spec/contracts/architecture-ir/architecture-ir.schema.json` | `ste-spec` publishes canonical contract; `adr-architecture-kit` compiles compatible ADR-derived IR fragments | `ste-kernel`, `adr-architecture-kit`, `ste-rules-library` tests/fixtures where needed |
| Architecture IR bundle | `ste-spec/contracts/architecture-ir/architecture-ir.yaml`, `ste-spec/contracts/architecture-ir/ARCHITECTURE_IR.md` | `ste-spec` publishes canonical bundle; compiled via kit-compatible IR production | `ste-kernel`, documentation and test consumers |
| ArchitectureEvidence schema | `ste-spec/contracts/architecture-evidence.schema.json` | `ste-spec` publishes contract; `ste-runtime` emits conformant evidence payloads | `ste-runtime`, `ste-kernel` |
| KernelAdmissionAssessment schema | `ste-spec/contracts/kernel-admission-assessment.schema.json` | `ste-spec` publishes contract; `ste-kernel` emits conformant admission payloads | `ste-kernel`, downstream callers/tests |
| Freshness contract mapping | `ste-spec/contracts/freshness-contract-mapping.md` | `ste-spec` | `ste-runtime`, `ste-kernel`, docs/tests |

## Kernel-private Contracts

These remain local to `ste-kernel/contracts/` and are not public cross-repo authority surfaces in this pass.

| Contract | Location | Notes |
| --- | --- | --- |
| Boot result schema | `ste-kernel/contracts/boot-result.schema.json` | CLI/internal only; no non-kernel consumer found |
| Admission context schema | `ste-kernel/contracts/admission-context.schema.json` | Internal request/context surface; no non-kernel consumer found |
| Query/explain contract notes | `ste-kernel/contracts/query-explain-contract.md` | Kernel-private output notes until explicitly promoted |
| Governance posture notes | `ste-kernel/contracts/governance-posture.md` | Kernel-private posture/output notes |
| Generic integration IR notes | `ste-kernel/contracts/generic-integration-ir.md` | Kernel-private supporting note |
| Subsystem registration note | `ste-kernel/contracts/subsystem-registration.md` | Kernel-private supporting note |

## Artifact Production

| Artifact | Producing repo | Notes |
| --- | --- | --- |
| ADR | `adr-architecture-kit` | ADR schemas, authoring, and authoring-time validation |
| IR bundle | `ste-spec` | Canonical public IR bundle is published in `ste-spec`; ADR-derived IR-compatible fragments are compiled via `adr-architecture-kit` |
| Evidence | `ste-runtime` | Emits factual evidence only; no admission or governance decisions |
| Admission | `ste-kernel` | Single decision authority; emits admission/assessment outputs |

## Contract Consumption

| Repo | Consumes public contracts |
| --- | --- |
| `adr-architecture-kit` | Architecture IR schema/bundle for compatibility and validation where needed |
| `ste-runtime` | ArchitectureEvidence schema and related public contract references |
| `ste-kernel` | Architecture IR schema/bundle, ArchitectureEvidence schema, KernelAdmissionAssessment schema |
| `ste-rules-library` | Architecture IR schema/bundle only as a downstream compatibility/test concern; rules remain advisory |
| `ste-handbook` | None as an authority source; explanatory only and should point readers to `ste-spec` |

## Authority Rules

- Public cross-repo contracts must exist in exactly one authoritative location: `ste-spec/contracts/`.
- Kernel-private contracts must remain in `ste-kernel/contracts/` and be labeled private.
- `ste-runtime` emits evidence only.
- `ste-kernel` emits admission only.
- `ste-rules-library` is advisory only and must not act as a shared contract authority source.
- `ste-handbook` is explanatory only and must not own schemas or contracts.
