<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: aa967863b2cd72a8512cbe6488efc462bcb52cb4b9e7694b0879c3ba41ccd4f3
rendered_hash: c02a965e96c9b02fb8bc3969bb001bbcbb24a79129b5fd6d7eaed225fd470a22
-->

# ADR-L-0034: Rule Projection Envelope Authority

**Status:** proposed<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** contracts, governance<br>
**Tags:** rule-projection, kernel<br>
**Alias name:** rule-projection-envelope-authority<br>

## Context

ste-spec will own the interchange envelope for ADR-bound rule projections and related
attestations under `contracts/rule-projection/` when promoted from draft. Semantic rules
live in `invariants/` (e.g. INV-0010). ste-kernel must not be treated as authoritative
signer or compiler of rule text for these envelopes.

Legacy: `adrs/published/ADR-034-rule-projection-envelope-authority.md` (draft contract).

**Reconciliation vs ADR-L-1008:** **coexist-with-precedence** — decision outcome vocabulary
governs admitted decisions; rule-projection envelopes are a **separate durable family**
with rules-engine-side closure.








## Invariants

### INV-3401

**Statement:** Until the rule-projection envelope family is promoted to accepted contract status,
ste-kernel integrations MUST treat draft schemas as interface-only and MUST NOT imply
normative closure beyond published disclaimers.
<br>
**Scope:** global<br>
**Enforcement:** should (policy)<br>
**Verification:** audit

**Rationale:**
Prevents draft artifacts from becoming shadow normative authority.






## Decisions

### DEC-3401: Centralize rule-projection envelope contract authority in ste-spec once promoted from draft

**Rationale:**
Avoids collapsing integration IR admission and workspace compliance gates into one payload.



**Consequences:**

**Positive:**
- Clear ownership before kernel adapters harden

**Negative:**
- Promotion requires schema stability work


### DEC-3402: Allow kernel to verify, route, or cache rules-engine outputs per contracts without owning rule closure

**Rationale:**
Preserves signing and compilation authority on the rules-engine side for this family.



**Consequences:**

**Positive:**
- Separation of concerns

**Negative:**
- Requires explicit adapter documentation



## Gaps

### GAP-3401: Promotion checklist in ADR-034 legacy prose (stable $id`, tests, index updates)

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0034 by ADR Architecture Kit*