# System of Thought Engineering (STE) — Manifest
## Canonical Artifact Map

# 1. Purpose

This manifest is the canonical map of published authority surfaces in
`ste-spec`.

It points to where contract shape, rules, decisions, and orientation artifacts
live. It does not define those rules itself.

## 1.1 Reading legend (normative vs orientation vs illustration)

- **Normative (law):** `contracts/` JSON Schemas, `invariants/`, binding `adr/` where they govern handoffs; Architecture IR **semantics** in `architecture/STE-Architecture-Intermediate-Representation.md` (`adr/ADR-035-architecture-ir-ontology-authority.md`).
- **Accepted normative supporting doctrine:** `architecture/STE-Spine-Lifecycle.md`, `architecture/STE-Spine-Authority.md`, `architecture/STE-Spine-Artifact-Mapping.md`, and `architecture/STE-Spine-State-Model.md`. These files are accepted supporting doctrine subordinate to ADR-040 and ADR-038 and do not override accepted ADR authority.
- **Orientation (viewpoint):** most of `architecture/`, `execution/`, and
  `governance/` is navigation and viewpoint material and does not override
  normative authority.
- **Analysis-only (non-normative):**
  `architecture/STE-Spine-Extracted-Doctrine.md` is reconstruction material for
  audit and traceability only.
- **Worked example (illustration):** `architecture/STE-Worked-Example-Walkthrough.md` - one fictional thread tying workspace tooling to integration surfaces; **not** additional MUSTs.
- **Figures (orientation):** `architecture/STE-Diagram-Standards.md` - canonical diagram representation and projection doctrine; `architecture/STE-Diagram-Conventions.md` provides editorial guidance only. Figures are projection artifacts and are **informative** unless a document explicitly says a figure is normative.

# 2. Suggested Reading Order (table of contents)

1. **Overview:** `README.md`, `status.md`, `scope-and-non-goals.md`, `glossary.md`
2. **Core concepts:** `architecture/STE-Foundations.md`, `architecture/STE-Reference-Embodiment.md` (informative spine), `architecture/STE-Worked-Example-Walkthrough.md` (informative end-to-end thread), `invariants/STE-Invariant-Hierarchy.md` (and referenced invariant docs)
3. **System components:** `architecture/STE-System-Components-and-Responsibilities.md`, `architecture/STE-System-Core.md`
4. **Integration model:** `architecture/STE-Integration-Model.md`, `architecture/STE-Architecture-Intermediate-Representation.md` (semantic Architecture IR), `architecture/STE-Diagram-Standards.md` (diagram doctrine), `architecture/STE-Diagram-Conventions.md` (editorial figure guidance)
5. **Spine doctrine:** `adr/ADR-040-ste-spine-lifecycle-and-authority.md` (canonical Spine definition), `architecture/STE-Spine-Lifecycle.md`, `architecture/STE-Spine-Authority.md`, `architecture/STE-Spine-Artifact-Mapping.md`, `architecture/STE-Spine-State-Model.md` (accepted normative supporting doctrine subordinate to ADR-040 and ADR-038), `architecture/STE-Spine-Extracted-Doctrine.md` (analysis-only, non-normative reconstruction)
6. **Boundary surfaces:** `architecture/OPEN_CLOSED_BOUNDARY.md`, `architecture/PUBLIC_SYSTEM_SURFACES.md`, `architecture/BOUNDARY_TERMINOLOGY_ALIGNMENT.md`
7. **Execution models**
   - Workspace cognition: `execution/STE-Cognitive-Execution-Model.md`
   - Kernel integration: `execution/STE-Kernel-Execution-Model.md`
8. **Contracts and schemas:** `contracts/README.md`
9. **Determinism (integration plane):** `architecture/STE-Determinism-and-Canonical-Identity.md`
10. **Failure taxonomy boundaries:** `invariants/STE-Failure-Taxonomy-Boundaries.md`, `invariants/STE-Divergence-Taxonomy.md`
11. **Cross-component invariants:** `invariants/STE-Cross-Component-Contract-Invariants.md` (INV-000x)
12. **Architecture orientation (broad):** `architecture/STE-Architecture.md`
13. **ADR doctrine:** `adr/README.md`, `adr/ARCHITECTURE_BOUNDARY_DECISION.md`
14. **Repository README contract:** `adr/ADR-036-repository-readme-contract.md`, `architecture/STE-Repository-README-Checklist.md`
15. **Artifact map (documentation-state):** `architecture/STE-Canonical-Project-Artifacts.md`
16. **Governance / security:** `governance/`, `SECURITY.md`
17. **Internal non-public notes:** `internal/` (informative only; not part of the public canonical specification surface)

# 3. Canonical Authority Split

- `contracts/` - normative serialized contract shape
- `invariants/` - normative rules and semantic constraints
- `adr/` - architectural decisions and rationale
- `architecture/`, `execution/`, `governance/` - generally orientation and
  viewpoint material, except explicitly named accepted supporting-doctrine files

For the Spine tranche:

- `adr/ADR-040-ste-spine-lifecycle-and-authority.md` is the canonical Spine
  lifecycle and authority-transition definition
- `adr/ADR-038-artifact-classification-and-versioning.md` is the canonical
  artifact taxonomy and versioning posture authority
- `architecture/STE-Spine-Lifecycle.md`,
  `architecture/STE-Spine-Authority.md`,
  `architecture/STE-Spine-Artifact-Mapping.md`, and
  `architecture/STE-Spine-State-Model.md` are accepted supporting doctrine that
  explain and map the Spine without overriding ADR-040 or ADR-038
- `architecture/STE-Spine-Extracted-Doctrine.md` is analysis-only and
  non-normative

If wording appears inconsistent, precedence is:

1. Accepted ADRs
2. Accepted invariants
3. Normative supporting doctrine in `architecture/`
4. Explanatory and orientation surfaces
5. Analysis-only material

# 4. Contract Surfaces

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
- `contracts/architecture-ir/spec-ir-fragments.json`
- `contracts/architecture-ir-kernel-contract-pin.json` (pinned `ir_version` / `schema_id` pointer)
- `contracts/rule-projection/` (draft rule projection envelope; pre-normative - see `contracts/README.md`)
- `contracts/governance-decision-record/` (draft decision rows referencing projections; pre-normative)
- `contracts/examples/`
- Referenced IR bundle: see `contracts/README.md` (kernel-owned)

`contracts/architecture-ir/spec-ir-fragments.json` is a generator-owned
published artifact. "Published" here names a publication role, not a separate
artifact class. Regenerate and validate it with
`python scripts/run_local_contract_checks.py`.

# 5. Handoff Invariant Surfaces

- `invariants/STE-Cross-Component-Contract-Invariants.md`
- `invariants/STE-Failure-Taxonomy-Boundaries.md`
- `invariants/INV-0001-runtime-evidence-factual-only.md`
- `invariants/INV-0002-kernel-final-admission-authority.md`
- `invariants/INV-0003-contract-version-required.md`
- `invariants/INV-0004-required-arrays-explicit.md`
- `invariants/INV-0005-unknown-freshness-explicit.md`
- `invariants/INV-0006-kernel-fails-closed-on-invalid-evidence.md`
- `invariants/INV-0007-closed-object-contract-discipline.md`
- `invariants/INV-0008-invalid-bundle-requires-error-diagnostics.md`
- `invariants/INV-0009-degraded-bundle-requires-diagnostic-context.md`
- `invariants/INV-0010-rule-projection-envelope-discipline.md` (draft scope; projection vs governance decision record)
- `invariants/INV-0011-kernel-fails-closed-on-unverifiable-execution-prerequisites.md`
- `invariants/INV-0012-evidence-must-reference-evaluated-subjects.md`

# 6. Handoff ADR Surfaces

- `adr/ADR-030-contract-authority-in-ste-spec.md`
- `adr/ADR-031-runtime-kernel-responsibility-boundary.md`
- `adr/ADR-032-fail-closed-enforcement-model.md`
- `adr/ADR-033-closed-object-discipline.md`
- `adr/ADR-034-rule-projection-envelope-authority.md` (proposed; envelope authority)
- `adr/ADR-035-architecture-ir-ontology-authority.md`
- `adr/ADR-036-repository-readme-contract.md`
- `adr/ADR-040-ste-spine-lifecycle-and-authority.md`

# 7. Orientation Surfaces

- `README.md`
- `architecture/STE-Architecture.md`
- `architecture/STE-Foundations.md`
- `architecture/STE-System-Components-and-Responsibilities.md`
- `architecture/STE-Integration-Model.md`
- `architecture/STE-Architecture-Intermediate-Representation.md`
- `architecture/OPEN_CLOSED_BOUNDARY.md`
- `architecture/PUBLIC_SYSTEM_SURFACES.md`
- `architecture/BOUNDARY_TERMINOLOGY_ALIGNMENT.md`
- `architecture/STE-Reference-Embodiment.md`
- `architecture/STE-Worked-Example-Walkthrough.md`
- `architecture/STE-Canonical-Project-Artifacts.md`
- `architecture/STE-System-Core.md`
- `architecture/STE-Determinism-and-Canonical-Identity.md`
- `architecture/STE-Diagram-Standards.md`
- `architecture/STE-Diagram-Conventions.md`
- `architecture/STE-Spine-Extracted-Doctrine.md` (analysis-only; non-normative)
- `architecture/STE-Repository-README-Checklist.md`
- `execution/STE-Cognitive-Execution-Model.md`
- `execution/STE-Kernel-Execution-Model.md`
- `glossary.md`
- `governance/`

## 7.1 Accepted Supporting Doctrine Exceptions

- `architecture/STE-Spine-Lifecycle.md`
- `architecture/STE-Spine-Authority.md`
- `architecture/STE-Spine-Artifact-Mapping.md`
- `architecture/STE-Spine-State-Model.md`

These accepted supporting-doctrine files explain and map the Spine but do not
override ADR-040 or ADR-038.

Files under `internal/` are tracked for internal planning but are **not** public
canonical specification surfaces and **MUST NOT** be cited as external
compatibility authority.

# 8. Synchronization Order

When the runtime/kernel handoff changes, update:

1. `contracts/` for shape
2. `invariants/` for rules
3. `adr/` for rationale
4. `architecture/STE-Integration-Model.md`, `execution/STE-Kernel-Execution-Model.md`, and `contracts/README.md` when boundaries shift
5. orientation surfaces only as needed for navigation
