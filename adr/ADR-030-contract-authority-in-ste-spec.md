# ADR-030: Contract Authority in ste-spec

## Status

Accepted

## Context

The runtime/kernel handoff became operational before `ste-spec` clearly owned
its contract surface. That left room for repo-local types, tests, and prose to
act as shadow authorities.

## Decision

Cross-repository handoff contracts are governed in `ste-spec`.

Contract shape lives in `contracts/`. Contract rules live in `invariants/`.
Rationale and boundary intent live in `adr/`.

## Lifecycle Placement in the STE Spine

This ADR operates in the Intent Definition stage of the STE Spine by governing
the normative contract authority that shapes Publication / Integration Input at
the runtime/kernel boundary. It also affects Publication / Integration Input by
constraining which contract-backed artifacts can participate there without
defining the full Spine sequence or state machine.

## Rationale

This keeps a single normative source for payload structure, semantic rules, and
architectural intent.

## Consequences

- Runtime and kernel representations are subordinate implementation surfaces.
- Contract changes require coordinated `ste-spec` updates.
- Repo-local tests consume `ste-spec` artifacts rather than inventing parallel authority.
