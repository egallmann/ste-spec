# STE Canonical Project Artifacts (documentation-state map)

## Purpose

This document lists **normative artifact classes** that constitute **documentation-state**
and related **publication surfaces** for the reference STE repositories. It answers
“what classes of files are authoritative, and who owns them?” without prescribing
internal implementation layout beyond what is already contract-backed.

**Normative companion:** `architecture/STE-Foundations.md` §2.3a (documentation-state
vs integration-state vs runtime evidence).

---

## Artifact classes by repository role

| Repository | Authoritative artifact classes (examples) | Generated vs hand-edited (typical) |
|------------|---------------------------------------------|-------------------------------------|
| **ste-spec** | JSON Schemas under `contracts/`; Architecture IR mechanical bundle under `contracts/architecture-ir/` (schema, YAML, split definitions, `ARCHITECTURE_IR.md`); `contracts/architecture-ir/spec-ir-fragments.json`; invariant markdown under `invariants/`; binding ADRs under `adr/`; orientation under `architecture/`, `execution/` | Schemas and INV docs: hand-edited; spec IR fragments: produced by `scripts/publish_architecture_ir_fragments.py` (deterministic) |
| **adr-architecture-kit** | Logical/physical ADR sources; `adrs/manifest.yaml`; `adrs/index/*`; kit JSON Schemas under `schema/` | Manifest and indices: **generated** by kit CLIs; ADR sources: hand-edited |
| **ste-runtime** | Runtime outputs that conform to `ArchitectureEvidence` schema; RECON/RSS state under conventional paths (see that repo) | Evidence and graphs: **generated** by tooling |
| **ste-rules-library** | Rule and signal schemas; `governance/manifest.yaml`; published **rules IR fragments** per kernel boot contract | Mix: hand-edited rules, generated manifests/fragments per repo policy |
| **ste-kernel** | `contracts/adapter-contracts.yaml`; kernel ADR corpus under `adrs/`; implementation and proof assets | Adapter policy: maintained; IR schema consumed from sibling `ste-spec` checkout in STE-workspace |

---

## MUST / MUST NOT (boundary)

**MUST:** Treat only **declared, contract-backed** paths as publication surfaces for
kernel consumption (see `ste-kernel/documentation/BOOT_SEQUENCE.md`).

**MUST NOT:** Treat ad-hoc repository directories as authoritative without mapping
them to a declared artifact class above or in `ste-spec` / `ste-kernel` contracts.

---

## Related

- `architecture/STE-Reference-Embodiment.md`
- `architecture/STE-Integration-Model.md`
- `invariants/STE-Artifact-Specifications.md`
- `contracts/README.md`

## Canon Status

This file is **canonical** for the **documentation-state artifact map** viewpoint in
`ste-spec`.
