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

## Lifecycle Placement in the STE Spine

This ADR anchors the semantic meaning of Architecture IR across Intent
Definition and Architecture IR Compilation while preserving the separate
kernel-owned mechanics of compiled integration-state. It also affects Admission
Decision by preserving that compiled integration-state does not change semantic
authority ownership.

## Relationship to Enforcement Model

This ADR supplies the IR Semantics step in the chain `Doctrine -> Object Shape
-> IR Semantics -> Enforcement -> Admission` by defining what Architecture IR
terms mean. It depends on
[`ADR-033-closed-object-discipline.md`](ADR-033-closed-object-discipline.md)
for encoded boundary shape and informs
[`ADR-032-fail-closed-enforcement-model.md`](ADR-032-fail-closed-enforcement-model.md)
when semantically inconsistent material must be rejected before admission.

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
