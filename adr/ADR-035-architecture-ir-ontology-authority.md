# ADR-035: Architecture IR Ontology Authority in ste-spec

## Status

Accepted

## Context

`ste-kernel` owns the mechanical `Compiled_IR_Document` contract (schema, merge
order, identity, compiled relationship enums). `adr-architecture-kit` owns ADR
artifact structure. STE still requires a single normative place for **what**
Architecture IR **means**: entity and relationship semantics, provenance
classes, lifecycle and completeness, governance roles, the architecture control
loop, and the Architecture Index.

Without an explicit authority split, readers conflate JSON `kind` enums with the
full architecture ontology, or duplicate mechanical schema in prose.

## Decision

`architecture/STE-Architecture-Intermediate-Representation.md` is the **canonical
semantic specification** of the STE Architecture Intermediate Representation
(Architecture IR).

Mechanical JSON Schema and compiled enumerations remain **referenced** from
`ste-kernel` per `contracts/README.md` and
`contracts/architecture-ir-kernel-contract-pin.json`. This ADR does not move
schema ownership.

## Rationale

- Preserves a single **meaning** authority in `ste-spec` while keeping **shape**
  authority in `ste-kernel`.
- Allows the semantic ontology to evolve ahead of mechanical `ir_version` bumps
  when realization is documented explicitly (registry surfaces, adapter
  projection, index artifacts).

## Consequences

- Cross-repository discussions of Architecture IR terminology **SHOULD** align
  with `STE-Architecture-Intermediate-Representation.md`.
- Extending mechanical IR enums **MUST** remain a `ste-kernel` contract change;
  semantic additions **MAY** land in `ste-spec` first with a realization section.
