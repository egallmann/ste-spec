# Architecture Boundary Decision

## Migration status

| Field | Value |
| --- | --- |
| **Canonical record** | Machine ADR **ADR-L-0042** — [`adrs/logical/ADR-L-0042-open-standards-closed-intelligence-boundary.yaml`](../logical/ADR-L-0042-open-standards-closed-intelligence-boundary.yaml) |
| **Human projection** | [`adrs/rendered/ADR-L-0042.md`](../rendered/ADR-L-0042.md) (generated; do not edit by hand) |
| **This file** | Legacy published markdown; **not canonical** |
| **Disposition** | Non-numbered note migrated to ADR-L-0042 |

Authority: treat **ADR-L-0042** as the source of truth for decisions and invariants.

---

## Decision

STE adopts an **open standards plus closed intelligence** architectural
boundary.

Public specifications define compatible artifact formats, schemas, interfaces,
and deterministic validation surfaces. Internal intelligence-bearing systems may
exist behind those public interfaces without disclosing proprietary
implementation.

## Why this decision exists

- external users and contributors need durable public contracts
- compatible third-party implementations should be possible without access to
  internal private reasoning systems
- proprietary leverage should remain in intelligence-bearing implementation, not
  in hidden public contract requirements

## Public interface requirement

Public interfaces are necessary so that:

- public artifacts can be validated independently
- deterministic handoff surfaces remain implementable by others
- closed systems do not become a hidden dependency for basic compatibility

## Intentional private implementation

Internal implementation secrecy is intentional where the subsystem derives its
value from:

- heuristics
- scoring
- activation strategy
- projection strategy
- orchestration behavior
- adversarial or optimization logic

This secrecy is architectural. It is not accidental omission.

## Risks mitigated

- leaking proprietary leverage through public docs
- coupling public compatibility to private heuristics
- forcing contributors to depend on hidden orchestration behavior

## Tradeoffs introduced

- interfaces must be defined with discipline
- documentation drift can create authority confusion if public and private
  boundaries are not maintained
- some subsystems must remain interface-only even when their role is publicly
  described

## Downstream decisions

Future plans should use this decision to determine:

- whether a new capability belongs in public specification, interface-only
  publication, or closed implementation
- whether a new subsystem may be publicly named without exposing internals
- whether a new contract is deterministic enough for open standardization

## Status

Architectural boundary decision for current STE publication and future planning.
