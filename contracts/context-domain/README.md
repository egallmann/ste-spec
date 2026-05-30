# Context domain contracts (draft)

**Status:** Draft / pre-normative. This folder sketches Context Domain
Definition and Context Domain Bundle contracts for MVC evolution experiments.
Until promoted by ADR and indexed in the cross-component contract inventory,
consumers must not treat these shapes as stable interchange.

A Context Domain Definition is a semantic view definition over Architecture IR
and referenced Graph Domain Definitions. It defines what kind of architectural
reality is needed, why it is needed, and under what authority, provenance,
integrity, traversal, projection, and admission constraints.

A Context Domain Bundle is a materialized instance of a Context Domain
Definition for a task, IR snapshot, graph snapshot, linkage surface, selector
version, and policy version.

## Hard Boundary

Context Domain Definitions are declarative. Context Domain Bundles are
materialized derived artifacts. Do not collapse these layers.

## Files

- `context-domain-definition.schema.json` - draft schema for declarative context
  domain definitions.
- `context-domain-bundle.schema.json` - draft schema for materialized candidate
  context domain bundles.

## Related

- `contracts/graph-domain/`
- `contracts/linkage-surface/`
- `contracts/mvc/`
- `contracts/architecture-ir/ARCHITECTURE_IR.md`
