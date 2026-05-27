# Workspace Graph Runtime Surfaces (Draft)

## Status

This directory documents draft, pre-normative runtime graph surfaces. It is a
docs-only classification: no stable JSON Schema is published here yet.

These surfaces are owned by `ste-runtime` unless and until an accepted
`ste-spec` ADR promotes a specific payload to a public cross-component
contract.

## Scope

The workspace graph family includes:

- **WorkspaceGraphSlice** - a per-repository graph slice emitted by runtime
  workspace RECON.
- **WorkspaceGraph** - a merged graph assembled from validated slices and
  cross-repo edges.
- **WorkspaceGraphIndex** - a runtime workspace index describing per-repo
  slice status and output locations.

These artifacts are derived runtime state. They are not Architecture IR, not
canonical ADR state, and not an admission decision.

## Authority

| Subject | Authority |
| --- | --- |
| Runtime emission algorithm | `ste-runtime` |
| Runtime-local slice contract ADR | `ste-runtime` ADR-L-0016 |
| Public Architecture IR | `ste-spec/contracts/architecture-ir/` |
| Admission decisions | `ste-kernel` |

If a workspace graph field conflicts with public Architecture IR semantics, the
public Architecture IR contract wins at the cross-component boundary.

## Draft Shape

### WorkspaceGraphSlice

Required core fields:

- `schema_version`
- `repo`
- `generated_by`
- `generated_at`
- `nodes`
- `edges`

Standard optional fields:

- `source_commit`
- `diagnostics`

Nodes carry stable runtime graph identity, type, display name, provenance, and
optional attributes. Edges carry source node ID, target node ID, verb, optional
confidence, optional provenance, and optional attributes.

### WorkspaceGraph

The merged graph records:

- `schema_version`
- `generated_at`
- `partial_from`
- `nodes`
- `edges`

`partial_from` identifies repositories whose slices failed validation or could
not be loaded. Consumers must treat a non-empty value as a visible partial-state
signal.

## Compatibility Policy

Runtime validation may support both warn and reject modes. Warn mode allows
unknown node types or edge verbs to surface without breaking staged adoption.
Reject mode is appropriate for stricter contract gates.

Unknown extension fields may be preserved by runtime consumers, but they are not
portable public contract authority.

## Promotion Criteria

Before any workspace graph payload becomes a stable `ste-spec` contract, it
needs:

- an accepted `ste-spec` ADR naming the handoff boundary
- schema files and examples under this directory
- invariant updates under `ste-spec/invariants/`
- contract guards in producing and consuming repositories
- clear distinction from Architecture IR and Kernel admission payloads
