# ADR-034: Rule Projection Envelope Authority (draft contract)

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
