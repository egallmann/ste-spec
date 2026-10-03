<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: b8ed8864f0a7233a267c3b8d41ebb1b92570364a1e6f49ad89f90410c44aa07a
rendered_hash: 491c7598c9aa8e5ceea198bb1ef2ddf7e3be0defd62960269756ce14b44f81f7
-->

# ADR-L-0042: Open Standards and Closed Intelligence Boundary

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, architecture<br>
**Tags:** boundary, standards<br>
**Alias name:** open-standards-and-closed-intelligence-boundary<br>

## Context

STE adopts **open standards plus closed intelligence**: public specifications define
compatible artifact formats, schemas, interfaces, and deterministic validation surfaces;
proprietary reasoning may remain behind those interfaces.

Legacy: `adrs/published/ARCHITECTURE_BOUNDARY_DECISION.md` (non-numbered published note).

**Reconciliation vs supporting architecture notes:** **coexist-with-precedence** — see
`architecture/OPEN_CLOSED_BOUNDARY.md` and related architecture notes for expanded prose;
this ADR-L captures the **binding boundary decision** in machine form.








## Invariants

### INV-4201

**Statement:** New capabilities MUST be classified explicitly as public specification, interface-only
publication, or closed implementation per this boundary before expanding ste-spec contracts.
<br>
**Scope:** global<br>
**Enforcement:** should (policy)<br>
**Verification:** audit

**Rationale:**
Operationalizes downstream planning checks described in the legacy document.






## Decisions

### DEC-4201: Require public, independently verifiable interfaces for handoff artifacts while allowing proprietary intelligence behind those surfaces

**Rationale:**
Enables third-party compatibility without leaking proprietary leverage into public contracts.



**Consequences:**

**Positive:**
- Clear public versus private architectural split

**Negative:**
- Interfaces must be maintained with discipline



## Gaps

### GAP-4201: Link detailed threat and tradeoff narratives from architecture supporting docs

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0042 by ADR Architecture Kit*