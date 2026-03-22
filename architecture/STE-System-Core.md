# STE-system-core (workspace and integration obligations)

## Purpose

**STE-system-core** names a **small, explicit** set of obligations that **MUST** hold
for STE to deliver its **advertised guarantees** at the **workspace** and **integration**
handoff boundaries. This is distinct from **optional** or **forkable** material in
`ste-rules-library` (technology rules, cooperative signals, project overlays).

This document **does not** add new MUSTs beyond what is already published in
`contracts/`, `invariants/`, and `adr/`; it **indexes** the core boundary.

---

## Core integration obligations (handoff)

These are **non-optional** for **STE kernel integration conformance** (Architecture IR
merge and admission interchange):

- Handoff contract schemas: `contracts/architecture-evidence.schema.json`,
  `contracts/kernel-admission-assessment.schema.json`
- Cross-component invariants: `invariants/STE-Cross-Component-Contract-Invariants.md`
  (INV-0001–INV-0009)
- Role split: `adr/ADR-031-runtime-kernel-responsibility-boundary.md`
- Architecture IR mechanical bundle: pinned in `contracts/architecture-ir-kernel-contract-pin.json`
  and referenced from `contracts/README.md`
- Adapter import policy: `ste-kernel/contracts/adapter-contracts.yaml` (kernel-owned)

**MUST NOT:** Forking or replacing `ste-rules-library` content **does not** remove these
obligations.

---

## Core workspace obligations (doctrine)

Workspace cognition guarantees assume alignment with **STE doctrine** surfaces,
including at minimum:

- `architecture/STE-Foundations.md`
- `invariants/STE-Invariant-Hierarchy.md`
- `execution/STE-Cognitive-Execution-Model.md`
- `invariants/STE-Divergence-Taxonomy.md`

Exact “full STE” workspace posture is **product and policy** dependent; ste-spec
remains the **normative** source for what those documents require.

---

## Tagging convention (informative)

Future invariant or rule artifacts **MAY** declare a metadata tag **`ste-system-core`**
when they belong to this non-optional set. Until a machine index exists, this file
and `STE-Manifest.md` are the **human registry**.

---

## Related

- `architecture/STE-Reference-Embodiment.md`
- `architecture/STE-System-Components-and-Responsibilities.md`
- `glossary.md`

## Canon Status

This file is **canonical** for the **STE-system-core** registry viewpoint in `ste-spec`.
