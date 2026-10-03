<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 3429c20ec1a86cf07ac703935d50cf75fab4ae3e41dcd9eb58e1ecc8b2b991d9
rendered_hash: c735947ae26f0c3d0ffb5ffb31d73e126689584752f2fad879571477d1ee65f6
-->

# ADR-L-0039: Structured Diagram Format (Mermaid)

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** documentation, architecture<br>
**Tags:** mermaid, diagrams<br>
**Alias name:** structured-diagram-format-mermaid<br>

## Context

Canonical architecture diagrams in ste-spec MUST use structured, text-based
representation; Mermaid is the standard for canonical diagrams. Diagrams are projections
only and MUST NOT introduce semantics absent from ADRs, contracts, or architecture doctrine.

Legacy: `adrs/published/ADR-039-structured-diagram-format-mermaid.md`.

**Reconciliation vs ADR-L-0040:** **coexist-with-precedence** — Spine lifecycle is defined
in ADR-L-0040; this ADR governs **diagram representation format** for ste-spec projections.








## Invariants

### INV-3901

**Statement:** Canonical architecture diagrams MUST NOT be the sole location where a rule, requirement,
or invariant is first defined; authoritative text remains in ADRs, contracts, or doctrine.
<br>
**Scope:** repository<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Prevents diagrams from becoming shadow normative sources.






## Decisions

### DEC-3901: Standardize canonical ste-spec architecture diagrams on Mermaid text sources

**Rationale:**
Reduces format drift and keeps diagrams diffable and reviewable.



**Consequences:**

**Positive:**
- Consistent authoring across architecture docs

**Negative:**
- Styling and CI enforcement remain out of scope here



## Gaps

### GAP-3901: Authoring conventions and CI checks may be added under separate governance

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0039 by ADR Architecture Kit*