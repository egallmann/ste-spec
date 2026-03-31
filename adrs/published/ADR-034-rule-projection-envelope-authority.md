# ADR-034: Rule Projection Envelope Authority (draft contract)

## Migration status

| Field | Value |
| --- | --- |
| **Canonical record** | Machine ADR **ADR-L-0034** — [`adrs/logical/ADR-L-0034-rule-projection-envelope-authority.yaml`](../logical/ADR-L-0034-rule-projection-envelope-authority.yaml) |
| **Human projection** | [`adrs/rendered/ADR-L-0034.md`](../rendered/ADR-L-0034.md) (generated; do not edit by hand) |
| **This file** | Legacy published markdown; **not canonical** |
| **Disposition** | Migrated one-to-one (draft envelope remains proposed in machine ADR) |

Authority: treat **ADR-L-0034** as the source of truth for decisions and invariants.

---

## Status

Proposed

## Context

STE needs **ADR-bound rule projections** and related **attestations** (for example
**steelman** outcomes) that are **machine-native**, **replayable**, and **separate**
from **`ArchitectureEvidence`** and **`KernelAdmissionAssessment`**. Early prototypes may
inline adjudication; the **durable** boundary keeps **rule closure and signing** on the
**rules-engine** side while **`ste-kernel` orchestrates** consumption.

## Decision

1. **`ste-spec` owns** the interchange **envelope** shape for these artifacts under
   `contracts/rule-projection/` once promoted from draft (today: **draft JSON Schema**
   only).

2. **Semantic rules** for envelopes are expressed in **`invariants/`** (see
   **INV-0010**).

3. **`ste-kernel` MUST NOT** be treated as the authoritative signer or compiler of
   rule text for these envelopes; it **MAY** verify, route, or cache **rules-engine**
   outputs per published contracts.

4. Kernel rule evaluation may be normative in `ste-spec` doctrine without
   promoting this envelope family to accepted contract status. Until promotion,
   the envelope remains draft and interface-only.

## Rationale

Centralizes **contract authority** (ADR-030) for a new handoff family without collapsing
**integration IR admission** and **workspace compliance gates** into one payload.

## Consequences

- Promotion requires: stable `$id`, tests/examples, and index updates in
  `contracts/README.md` and `invariants/STE-Cross-Component-Contract-Invariants.md`.
- Kernel adapter surfaces (`adapter-contracts.yaml`) change only when merge policy
  explicitly extends the adapter star.

## Related

- `contracts/rule-projection/README.md`
- `invariants/INV-0010-rule-projection-envelope-discipline.md`
- `execution/STE-Kernel-Execution-Model.md` (**Rules projections and adjudication**)
