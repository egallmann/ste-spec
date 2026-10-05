# Cross-Component Contracts

This directory is the canonical home for published **runtime/kernel handoff**
contracts governed by `ste-spec` (see
[`ADR-L-0030`](../adrs/adr-projection/logical/ADR-L-0030-contract-authority-in-ste-spec.md)).

**Story (informative):** for a single walkthrough that shows how handoff
artifacts fit into a fictional team thread, read
`architecture/STE-Worked-Example-Walkthrough.md`.

## ste-spec-owned artifacts (normative shape)

| Artifact | Purpose |
|----------|---------|
| `architecture-evidence.schema.json` | **`ArchitectureEvidence`** - factual bundle health, freshness, and subject-linked validation or invalidation references from `ste-runtime` |
| `kernel-admission-assessment.schema.json` | **`KernelAdmissionAssessment`** - caller-facing admission from `ste-kernel` |
| [`architecture-ir/architecture-ir.schema.json`](architecture-ir/architecture-ir.schema.json) | **`Compiled_IR_Document`** mechanical JSON Schema (Architecture IR) |
| [`architecture-ir/architecture-ir.yaml`](architecture-ir/architecture-ir.yaml) | Merge and identity YAML bundle for Architecture IR |
| [`architecture-ir/ARCHITECTURE_IR.md`](architecture-ir/ARCHITECTURE_IR.md) | Mechanical specification narrative for Architecture IR |
| [`architecture-ir/spec-ir-fragments.json`](architecture-ir/spec-ir-fragments.json) | **Spec adapter IR fragments** - generator-owned published `SpecAdapter` input to kernel merge (see [`architecture-ir/README.md`](architecture-ir/README.md)) |
| `examples/` | Non-normative examples |

### Draft / pre-normative (rule projections)

| Artifact | Purpose |
|----------|---------|
| `rule-projection/README.md` | Status and scope for **ADR-bound rule projection** envelope work |
| `rule-projection/rule-projection-envelope.schema.json` | **Draft** JSON Schema sketch (not yet stable `$id` for interchange) |

### Draft / pre-normative (governance decisions)

| Artifact | Purpose |
|----------|---------|
| `governance-decision-record/README.md` | Minimum **decision row** semantics (references **projection**; distinct artifact family) |
| `governance-decision-record/decision-record.schema.json` | **Draft** JSON Schema for append-only / CI replay rows |

### Draft / pre-normative (runtime derived surfaces)

| Artifact | Purpose |
|----------|---------|
| `workspace-graph/README.md` | Draft docs-only classification for runtime-owned workspace graph slices, merged workspace graph output, and workspace graph index posture |
| `projection-metadata/README.md` | Draft docs-only classification for deterministic multi-resolution projection metadata |
| `implementation-attribution-evidence/README.md` | Draft handoff notes for implementation attribution evidence; current schema authority remains in `adr-architecture-kit` |

### Draft / pre-normative (MVC evolution)

| Artifact | Purpose |
|----------|---------|
| `graph-domain/README.md` | Draft classification for Graph Domain Definition boundaries; graph domains are derived surfaces and do not create authority |
| `graph-domain/graph-domain-definition.schema.json` | **Draft** schema sketch for declarative graph-domain view/materialization contracts |
| `linkage-surface/README.md` | Draft classification for materialized cross-domain linkage surfaces consumed by RSS/MVC assembly |
| `linkage-surface/linkage-surface.schema.json` | **Draft** schema sketch for materialized cross-domain relationship surfaces, independent of generation strategy |
| `context-domain/README.md` | Draft classification for Context Domain Definition vs Context Domain Bundle boundaries |
| `context-domain/context-domain-definition.schema.json` | **Draft** schema sketch for semantic context-domain view definitions |
| `context-domain/context-domain-bundle.schema.json` | **Draft** schema sketch for materialized candidate context-domain bundles |
| `persona/README.md` | Draft classification for Persona as Context Selection Policy |
| `persona/persona-definition.schema.json` | **Draft** schema sketch for persona context-selection policy |
| `mvc/README.md` | Draft classification for MVC-D, MVC-S, and MVC-M boundaries |
| `mvc/mvc-definition.schema.json` | **Draft** schema sketch for MVC-D declarative context definitions |
| `mvc/mvc-snapshot.schema.json` | **Draft** schema sketch for MVC-S candidate architectural reality surfaces |
| `mvc/mvc-materialization-result.schema.json` | **Draft** schema sketch for MVC-M admitted materialized surfaces |

Promotion path: ADR + update this table +
`invariants/STE-Cross-Component-Contract-Invariants.md` when the envelope
becomes normative.

**Behavioral rules** for these payloads live under `invariants/` (INV-000x
index: `invariants/STE-Cross-Component-Contract-Invariants.md`). **Rationale**
lives in canonical authored ADRs under `adrs/logical/`; consult generated human
views under `adrs/adr-projection/logical/`.

**Freshness layering** across `ArchitectureEvidence` and
`KernelAdmissionAssessment` is normative in
[`freshness-contract-mapping.md`](freshness-contract-mapping.md).

## Architecture IR mechanical bundle (ste-spec-owned)

The **Architecture IR** JSON Schema, YAML merge contract, split entity and
relationship definitions, and mechanical narrative (`ARCHITECTURE_IR.md`) are
**normative in `ste-spec`** under `contracts/architecture-ir/`. **Semantic**
Architecture IR (ontology, lifecycle, completeness, governance, Architecture
Index) remains **normative** in
`architecture/STE-Architecture-Intermediate-Representation.md`
([`ADR-L-0035`](../adrs/adr-projection/logical/ADR-L-0035-architecture-ir-ontology-authority-in-ste-spec.md)).

**`ste-kernel`** **consumes** this bundle (for example by resolving the sibling
`ste-spec` checkout in the STE-workspace layout) and **does not** own the
normative mechanical definition.

**Adapter publication policy** (which paths adapters publish to) remains
versioned in `ste-kernel/contracts/adapter-contracts.yaml` as **kernel
integration policy**, not as a substitute for the IR interchange contract.

**Pinned pointer (ste-spec):** `contracts/architecture-ir-contract-pin.json`
records the current **`ir_version`**, **`schema_id`**, and relative paths under
this repository. Update it when the IR contract bumps.

## Golden contract bundles (anti-drift gate)

**Informative** JSON under `contracts/examples/` illustrates shape only.

For **machine-verifiable** convergence, use **golden contract bundles** (pinned
fragment sets, stable `ArchitectureEvidence` / `KernelAdmissionAssessment`
fixtures where applicable, and expected **`Compiled_IR_Document`** identity
such as `document_id` or canonical byte hash per **`ir_version`**) exercised by
**`ste-kernel`** verify commands or CI jobs that invoke them. That gate catches
schema staleness and integration regressions without elevating narrative
examples to normative truth.

## Adapter publication surfaces (informative summary)

Kernel consumption paths for fragments and evidence are documented in
`ste-kernel/documentation/BOOT_SEQUENCE.md` (Adapter Artifact Loading Contract).
Normative integration narrative: `architecture/STE-Integration-Model.md`.

## Canonical vs derived (at the boundary)

| Kind | Examples | Authority |
|------|----------|-----------|
| **Canonical handoff schemas** | Files in this `contracts/` directory | `ste-spec` |
| **Spec IR fragments** | `architecture-ir/spec-ir-fragments.json` | `ste-spec` publishes; `ste-kernel` consumes |
| **ADR / Rules IR fragments** | Adapter-published JSON arrays | Respective repositories publish; `ste-kernel` consumes |
| **ArchitectureEvidence** | Runtime output linked to evaluated subjects | `ste-runtime` produces; `ste-kernel` consumes |
| **Compiled_IR_Document** | Canonical Architecture IR contract bundle | `ste-spec` owns the public contract; `ste-kernel` consumes it |
| **KernelAdmissionAssessment** | Admission JSON | **Derived** by `ste-kernel` from projected slice + policy |

Contract lock for this boundary:

- adapter fragments are deterministic normalized record arrays
- `spec-ir-fragments.json` is an adapter input artifact, not a grouped-envelope schema
- `ste-runtime` publishes `ArchitectureEvidence` only
- kernel execution state is derived from consumed publications
- public `Compiled_IR_Document` contracts are owned by `ste-spec`
- `ste-kernel` alone emits `KernelAdmissionAssessment`
- `Compiled_IR_Document` public contract authority lives in `ste-spec`

`ArchitectureEvidence` remains factual only. Its required `subjects` linkage
identifies which ADRs, requirements, invariants, rules, systems, or components
the evidence validates or invalidates. Subject linkage does not make evidence a
caller-facing admission decision or a new authority source.

## Related orientation

- `architecture/STE-Reference-Embodiment.md`
- `architecture/STE-Architecture-Intermediate-Representation.md`
- `architecture/STE-Determinism-and-Canonical-Identity.md`
- `invariants/STE-Failure-Taxonomy-Boundaries.md`
- `execution/STE-Kernel-Execution-Model.md`
