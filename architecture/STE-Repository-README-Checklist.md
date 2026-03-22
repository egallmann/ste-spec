# STE Repository README Checklist

This checklist operationalizes
[`ADR-036`](../adr/ADR-036-repository-readme-contract.md) and is intended to
help STE repositories converge their `README.md` files to the STE Repository
README Contract.

This checklist is guidance for convergence. It does not replace the ADR and it
does not create additional normative requirements beyond `ADR-036`. It does
not override normative ADRs, contracts, invariants, or Architecture IR
documentation.

Some sections are conditional by repository role and should be omitted only
when they are genuinely not applicable.

## Checklist

- [ ] `STE System Statement`
  Purpose: ensure every repository identifies itself as part of the STE system.

- [ ] `Mental Model and Pipeline Position`
  Purpose: ensure readers understand where the repository fits in the STE
  pipeline.

- [ ] `Inputs`
  Purpose: make dependencies and upstream authorities explicit.

- [ ] `Outputs`
  Purpose: make downstream consumers and integration surfaces explicit.

- [ ] `Responsibilities`
  Purpose: define what this repository must do.

- [ ] `Non-Responsibilities`
  Purpose: prevent responsibility drift.

- [ ] `Authority Boundary`
  Purpose: clarify decision-making authority and limits.

- [ ] `Determinism and Guarantees` when applicable
  Purpose: document behavioral guarantees and reproducibility expectations.

- [ ] `Failure Behavior` when applicable
  Purpose: document fail-open versus fail-closed and related error behavior.

- [ ] `CLI / Usage` when applicable
  Purpose: document the public operational surface.

- [ ] `Repository Boundary and Adapter Model`
  Purpose: clarify integration boundaries and adapter relationships.

- [ ] `Canonical Documents and Contracts`
  Purpose: point readers to the normative ADRs, schemas, invariants, and
  contracts.

## Review reminder

Before treating a README as converged, confirm that it:

- includes the required communicative content and makes it easy to find
- describes repository role and boundary clearly
- states responsibilities and non-responsibilities explicitly
- makes authority boundaries explicit
- makes repository pipeline position explicit
- identifies repository authority, if any
- identifies the canonical documents and contracts readers should rely on
- points to the actual normative artifacts for contracts and decisions
- does not contradict normative ADRs, contracts, invariants, schemas, or
  Architecture IR doctrine
- remains consistent with the STE integration model and authority ADRs
