# STE Kernel Execution Model

## Purpose

This document defines the **normative execution sequence** and **normative
kernel enforcement contract** for `ste-kernel` integration: boot through
admission. Field-level rules and schema mechanics are in `ste-spec/contracts/`
and the referenced IR bundle under `ste-kernel`.

---

## Conformance scope

This sequence is **normative** for **STE kernel integration conformance**. Teams
**MAY** omit `ste-kernel` from local workflows, but **MUST NOT** claim interchange
compatibility with the Architecture IR admission path while altering the ordered
phases, merge precedence, or fail-closed rules defined by the referenced kernel
contracts.

---

## Sequencing (normative)

**MUST** execute in order; each phase completes before the next begins.

1. **Workspace discovery** — Resolve project root and contract-relevant paths deterministically.
2. **Adapter resolution** — Verify required adapters are reachable per boot profile.
3. **Artifact loading** — Eagerly load publication-surface artifacts (fragments, evidence) required for this boot.
4. **IR compilation (merge)** — Produce a single merged document candidate (`Compiled_IR_Document` semantics) using fixed adapter precedence.
5. **IR validation** — Validate merged IR against the Architecture IR schema and normative IR rules.
6. **Kernel ready** — Expose immutable boot result (validated IR snapshot handle, adapter status, freshness summary) as defined by kernel documentation.
7. **Admission evaluation** — Evaluate policy using **only** the projected admission slice and context overlay; emit **`KernelAdmissionAssessment`**.

**MUST NOT:** Admission evaluation MUST NOT run on unvalidated IR.

---

## IR validation vs admission evaluation

| Concern | Owner | Fails when |
|--------|-------|------------|
| **IR validation** | `ste-kernel` IR validator | Schema/provenance/graph contract violations |
| **Admission evaluation** | `ste-kernel` admission | Policy/eligibility blocking, acknowledgements |

**MUST:** IR validation failures are **boot/integration failures**, not “policy
deny” outcomes masquerading as admission success.

**MUST NOT:** Admission logic MUST NOT re-merge or re-validate full IR (see
kernel `IR_INGESTION_PIPELINE.md` — informative reference).

---

## Runtime evidence vs admission decision

**MUST:** `ste-runtime` emits **`ArchitectureEvidence`** only.

**MUST:** `ste-kernel` emits **`KernelAdmissionAssessment`** only at the
handoff boundary.

**MUST NOT:** Evidence payloads MUST NOT embed caller-facing admission decision
semantics.

---

## Fail-closed behavior

**MUST:** Boot failure aborts before admission; CLI MUST NOT emit success
admission JSON alongside boot failure (kernel boot contract).

**MUST:** Invalid or incomplete evidence handling follows INV-0006 and related
handoff invariants.

**MUST:** If required execution prerequisites cannot be verified, the kernel
fails closed and refuses execution eligibility.

---

## Kernel Enforcement Model

### Kernel Enforcement Responsibility

`ste-kernel` is the deterministic enforcement control point at the integration
and admission boundary.

`ste-kernel` is responsible for:

- verifying artifact authority
- verifying required lifecycle state
- determining execution eligibility
- refusing execution when required conditions are not satisfied
- recording enforcement decisions and violations

### Kernel Is Not An Authority Creator

**MUST:** The Kernel does not create authority.

**MUST:** The Kernel enforces authority defined by accepted artifacts,
lifecycle state, and governance configuration.

### Kernel Inputs

Kernel inputs are:

- ADR artifacts required for the active execution scope
- Manifest inputs
- Architecture Index inputs
- rules inputs available on declared publication surfaces
- lifecycle state and accepted-status inputs
- evidence inputs
- governance configuration inputs
- environment and system context required by the active enforcement path

### Kernel Outputs

Kernel outputs are:

- execution allowed or denied
- violations
- required lifecycle transitions or missing prerequisites
- audit record
- enforcement decision log

## Execution Eligibility Matrix

`Publication` is a lifecycle role, not an artifact class. Projection artifacts
are derived representational outputs and are not execution-authorizing inputs.

| Artifact / Input | Required lifecycle state | Required authority condition | Kernel may use artifact? | Kernel must block execution if invalid or unverifiable? |
| --- | --- | --- | --- | --- |
| ADR-L | `Accepted` | Accepted normative authority in `ste-spec` or accepted authoritative source referenced by doctrine | Yes | Yes, when required for the active execution scope |
| ADR-PS | `Accepted` | Accepted normative authority | Yes | Yes, when required for the active execution scope |
| ADR-PC | `Accepted` | Accepted normative authority | Yes | Yes, when required for the active execution scope |
| Rules | `Published`, or equivalent active availability on the declared publication surface | Published rule inputs are available from their accepted authority surface; rule projections or decision records are not self-authorizing | Yes | Yes, when required by the active enforcement path |
| Manifest | `Accepted`, or current published repository authority surface where the enforcement path depends on it | Authoritative manifest surface is current enough for the enforcement path being used | Yes | Yes, if the manifest is required to resolve required kernel inputs |
| Architecture Index | `Assessed`, or latest accepted or published governance snapshot as applicable to the enforcement path | Used as governance or system-state input and not as replacement normative authority | Yes | Yes, when the active enforcement path declares index completeness or gap status as required |
| Evidence | `Observed` | Factual evidence only, valid within the evidence boundary | Yes | Yes |
| Governance configuration | `Assessed` and/or `Remediated`, as applicable to current governance completeness | Accepted governance-side inputs are complete enough for the execution path; draft governance-decision contracts are not mandatory authority sources | Yes | Yes, when governance completeness is required and cannot be verified |

## Kernel Execution Eligibility Checklist

Before allowing execution, the kernel evaluates this checklist against the
active execution scope:

- required Logical ADRs are accepted
- required Physical-System ADR is accepted
- required Physical-Component ADRs are accepted
- required rules inputs are active and available on declared publication surfaces
- no blocking gaps or violations exist for the requested execution path
- required manifest input is current and loadable
- required Architecture Index input is present when the active enforcement path depends on governance or system-state completeness
- governance configuration is complete enough for the requested execution path
- required invariants are satisfied
- required evidence checks pass
- required lifecycle state for each execution-authorizing input is verified

**MUST:** If any required checklist condition fails or cannot be verified, the
Kernel MUST refuse execution.

**MUST:** `cannot be verified` and `verified as failing` both produce refusal.

**MUST:** Checklist evaluation is deterministic and replayable from the same
input set.

**MUST NOT:** The kernel MUST NOT infer missing acceptance, missing authority,
or missing governance completeness.

## Audit and Traceability Requirement

**MUST:** The kernel must produce an audit-capable enforcement decision record
for every allow or deny result.

The enforcement record must include:

- what was checked
- what passed
- what failed
- why execution was allowed or denied
- which artifact versions or identities were used
- which lifecycle states were relied on
- which authority conditions were relied on

The audit record is an output of enforcement, not a new authority source. It
does not create authority; it documents enforcement of existing authority.

---

## Referenced mechanical specifications (informative anchors)

Authoritative for merge order, identity, serialization, and boot failure classes:

- `ste-kernel/documentation/BOOT_SEQUENCE.md`
- `ste-kernel/documentation/IR_INGESTION_PIPELINE.md`
- `ste-kernel/documentation/ARCHITECTURE_IR.md`
- `ste-kernel/architecture-ir/architecture-ir.yaml`
- `ste-kernel/architecture-ir/architecture-ir.schema.json`
- `ste-kernel/contracts/adapter-contracts.yaml`

---

## Kernel control plane vision (informative)

`ste-kernel` publishes **vision** logical ADRs whose IDs use the **`ADR-V-*`**
prefix (**V** = **vision** in this taxonomy, not “verification” or a product name).
**ADR-V-0001** (*Kernel Control Plane IR-Mediated Evolution*) states that the kernel
behaves as a **workspace control plane** that evolves primarily through **validated
integration IR** produced by the adr-kit compiler, while **human-authored ADRs** stay
authoritative at their home repositories and assistant-facing behavior depends on
**explicit, checkable bundles**. Source:
`ste-kernel/adrs/logical/ADR-V-0001-kernel-control-plane-ir-mediated-evolution.yaml`
(status and promotion are kernel-owned; this pointer is **informative**).

A **separate governance hub** (attestation registry, deterministic CI hooks, merge-path
verification—**scale-agnostic**, solo dev through org) **MAY** integrate with
`ste-kernel` like any other subsystem; **do not** label that product **ADR-V**, which
already names **vision** ADRs here.

---

## Rules projections and adjudication (informative)

**Terminology (one release):** Use these names consistently in orientation and tooling docs until a deliberate rename:

- **rules-engine** — Operational component (typically in `ste-rules-library`) that **materializes** rule projections: pins, identifiers, **closure hashes**, encoded payloads, optional signing.
- **governance-engine** — Product/surface that **stores and serves** durable **governance decisions** while **consuming** projections from the rules-engine (prototype may live **inside** `ste-rules-library`).
- **adjudicator** — **Role** at the boundary (verdict, replay, mechanical verify)—not a second product name competing with governance-engine.

**Orchestration choke point:** Interactive or on-demand **ADR-bound rule projections**
(name TBD) are **requested via `ste-kernel`** so ID resolution, policy, and publication
discipline stay centralized. The **rules-engine** (`ste-rules-library` operational
component) **materializes** projections: **identifiers**, **content hashes**, **ruleset
pins**, and the **encoded rule-closure structure** needed to reproduce checks—**normatively** it **MUST NOT** be treated as the long-lived store of **steelman outcomes,
merge decisions, or attestation registry rows**.

**Governance-engine / adjudicator (name TBD):** A **consumer of rule projections** from
the rules-engine. It **records and serves** durable **decisions** (verdicts, accepted
attestations, overrides, registry entries) while **relying** on the projection envelope
for **what was checked** and **which closure** applied. That keeps **checks mechanical**
(projection in hand → verify hash / signature / closure identity) without the
rules-engine owning decision history. **`ste-kernel` MAY** call into this service for
verify routes or **consume** the same projection artifacts **without** becoming the
authority for rule text or for storing governance decisions.

**Adapter IR for checks (optional):** Mechanical **check** definitions (lint-shaped gates,
policy hooks) **MAY** publish as **rules IR fragments** or a future **adapter-shaped IR**
surface so merge and CI share one encoded structure—only with published merge policy
(`ste-kernel/contracts/adapter-contracts.yaml`); avoid an implicit **sixth adapter**.

**In-process prototypes** colocating projection materialization and decision storage are
**transitional** until split and expressed in published contracts (draft envelope:
`contracts/rule-projection/`).

**Steelman / compliance gates** produce **documentation-state** or attested artifacts
held by the **governance** side, not **`KernelAdmissionAssessment`**. Keep **merge-path
CI** checks **mechanical** (reconstruct closure from the **same git tree**, verify
signatures) unless policy explicitly accepts non-deterministic steps.

---

## Authoring vs compilation (informative)

**Authoring** (for example ADR composition in `adr-architecture-kit`) and **semantic
extraction** (for example RECON/RSS-style tooling in `ste-runtime`) are separate from
**IR compilation** in `ste-kernel`. The **compiler of record** for merged, validated
**`Compiled_IR_Document`** semantics at the integration boundary is **`ste-kernel`**,
consuming only declared publication surfaces.

---

## Related Documents

- `glossary.md` (ADR-V vision ADR taxonomy)
- `architecture/STE-Integration-Model.md`
- `architecture/STE-System-Components-and-Responsibilities.md`
- `architecture/STE-Determinism-and-Canonical-Identity.md`
- `invariants/INV-0011-kernel-fails-closed-on-unverifiable-execution-prerequisites.md`
- `invariants/STE-Failure-Taxonomy-Boundaries.md`

## Canon Status

This file is **canonical** for the kernel execution viewpoint in `ste-spec`.
