<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: ec31d191de525cdeb255d7aa0310389fedcf0e1752d20cd44b7cc42f6a61965a
rendered_hash: f6b2589d428e71c7901763e7f700849f1c53f5e799cb7ace8c612fa069575790
-->

# ADR-L-0023: Validation Timing and Responsibility

**Status:** accepted<br>
**Created:** 2025-12-23<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** gateway, validation<br>
**Tags:** lifecycle, eligibility<br>
**Alias name:** validation-timing-and-responsibility<br>

## Context

Validation occurs at merge-time (ADF), pre-execution (Gateway), and locally (Runtime).
Only Gateway may authorize execution; ADF blocks canonical promotion; Runtime checks are
advisory for eligibility. Normalized outcomes treat INDETERMINATE as blocking for
authoritative paths.

Legacy: `adrs/published/ADR-023-validation-timing-responsibility.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1002** admission
semantics and **ADR-L-1009** caller contracts apply at the kernel documentation boundary;
this ADR assigns **STE-system component responsibilities** for validation stages.

**Reconciliation vs ADR-L-0026:** Gateway normative conflict handling is **verification of
Fabric-attested conflict status**, not independent content parsing (see ADR-L-0026).








## Invariants

### INV-2301

**Statement:** No component other than Gateway MAY treat local or merge-time validation success as
sufficient to authorize execution eligibility when Gateway has not returned an explicit
ALLOW outcome per contract.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves synchronous enforcement at the Gateway boundary.






## Decisions

### DEC-2301: Assign ADF merge-time validation to canonical promotion blocking only; Gateway sole execution approval; Runtime local checks advisory only

**Rationale:**
Prevents Runtime self-approval and clarifies layered enforcement.



**Consequences:**

**Positive:**
- Single authoritative execution gate

**Negative:**
- Runtime cannot substitute for Gateway


### DEC-2302: Normalize validation outcomes; treat INDETERMINATE as FAIL for execution eligibility and canonical promotion

**Rationale:**
Eliminates ambiguous partial success for authoritative transitions.



**Consequences:**

**Positive:**
- Aligns with fail-closed posture

**Negative:**
- Transient validation issues block promotion or execution


### DEC-2303: Require normative invariant conflict verification at Gateway during eligibility; allow optional preventative detection at ADF merge-time

**Rationale:**
Gateway remains the definitive enforcement boundary; ADF may fail fast before publication.



**Consequences:**

**Positive:**
- Clear normative vs preventative split

**Negative:**
- Algorithmic detail delegated to Fabric attestation model (ADR-L-0026)



## Gaps

### GAP-2301: Machine schemas for validation result envelopes in Architecture IR

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0023 by ADR Architecture Kit*