# System of Thought Engineering (STE) — Manifest
## Canonical Artifact Map

# 1. Purpose

This manifest is the canonical map of published authority surfaces in
`ste-spec`.

It points to where contract shape, rules, decisions, and orientation artifacts
live. It does not define those rules itself.

# 2. Canonical Authority Split

- `contracts/` — normative serialized contract shape
- `invariants/` — normative rules and semantic constraints
- `adr/` — architectural decisions and rationale
- `architecture/`, `execution/`, `governance/` — orientation and viewpoint material

# 3. Contract Surfaces

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
- `contracts/examples/`

# 4. Handoff Invariant Surfaces

- `invariants/STE-Cross-Component-Contract-Invariants.md`
- `invariants/INV-0001-runtime-evidence-factual-only.md`
- `invariants/INV-0002-kernel-final-admission-authority.md`
- `invariants/INV-0003-contract-version-required.md`
- `invariants/INV-0004-required-arrays-explicit.md`
- `invariants/INV-0005-unknown-freshness-explicit.md`
- `invariants/INV-0006-kernel-fails-closed-on-invalid-evidence.md`
- `invariants/INV-0007-closed-object-contract-discipline.md`
- `invariants/INV-0008-invalid-bundle-requires-error-diagnostics.md`
- `invariants/INV-0009-degraded-bundle-requires-diagnostic-context.md`

# 5. Handoff ADR Surfaces

- `adr/ADR-030-contract-authority-in-ste-spec.md`
- `adr/ADR-031-runtime-kernel-responsibility-boundary.md`
- `adr/ADR-032-fail-closed-enforcement-model.md`
- `adr/ADR-033-closed-object-discipline.md`

# 6. Orientation Surfaces

- `README.md`
- `architecture/STE-Architecture.md`
- `architecture/STE-Foundations.md`
- `execution/STE-Cognitive-Execution-Model.md`
- `governance/`

# 7. Synchronization Order

When the runtime/kernel handoff changes, update:

1. `contracts/` for shape
2. `invariants/` for rules
3. `adr/` for rationale
4. orientation surfaces only as needed for navigation
