<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: f67405a2918969367488b6475caa644b219c94f4a079620abedab5ee627aa691
rendered_hash: 61b677a018323219b0a9dfe92a1cad3cf2f607dc11eb324f61a08e0362eefc93
-->

# ADR-L-0036: Repository README Contract

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, documentation<br>
**Tags:** readme, boundaries<br>
**Alias name:** repository-readme-contract<br>

## Context

Every STE repository `README.md` MUST serve as a human-readable architectural boundary
and responsibility description. README is an orientation entry point, subordinate to ADRs,
contracts, invariants, and Architecture IR doctrine.

Legacy: `adrs/published/ADR-036-repository-readme-contract.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — kernel governance ADRs do
not define README structure; this ADR governs **repository human entrypoints** only.








## Invariants

### INV-3601

**Statement:** When README content conflicts with a normative ADR, invariant, schema, contract, or
Architecture IR doctrine, the normative artifact MUST govern and README MUST be corrected.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves README as explanatory orientation only.






## Decisions

### DEC-3601: Require README.md to communicate authority, responsibilities, non-responsibilities, inputs, outputs, boundaries, and lifecycle position without becoming normative authority

**Rationale:**
Prevents repository responsibility drift while keeping normative truth in ADRs and contracts.



**Consequences:**

**Positive:**
- Faster onboarding and boundary clarity

**Negative:**
- README maintenance burden



## Gaps

### GAP-3601: Optional checklist templates per repository role belong in handbook or scripts

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0036 by ADR Architecture Kit*