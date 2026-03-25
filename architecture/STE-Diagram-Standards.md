# STE Diagram Standards
## Canonical Diagram Representation and Projection Doctrine

## Purpose

Canonical diagrams in `ste-spec` are architecture artifacts for documentation
and governance, not just illustrations.

This document defines representation standards for diagrams in `ste-spec`. It
governs how canonical diagrams are represented and how they relate to the
authoritative architecture model. It does not redefine architecture intent,
contract authority, or runtime behavior.

## Relationship to Authority

Architecture semantics authority in STE is ordered as follows:

1. ADRs
2. Contracts / specifications
3. Architecture doctrine documents
4. Diagrams as representational views only

[`../adr/ADR-039-structured-diagram-format-mermaid.md`](../adr/ADR-039-structured-diagram-format-mermaid.md)
defines the governance decision to use Mermaid for canonical diagrams.

[`../adr/ADR-038-artifact-classification-and-versioning.md`](../adr/ADR-038-artifact-classification-and-versioning.md)
and
[`STE-Artifact-Classification-and-Versioning.md`](./STE-Artifact-Classification-and-Versioning.md)
define artifact and versioning posture for derived documentation artifacts.

ADRs, contracts, and architecture doctrine remain the authoritative source of
architecture intent. Diagrams are not the sole source of architecture
semantics and must remain subordinate to those authoritative sources.
No rule, requirement, or invariant may exist only in a diagram.

## Diagram Projection Principle

STE uses a model-driven architecture approach.

ADR frontmatter, contracts, component specifications, and implementation
metadata define the architecture graph. Architecture IR is the canonical
machine-readable model of that graph.

Mermaid diagrams are human-readable projections or views of that model.
Diagrams in STE are representational projection artifacts. They are not
authoritative sources of architecture intent and must be derivable from
authoritative sources such as ADRs, contracts, component specifications, and
implementation artifacts.

Per ADR-038 posture, these projection artifacts are a Derived representational
posture rather than a separate artifact class.

If a diagram and an ADR or contract disagree, the ADR or contract is
authoritative.

Diagrams must not introduce components, capabilities, invariants, contracts,
or flows that are not defined in authoritative sources. Canonical diagrams
typically correspond to logical, physical, component, traceability, lifecycle,
authority, or runtime views derived from ADRs and contracts.

## Reproducible Projection Principle

STE uses a model-driven architecture approach.

ADRs, contracts, component specifications, and implementation artifacts define
the authoritative architecture model. Architecture IR is the canonical
machine-readable model of the system.

Mermaid diagrams and architecture projection documents are human-readable
projections derived from that model.

Projection artifacts:

- are derived artifacts
- are not authoritative sources of architecture intent
- should be reproducible from ADRs, contracts, components, and implementation
  artifacts
- may be versioned for documentation, audit, and review purposes
- must not contain architecture elements not defined in authoritative sources
- must not be the sole location where a rule, requirement, or invariant is
  defined

If a projection and an ADR or contract disagree, the ADR or contract is
authoritative.

## Canonical Diagram Definition

A canonical diagram is a diagram that represents system architecture,
structure, lifecycle, authority, flows, or relationships and is intended to
represent the architecture of the system rather than illustrate a local
concept.

Canonical diagrams are representational projection artifacts. They are not
authoritative sources of architecture intent. Versioning a diagram does not
make it authoritative; diagram authority comes only from ADRs, contracts, and
architecture doctrine.

Local conceptual sketches, terminal-oriented examples, and narrative
illustrations that do not define or summarize canonical architecture views are
not canonical diagrams.

## Architecture Projection Documents

Architecture projection documents are human-readable architecture views
generated from or derivable from authoritative architecture sources.

They may describe logical, physical, component, traceability, runtime, or
certification views.

| Projection Document | Primary Source |
|---------------------|----------------|
| Logical Architecture | ADR-L |
| Physical Architecture | ADR-PS |
| Component Architecture | ADR-PC |
| Capability Map | ADR capabilities |
| Invariant Map | ADR invariants |
| Contract Map | interaction contracts |
| Traceability | ADR relationships |
| Runtime Architecture | Architecture IR |
| Certification / Proof | conformance outputs |

Projection documents:

- are non-authoritative
- are derived from authoritative architecture sources
- exist to help humans understand, review, and govern the system
- should be reproducible from the architecture model
- may be versioned as part of architecture documentation and audit history

## Diagram Source Mapping

| Diagram Type | Projection Source |
|--------------|-------------------|
| Logical architecture | ADR-L relationships |
| Physical architecture | ADR-PS relationships |
| Component diagram | ADR-PC components and interfaces |
| Capability map | ADR capabilities |
| Invariant map | ADR invariants |
| Contract map | interaction contracts |
| Authority boundaries | ADR domains and component authority |
| Traceability diagram | ADR-L -> ADR-PS -> ADR-PC -> Component |
| Runtime flow | contracts and runtime components |
| Certification / proof flow | verification ADRs and conformance flows |

This mapping is doctrinal. It defines what canonical diagram families are views
of; it does not define generation tooling or IR schema.

## Logical vs Physical vs Component Diagram Definitions

### Logical Architecture Diagram

Derived from ADR-L relationships, capabilities, invariants, and contracts. It
shows intent and logical structure.

### Physical Architecture Diagram

Derived from ADR-PS relationships. It shows how logical intent is realized in
system design.

### Component Diagram

Derived from ADR-PC components, interfaces, and implementation identifiers. It
shows what components exist and how they interact.

### Traceability Diagram

Shows ADR-L -> ADR-PS -> ADR-PC -> Component relationships.

## Traceability Diagrams

Traceability diagrams are a canonical architecture diagram type. They
visualize how logical intent is realized by physical design, implemented by
components, and embodied in code or infrastructure.

Traceability diagrams must use Mermaid.

## Projection Scope Stability

Each projection type, including logical, physical, component, traceability,
lifecycle, authority, and runtime views, must have a stable definition and
scope over time.

Changes in a projection should reflect architecture changes, not layout,
interpretation, or scope changes. Projection diffs must remain usable for
architecture review, governance, and audit, and projection documents must
remain comparable across versions.

If the definition of what a projection includes changes, that is an
architecture doctrine change and must be documented accordingly. Projection
scope changes are architecture changes, not editorial diagram updates.

## Diagram-as-Code Principle

Canonical diagrams must be:

- text-based
- version-controlled
- diffable
- renderable
- machine-readable

Mermaid is the standard format because it satisfies these properties.

## Standard Mermaid Diagram Types by Architecture Concept

| Architecture Concept | Mermaid Type |
|----------------------|--------------|
| artifact flow | `flowchart` |
| lifecycle / spine | `stateDiagram` or `flowchart` |
| component relationships | `flowchart` or `C4` |
| repository relationships | `flowchart` |
| authority surfaces | `flowchart` |
| contract boundaries | `flowchart` |
| sequence / interaction | `sequenceDiagram` |
| state transitions | `stateDiagram` |
| data model | `erDiagram` |
| system context | `C4Context` |

## When Mermaid Is Required

Mermaid is required for canonical diagrams that represent:

- system architecture
- component relationships
- artifact lifecycle
- documentation-state -> integration-state -> runtime evidence -> reporting
  flows
- authority boundaries
- repository relationships
- contract boundaries
- certification / proof flow
- activation / governance flow
- traceability diagrams

## When ASCII Is Allowed

ASCII or Unicode box diagrams may be used for:

- small inline conceptual sketches
- brief narrative examples
- terminal-only contexts
- explicitly illustrative content that is not a canonical architecture diagram

## Normalization Guidance

During ASCII-to-Mermaid conversion, the architecture must not change. Only the
representation format may change.

Preserve labels, structure, flow direction, and authority meaning.

Not all ASCII diagrams must be converted. Only diagrams representing canonical
system architecture, lifecycle, authority, or flows must be converted. Inline
conceptual ASCII diagrams may remain ASCII when they are not canonical
architecture diagrams.

## Stability Guidance

- Prefer stable node IDs.
- Prefer simple layouts such as `TD` or `LR`.
- Avoid unnecessary layout complexity.
- Keep Mermaid source readable in raw Markdown.
- Diagram diffs should reflect architecture changes, not layout churn.

Stability applies both to Mermaid layout choices and to the semantic scope of
what each projection type includes. Layout stability and projection scope
stability together ensure that diffs primarily reflect architecture changes
rather than formatting or interpretation changes.

## Non-Goals

This document does not define:

- styling guidance
- theming guidance
- CI enforcement
- diagram generation tooling
- renderer pipelines
- schema change
- runtime behavior change
- repository restructuring
