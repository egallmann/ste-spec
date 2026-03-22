# Open Core vs Closed Intelligence Boundary

## Purpose

This document defines the canonical architectural boundary between the STE
**open core** and the STE **closed intelligence layer**.

It exists to make the publication boundary explicit and durable:

- third parties **MAY** build compatible systems against public STE contracts
- internal STE implementations **MAY** retain proprietary intelligence-bearing
  behavior behind those contracts

This document is architectural. It does **not** license software, disclose
private heuristics, or define hidden implementation strategy.

## Boundary Principles

### 1. Spec vs implementation

Public specifications **MAY** define:

- what a subsystem does
- where it appears in the lifecycle
- what it consumes
- what it emits
- schemas, interfaces, and artifact contracts

Public specifications **MUST NOT** define:

- hidden prompts
- internal heuristics
- internal scoring formulas
- semantic weighting logic
- proprietary orchestration behavior
- optimization strategies used to shape reasoning outcomes

### 2. Deterministic vs intelligence-bearing subsystems

STE distinguishes between:

- **deterministic subsystems**, which are suitable for open specification,
  compatibility contracts, and external reimplementation
- **intelligence-bearing subsystems**, where proprietary leverage lives and
  whose role may be described without disclosing implementation

### 3. Public describability

Closed subsystems **MAY** be named and described at the role level.

They **MUST NOT** be described in ways that disclose:

- prompts
- hidden orchestration policy
- internal ranking or weighting
- scoring formulas
- algorithmic strategies that are intentionally private

## Layered Boundary

| Layer | Character | Public status | Examples |
|-------|-----------|---------------|----------|
| Canonical artifact layer | Declarative, deterministic, repository-authored | Open | ADR schemas, Architecture IR semantics, invariant declarations, evidence schemas |
| Deterministic integration and validation layer | Deterministic orchestration and validation against published contracts | Open or mixed/interface-only | kernel validation outputs, rule evaluation interfaces, evidence ingestion interfaces |
| Intelligence-bearing layer | Heuristic, adaptive, optimization-bearing, or adversarial reasoning behavior | Closed | conversation compilation internals, activation logic, projection logic, scoring logic, inference/healing logic |

## Repository Authority Alignment

This boundary aligns with current repository authority:

- `adr-architecture-kit` publishes ADR-derived artifacts and authoring/validation
  surfaces
- `ste-spec` owns normative schemas, semantic meaning, and public contract
  definitions
- `ste-runtime` emits factual runtime evidence and derived runtime-state
- `ste-rules-library` publishes rule material and rule-facing interfaces
- `ste-kernel` performs deterministic boot, validation, merge, and admission

## Subsystem Classification

| Subsystem | Classification | Why |
|-----------|----------------|-----|
| ADR schema and templates | Open | Canonical authoring contracts are intended for public use and compatible implementations. |
| Architecture IR semantic specification | Open | Semantic ontology is a public compatibility surface. |
| Architecture IR mechanical contract reference | Mixed / interface-only | Publicly referenceable and pinnable, but mechanically owned by `ste-kernel`. |
| Semantic graph model and published registries | Open | Public model and deterministic publication artifacts are compatible surfaces. |
| Decorators and explicit intent markers | Open | Explicit author intent markers are safe to standardize when published. |
| RECON extraction surfaces | Mixed / interface-only | Public contract may define extraction inputs/outputs, but internal extraction strategies remain private. |
| Invariant definitions | Open | Normative declarations are intended to be externally readable and implementable. |
| Rule declaration formats | Open | Declared rule material is a compatible artifact surface. |
| Rule evaluation interfaces and results | Mixed / interface-only | Interfaces and result envelopes may be public; evaluation internals need not be public. |
| Kernel validation interfaces and outputs | Open | Deterministic validation outputs and admission contracts are suitable for public specification. |
| Runtime evidence schema / ArchitectureEvidence | Open | Factual evidence format is a public handoff contract. |
| EDR-related public schema surfaces | Mixed / interface-only | Public only where an explicit schema or artifact format is published; confidence/scoring internals stay closed. |
| Provider proposal schemas | Mixed / interface-only | Proposal envelopes may be public where declared; acceptance heuristics remain private. |
| Conversation compiler | Closed | Internal architecture compilation intelligence is proprietary even when role and I/O can be described. |
| Semantic activation engine | Closed | Activation logic is intelligence-bearing and not required for public compatibility. |
| Constraint projection engine | Closed | Projection logic may expose interfaces, but internal projection behavior is proprietary. |
| Adversarial reasoning engine | Closed | Triggering and challenge logic are intelligence-bearing. |
| EDR scoring engine | Closed | Confidence/scoring behavior is proprietary and not part of the public contract. |
| Graph healing / inference engine | Closed | Inferential repair and healing logic is private implementation behavior. |
| Autonomous orchestration layer | Closed | Internal orchestration strategy is proprietary even when lifecycle placement is describable. |

## Mixed / Interface-Only Subsystems

### Architecture IR mechanical contract reference

- Public interface/contract:
  pinned `ir_version`, referenced schema identity, and compiled-document contract
- Lifecycle placement:
  deterministic integration and kernel boot/admission
- Permitted public description:
  shape, versioning, and validation boundary
- Prohibited disclosure:
  hidden merge heuristics beyond published deterministic rules, internal tooling
  shortcuts, or unpublished projection behavior

### RECON extraction surfaces

- Public interface/contract:
  declared extraction inputs, emitted artifact classes, and deterministic
  publication surfaces where those are published
- Lifecycle placement:
  documentation-state and extraction boundary before integration
- Permitted public description:
  that extraction exists, what artifact classes it reads, and what declared
  surfaces it emits
- Prohibited disclosure:
  prompt strategies, latent ranking, hidden recovery heuristics, or internal
  semantic inference policy

### Rule evaluation interfaces and results

- Public interface/contract:
  rule-facing envelopes, result shapes, identifiers, and closure pins where
  published
- Lifecycle placement:
  governance evaluation and review boundary after deterministic data projection
- Permitted public description:
  result types, contract fields, and decision handoff position
- Prohibited disclosure:
  hidden evaluation prioritization, internal weighting, unpublished trigger logic

### EDR-related public schema surfaces

- Public interface/contract:
  only the published evidence or EDR-shaped envelope, if declared in canonical
  artifacts
- Lifecycle placement:
  observed embodiment and evidence handoff
- Permitted public description:
  role as observed or extracted embodiment material
- Prohibited disclosure:
  confidence-scoring internals, hidden feature extraction, private ranking

### Provider proposal schemas

- Public interface/contract:
  proposal envelope, identity fields, signatures, and declared metadata where
  architecture artifacts define them
- Lifecycle placement:
  proposal intake and review boundary
- Permitted public description:
  submitted proposal structure and validation boundary
- Prohibited disclosure:
  private trust scoring, acceptance ranking, hidden adjudication policy

## Boundary Rules

### Open core

The following are candidates for public specification and ecosystem use:

- declarative artifact schemas
- semantic ontology
- deterministic validation interfaces
- evidence formats
- declared rule formats
- published registry and index formats

### Closed intelligence layer

The following remain implementation-private:

- conversation compiler internals
- semantic activation logic
- constraint projection logic
- adversarial reasoning logic
- EDR scoring internals
- graph healing / inference intelligence
- autonomous orchestration intelligence

### Interface-only rule

If a subsystem needs external compatibility but contains intelligence-bearing
implementation, only the **interface, contract, and lifecycle role** are public.
The implementation remains closed.

## Canon Status

This file is canonical for the open-versus-closed architectural boundary in the
public `ste-spec` architecture set.
