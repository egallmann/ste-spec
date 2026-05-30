# Graph domain contracts (draft)

**Status:** Draft / pre-normative. This folder sketches Graph Domain
Definition contracts for MVC evolution experiments. Until promoted by ADR and
indexed in the cross-component contract inventory, consumers must not treat this
shape as stable interchange.

A Graph Domain Definition is a declarative view/materialization contract over
Architecture IR or derived runtime/workspace graph sources. It defines graph
posture, source classes, selectors, topology metrics, provenance requirements,
freshness requirements, integrity constraints, and materialization boundaries.

Graph Domains are materialized derived state. They may expose relationships for
exploration, traversal, MVC assembly, topology analysis, and discovery, but they
do not create architectural authority.

## Authority Rule

A relationship materialized within a Graph Domain remains derived unless it is
independently established by authoritative artifacts. Traversability does not
prove authority, causal truth, completeness, or current validity.

## Files

- `graph-domain-definition.schema.json` - draft schema for declarative graph
  domain definitions.

## Related

- `contracts/workspace-graph/README.md`
- `contracts/architecture-ir/ARCHITECTURE_IR.md`
- `adrs/published/ADR-030-contract-authority-in-ste-spec.md`
- `adrs/published/ADR-031-runtime-kernel-responsibility-boundary.md`
- `adrs/published/ADR-035-architecture-ir-ontology-authority.md`
- `adrs/published/ADR-041-compiler-and-merge-authority.md`
