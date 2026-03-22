# Cross-Component Contracts

This directory is the canonical home for published **runtime/kernel handoff**
contracts governed by `ste-spec` (see `adr/ADR-030-contract-authority-in-ste-spec.md`).

**Story (informative):** for a single walkthrough that shows how handoff artifacts fit
into a fictional team thread, read `architecture/STE-Worked-Example-Walkthrough.md`.

## ste-spec-owned artifacts (normative shape)

| Artifact | Purpose |
|----------|---------|
| `architecture-evidence.schema.json` | **`ArchitectureEvidence`** — factual bundle health and freshness from `ste-runtime` |
| `kernel-admission-assessment.schema.json` | **`KernelAdmissionAssessment`** — caller-facing admission from `ste-kernel` |
| [`architecture-ir/spec-ir-fragments.json`](architecture-ir/spec-ir-fragments.json) | **Spec adapter IR fragments** — generator-owned published `SpecAdapter` input to kernel merge (see [`architecture-ir/README.md`](architecture-ir/README.md)) |
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

Promotion path: ADR + update this table + `invariants/STE-Cross-Component-Contract-Invariants.md`
when the envelope becomes normative.

**Behavioral rules** for these payloads live under `invariants/` (INV-000x index:
`invariants/STE-Cross-Component-Contract-Invariants.md`). **Rationale** lives under
`adr/`.

## Referenced mechanical contract bundle (kernel-owned)

The **Architecture IR** schema, merge configuration, and identity rules are
**versioned and maintained in `ste-kernel`**. `ste-spec` **references** them as
the mechanical authority for `Compiled_IR_Document`. **Semantic** Architecture IR
(ontology, lifecycle, completeness, governance, Architecture Index) is **normative**
in `architecture/STE-Architecture-Intermediate-Representation.md` (`adr/ADR-035-architecture-ir-ontology-authority.md`).

- `ste-kernel/architecture-ir/architecture-ir.schema.json`
- `ste-kernel/architecture-ir/architecture-ir.yaml`
- `ste-kernel/documentation/ARCHITECTURE_IR.md`
- `ste-kernel/contracts/adapter-contracts.yaml`

**Pinned pointer (ste-spec):** `contracts/architecture-ir-kernel-contract-pin.json`
records the current **`ir_version`**, **`schema_id`**, and relative paths into the
`ste-kernel` bundle. Update it when the kernel bumps the IR contract.

**MUST NOT:** Duplicate changing mechanical JSON Schema in `ste-spec` unless a
handoff requirement explicitly demands it.

## Golden contract bundles (anti-drift gate)

**Informative** JSON under `contracts/examples/` illustrates shape only.

For **machine-verifiable** convergence, use **golden contract bundles** (pinned
fragment sets, stable `ArchitectureEvidence` / `KernelAdmissionAssessment` fixtures
where applicable, and expected **`Compiled_IR_Document`** identity such as
`document_id` or canonical byte hash per **`ir_version`**) exercised by **`ste-kernel`**
verify commands or CI jobs that invoke them. That gate catches schema staleness and
integration regressions without elevating narrative examples to normative truth.

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
| **ArchitectureEvidence** | Runtime output | `ste-runtime` produces; `ste-kernel` consumes |
| **Compiled_IR_Document** | Merged validated IR | **Derived** by `ste-kernel` from fragments + mapping rules |
| **KernelAdmissionAssessment** | Admission JSON | **Derived** by `ste-kernel` from projected slice + policy |

## Related orientation

- `architecture/STE-Reference-Embodiment.md`
- `architecture/STE-Architecture-Intermediate-Representation.md`
- `architecture/STE-Determinism-and-Canonical-Identity.md`
- `invariants/STE-Failure-Taxonomy-Boundaries.md`
- `execution/STE-Kernel-Execution-Model.md`
