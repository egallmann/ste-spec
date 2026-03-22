# STE Reference Embodiment (informative)

## Status

**Informative only.** This document does not add, remove, or restate normative MUSTs.
Normative authority remains in `contracts/`, `invariants/`, `adr/`, and the referenced
Architecture IR bundle in `ste-kernel` (see `contracts/README.md`).

---

## Purpose

Provide one **guided path** through **core concepts** and identify the **reference STE
system**: the converged repositories that implement the **integration plane** under
`ste-spec` contracts. Use this file for **onboarding and orientation**, not as a second
specification.

---

## Dedicated worked example (onboarding thread)

For a **single** narrative that walks from **workspace / IDE rule packs** and optional
**scoped design agents** (ADR-L / ADR-PS / ADR-PC) through **publication surfaces** to
`ste-kernel` boot semantics—explicitly **informative**—read
`architecture/STE-Worked-Example-Walkthrough.md`. It complements this spine without
turning this file into a long tutorial.

---

## Projection engine and conversation-engine (informative)

**Projection-engine–first** means: **one pipeline** resolves **stable IDs**, **versions**,
and **caches** for ADR slices, **rule projections**, and **decision references**; every
**surface** (IDE rule injection, chat UI, agent tool payloads, PR comment renderers) is
an **adapter** that **serializes or styles** those slices—not a second authority that
retypes rules or ADR prose from memory.

**Trust boundaries:**

- **Authority** lives in **declared artifacts** (documentation-state, publication
  surfaces, signed envelopes from the **rules-engine**).
- **Conversation-engine** orchestrates **turns and UX**; it **MUST NOT** silently
  substitute ad hoc text where a **projection** or **verdict** is required for a gate.
- **Adjudication** (closure, signing, attestation acceptance) stays **off the default
  chat hot path** except when a **gate** explicitly requests a **verdict slice**—see
  `execution/STE-Kernel-Execution-Model.md` (**Rules projections and adjudication**).

---

## One design problem, two operational faces (human-first)

STE is trying to solve **one** kind of problem: how to keep a system of thought **honest**
over time—so what people *say* the system is, what the tools *see*, and what can *run*
without silent drift stay connected.

That problem shows up in **two different places**: in the **day-to-day design
conversation** (where Cognitive Execution Model–style discipline forces explicit state
and reconciliation), and in the **integration spine** (where IR fragments,
`ArchitectureEvidence`, and kernel IR/admission make cross-repo truth **machine-checkable**
at declared boundaries).

Those are **not** the same mechanism, and the normative specification should not blur
them—but they **only stay aligned** if implementations accept a **tight architecture
schema**: invariants and artifact rules, plus **normative contracts** wherever the
handshake is real.

The practical bet is to **operationalize the conversation**: turn agreements into
**artifacts on known surfaces**, so “embodied STE” means something you can **point to**,
not something you *remember* the team meant.

---

## Relationship to the normative specification

The normative specification defines requirements. The reference repositories are an
**embodiment** of those contracts under continued integration work. This document does
not narrate project history; it orients readers to the **current** reference layout.

---

## Core concepts (read in order)

1. `architecture/STE-Foundations.md` — principles; documentation-state vs integration-state vs evidence
2. `glossary.md` — shared terms (Invariant Kernel vs `ste-kernel`, IR, fragments, publication surfaces)
3. `invariants/STE-Invariant-Hierarchy.md` — layering and precedence
4. `invariants/STE-Divergence-Taxonomy.md` — cognitive / documentation-state divergence
5. `invariants/STE-Failure-Taxonomy-Boundaries.md` — divergence vs boot/IR vs admission layers
6. `invariants/STE-Cross-Component-Contract-Invariants.md` — runtime/kernel handoff index (INV-000x)
7. `invariants/STE-Artifact-Specifications.md` — artifact-layer structure (where applicable)
8. `architecture/STE-Canonical-Project-Artifacts.md` — canonical artifact classes by repository

Then continue with **integration** and **execution** per `architecture/STE-Manifest.md`.

---

## Reference repositories (example embodiment)

| Repository | Role in the reference system | Visibility |
|------------|------------------------------|------------|
| **ste-spec** | Normative contracts, invariants, ADRs; publishes spec IR fragments | **public reference** |
| **adr-architecture-kit** | ADR authoring and validation; publishes ADR IR fragments | **public reference** |
| **ste-runtime** | Semantic extraction; publishes `ArchitectureEvidence` | **public reference** |
| **ste-rules-library** | Rule artifacts; publishes rules IR fragments | **public reference** |
| **ste-kernel** | Merge, IR validation, admission; consumes publication surfaces | **public reference** |

**Visibility** means **role in the minimum public integration star**, not whether a repo
is private. **Open-sourcing** an additional module does **not** by itself make it a sixth
**adapter leg**; only a **published adapter contract** and merge policy change can do that.

Optional tooling (for example a **conversational integration** or **transpiler** layer)
**MAY** appear in a future row as **`optional extension`** or **`premium / OSS TBD`** when
you publish and scope it; until then it is out of scope for this table.

**Governance hub (informative):** A **scale-agnostic** optional product (solo dev through
enterprise) for **attestations**, **registry**, and **first-class CI / merge-path verify**
is **not** part of the minimum integration star above. Name it **without** the **ADR-V**
prefix—**`ADR-V-*`** in `ste-kernel` means **vision** logical ADRs (see
`ste-kernel/adrs/logical/ADR-V-0001-kernel-control-plane-ir-mediated-evolution.yaml` and
`glossary.md`). Kernel **control plane** direction for **IR-mediated evolution** is
summarized in `execution/STE-Kernel-Execution-Model.md` (**Kernel control plane
vision**).

---

## Convergence, examples, and golden bundles

**Informative** JSON under `contracts/examples/` illustrates contract shape only.

**Machine-checkable** convergence is expected to use **golden contract bundles** and
`ste-kernel` (or CI jobs invoking it): pinned inputs, expected `Compiled_IR_Document`
identity where stable, and schema validation. See `contracts/README.md`.

---

## Related

- `architecture/STE-Worked-Example-Walkthrough.md`
- `architecture/STE-Manifest.md`
- `architecture/STE-System-Core.md`
- `architecture/STE-Integration-Model.md`
- `execution/STE-Kernel-Execution-Model.md`

## Canon Status

This file is **informative orientation** for the reference STE system; it is not a
normative contract surface.
