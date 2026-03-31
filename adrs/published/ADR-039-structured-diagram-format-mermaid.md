# ADR-039: Structured Diagram Format (Mermaid)

## Migration status

| Field | Value |
| --- | --- |
| **Canonical record** | Machine ADR **ADR-L-0039** — [`adrs/logical/ADR-L-0039-structured-diagram-format-mermaid.yaml`](../logical/ADR-L-0039-structured-diagram-format-mermaid.yaml) |
| **Human projection** | [`adrs/rendered/ADR-L-0039.md`](../rendered/ADR-L-0039.md) (generated; do not edit by hand) |
| **This file** | Legacy published markdown; **not canonical** |
| **Disposition** | Migrated one-to-one |

Authority: treat **ADR-L-0039** as the source of truth for decisions and invariants.

---

## Status

Accepted

## Context

`ste-spec` already uses diagrams to represent architecture, boundaries,
lifecycle, authority, flows, and relationships across the STE system.
Mermaid is already used in some architecture documents, but current guidance is
editorial rather than a binding governance decision.

STE also treats diagrams as subordinate to ADRs, contracts, and doctrine.
Without an explicit representation standard, canonical architecture diagrams
can drift between formats and be mistaken for independent architecture
definitions rather than structured projections of authoritative sources.

## Decision

Canonical architecture diagrams in `ste-spec` **MUST** use a structured,
text-based representation.

Mermaid is the standard structured diagram format for canonical diagrams in
`ste-spec`.

A canonical diagram is a diagram that represents system architecture,
structure, lifecycle, authority, flows, or relationships and is intended to
represent the architecture of the system rather than illustrate a local
concept.

ASCII and Unicode box diagrams are allowed only for:

- small inline conceptual sketches
- terminal-oriented examples
- narrative illustrations that are not canonical architecture diagrams

Canonical diagrams are structured projection artifacts and representational
views only. They **MUST NOT** introduce semantics not defined in ADRs,
contracts, or architecture doctrine.

Canonical diagrams **MUST NOT** be the sole location where a rule,
requirement, or invariant is defined.

This tranche converts only the explicitly identified canonical diagrams. It
does not require repo-wide ASCII conversion.

This ADR governs representation format only.

This ADR does not define:

- diagram styling
- Mermaid authoring conventions
- CI enforcement
- diagram generation tooling
- Architecture IR schema
- repository structure
- automatic diagram generation
- runtime behavior

## Lifecycle Placement in the STE Spine

This ADR governs Derived projection posture across the STE Spine by defining how
representational outputs generated from lifecycle material express lifecycle,
authority, and flow without becoming authoritative sources or separate
lifecycle states themselves.

## Consequences

- Canonical diagrams are projection artifacts derived from ADRs, contracts,
  components, and implementation artifacts.
- Mermaid standardizes the representation format for those projection
  artifacts.
- Canonical diagrams are version-controlled representation artifacts and are
  not authoritative architecture definitions.
- Canonical diagrams must be compatible with future generation from structured
  architecture data, but this ADR does not require automatic generation.
- ASCII and Unicode diagrams remain acceptable for small conceptual
  illustrations and non-canonical narrative aids.
- This decision changes representation governance, not architecture semantics.

## Related

- [`ADR-036-repository-readme-contract.md`](ADR-036-repository-readme-contract.md)
- [`ADR-038-artifact-classification-and-versioning.md`](ADR-038-artifact-classification-and-versioning.md)
- [`../architecture/STE-Artifact-Classification-and-Versioning.md`](../architecture/STE-Artifact-Classification-and-Versioning.md)
