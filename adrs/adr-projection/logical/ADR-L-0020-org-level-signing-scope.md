<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: f8c2d4538ffeaeb66ef721bcb139683fcd12cf543f229aece6bc4d0457b0f894
rendered_hash: e4d42a79c7864d146c8c80dd07e3122b5fbd3b90056de709d9f6d3e643734d8e
-->

# ADR-L-0020: ORG-Level Signing Scope

**Status:** accepted<br>
**Created:** 2025-12-23<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, signing<br>
**Tags:** org-authority, signing-scope<br>
**Alias name:** org-level-signing-scope<br>

## Context

ORG-level signing applies only to artifacts that establish or ratify **canonical truth**;
ephemeral enforcement outputs, workspace-local bundles, and derived indexes are out of
scope for ORG signing.

Legacy: `adrs/published/ADR-020-org-signing-scope.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — complements **ADR-L-1009**
on fail-closed caller contracts; this ADR defines **what must be ORG-signed** versus
derived or ephemeral artifacts.








## Invariants

### INV-2001

**Statement:** ORG signing requirements MUST NOT be expanded to cover derived query results,
enforcement-only outcomes, or caches without a new ADR-L that documents the rationale.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Keeps ORG signatures meaningful as canonical-truth signals.






## Decisions

### DEC-2001: Require ORG signing only for canonical invariants, canonical artifacts, trust registry operations, and canonicalization events

**Rationale:**
Limits ORG keys to durable attestation surfaces; excludes eligibility decisions,
derived graph indexes, caches, and typical Context Bundle payloads except where other
ADRs require Human/PROJECT signing.



**Consequences:**

**Positive:**
- Prevents authority inflation across operational outputs

**Negative:**
- Implementers must classify artifacts carefully


### DEC-2002: Exclude ephemeral enforcement outcomes and derived state from mandatory ORG signing

**Rationale:**
Derived and short-lived results must remain verifiable from signed inputs without
expanding ORG signing to every computation.



**Consequences:**

**Positive:**
- Operational simplicity at the enforcement boundary

**Negative:**
- Requires clear labeling of non-canonical outputs



## Gaps

### GAP-2001: Enumerate artifact kinds in Architecture IR that require ORG signatures

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0020 by ADR Architecture Kit*