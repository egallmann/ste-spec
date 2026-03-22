# System of Thought Engineering (STE)
## Architectural Specification for Governable Cognition

## Overview

`ste-spec` is the publishable architectural specification for STE.

This repository separates authority by artifact class:

- `contracts/` for normative contract shape
- `invariants/` for normative rules and semantic constraints
- `adr/` for architectural decisions and rationale
- `architecture/`, `execution/`, and `governance/` for orientation viewpoints

## How to read authority vs illustration

- **Normative (law):** `contracts/` JSON Schemas, `invariants/`, and binding `adr/` where they govern handoffs.
- **Orientation (viewpoint):** `architecture/`, `execution/`, and `governance/` prose.
- **Worked example (illustration):** `architecture/STE-Worked-Example-Walkthrough.md` — one fictional thread from workspace discipline through publication surfaces to `ste-kernel`; **not** additional MUSTs.
- **Figures (orientation):** `architecture/STE-Diagram-Conventions.md` — when to use Mermaid vs box diagrams; figures are informative unless a doc says otherwise.

The same legend appears in `architecture/STE-Manifest.md`.

## Canonical Entry Points

- `architecture/STE-Manifest.md` (full map and reading order)
- `architecture/STE-Diagram-Conventions.md` (Mermaid vs box diagrams)
- `glossary.md`
- `architecture/STE-Foundations.md`
- `architecture/STE-Reference-Embodiment.md` (informative spine for the reference multi-repo system)
- `architecture/STE-Worked-Example-Walkthrough.md` (informative end-to-end onboarding thread)
- `architecture/STE-Canonical-Project-Artifacts.md` (documentation-state artifact map)
- `architecture/STE-System-Core.md` (non-optional integration subset registry)
- `architecture/STE-System-Components-and-Responsibilities.md`
- `architecture/STE-Integration-Model.md`
- `execution/STE-Kernel-Execution-Model.md`
- `contracts/README.md`
- `invariants/STE-Cross-Component-Contract-Invariants.md`
- `invariants/STE-Failure-Taxonomy-Boundaries.md`
- `adr/README.md`
- `architecture/STE-Architecture.md`
- `execution/STE-Cognitive-Execution-Model.md`

## Editorial and link-check scope

When running consistency or internal-link checks over this repository:

- **Include** all `*.md` files under the repository root (architecture, execution, contracts, invariants, adr, governance, and root-level specs).
- **Exclude** `.pytest_cache/` and other cache or vendor trees if present; **exclude** `.git/`.

JSON and other contract files under `contracts/` are validated separately (schemas, canonical fragment bundles).

Repeatable **internal Markdown link** check (repository-local targets only):

`python scripts/check_internal_md_links.py` (non-zero exit if any target file is missing).

## Scope

This repository contains architectural specification artifacts only. Runtime
implementation authority remains outside this repository.

For boundaries, maturity, terminology, and adjacent reference material, use:

- `status.md`
- `scope-and-non-goals.md`
- `NON-GOALS.md`
- `glossary.md`
- `SECURITY.md`

## License

Copyright 2024-present Erik Gallmann
