# STE Worked Example Walkthrough (informative)

## Status

**Informative only.** This file is a **single threaded story** that ties together
workspace cognition, optional agent-shaped tooling, and the **integration plane**. It
does **not** add MUSTs. **Normative** requirements remain in `contracts/`,
`invariants/`, binding `adr/`, and the referenced Architecture IR bundle in
`ste-kernel`.

**How to read STE:** see the short legend in `README.md` and
`architecture/STE-Manifest.md` (normative vs orientation vs worked example).

---

## Why this exists

Readers can understand **fragments**, **evidence**, and **kernel boot** mechanically,
yet still ask: *what does a team actually do, in order?* This walkthrough answers that
at **narrative** depth. Replace names and tools with your own; keep the **boundary**
discipline.

---

## Cast (fictional, minimal)

**Team** is shipping a small internal service. **Repos in play** match the reference
star: `adr-architecture-kit`, `ste-spec`, `ste-runtime`, `ste-rules-library`,
`ste-kernel`. **Product-shaped pieces** below are **illustrative** implementations,
not required adapters.

| Illustrative piece | Role in the story |
|--------------------|-------------------|
| **Conversation-engine** | Orchestrates turns; **projection-engine–first** with **adapters** (IDE, chat, agent tools) so responses are **views** of the same **projection IDs / versions** as kernel and CI—not parallel copies of rules or ADR prose. **Adapters** differ by **serialization and affordances** only; they do not introduce shadow rule text. Heavy **adjudication** runs on **explicit gates** (steelman, merge verify), not every token. |
| **Design interrogation subsystem** | Optional **orchestrated agents** (for example a LangGraph-style graph) running **narrow subagents**—not a single general coding agent—for **ADR-L**, **ADR-PS**, and **ADR-PC** drafting and Q&A. |
| **`ste-rules-library`** | Supplies **rule artifacts** (acceptable vs banned stacks, prompts-as-rules, cooperative checks) consumed as **rules IR fragments** where applicable. |
| **`adr-architecture-kit`** | Templates and validation for structured ADRs; emits **ADR IR fragments** on declared surfaces. |
| **`ste-runtime`** | RECON/RSS-style extraction; emits factual **`ArchitectureEvidence`**. |
| **`ste-kernel`** | Loads publication surfaces, merges/validates IR, evaluates admission; **orchestrates** consumption of **rule projections** / **adjudicator** verdicts from the **rules-engine** (does not own rule semantics). |
| **Governance hub** (name TBD) | **Optional**, **scale-agnostic** (solo through org): attestation registry, **deterministic CI / merge-path verify** (CLI or reusable workflow), merge-friendly output—**not** `ste-kernel` internals; integrates via published surfaces like any subsystem. **Not** called **ADR-V**; in this taxonomy **`ADR-V-*`** = **vision** ADRs in `ste-kernel` (see `execution/STE-Kernel-Execution-Model.md`, **Kernel control plane vision**). |

**MUST NOT:** Open-sourcing or deploying a conversational subsystem **does not** by
itself extend the kernel adapter star. Only **published adapter contracts** and merge
policy changes can do that (`architecture/STE-Reference-Embodiment.md`).

---

## Thread (end-to-end)

1. **Load workspace discipline** — The conversation-engine activates **IDE rule packs**
   aligned to `ste-spec` doctrine and forked technology rules from
   `ste-rules-library`. The goal is **bounded questions** and **explicit** stack
   choices before prose explodes.

2. **Early design passes (optional model sizing)** — For tightly scoped prompts
   (checklists, table-filling, first-cut ADR sections), a **smaller** language model
   **may** run under those packs. This is a **cost/latency** choice, not a spec
   requirement.

3. **Structured ADR work** — Subagents handle **ADR-L** (logical decision),
   **ADR-PS** / **ADR-PC** (physical / component slices per your kit’s definitions) with
   **separate system prompts and tools**—each pass has a **narrow contract** (what it
   may edit, what it must cite, which validators must pass). A **stronger** model then
   performs a **steelman** pass as a **targeted compliance / convergence** check: the
   plan is validated against **authoritative rule projections** (not generic lint),
   still producing **documentation-state** artifacts—not admission decisions. Record
   outcomes in a **rule projection envelope** family when tooling exists (draft schema:
   `contracts/rule-projection/rule-projection-envelope.schema.json`; see `glossary.md`
   **Steelman gate**, **Rule projection**). The **adjudicator** (rules-engine boundary)
   owns **closure + signing**; **`ste-kernel`** later **verifies** or routes those
   bundles—**cheap in-process prototypes** are OK until the contracted boundary ships.
   If a coding-oriented reviewer **disagrees**, a **human** may **override**; record the
   outcome as a **decision** per your **contracts** (shape TBD)—optionally as an
   **ID-only** reference from impacted ADRs.

4. **Publish integration inputs** — ADR kit writes **ADR IR fragments**;
   `ste-spec` publishes **`spec-ir-fragments.json`**; rules library publishes **rules IR
   fragments**; `ste-runtime` publishes **`ArchitectureEvidence`**. Paths are **only**
   those declared as publication surfaces (`architecture/STE-Integration-Model.md`,
   `ste-kernel/documentation/BOOT_SEQUENCE.md`).

5. **Kernel boot and admission** — `ste-kernel` loads fragments and evidence,
   merges in fixed order, validates IR, then emits **`KernelAdmissionAssessment`** per
   contracts. IR validation failures remain **errors/boot failures**, not taxonomy
   **divergence** unless you explicitly route them there for analysis
   (`invariants/STE-Failure-Taxonomy-Boundaries.md`).

6. **Human gate still exists** — Even with agents, **merge approval**, **CI**, and
   **invariant evolution** remain organizational responsibilities. Agents accelerate
   drafting; they do not replace declared authority surfaces.

7. **Optional governance verify** — **Reference pattern (informative):** `ste-rules-library`
   ships a **mechanical** prototype: `scripts/governance_cli.py` **`project`** (write
   **rule projection envelope** + **closure hash**) then **`validate-hash`** / **`verify`**
   on the **merge path** (stable exit codes, **no LLM**). CI example:
   `.github/workflows/governance-cli.yml` in that repo. Decision rows **MAY** append via
   **`record`** to `.ste/governance/decisions.jsonl` (see `ste-spec/contracts/governance-decision-record/`).
   This is **orthogonal** to **IR validation** and **admission** in `ste-kernel`.
   **Merge-path verify is commit-scoped:** mechanical checks recompute from the **same
   git revision** the merge is about; otherwise **closure hashes attest nothing**. That
   keeps **documentation-state**, **rule closure**, and **CI** from drifting into **two
   competing truths**—aligned with STE’s **honesty-at-boundaries** posture (pins must be
   **addressable** from the tree under verify). **Offline adjudicator** semantics:
   `execution/STE-Kernel-Execution-Model.md` (**Rules projections and adjudication**).

---

## Where to go next (normative and orientation)

- Boundaries and diagram: `architecture/STE-Integration-Model.md`
- Boot sequence concept: `execution/STE-Kernel-Execution-Model.md`
- Handoff schemas: `contracts/README.md`
- Cognitive lifecycle (parallel track): `execution/STE-Cognitive-Execution-Model.md`
- Reference repo roles: `architecture/STE-Reference-Embodiment.md`

## Canon Status

This file is **informative illustration** for onboarding; it is not a normative
contract surface.
