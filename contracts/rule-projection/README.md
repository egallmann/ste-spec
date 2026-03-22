# Rule projection envelope (draft)

**Status:** **Draft / pre-normative.** This folder holds a **sketch** JSON Schema for
**ADR-bound rule projections** signed or emitted by the **rules-engine**
(`ste-rules-library` operational component). Until promoted via ADR and indexed in
`invariants/STE-Cross-Component-Contract-Invariants.md`, consumers **MUST NOT** treat
these files as stable interchange contracts.

**Orientation:** `ste-kernel` **orchestrates** requests for projections and **verifies**
or consumes **verdicts / signed bundles** from the rules side; it **MUST NOT** be the
authoritative home for rule closure semantics (see `execution/STE-Kernel-Execution-Model.md`,
**Rules projections and adjudication**).

- `rule-projection-envelope.schema.json` — draft envelope shape (IDs, ruleset pin,
  binding to ADR snapshot, optional attestation handle).

## Non-goals for v0 (prototype)

Until **ADR-034** is **Accepted** and the envelope **`$id`** is declared stable:

- **No normative signing algorithm** or key-management profile—optional `attestation` blobs are **opaque** in this draft.
- **No remote registry schema** in `ste-spec`—local append-only logs and **git-committed** indexes only.
- **Envelope fields** are authoritative for **local experiments** and **mechanical verify** prototypes; breaking changes **MAY** occur while `ste-rules-library` CLI output is aligned to this sketch.
- **Kernel adapter surfaces** for governance are **out of scope** for v0; see `ste-spec/contracts/governance-decision-record/` and Phase 6 orientation in `status.md` (**Deferred governance–kernel bridge**).

## Related

- `architecture/STE-Worked-Example-Walkthrough.md` (steelman / governance thread)
- `invariants/INV-0010-rule-projection-envelope-discipline.md`
- `glossary.md` (**Rule projection**, **Steelman gate**, **Adjudicator**)
