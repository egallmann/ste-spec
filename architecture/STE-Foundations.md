# STE Foundations  
## Canonical Conceptual Foundations of the System of Thought Engineering (STE)

# 1. Purpose of This Document
This file defines the **conceptual foundations** that govern how STE structures, bounds, and interprets cognition.  
These foundations are prerequisites for all invariant layers, the divergence taxonomy, artifact specifications, validators, and synchronization mechanisms.

Its goals are to:

- establish the core principles that anchor deterministic reasoning  
- define the constraints that prevent drift and implicit state  
- articulate the conceptual model used by all STE components  
- provide a stable substrate for the invariant hierarchy  

This file is canonical and must remain aligned with:

- STE-Manifest  
- STE-Prime-Invariant  
- STE-System-Invariants  
- STE-Invariant-Hierarchy  
- STE-Divergence-Taxonomy  
- STE-Artifact-Specifications  
- STE-Cognitive-Execution-Model
- STE-RECON-Protocol
- STE-Integration-Model
- STE-Architecture-Intermediate-Representation
- STE-Kernel-Execution-Model

---

# 2. Core Principles of STE

## 2.1 Explicitness Over Implicitness
STE enforces the Prime Invariant:

**No undeclared reasoning.**

All assumptions must be explicit.  
All boundaries must be declared.  
All conceptual constructs must be defined within the framework.

Implicit knowledge is treated as drift.

**Formal Definition:** See `/.ste/core/STE-Prime-Invariant.md` for the five enumerated Prime Invariant constraints (PRIME-1 through PRIME-5).

---

## 2.2 Deterministic Cognition Through Constraints
STE does not pursue determinism through behavior prediction.  
STE achieves determinism through **constraint engineering**, enforced by:

- layered invariants  
- validated documentation-state  
- divergence detection and reconciliation  
- structural rules governing all artifacts  
- RECON-driven bootstrap of explicit state  

When constraints are explicit, the cognitive path becomes predictable.

**Formal Definition:** See `/.ste/core/STE-System-Invariants.md` for the sixteen enumerated System Invariants (SYS-1 through SYS-16) that operationalize the Prime Invariant into system-wide constraints.

---

## 2.3 Separation of Definition and Execution
STE cleanly separates:

- **what must be true** (invariants)  
- **what is declared** (documentation-state)  
- **how cognition proceeds** (execution model)  
- **how correctness is enforced** (validators)  
- **how state is bootstrapped** (RECON protocol)  

This separation ensures clarity, stability, and non-overlapping responsibilities.

---

## 2.3a Documentation-State, Integration-State, and Runtime Evidence

STE **MUST** treat three related planes as distinct:

1. **Documentation-state** — governed declarations in repositories (AI-DOC, ADRs, manifests, schemas). Documentation-state is authoritative for what the organization has declared, within the competence of each declaring source; it is not, by itself, a record of everything the embodied system contains.
2. **Integration-state** — the merged, validated **`Compiled_IR_Document`** consumed by `ste-kernel` for orchestration and admission projection. Integration-state is the mechanical instantiation of **Architecture IR** at a pinned `ir_version`; **normative semantics** for that IR (entities, relationships, provenance classes, lifecycle, completeness, governance, Architecture Index) live in `architecture/STE-Architecture-Intermediate-Representation.md`, while **JSON Schema and compiled enumerations** remain **referenced** from `ste-kernel` per `contracts/README.md`.
3. **Runtime evidence** — factual **`ArchitectureEvidence`** from `ste-runtime` (bundle health, freshness); non-decision-bearing at the handoff boundary.

These planes do not substitute for one another. Compiling or projecting documentation-state into integration-state does not add authority the source declarations lack, and Runtime evidence does not become architectural intent by being observed ([ADR-L-0044](../adrs/adr-projection/logical/ADR-L-0044-governed-semantic-reasoning-foundation.md) INV-4407, INV-4410). State that no plane declares or establishes remains unknown (§3.3).

Normative handoff contracts and roles: `architecture/STE-Integration-Model.md`, `execution/STE-Kernel-Execution-Model.md`, `glossary.md`.

**Documentation-state map:** `architecture/STE-Canonical-Project-Artifacts.md`.

**Non-optional integration subset (registry):** `architecture/STE-System-Core.md`.

**Informative (human-first):** how workspace cognition and the integration spine relate
as **one design problem with two operational faces** — see section **One design problem,
two operational faces (human-first)** in `architecture/STE-Reference-Embodiment.md`.

---

## 2.4 Drift Prevention as a First-Class Objective
STE treats drift not as failure but as a detectable and correctable condition.

All forms of drift—semantic, structural, documentation-state, or conceptual—must be surfaced via divergence and corrected before execution continues.

Drift is expected.  
Uncorrected drift is prohibited.

---

## 2.5 Layered Reasoning
STE's hierarchical structure ensures that:

- higher-level constraints dominate  
- lower-level invariants specialize without contradiction  
- artifact specifications reinforce consistency  
- documentation-state provides the declared state reasoning relies on  
- synchronization rules maintain coherence  

Layering creates predictable cognitive boundaries.

---

## 2.6 Deterministic Documentation-State
Documentation-state (AI-DOC) is the substrate that grounds reasoning.  
It enables a stateless model to operate deterministically by supplying:

- inventories  
- schemas  
- system state  
- decisions (ADR)  
- diagnostics (RCA)  
- operational definitions  

STE requires documentation-state to be accurate, explicit, complete, and validated at all checkpoints.

---

# 3. STE Conceptual Model

## 3.1 Invariants as Cognitive Law
Invariants define **what must always hold** during reasoning.

They:

- bound cognition  
- remove ambiguity  
- eliminate implicit assumptions  
- enforce deterministic structures  
- define permissible transformations  

Invariants must be:

- explicit  
- non-narrative  
- non-persuasive  
- internally consistent  
- mapped to divergence types  
- placed in the correct hierarchy layer  

**Invariant vs Rule:** In STE doctrine and the invariant hierarchy, use **invariant** for normative constraints. In the **integration plane**, **rules** are additionally a distinct artifact class (for example governance rules from `ste-rules-library`) and map to IR **`rule`** entities where applicable. **MUST NOT** treat “invariant” and “rule” as interchangeable when discussing Architecture IR or kernel admission inputs.

---

## 3.2 Divergence as Signal, Not Error
STE treats inconsistency as **divergence**, which must be:

1. detected  
2. classified  
3. corrected  
4. revalidated  
5. reconverged  

Divergence is the core mechanism for preventing drift and maintaining the integrity of the cognitive system.

---

## 3.3 Documentation-State as Authoritative Declared State
Documentation-state expresses the **current declared state** of the system: what the organization has explicitly declared, within the competence of each declaring source. It is the authoritative input for governed reasoning; it is not, by itself, proof of what the embodied system contains.

It must:

- be accurate and current for what it declares  
- precede reasoning  
- be updated before cognitive steps that depend on it  
- be validated at required checkpoints  

Undocumented state must not influence governed reasoning. This constrains reasoning inputs; it is not a claim about the system. Absence from documentation-state does not establish that something does not exist. What no competent source establishes remains **unknown**, and reasoning must not resolve it into existence or nonexistence by assumption. A negative conclusion requires a competent source that establishes it within a bounded scope.

---

## 3.4 Validators as Enforcement Mechanisms
Validators enforce correctness across:

- structure  
- semantics  
- documentation-state  
- taxonomy alignment  
- hierarchy consistency  

Validators do not introduce new rules.  
Validators execute existing rules.

---

## 3.5 Synchronization as a System Requirement
The STE Framework Synchronization Layer ensures:

- file placement correctness  
- inventory completeness  
- naming consistency  
- cross-file alignment  
- cohesion across all artifacts  

Synchronization prevents the framework itself from drifting.

---

# 4. Conceptual Responsibilities of STE Components

| Component | Responsibility |
|----------|----------------|
| **Invariants** | Bound cognition through explicit constraints |
| **Taxonomy** | Classify and route divergence |
| **Artifact Specifications** | Define structure and formatting rules |
| **Documentation-State** | Express authoritative declared project state |
| **Validators** | Enforce rule correctness and consistency |
| **Execution Model** | Govern how reasoning proceeds |
| **Sync Layer** | Maintain coherence of the entire framework |
| **RECON Protocol** | Bootstrap explicit state from existing artifacts |
| **Multi-repository integration** | Adapter publication surfaces, merged Architecture IR, kernel admission (`architecture/STE-System-Components-and-Responsibilities.md`) |

All components must work together.  
None may contradict another.

## 4.1 Worked example (informative)

For **one** onboarding narrative that threads workspace tooling, optional scoped
agent passes, publication surfaces, and `ste-kernel` consumption—without adding
MUSTs—read `architecture/STE-Worked-Example-Walkthrough.md`. See also the **reading
legend** in `README.md` and `architecture/STE-Manifest.md`.

---

# 5. Essential STE Properties

## 5.1 No Implicit State
All state that reasoning relies on must be explicit in documentation-state (AI-DOC).  
Anything not documented must not influence reasoning.

## 5.2 No Undeclared Concepts
All terminology must be defined within the framework.

## 5.3 No Skipped Validation
Checkpoints and validators are mandatory.  
Skipping them invalidates all dependent outputs.

## 5.4 No Out-of-Bound Reasoning
Reasoning beyond declared scope triggers divergence.

## 5.5 No Partial Updates
Documentation-state must be updated completely before reasoning.

---

# 6. Dependencies
This file depends on:

- STE-Prime-Invariant (formal Prime Invariant definitions)  
- STE-System-Invariants (formal System Invariant definitions)  
- STE-Manifest  
- STE-Invariant-Hierarchy  
- STE-Divergence-Taxonomy  
- STE-Artifact-Specifications  

It does not override any higher-level invariant.

---

# 7. Canon Status
This file is canonical.  
Changes require:

- Framework Validator approval  
- Inventory update  
- Directory verification  
- Reconvergence under divergence rules  

All reasoning must remain consistent with these foundations.

