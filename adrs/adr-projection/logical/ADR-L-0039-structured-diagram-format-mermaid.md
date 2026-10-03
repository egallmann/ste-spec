<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: be335ef631acb5163b737d2225150d6f8be51e8b1b3be9832c0ac624d8d9e58a
rendered_hash: b25fcc96526530b6ad8684dd0ff936ef81c99f20643f3bbbd70f38333d260d19
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

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0039 by ADR Architecture Kit*