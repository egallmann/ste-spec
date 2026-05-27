# Implementation Attribution Evidence (Draft Handoff)

## Status

This directory documents the cross-repo handoff role for implementation
attribution evidence. It is draft/pre-normative in `ste-spec`; the current
schema authority remains in `adr-architecture-kit` until promoted by accepted
`ste-spec` governance.

## Purpose

Implementation attribution evidence records explicit claims that an
implementation artifact realizes ADR authority or enforces invariants. It gives
tools and reviewers a provenance-rich bridge from embodiment back to declared
intent.

## Current Authority Split

| Responsibility | Owner |
| --- | --- |
| Decorator and metadata semantics | `adr-architecture-kit` |
| Evidence schema and validation semantics | `adr-architecture-kit` |
| Source parsing and evidence emission | `ste-runtime` |
| Public contract promotion | `ste-spec` |
| Admission or governance decision | `ste-kernel` / governance |

`ste-runtime` may emit implementation attribution evidence. That emission is a
factual extracted claim, not proof of correctness and not an admission decision.
`adr-architecture-kit` validates those claims against canonical ADR state.

## Draft Record Semantics

An attribution evidence record identifies:

- implementation entity ID
- implementation entity type
- attributed ADR IDs
- enforced invariant IDs
- provenance, including source file and extractor
- optional metadata

Missing attribution, invalid ADR references, or superseded ADR references are
validation concerns owned by ADR-Kit policy profiles such as greenfield,
brownfield, and migration.

## Promotion Criteria

Before this becomes a stable `ste-spec` contract, the workspace needs:

- an accepted contract authority ADR
- a `ste-spec` schema and example fixtures
- validation alignment with ADR-Kit
- runtime fixture sync tests or contract guards
- consuming behavior in Kernel or governance tooling that justifies promotion
