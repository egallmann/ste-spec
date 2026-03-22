# STE Glossary

## Purpose

This glossary defines terminology used throughout the STE architectural specification. Consistent use of these terms ensures precision and prevents ambiguity.

## Core Architectural Concepts

### System of Thought Engineering (STE)

An architectural framework for governing artificial intelligence cognition through explicit constraints, deterministic execution, and validated documentation-state. STE transforms raw LLM execution into bounded, deterministic reasoning through layered invariants, execution lifecycle stages, and divergence detection mechanisms.

### System-of-Interest

The scope of the STE architecture: the governance framework that constrains, validates, and directs AI cognition. Excludes implementation mechanisms, deployment topology, and operational procedures.

### Governance Framework

The complete set of constraints, protocols, validators, and execution semantics that bound AI reasoning. Operates as an AI Operating System, transforming unconstrained token generation into deterministic, validated cognition.

## State Planes

STE uses related but distinct state notions. **MUST** use the term that matches the plane being discussed.

### Documentation-State

The explicit, machine-readable substrate that grounds **workspace cognition** (AI-DOC, inventories, architecture prose, ADR sources). **Normative artifact classes** and publication roles by repository are mapped in [`architecture/STE-Canonical-Project-Artifacts.md`](architecture/STE-Canonical-Project-Artifacts.md). Documentation-state is authoritative for what the organization has **declared** about the system (distinct from **integration-state** and **runtime evidence**).

### Integration-State

The **compiled, merged Architecture IR** and its envelope (`Compiled_IR_Document`) that `ste-kernel` consumes for orchestration and admission. Integration-state is **derived** from publication surfaces and runtime evidence inputs. It is authoritative for **kernel integration decisions** only in the sense that the kernel MUST treat validated IR as the sole merged input to admission projection—not as a replacement for documentation-state in repositories.

### Runtime-State (evidence)

**Observed** signals about the workspace and tooling, carried in the `ArchitectureEvidence` contract (bundle health, freshness, diagnostics). Runtime-state is **factual evidence**, not architectural authority. It informs admission only through kernel evaluation of evidence-shaped fields, never by substituting for declared architecture.

## Invariant Hierarchy

### Prime Invariant

The highest-level constraint governing all STE reasoning. Prohibits implicit assumptions, undeclared state, unbounded reasoning, unvalidated modifications, and non-framework concepts. All other invariants derive from the Prime Invariant.

**Formal Definition**: Five enumerated constraints (PRIME-1 through PRIME-5) are summarized in [`invariants/STE-Invariant-Hierarchy.md`](invariants/STE-Invariant-Hierarchy.md) (section 2, Layer 1 — Prime Invariant). A standalone `STE-Prime-Invariant.md` is not published in this repository.

### System Invariants

Global rules governing the entire STE cognitive system. Define system-wide requirements for explicitness, determinism, validator enforcement, divergence resolution, and documentation-state discipline. Apply universally to all reasoning tasks, domains, and artifacts.

**Formal Definition**: Sixteen enumerated constraints (SYS-1 through SYS-16) are summarized in [`invariants/STE-Invariant-Hierarchy.md`](invariants/STE-Invariant-Hierarchy.md) (section 2, Layer 2 — System Invariants). A standalone `STE-System-Invariants.md` is not published in this repository.

**Note:** Files named `INV-0001-*.md` under `invariants/` are **cross-component contract invariants** for kernel/runtime handoffs. They use a different identifier scheme than **SYS-1–SYS-16** (doctrine system invariants).

### Domain Invariants

Constraints governing reasoning within a specific domain. Examples include AWS Domain Invariants, Documentation Domain Invariants, and IAM Subdomain Invariants. Must align with System Invariants and define bounded scope.

### Artifact Specifications

Structural and formatting rules for all STE artifacts. Define required sections, naming conventions, placement rules, and conformance requirements. Layer 4 of the Invariant Hierarchy.

### Invariant Layer

One of seven hierarchical constraint levels (Prime → System → Domain → Artifact → Documentation-State → Framework Synchronization → Meta-Invariants). Lower layers may specialize but cannot override higher layers.

### Invariant (STE doctrine sense)

A normative constraint in the invariant hierarchy, or a constraint declared in STE/ADR artifacts, expressed as **what must hold**. **MUST NOT** be treated as interchangeable with **Rule** in integration or IR contexts.

### Rule (governance / IR sense)

An executable or catalogued governance **rule artifact** (for example from `ste-rules-library`) represented in IR as a `rule` entity where applicable. Rules express **how checks or activations apply**; they complement, not replace, invariants.

### Rules-engine

The **operational component** (typically packaged with `ste-rules-library`) that **builds** **rule projections**: **ruleset pins**, **identifiers**, **closure hashes**, and **encoded** rule slices for verify and UI. It **does not** replace the **governance-engine** as the durable **decision store**.

### Governance-engine

The **product or module** that **records and serves** governance **decisions** (merge/steelman outcomes, registry rows, overrides) while **consuming** **rule projections** from the **rules-engine**. For prototyping it **MAY** ship **inside** `ste-rules-library`; later it **MAY** expose a **publication surface** for `ste-kernel` per contracts.

### Rule projection

A **machine-native** slice of catalogued rules (and related metadata) **bound to an ADR**
(or ADR lifecycle stage) for agents, gates, or review tools. Projections are **derived**
from `ste-rules-library` / **rules-engine** authority, not ad hoc paraphrases in the
kernel. Human-readable summaries are **projections** of the same envelope, not a second
authority. Draft interchange shape: `contracts/rule-projection/rule-projection-envelope.schema.json`.

### Steelman gate

A **workspace** checkpoint where a proposal is checked for **compliance / convergence**
against **authoritative rule projections**—distinct from schema validators, MCP checks,
**IR validation**, and **`KernelAdmissionAssessment`**. Outcomes **MAY** be recorded as
attested envelopes (see **Rule projection**). A **human override** after disagreement
**MUST** be logged as an explicit **decision** per workspace contracts.

### Adjudicator

The **governance-side** component (service name TBD—for example **governance-engine**)
that **consumes rule projections** from the **rules-engine** and **stores or serves**
durable **decisions** (verdicts, attestations, overrides, registry). The **rules-engine**
supplies **identifiers**, **hashes**, **ruleset pins**, and **encoded closure** in the
projection envelope; it **does not** replace the adjudicator as the **decision store**.
**`ste-kernel` orchestrates** and **MAY** verify or route to the same projections **without**
owning rule semantics or governance history. **Cheap prototypes** MAY colocate roles **in-process**; the **durable** shape separates **projection materialization** from **decision
persistence**. **MUST NOT** conflate adjudicator outcomes with **`ArchitectureEvidence`**
(factual only) or silently duplicate a second rules compiler inside `ste-kernel`.

## Execution Model

### Cognitive Execution Model (CEM)

The deterministic lifecycle STE uses to ensure constraint-governed cognition. Nine stages executed in sequence: Initialization → State Loading → Pre-Task Validation → Divergence Detection → Divergence Communication → Correction and Reconvergence → Reasoning Execution → Post-Task Validation → Final Convergence.

### Stage

A discrete phase in the Cognitive Execution Model. Each stage has explicit responsibilities, inputs, outputs, and validation requirements. No stage may be skipped.

### Initialization

Stage 1 of CEM. Loads Prime Invariant, System Invariants, establishes invariant hierarchy boundaries, prepares validators, and verifies RECON completion status.

### State Loading

Stage 2 of CEM. Loads only explicit state relevant to the task through Task Analysis, Entry Point Discovery, RSS Graph Traversal, and Context Assembly.

### Validation

Stages 3 and 8 of CEM. Pre-Task Validation ensures reasoning begins from valid, explicit state. Post-Task Validation ensures no divergence was introduced and outputs conform to artifact specifications.

### Divergence Detection

Stage 4 of CEM. Identifies inconsistencies such as stale documentation, missing inventories, implicit assumptions, structural violations, hierarchy conflicts, taxonomy gaps, misplaced artifacts, or semantic drift.

### Reconvergence

Stage 6 of CEM. Correction process ensuring no further divergence exists, validation succeeds, and consistency is restored across artifacts, invariants, and documentation-state.

### Final Convergence

Stage 9 of CEM. The cognitive task is accepted only when all validators pass, all invariants remain satisfied, framework synchronization is preserved, documentation-state is complete, divergence is absent, and all dependencies are satisfied.

## Divergence and Drift

### Divergence

Any inconsistency, drift, or constraint violation detected during **workspace cognition** that **MUST** be classified using the Divergence Taxonomy before correction. Reasoning cannot proceed until divergence is resolved. **MUST NOT** relabel ordinary **schema validation failures**, **JSON parse errors**, **contract shape violations**, or **`ste-kernel` IR validation / boot failures** as “divergence” unless you are explicitly routing them through the taxonomy for documentation-state analysis; those cases use **error** / **validation failure** / **boot failure** vocabulary (see `invariants/STE-Failure-Taxonomy-Boundaries.md`).

### Divergence Taxonomy

Canonical classification system for detecting, routing, and resolving divergence. Categories include documentation-state drift, structural violations, constraint violations, and framework synchronization drift.

### Divergence Type

Specific classification within the taxonomy. Examples: Doc-Missing-Inventory, Doc-State-Staleness, Doc-Implicit-State, Artifact-Structure-Violation, Domain-Constraint-Violation.

### Drift

Gradual divergence from documented truth over time. STE treats drift as detectable and correctable condition, not inevitable failure. Uncorrected drift is prohibited.

### Gate Type

Classification determining how divergence is communicated to users: Auto-Resolvable (agent may proceed), User-Gated (requires user confirmation), or Blocking (requires user guidance).

## Documentation-State

### Documentation-State

The explicit, machine-readable substrate that grounds reasoning. Provides complete, consistent, validated truth for cognition. Must be synchronized before reasoning proceeds.

### AI-DOC

Structured, explicit, machine-interpretable representation of system state. Bidirectional references, sliceability, graph completeness. Stored as YAML files. Generated by RECON, maintained incrementally.

### RECON (Reconciliation Protocol)

The protocol for bootstrapping explicit domain truth from existing artifacts. Extracts project structure, relationships, and semantics into AI-DOC. Prerequisite for reasoning (SYS-6: RECON Completion Prerequisite).

### RSS (Runtime State Slicing)

Graph traversal protocol for deterministic context assembly. Starts at entry points, traverses explicit references with depth bounds, assembles Minimally Viable Context. Includes convergence validation for multi-entry traversals. Deterministic: same entry points → same traversal → same context.

### Convergence Validation

Protocol for validating semantic coherence of multiple RSS entry points. Measures subgraph overlap between independent traversals. Classification: 3 of 3 converge (ideal), 2 of 3 converge (strong), <2 of 3 converge (divergence detected). Enables detection of ambiguous identifiers, stale graph structure, and Task Analysis errors.

### Subgraph Overlap

Measurement of semantic relationship between two RSS traversal results. Calculated as intersection over union of traversed nodes. Threshold: ≥70% overlap indicates convergent (semantically coherent) subgraphs. Used in convergence validation to detect entry points leading to different architectural regions.

### MVC (Minimally Viable Context)

The smallest set of state needed to reason about a task. Bounded (explicit depth limits), minimal (only necessary state), deterministic (reproducible), explicit (every item justified by graph path).

### Task Analysis

Deterministic algorithm mapping natural language tasks to AI-DOC entry points. Decomposes requests, resolves domains, discovers candidates, scores relevance, selects entry points. No probabilistic matching.

### Entry Point

Starting node for RSS traversal, identified by Task Analysis. High-scoring slices matching task intent, type, identifier, and keywords.

### Graph Traversal

Following explicit edges from entry points to discover related state. Deterministic, auditable, depth-bounded. Uses `_slice` metadata for dependencies and dependents.

### Sliceability

Property of AI-DOC enabling graph traversal through explicit `_slice` metadata. Every item declares dependencies (forward edges) and dependents (backward edges). Bidirectional relationships maintained consistently.

## Validation and Enforcement

### Validator

A gate that enforces constraints before operations proceed. Validators detect divergence, enforce artifact specifications, ensure documentation-state integrity, apply domain and system rules, validate cross-file consistency, and prevent implicit reasoning. In the **integration plane**, **IR validation** checks merged graph shape, provenance, and contract rules; **admission evaluation** consumes a projected slice and **MUST NOT** re-validate IR mechanics.

### Checkpoint

Mandatory validation gate in the cognitive lifecycle. Pre-Task Checkpoint validates state before reasoning. State-Mutating Checkpoint validates updates after changes.

### Documentation Validator

Checks structure, completeness, explicitness of documentation-state artifacts.

### Framework Validator

Ensures canonical artifacts (schemas, inventories) remain synchronized.

### Domain Validator

Validates domain-specific correctness when reasoning requires specialized constraints.

## Authority and Governance

### Authority Boundary

Clear separation between attestation (signing canonical artifacts), enforcement (verifying eligibility), and execution (performing operations). Prevents single entities from signing their own eligibility or executing without verification.

### Attestation Authority

Responsibility for signing canonical artifacts and producing non-repudiable truth claims. Example: Organizational (ORG) authority signs AI-DOC slices.

### Enforcement Authority

Responsibility for verifying prerequisites and eligibility. Example: Gateway verifies signatures and queries trust registry but does not sign canonical artifacts.

### Execution Authority

Responsibility for performing operations based on verified eligibility. Acts only after enforcement authority confirms prerequisites are satisfied.

### Gateway

Component with ORG-scoped enforcement authority. Verifies artifacts signed by ORG authority, enforces execution eligibility based on ORG-signed invariants, queries trust registry, produces ephemeral unsigned eligibility decisions.

## Protocols and Workflows

### Protocol

A canonical workflow defining how operations must be performed. Examples: Documentation Checkpoint Protocol, AI-DOC Update Workflow Protocol, RECON Protocol, Divergence Communication Protocol.

### Documentation Checkpoint Protocol

Standard for documentation-state validation before and after tasks. Defines Pre-Task Checkpoint and State-Mutating Checkpoint requirements.

### AI-DOC Update Workflow Protocol

Standard for mutating documentation-state artifacts. Eight-step workflow: Identify Update Type → Load Artifacts → Apply Update → Synchronize Inventory → Execute Checkpoint → Validate → Reconverge → Finalize.

### Divergence Communication Protocol

Standard for how divergence is communicated to users. Defines gate type determination, communication flow, consent requirements, and decline handling.

## Architectural Decisions

### ADR (Architectural Decision Record)

A durable architecture decision artifact, typically authored in structured form (for example YAML logical ADRs), validated under `adr-architecture-kit`, and published into discovery surfaces (manifest, indices) and **IR fragments** for `ste-kernel`. In STE doctrine, an ADR is also a **converged, binding** commitment where alternatives have been explicitly rejected and reversal would be expensive or destabilizing. Governs future work and enforcement behavior.

### E-ADR (Exploratory Architectural Decision Record)

Provisional, explicitly reversible decision existing to force execution and generate learning. Operationally binding but architecturally non-binding. Does not define system truth. Not published in this specification.

### Execution-Pressure

The use of E-ADRs to force implementation and surface friction, conflicts, and learning. Drives experimentation without establishing architectural truth.

## Determinism and Explicitness

### Determinism

Property where identical inputs always produce identical outputs. In **workspace cognition**, STE achieves determinism through constraint engineering, layered invariants, validated documentation-state, divergence detection, and structural rules. In the **integration plane**, determinism additionally requires canonical merge order, canonical serialization, and stable identity rules for `Compiled_IR_Document` as specified by the Architecture IR contract referenced from `ste-spec`.

### Explicitness

Requirement that all assumptions, boundaries, state, and reasoning be declared. Implicit knowledge is treated as drift (PRIME-1: No Implicit Assumptions, PRIME-2: No Undeclared State).

### Boundedness

Requirement that reasoning remain within declared scopes and domains. Unbounded reasoning is prohibited (PRIME-3: No Unbounded Reasoning).

## Framework and Synchronization

### Framework

The complete set of STE artifacts defining the governance system: core architecture, invariants, validators, protocols, divergence taxonomy, and canonical references.

### Framework Synchronization

Requirement that modifications to any canonical artifact trigger synchronization updates to dependent artifacts (SYS-16: Cascade Update Requirement).

### Canon Status

Declaration that a file is canonical and modifications require Framework Validator approval, inventory updates, directory verification, and reconvergence.

### Inventory

Authoritative list of all artifacts within a category. Ensures completeness and prevents undeclared artifacts (Doc-Missing-Inventory divergence if inventory is stale).

## Operating System Analogy

### AI Operating System

Conceptual framing of STE as an OS for AI cognition. Invariant Hierarchy acts as kernel, AI-DOC as filesystem, Validators as system calls, Divergence Taxonomy as error handling, CEM as runtime.

### Invariant Kernel (concept)

The **Invariant Kernel** is the Prime and System invariant layers that provide foundational governance rules analogous to an OS kernel. **MUST NOT** conflate this with the `ste-kernel` product.

### STE Kernel (`ste-kernel`) (product)

**`ste-kernel`** is the orchestration component that loads adapter publication surfaces, merges Architecture IR fragments, validates `Compiled_IR_Document`, and evaluates admission. It implements the **kernel execution model**; it is not the same thing as the **Invariant Kernel** concept.

### Filesystem

AI-DOC, providing explicit structured machine-interpretable truth analogous to OS filesystem.

### System Calls

Validators, enforcing constraints before operations proceed analogous to OS system calls.

## ISO/IEC/IEEE 42010 Concepts

### Viewpoint

Perspective on system structure addressing specific stakeholder concerns. Examples: Invariant Hierarchy (constraint layering viewpoint), Cognitive Execution Model (lifecycle viewpoint), Authority Boundary Model (responsibility separation viewpoint).

### Stakeholder Concern

What different audiences need to understand. Examples: Governance system designers need to know how to bound AI reasoning; Implementation teams need to know normative requirements for conformance.

### Architectural View

Complete realization of a viewpoint with exhaustive detail. This specification intentionally provides viewpoints without complete views to preserve design freedom.

## Multi-Repository Integration and Kernel Terminology

### Architecture IR

The versioned, schema-governed **graph interchange** that `ste-kernel` compiles and validates. Architecture IR is **derived** from adapter inputs. The mechanical contract (schema bundle, merge order, identity rules) is **authoritative in the `ste-kernel` repository** and **referenced normatively** from `ste-spec`.

### ADR-V (vision logical ADR)

In the `ste-kernel` / `adr-architecture-kit` taxonomy, **`ADR-V-*`** identifies **vision**
logical ADRs (`vision_category: true`). Example: **`ADR-V-0001`** (*Kernel Control Plane
IR-Mediated Evolution*) in
`ste-kernel/adrs/logical/ADR-V-0001-kernel-control-plane-ir-mediated-evolution.yaml`
frames the kernel as an **IR-mediated workspace control plane**. **MUST NOT** reuse
**ADR-V** as a **product** or **governance hub** name without redefining the taxonomy
everywhere—use a distinct name (for example **governance hub**, **governance plane**) for
optional scale-agnostic tooling (registry, **CI verify hooks**, attestations) that
composes with `ste-spec` / `ste-kernel`.

### IR Fragment

A UTF-8 JSON array of Architecture IR **entity and relationship records** published by an adapter on a **publication surface**. Each record **MUST** include `provenance` whose adapter identity matches the publishing adapter role.

### Compiled IR / Compiled_IR_Document

The single merged, validated Architecture IR document produced by `ste-kernel` after deterministic merge and IR validation. This is the **integration-state** artifact consumed for admission projection. **MUST NOT** be treated as a second authoritative documentation-state store in repositories.

### Boot

The ordered, blocking `ste-kernel` pipeline that ends in `kernel_ready`: workspace discovery, adapter resolution, artifact loading, IR compilation (merge), IR validation, then readiness. **MUST** complete before admission evaluation uses merged IR. See `execution/STE-Kernel-Execution-Model.md`.

### Admission

Caller-facing eligibility and blocking semantics emitted only as **`KernelAdmissionAssessment`**. Admission **MUST NOT** be emitted by `ste-runtime`.

### ArchitectureEvidence

The `ste-runtime` contract payload describing bundle health, freshness, and related factual diagnostics. **MUST** be non-decision-bearing. Schema: `contracts/architecture-evidence.schema.json`.

### KernelAdmissionAssessment

The `ste-kernel` contract payload describing admission decision, blocking, acknowledgements, and summary. **MUST** be decision-bearing at the handoff boundary. Schema: `contracts/kernel-admission-assessment.schema.json`.

### Adapter (integration role)

A bounded integration role (`ADRAdapter`, `SpecAdapter`, `RuntimeAdapter`, `RulesAdapter`) that translates repository-native material into IR fragments or evidence without `ste-kernel` importing sibling implementation internals. Policy is expressed in `ste-kernel/contracts/adapter-contracts.yaml` (referenced from `architecture/STE-Integration-Model.md`).

### Publication Surface

A stable, contract-backed path or export through which an adapter publishes fragments or other kernel-consumable artifacts. `ste-kernel` **MUST** consume only publication surfaces (or explicit caller-supplied paths), not arbitrary repository internals.

### Canonical Artifact

An artifact that is authoritative for a stated purpose: for example `ste-spec` JSON Schemas for handoff shape, `ste-spec` published `spec-ir-fragments.json`, adapter-published fragment files per the boot contract, and the versioned Architecture IR schema bundle owned by `ste-kernel`. **Derived** artifacts include merged `Compiled_IR_Document` and internal projections.

### STE-system-core

The **non-optional** subset of workspace and **integration** obligations that **MUST** hold for STE’s advertised handoff guarantees (handoff schemas, INV-000x index, role ADR, pinned IR bundle pointer)—distinct from **forkable** technology rules in `ste-rules-library`. Registry: `architecture/STE-System-Core.md`.

## Common Abbreviations

- **ADR**: Architectural Decision Record
- **ADR-V**: Vision-category logical ADR in `ste-kernel` / adr-kit taxonomy (not a governance product name); see **ADR-V (vision logical ADR)**
- **AI-DOC**: Artificial Intelligence Documentation (semantic index)
- **CEM**: Cognitive Execution Model
- **E-ADR**: Exploratory Architectural Decision Record
- **IR**: Architecture IR (graph interchange compiled by `ste-kernel`)
- **MVC**: Minimally Viable Context
- **RECON**: Reconciliation Protocol
- **RSS**: Runtime State Slicing
- **STE**: System of Thought Engineering

## State Transition and Environment Management

### Canonization

The process by which provisional workspace state becomes canonical state through version control, CI/CD security gates, and merge approval. Only canonical state is eligible for RECON extraction.

### Canonical State

Security-vetted artifacts in target branches (develop, master) that serve as organizational source of truth. RECON operates exclusively on canonical state. Security validation occurs via CI/CD gates before artifacts reach canonical state.

### Environment

Deployment context for reasoning (nonprod, production, staging, etc.). Attestations are scoped to specific environments. Gateway enforces environment matching during verification. Organizations may use separate signing keys per environment for cryptographic isolation.

### Trust Registry

Service that distributes public keys, maintains authorized signing authorities, and maps signing identities to authorized environments. Enables Gateway to verify Fabric attestation signatures and authority-environment matches. May be implemented using cloud IAM systems, certificate authorities, or dedicated services.

### Key Management Service

Enterprise service for cryptographic key lifecycle management, typically with hardware security module (HSM) backing. Examples: AWS KMS, Azure Key Vault, GCP Cloud KMS, Thales HSM. Used by Fabric to sign attestations with keys that never leave hardware security boundary.

### Multi-Key Architecture

Deployment pattern where single Fabric control plane coordinates multiple data planes, each with environment-specific signing key (managed by key service), authorization scope, and storage. Provides cryptographic environment isolation while maintaining operational simplicity. Nonprod key compromise cannot affect production.

### Authorization Scope

Set of permissions granted to a signing authority. Typically managed by identity and access management (IAM) systems or policy engines. Examples: AWS IAM role with kms:Sign permission, Azure Managed Identity with key signing permission, service account with signing capability.

## Usage Guidelines

### Preferred Terminology

Use these terms consistently:

- Say **"invariant"** for hierarchical STE constraints and ADR-declared constraints; say **"rule"** when referring to `ste-rules-library` rule artifacts or IR `rule` entities—**do not** collapse these into one term in integration contexts
- Say **"divergence"** for **STE Divergence Taxonomy** classifications and documentation-state / cognitive drift that the taxonomy names; say **"error"**, **"validation failure"**, or **"boot failure"** for schema, JSON, API, and IR contract mechanics (including `ste-kernel` IR validation)—**do not** substitute “divergence” for those mechanical failures
- Say **"validator"**, not "checker", "gate", or "enforcer" for constraint enforcement mechanisms; say **"IR validation"** vs **"admission evaluation"** in kernel contexts
- Say **"documentation-state"**, not "docs", "state", or "context" for AI-DOC substrate; say **"integration-state"** or **"Compiled_IR_Document"** when referring to merged IR
- Say **"cognitive execution"**, not "reasoning", "thinking", or "processing" for governed lifecycle
- Say **"reconvergence"**, not "fixing", "correction", or "repair" for divergence resolution
- Say **"authority boundary"**, not "separation of concerns" or "responsibility model" for attestation/enforcement/execution separation
- Say **"Invariant Kernel"** vs **`ste-kernel`** explicitly when mixing OS analogy with the orchestration product

### Capitalization

- Capitalize proper names: System of Thought Engineering, Prime Invariant, Cognitive Execution Model
- Lowercase common terms: invariant, divergence, validator, protocol, documentation-state
- Capitalize layer names: Prime Invariant, System Invariants, Domain Invariants, Artifact Specifications

### Acronyms

Spell out acronyms on first use in each document, then use acronym consistently.

**First use**: "Cognitive Execution Model (CEM)"  
**Subsequent uses**: "CEM"

---

**This glossary defines STE architectural terminology for precision and consistency across the specification.**

