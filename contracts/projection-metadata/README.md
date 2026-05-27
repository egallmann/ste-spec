# Projection Metadata Runtime Surface (Draft)

## Status

This directory documents draft, pre-normative metadata for runtime-generated
projections. It is a docs-only classification: no stable JSON Schema is
published here yet.

Projection metadata is currently a runtime-owned derived surface emitted by
`ste-runtime` multi-resolution projection workflows.

## Scope

Projection metadata describes how a human- or tool-facing projection was
derived from runtime graph material. It does not make the projection
authoritative.

Typical projection files may include frontmatter fields such as:

- `projection_level`
- `projection_family`
- `projection_intent`
- `source_query`
- `generation_timestamp`
- `derivation`
- `confidence`
- `node_count`
- `edge_count`
- `compression_ratio`
- `generation_hash`
- `drill_down`
- `drill_up`

## Resolution Levels

`ste-runtime` currently uses five conceptual resolution levels:

| Level | Intended use |
| --- | --- |
| `L0` | System context for human orientation |
| `L1` | Service topology with infrastructure aggregation |
| `L2` | Capability-domain topology for human architecture review |
| `L3` | Contract and integration topology with endpoint detail |
| `L4` | Full graph fidelity for machine consumption |

The levels describe projection posture, not artifact authority. An `L0`
projection is not less valid than an `L4` projection; it is less detailed and
must preserve traceability to the source graph.

## Authority Rules

- Projection metadata is derived from runtime graph state and projection
  configuration.
- Projections must not be treated as canonical intent or public Architecture IR.
- Deterministic projection logic is preferable to model-generated summaries when
  the output is used for review, diffing, or governance.
- Aggregate nodes and compressed edges should preserve traceability to source
  graph nodes and edges.

## Promotion Criteria

Before projection metadata becomes a stable `ste-spec` contract, it needs:

- an accepted `ste-spec` ADR naming the consumer boundary
- schema and example fixtures
- validation commands in producer repositories
- explicit rules for freshness, lineage, and traceability
