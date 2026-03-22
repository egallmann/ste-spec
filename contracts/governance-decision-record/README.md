# Governance decision record (draft)

**Status:** **Draft / pre-normative.** Describes the **minimum** shape for a **durable
governance decision** that references a **rule projection envelope**—distinct from
the envelope itself (`contracts/rule-projection/`). **ste-spec** owns this sketch;
implementations **MAY** store rows as JSONL, SQLite, or git-committed index.

**Purpose:** Reviewers can confirm “enough for **CI replay**” without choosing storage
technology: same **git tree** → recompute **closure hash** → compare to recorded
expectation bound to **ADR snapshot**.

**Merge-path verify (methodology):** **Merge-path verify is commit-scoped:** mechanical
checks recompute from the **same git revision** the merge is about; otherwise **closure
hashes attest nothing**. **Why (STE):** that keeps **documentation-state**, **rule
closure**, and **CI** from drifting into **two competing truths**—the **addressable**
pin is the commit (and paths) under verify, not a floating “latest rules” source.

## Minimum fields (logical)

| Field | Required | Meaning |
|-------|----------|---------|
| `decision_id` | yes | Stable id for this row (UUID or content-address) |
| `projection_id` | yes | References `rule-projection-envelope.projection_id` |
| `rules_closure_hash` | yes\* | Same as `ruleset_pin.rules_catalog_hash` or dedicated closure id |
| `adr_id` | yes | ADR identifier |
| `adr_content_hash` | recommended | Hash of ADR body at decision time |
| `outcome` | yes | e.g. `pass`, `fail`, `waived`, `override` |
| `actor` | yes | User or service principal |
| `recorded_at` | yes | ISO-8601 timestamp (audit only; verify uses hashes) |
| `override_of` | no | Prior `decision_id` if this supersedes |
| `envelope_path` | no | Workspace-relative path to envelope JSON |
| `notes_uri` | no | Link to rationale (human projection) |

\*Required when verify compares closure; may be embedded in envelope only if verify always loads envelope by `projection_id`.

## Related

- `contracts/rule-projection/rule-projection-envelope.schema.json`
- `invariants/INV-0010-rule-projection-envelope-discipline.md`
- `execution/STE-Kernel-Execution-Model.md` (**Rules projections and adjudication**)
- `ste-rules-library/scripts/governance_cli.py` (prototype CLI; informative)

## Machine shape (draft)

See `decision-record.schema.json` (draft JSON Schema; unstable `$id` until promoted).
