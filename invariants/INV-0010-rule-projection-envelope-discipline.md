# INV-0010: Rule Projection Envelope Discipline (draft scope)

## Scope

**ADR-bound rule projections**, **steelman / compliance attestations**, and related
artifacts that cross the **`ste-kernel` ↔ rules-engine** boundary.

**Two artifact families (informative):**

1. **Rule projection envelope** — what the **rules-engine** materializes (`contracts/rule-projection/`): closure pins, hashes, encoded slice. **Not** the durable “we accepted this at merge” row by itself.
2. **Governance decision record** — what the **governance-engine** persists (`contracts/governance-decision-record/`): references **`projection_id`** / **closure hash**, **ADR** bind, **outcome**, **actor**, **time**.

This invariant applies when implementations adopt the draft schema under
`contracts/rule-projection/`. Until that schema is **promoted** to normative status
via `ste-spec` ADR and contract index updates, treat this document as **design
intent**.

## Rule

1. **Binding:** A rule projection envelope **MUST** name **`adr_id`** and **`ruleset_pin`**
   (`ruleset_version` and, when used for verify, a **content hash** or reproducible
   closure expansion) so the same **git tree** can reconstruct the rule closure under
   verify.

2. **Authority:** **Signing / attestation semantics** for the projection **MUST** remain
   with the **rules-engine** (or delegated signer); **`ste-kernel` MUST NOT** silently
   replace or re-author rule semantics while claiming the same **`projection_id`**.

3. **Separation:** **IR validation** and **`KernelAdmissionAssessment`** remain
   distinct from **steelman / compliance** outcomes carried in projection envelopes;
   do not encode admission decisions inside evidence-only contracts.

## Enforcement Expectation

- **On-demand projection:** Consumers honor **timeouts and size budgets**; overload
  responses are explicit (partial + diagnostic or fail-closed), never “empty means
  no rules.”
- **CI / merge verify:** Prefer **mechanical** reconstruction + signature checks over
  live LLM replay unless policy explicitly accepts non-deterministic gates.

## Related Artifacts

- `contracts/rule-projection/rule-projection-envelope.schema.json`
- `contracts/rule-projection/README.md`
- `contracts/governance-decision-record/README.md`
- `contracts/governance-decision-record/decision-record.schema.json`
- `architecture/STE-Worked-Example-Walkthrough.md`
- `execution/STE-Kernel-Execution-Model.md` (**Rules projections and adjudication**)
- `adrs/published/ADR-030-contract-authority-in-ste-spec.md`
- `adrs/published/ADR-034-rule-projection-envelope-authority.md`
