# Linkage surface contracts (draft)

**Status:** Draft / pre-normative. This folder sketches Linkage Surface
contracts for MVC evolution experiments. Until promoted by ADR and indexed in
the cross-component contract inventory, consumers must not treat this shape as
stable interchange.

A Linkage Surface is a materialized set of cross-domain relationships available
for traversal and MVC assembly. It does not prescribe how relationships were
discovered. Relationships may originate from explicit schema references,
embodiment declarations, contract mappings, validator outputs, compiler outputs,
manually curated mappings, or future automated extraction mechanisms.

MVC, RSS, Context Domains, and Graph Domains consume Linkage Surfaces. They do
not depend on a specific linkage generation strategy.

## Boundary

Linkage improves discoverability. It does not automatically establish truth,
current validity, or embodiment. Authority, provenance, integrity, validation,
and admission remain separate concerns.

## Files

- `linkage-surface.schema.json` - draft schema for materialized cross-domain
  relationship surfaces.

## Related

- `contracts/graph-domain/`
- `contracts/context-domain/`
- `contracts/mvc/`
