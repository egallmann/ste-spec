# Architectural Decision Records

## Purpose

This directory contains the binding architectural decisions published as part of
`ste-spec`.

ADRs explain why authority is placed where it is. They do not replace
contracts, invariants, or implementation tests.

**Migration note:** Numbered `adrs/published/*.md` files in this directory now carry a **Migration status** header and are **historical projections** once a machine ADR-L exists. Canonical decisions and invariants live under `../logical/*.yaml`; human-friendly renderings are generated under `../rendered/` and `../manifest.yaml` via **adr-architecture-kit** (`adr validate`, `adr compile` with graph emit).

## Published Decision Areas

### Foundational Architectural Principles

- `ADR-001-deterministic-extraction.md` — **migrated**; canonical **ADR-L-0001**
- `ADR-006-explicit-unknowns.md` — **migrated**; canonical **ADR-L-0006**
- `ADR-007-slice-identity-strategy.md` — **migrated**; canonical **ADR-L-0007**
- `ADR-008-correctness-consistency-contract.md` — **migrated**; canonical **ADR-L-0008**
- `ADR-009-assertion-precedence-model.md` — **migrated**; canonical **ADR-L-0009**

**ADR numbers 010 through 018 are not used in this repository** (intentionally
unallocated). The published series continues at ADR-019.

### STE Authority and Enforcement Model

- `ADR-019-gateway-authority-signing.md` — **migrated**; **ADR-L-0019**
- `ADR-020-org-signing-scope.md` — **migrated**; **ADR-L-0020**
- `ADR-021-gateway-trust-verification.md` — **migrated**; **ADR-L-0021**
- `ADR-022-fail-closed-enforcement-scope.md` — **migrated**; **ADR-L-0022**
- `ADR-023-validation-timing-responsibility.md` — **migrated**; **ADR-L-0023**
- `ADR-024-cross-component-contracts.md` — **migrated**; **ADR-L-0024**
- `ADR-025-environment-semantics.md` — **migrated**; **ADR-L-0025**
- `ADR-026-invariant-conflict-detection-semantics.md` — **migrated**; **ADR-L-0026**
- `ADR-027-scope-semantics.md` — **migrated**; **ADR-L-0027**
- `ADR-028-fabric-gateway-authority-boundaries.md` — **migrated**; **ADR-L-0028**
- `ADR-029-gateway-enforcement-authority.md` — **migrated**; **ADR-L-0029**

### Runtime/Kernel Contract Authority

- `ADR-030-contract-authority-in-ste-spec.md` — **migrated**; **ADR-L-0030**
- `ADR-031-runtime-kernel-responsibility-boundary.md` — **migrated**; **ADR-L-0031**
- `ADR-032-fail-closed-enforcement-model.md` — **migrated**; **ADR-L-0032**
- `ADR-033-closed-object-discipline.md` — **migrated**; **ADR-L-0033**
- `ADR-034-rule-projection-envelope-authority.md` (proposed) — **migrated**; **ADR-L-0034** (still **proposed** in machine form)
- `ADR-035-architecture-ir-ontology-authority.md` — **migrated**; **ADR-L-0035**
- `ADR-036-repository-readme-contract.md` — **migrated**; **ADR-L-0036**
- `ADR-037-repository-readme-conformance-and-reference-implementation.md` — **migrated**; **ADR-L-0037**
- `ADR-041-compiler-and-merge-authority.md` — **migrated**; **ADR-L-0041**

### Documentation and Taxonomy

- `ADR-038-artifact-classification-and-versioning.md` — **migrated**; canonical **ADR-L-0038** (machine title: Artifact Taxonomy and Versioning Posture)
- `ADR-039-structured-diagram-format-mermaid.md` — **migrated**; **ADR-L-0039**

### STE Spine Consolidation

- `ADR-040-ste-spine-lifecycle-and-authority.md` — **migrated**; **ADR-L-0040**

**ADR-L-0040** is the canonical definition of the STE Spine lifecycle and
authority-transition model. **ADR-L-0038** remains the canonical artifact taxonomy and
versioning posture authority. Supporting Spine documents live in
`architecture/` and are subordinate to those ADRs.

### Non-numbered published notes

- `ARCHITECTURE_BOUNDARY_DECISION.md` — **migrated**; canonical **ADR-L-0042**

## Machine-verifiable ADR-L (adr-architecture-kit)

Cross-cutting **governance semantics** for STE-wide kernel admission (actions, admission,
posture, freshness, drift, evidence authority, Golden, decision outcomes, and the kernel
decision contract) are authored as **schema-valid YAML Logical ADRs** under
`../logical/` and regenerated with **adr-architecture-kit** (`adr validate`,
`adr compile --emit registries,manifest,markdown,graph`, `adr validate-generated-docs`).

**Runtime compiler of record** for machine artifacts is **ste-runtime** (`ste architecture compile --project-root <repo>`); see `ste-runtime/COMPILER-AUTHORITY.md` and `adrs/MIGRATION-INVENTORY.md` Phase 5.

Where both legacy markdown and machine YAML exist, resolve conflicts using explicit
precedence statements inside each ADR-L and the migrated Spine anchors (**ADR-L-0031**,
**ADR-L-0040**, **ADR-L-0038**), plus `execution/STE-Kernel-Execution-Model.md`.

Published machine ADR-L files (ste-spec `adrs/logical/`) include **ADR-L-0001**, **ADR-L-0006–0009**, **ADR-L-0019–0029**, **ADR-L-0030–0042**, and the **ADR-L-1001–1009** kernel governance series. See `../rendered/` for generated markdown projections.

## Relationship to Other Surfaces

- `architecture/STE-Spine-Lifecycle.md`, `architecture/STE-Spine-Authority.md`, `architecture/STE-Spine-Artifact-Mapping.md`, and `architecture/STE-Spine-State-Model.md` are normative supporting doctrine for ADR-040 and do not override **ADR-L-0040** or **ADR-L-0038**
- `architecture/STE-Spine-Extracted-Doctrine.md` is analysis-only and non-normative
- `contracts/` defines normative shape
- `invariants/` defines normative rules
- `adrs/published/` defines architectural rationale (non-canonical after migration headers)
- `architecture/STE-Integration-Model.md` and `execution/STE-Kernel-Execution-Model.md` integrate ADR-030–034 themes with repository boundaries (see machine **ADR-L-0030–0035**)
