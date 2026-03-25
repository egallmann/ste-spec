# STE System Components and Responsibilities

## Purpose

This document normatively defines **repository boundaries** for the converged STE
stack. It complements workspace-oriented doctrine (`STE-Foundations.md`,
`STE-Cognitive-Execution-Model.md`) with the **integration plane** bounded by
`ste-kernel`, adapter publication surfaces, and `ste-spec` handoff contracts.

**Informative:** Each repository may contain additional internal documentation;
this file states only cross-repo obligations.

---

## Responsibility Table

| Repository | MUST provide | MUST NOT | Publishes (examples) | Consumes (examples) |
|------------|--------------|----------|----------------------|----------------------|
| **ste-spec** | Normative definitions; JSON Schemas for runtime/kernel handoff; cross-component INV-000x; spec IR fragments | Implement kernel orchestration or runtime extraction | `contracts/architecture-evidence.schema.json`, `contracts/kernel-admission-assessment.schema.json`, `contracts/architecture-ir/spec-ir-fragments.json` | — (normative authority) |
| **adr-architecture-kit** | ADR schemas and validation; authoring/generation CLIs; ADR discovery artifacts within the kit; **ADR IR fragments** on the kernel publication surface | Emit `KernelAdmissionAssessment`; act as admission authority | ADR IR fragment file(s) per kernel boot contract (e.g. under `dist/` as documented by that repo) | `ste-spec` doctrine and schemas as applicable |
| **ste-runtime** | **`ArchitectureEvidence`** payloads; semantic extraction / graph tooling per repo maturity claims | Emit caller-facing admission decisions or `KernelAdmissionAssessment` | Evidence via subprocess/file contract consumed by `ste-kernel` | Project sources; `ste-spec` contracts as applicable |
| **ste-rules-library** | Rule and signal schemas; governance manifest; **rules IR fragments** on the kernel publication surface | Emit `KernelAdmissionAssessment` | Rules IR fragment file(s) per kernel boot contract | `ste-spec` / ADR doctrine as applicable |
| **ste-kernel** | Boot orchestration (when implemented), IR merge and validation, admission evaluation, deterministic execution eligibility enforcement, adapter import policy enforcement, enforcement decision and audit record production | Import sibling repo **internals**; treat derived graph caches as authoritative architecture truth; create authority instead of enforcing accepted authority; execute business logic or replace runtime systems or CI/CD | `Compiled_IR_Document` (internal/CLI); **`KernelAdmissionAssessment`**; enforcement decision and audit outputs | Adapter publication surfaces; `adapter-contracts.yaml`; referenced IR schema bundle in-repo |

---

## Open Boundary Note

The open-versus-closed architectural boundary is defined in
[`OPEN_CLOSED_BOUNDARY.md`](OPEN_CLOSED_BOUNDARY.md) and the public-compatible
surface inventory is defined in
[`PUBLIC_SYSTEM_SURFACES.md`](PUBLIC_SYSTEM_SURFACES.md).

Those documents identify which subsystem roles are:

- open and publicly standardizable
- mixed / interface-only
- closed in implementation while still publicly describable at the role level

## Authority Boundaries

### Documentation authority

**Authoritative:** Declared artifacts in repositories (ADRs, invariants, rules,
schemas, manifests). **`ste-kernel` MUST NOT** silently mutate these sources
based on evidence alone.

### Integration authority

**Authoritative:** Validated **`Compiled_IR_Document`** for the purpose of kernel
orchestration and admission **projection**, per the Architecture IR contract
referenced from `ste-spec`.

### Admission authority

**Authoritative:** **`KernelAdmissionAssessment`** is emitted **only** by
`ste-kernel` (see `adr/ADR-031-runtime-kernel-responsibility-boundary.md`,
`invariants/INV-0002-kernel-final-admission-authority.md`). `ste-kernel`
determines execution eligibility at the same boundary and does not emit
permissive caller-facing outcomes when required prerequisites are invalid or
unverifiable.

### Evidence authority

**Authoritative:** Factual bundle/freshness fields in **`ArchitectureEvidence`**
from `ste-runtime`. Evidence is **input** to kernel evaluation, not a decision
payload.

### Kernel enforcement and audit responsibility

**Authoritative responsibility:** `ste-kernel` enforces accepted authority,
verified lifecycle state, and required governance completeness at the admission
boundary. It does not create authority. It produces enforcement decision and
audit records that document what was checked and why execution was allowed or
denied. It does not perform the business execution it approves.

### Rule projection and adjudicator authority (informative)

**Authoritative** for **rule closure materialization**, **projection envelopes** (hashes,
identifiers, encoded closure, ruleset pins), and **signing / attestation of the projection
artifact** is the **rules-engine** side (`ste-rules-library` and its operational
components). **Durable governance decisions** (what was accepted at merge, registry rows,
override records) are **authoritative** for the **governance-engine / adjudicator**
(consumer of projections), not the rules-engine as the system of record. **`ste-kernel`**
**orchestrates** and **verifies or consumes** envelopes per published contracts (draft:
`contracts/rule-projection/`). See `architecture/STE-Integration-Model.md`
(**Adjudicator boundary**) and `execution/STE-Kernel-Execution-Model.md` (**Rules
projections and adjudication**).

---

## Conflicts Resolved in Specification (informative)

| Tension | Resolution in ste-spec |
|--------|-------------------------|
| Glossary historically discouraged “rule” in favor of “invariant” | **Invariant** remains doctrine term; **rule** is explicit for rules-library and IR `rule` entities (`glossary.md`). |
| “Kernel” in OS analogy vs product name | **Invariant Kernel** (concept) vs **`ste-kernel`** (product) (`glossary.md`). |
| Multiple compilers (kit vs runtime) | Authoring-time kit outputs vs runtime compilation posture are **repository-documented**; ste-spec defines **handoff contracts** and adapter surfaces, not internal compiler algorithms. |

---

## Dependencies

- `glossary.md`
- `architecture/STE-Integration-Model.md`
- `execution/STE-Kernel-Execution-Model.md`
- `contracts/README.md`
- `adr/ADR-030-contract-authority-in-ste-spec.md`
- `adr/ADR-031-runtime-kernel-responsibility-boundary.md`
- `adr/ADR-034-rule-projection-envelope-authority.md` (proposed)

## Canon Status

This file is **canonical** orientation for multi-repository responsibilities.
