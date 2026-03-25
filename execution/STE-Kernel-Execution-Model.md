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

### Kernel Boundary

Inside the Kernel:

- lifecycle enforcement authority
- authority verification authority
- execution eligibility decision authority
- rule enforcement authority
- admission control point
- audit producer

Outside the Kernel:

- business logic execution
- direct infrastructure deployment
- CI/CD replacement
- runtime system replacement
- authority creation
- governance decision creation

**MUST:** The kernel enforces accepted authority. It does not create new
authority or governance decisions.

**MUST:** The kernel is the admission and execution-eligibility control point.
It is not the actor that performs the business operation being approved.

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

### Definition of Execution

Execution is any action that:

- changes system state
- processes production data
- provisions or modifies infrastructure
- invokes workflows or agents
- produces externally visible effects

**MUST:** The kernel must approve execution before execution occurs.

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

## Execution Eligibility by Conformance State

| Conformance state | Execution eligible? | Kernel effect |
| --- | --- | --- |
| `Accepted` | No | Accepted intent alone is insufficient for execution eligibility. |
| `Implemented` | No | Implemented scope must still be verified for conformance. |
| `Verified` | Yes | Verified is the only execution-eligible conformance state for active scope. |
| `Divergent` | No | Drift or conflicting evidence blocks execution pending assessment. |
| `Non-conformant` | No | Confirmed violation blocks execution pending remediation. |
| `Suspended` | No | Governance- or enforcement-blocked scope remains non-executable. |
| `Retired` | No | Retired scope remains non-executable. |

## Minimum Required Artifact Set for Execution Eligibility

The minimum required artifact set for an execution-eligible system is:

- required Logical ADRs
- required Physical-System ADR
- required Physical-Component ADRs
- active rules
- current manifest
- current Architecture Index when the active enforcement path depends on governance or system-state completeness
- no blocking gaps or violations

This minimum set is enforced through the execution eligibility matrix and
checklist. Missing or unverifiable required artifacts make the execution
request non-eligible.

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
- referenced evidence subjects are present and valid
- active scope conformance state is `Verified`
- no current subject is in `Divergent`, `Non-conformant`, `Suspended`, or `Retired`
- required lifecycle state for each execution-authorizing input is verified

**MUST:** If any required checklist condition fails or cannot be verified, the
Kernel MUST refuse execution.

**MUST:** `cannot be verified` and `verified as failing` both produce refusal.

**MUST:** Checklist evaluation is deterministic and replayable from the same
input set.

**MUST NOT:** The kernel MUST NOT infer missing acceptance, missing authority,
or missing governance completeness.

## Evidence and Lifecycle Effects

This execution model does not add lifecycle states to the Spine.

- implementation deployed or otherwise realized remains within the existing
  `Implemented` state model and does not create a separate deployment state
- evidence that validates conformance supports continued use of `Observed`,
  `Assessed`, and existing downstream eligibility
- evidence that shows a violation produces a blocking or non-blocking
  enforcement status and feeds `Assessed` and `Remediated` through the
  existing governance flow
- incidents or severe violations do not create `Suspended` or `Review Required`
  as new lifecycle states; they are expressed as denial, blocking violation,
  and governance-required remediation within the existing Spine
- evidence is evaluated per referenced subject; subject linkage identifies what
  the evidence validates or invalidates without turning evidence into a
  caller-facing decision

**MUST:** The kernel considers required lifecycle state together with
evidence-derived enforcement status when determining execution eligibility.

**MUST:** The kernel considers conformance state, not only accepted status,
when determining execution eligibility.

See `architecture/STE-Spine-State-Model.md` for the conformance-state overlay,
lifecycle feedback transition table, and escalation definitions that govern how
subject-linked evidence affects execution eligibility.

## Violation Handling

**MUST:** The kernel denies execution for blocking violations.

**MUST:** The kernel records each blocking or non-blocking violation it relies
on during enforcement.

**MUST:** The kernel requires a lifecycle transition where accepted doctrine
already implies one.

**MUST:** The kernel produces an audit record for violation-driven allow or
deny outcomes.

Blocking violations cause denial. Non-blocking findings may be recorded without
permissive authority expansion. Unverifiable prerequisites are treated as
blocking for execution eligibility. Violation handling does not invent new
lifecycle states; it uses denial plus existing governance and remediation flow.

Invalidating evidence on a required subject moves the scope into `Divergent`
until assessed. Confirmed violation moves the scope into `Non-conformant`.
Blocking governance disposition or required hard stop moves the scope into
`Suspended`. Remediation plus re-verification returns the scope to `Verified`.
Retired scopes remain non-executable.

## Audit and Traceability Requirement

**MUST:** The kernel must produce an audit-capable enforcement decision record
for every allow or deny result.

The required decision record must include:

- execution allowed or denied
- reason
- artifacts evaluated
- lifecycle states used
- rules applied
- timestamp or equivalent decision-time marker
- artifact versions or identities used
- what was checked
- what passed
- what failed
- authority conditions relied on

The decision record is the audit-capable enforcement record for the allow or
deny outcome.

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
- `invariants/INV-0012-evidence-must-reference-evaluated-subjects.md`
- `invariants/STE-Failure-Taxonomy-Boundaries.md`

## Canon Status

This file is **canonical** for the kernel execution viewpoint in `ste-spec`.
