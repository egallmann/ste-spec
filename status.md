# STE Specification Status

## Specification Maturity

**Current status**: The **stable** surface is the **v1.0.0 public handoff-contract subset**. The authoritative list of public cross-repo contracts is `architecture/authority-map.md`.

**Draft** contract families and deferred governance–kernel bridge work (below) are **pre-normative**; they do not revoke the stable subset except through an explicit **MAJOR** version change. “Doctrine under review” means **extensions and refinement**, not reopening the published boundary without semver.

**Maturity Indicators**:
- System-of-interest definition: Stable
- Invariant hierarchy: Converged
- Cognitive Execution Model: Stable
- Divergence taxonomy: Converged
- Governance protocols: Stable at the handoff boundary; some governance extension contracts remain draft
- Architectural decisions: Converged for the published handoff boundary (operational and governance extension details remain in flux)

## Versioning

This specification follows semantic versioning (MAJOR.MINOR.PATCH):

- **MAJOR**: Breaking changes to architectural invariants, system-of-interest definition, or execution semantics
- **MINOR**: New viewpoints, protocols, ADRs, or non-breaking constraint additions
- **PATCH**: Clarifications, corrections, documentation improvements, or terminology refinements

**Current Version**: 1.0.0 (stable public handoff-contract subset)

## Evolution Stance

### Architectural Stability

Core architectural elements are considered stable:

- Prime Invariant and System Invariants (Layers 1-2 of Invariant Hierarchy)
- Cognitive Execution Model stage definitions
- Authority boundary model
- Divergence classification taxonomy
- Documentation-state governance protocols

Changes to these elements would constitute MAJOR version changes and require careful impact analysis.

The following remain explicitly **draft / pre-normative** within this repository:

- `contracts/rule-projection/`
- `contracts/governance-decision-record/`
- `adrs/published/ADR-034-rule-projection-envelope-authority.md`
- `invariants/INV-0010-rule-projection-envelope-discipline.md`

### Design Freedom Preserved

The following remain intentionally variable:

- Implementation mechanisms (how constraints are enforced)
- Deployment topology (where components execute)
- Runtime optimization strategies
- Domain-specific invariants (Layer 3 extensions)
- Operational procedures and tooling

These are excluded from this specification to preserve implementation design freedom.

## Execution-Pressure and E-ADRs

This specification distinguishes between:

### ADRs (Architectural Decision Records)

- Converged, binding architectural commitments
- Alternatives explicitly rejected
- Reversal expensive or destabilizing
- Published in this specification

### E-ADRs (Exploratory Architectural Decision Records)

- Provisional, explicitly reversible
- Exist to force execution and generate learning
- Surface friction and conflicts
- Operationally binding but architecturally non-binding
- **NOT published in this specification**

E-ADRs serve as execution-pressure mechanisms in the working repository. They drive implementation experiments without establishing architectural truth. Only decisions that have converged through repeated validation and proven necessary are promoted to binding ADRs.

**This specification contains only converged ADRs.** E-ADRs and their associated learning artifacts remain in the private working repository.

## Completeness Acknowledgment

This specification intentionally publishes architectural viewpoints without complete architectural views.

**Published**:
- System-of-interest definition (what STE is)
- Stakeholder concerns (what audiences need)
- Architectural viewpoints (perspectives on structure)
- Constraint specifications (invariants and protocols)
- Execution semantics (stage definitions and responsibilities)
- Authority boundaries (who signs, enforces, executes)
- Multi-repository **integration boundaries** and **kernel execution sequencing** at contract level (`architecture/STE-Integration-Model.md`, `execution/STE-Kernel-Execution-Model.md`)
- **Authoritative index** of public contracts and producer/consumer roles (`architecture/authority-map.md`)

**Intentionally Excluded**:
- Implementation details (how to build)
- Deployment views (where to deploy)
- Operational procedures (how to operate)
- Runtime optimization (how to tune performance)
- Exhaustive operational runbooks and step-by-step end-to-end deployment guides (contract-level end-to-end narrative is in-scope; operator playbooks are not)

**This follows ISO/IEC/IEEE 42010 principles regarding architectural description.** The standard requires viewpoints addressing stakeholder concerns, not exhaustive system documentation. Implementation details are preserved as design freedom, not architectural specification.

## Review and Feedback

This specification is published for architectural review. Feedback is welcomed on:

- Clarity of architectural viewpoints
- Precision of constraint definitions
- Completeness of stakeholder concern coverage
- Use of ISO/IEC/IEEE 42010 architectural description concepts
- Terminology consistency and precision

Feedback should distinguish between:

- **Architectural concerns** (invariants, execution semantics, authority boundaries)
- **Operational concerns** (implementation, deployment, optimization)

This specification addresses architectural concerns. Operational concerns belong to implementation guidance, not architectural specification.

## Future Evolution

Anticipated minor version updates:

- Additional domain invariant specifications (Layer 3 extensions)
- New governance protocol specifications
- Refined divergence taxonomy categories
- Additional architectural viewpoints
- Glossary expansions

Anticipated major version changes (requiring careful consideration):

- Prime Invariant or System Invariant modifications
- Cognitive Execution Model stage redefinition
- Authority boundary model changes
- Breaking changes to governance protocols

## Publication Intent

This specification is published to:

1. Enable architectural review by governance system researchers
2. Establish clear architectural boundaries for STE implementations
3. Provide normative constraints for deterministic cognition systems
4. Support standards development for AI governance
5. Demonstrate architectural description using ISO/IEC/IEEE 42010 concepts

This is not a marketing document, tutorial, or implementation guide. It is an architectural specification intended for technical audiences requiring precision and rigor.

## Relationship to Implementation

Reference implementations and operational guidance exist separately from this specification. Implementations may vary in:

- Programming languages and frameworks
- Deployment platforms and infrastructure
- Runtime architectures and optimization strategies
- Tooling and automation approaches

As long as implementations satisfy the architectural invariants and execution semantics defined here, they are conformant. This specification intentionally preserves implementation design freedom.

## Deferred governance–kernel bridge (informative)

The following are **explicitly deferred** until **rule-projection** and **governance-decision-record** drafts stabilize and `ste-rules-library` prototype CLIs stop churning:

- **Normative signing algorithm** and **key management** for projection envelopes.
- **Full remote registry** product (prefer **git-committed** index / local JSONL first).
- **New Architecture IR adapter leg** or **sixth public adapter** for governance-only fragments—requires **merge policy** change in `ste-kernel/contracts/adapter-contracts.yaml` and coordinated `ste-spec` ADR.

**Current bridge (prototype):** `ste-rules-library/scripts/governance_cli.py` + `.github/workflows/governance-cli.yml`; orientation in `architecture/STE-Worked-Example-Walkthrough.md` step **7**. **RulesAdapter** wording in `ste-kernel/contracts/adapter-contracts.yaml` acknowledges future **published sub-surfaces** without adding a new adapter name.

---

**Last Updated**: 2026-03-30  
**Version**: 1.0.0  
**Status**: Stable handoff subset (v1.0.0); draft extensions as documented above

