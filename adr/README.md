# Architectural Decision Records

## Purpose

This directory contains the binding architectural decisions published as part of
`ste-spec`.

ADRs explain why authority is placed where it is. They do not replace
contracts, invariants, or implementation tests.

## Published Decision Areas

### Foundational Architectural Principles

- `ADR-001-deterministic-extraction.md`
- `ADR-006-explicit-unknowns.md`
- `ADR-007-slice-identity-strategy.md`
- `ADR-008-correctness-consistency-contract.md`
- `ADR-009-assertion-precedence-model.md`

### STE Authority and Enforcement Model

- `ADR-019-gateway-authority-signing.md`
- `ADR-020-org-signing-scope.md`
- `ADR-021-gateway-trust-verification.md`
- `ADR-022-fail-closed-enforcement-scope.md`
- `ADR-023-validation-timing-responsibility.md`
- `ADR-024-cross-component-contracts.md`
- `ADR-025-environment-semantics.md`
- `ADR-026-invariant-conflict-detection-semantics.md`
- `ADR-027-scope-semantics.md`
- `ADR-028-fabric-gateway-authority-boundaries.md`
- `ADR-029-gateway-enforcement-authority.md`

### Runtime/Kernel Contract Authority

- `ADR-030-contract-authority-in-ste-spec.md`
- `ADR-031-runtime-kernel-responsibility-boundary.md`
- `ADR-032-fail-closed-enforcement-model.md`
- `ADR-033-closed-object-discipline.md`
- `ADR-034-rule-projection-envelope-authority.md` (proposed)
- `ADR-035-architecture-ir-ontology-authority.md`
- `ADR-036-repository-readme-contract.md`

### STE Spine Consolidation

- `ADR-040-ste-spine-lifecycle-and-authority.md`

## Relationship to Other Surfaces

- `architecture/STE-Spine-Lifecycle.md`, `architecture/STE-Spine-Authority.md`, `architecture/STE-Spine-Artifact-Mapping.md`, and `architecture/STE-Spine-State-Model.md` support ADR-040 with consolidated Spine doctrine
- `contracts/` defines normative shape
- `invariants/` defines normative rules
- `adr/` defines architectural rationale
- `architecture/STE-Integration-Model.md` and `execution/STE-Kernel-Execution-Model.md` integrate ADR-030–034 with repository boundaries
