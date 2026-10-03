<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: a06b991a5b9bd51c27b97b268bf582ac6c1ca36c3e50a5a95a0432200b18055e
rendered_hash: c6379764969fa2350c705e433e0b8ab20294cd45403c4a967fd2f9eaf90d9413
-->

# ADR-L-0027: Scope Semantics and Versioning

**Status:** accepted<br>
**Created:** 2025-12-29<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** gateway, trust<br>
**Tags:** scope, authority<br>
**Alias name:** scope-semantics-and-versioning<br>

## Context

Scope is a colon-delimited hierarchical identifier participating in authority checks.
Version 1 uses exact string equality; version 2 uses segment-prefix matching with
most-specific authority resolution and denial on equal-depth ambiguity. Trust Registry
and Context Bundle must declare `scope_semantics_version` consistently.

Legacy: `adrs/published/ADR-027-scope-semantics.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — trust and admission
stories in **ADR-L-1002** / **ADR-L-1009** apply at kernel documentation boundaries;
this ADR defines **STE scope string mechanics** for Gateway checks.








## Invariants

### INV-2701

**Statement:** Gateway MUST NOT upgrade or infer `scope_semantics_version`; mismatched declared
versions between Trust Registry and Context Bundle MUST result in denial.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Prevents silent semantic upgrades.






## Decisions

### DEC-2701: Validate scope grammar (segments of alphanumerics, underscore, hyphen; length and depth limits) and require explicit semantics version per Trust Registry entry and Context Bundle

**Rationale:**
Prevents ambiguous or unbounded scope strings and enables safe evolution.



**Consequences:**

**Positive:**
- Portable scope identifiers

**Negative:**
- Version mismatch becomes a hard denial


### DEC-2702: For version 1, require exact case-sensitive equality between authority scope and claimed scope

**Rationale:**
Minimal deterministic baseline compatible with pre-v2 artifacts when version omitted.



**Consequences:**

**Positive:**
- Simple matching semantics

**Negative:**
- No hierarchical delegation in v1


### DEC-2703: For version 2, require prefix match on segment boundaries; select deepest matching authority; deny with SCOPE_CONFLICT on equal-depth ties

**Rationale:**
Supports delegated authority without regex or fuzzy matching.



**Consequences:**

**Positive:**
- Predictable delegation resolution

**Negative:**
- Registry hygiene required to avoid conflicts



## Gaps

### GAP-2701: Future versions beyond v2 require new ADR-L and explicit version values

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0027 by ADR Architecture Kit*