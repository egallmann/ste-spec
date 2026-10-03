<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 85998f894400f9108d26e74d00008ac41d23d65b84cfa3d39892a655f880df20
rendered_hash: 88b9a1cd45af8c77c3baeb8f4e61e83cd3803be80c6d7dcca1f13fb49187ef91
-->

# ADR-L-0006: Explicit Unknowns Over Inference

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** extraction, documentation-state, recon<br>
**Tags:** unknowns, transparency, extraction<br>
**Alias name:** explicit-unknowns-over-inference<br>

## Context

When extractors cannot fully determine relationships or properties, the system must not
silently guess. This ADR-L encodes explicit **unknowns** alongside known facts.

Legacy human projection: `adrs/published/ADR-006-explicit-unknowns.md`. Aligns with
**ADR-L-0001** (deterministic extraction; unknowns when patterns are not observable).

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — kernel governance ADRs
(1001–1009) govern admission and documentation-state authority at the STE kernel
boundary; this ADR governs **Fabric extraction and slice truth** semantics. If a
conflict appears, kernel governance precedes for **admission**, this ADR for **slice
unknown recording** unless explicitly merged in a future ADR-L.








## Invariants

### INV-0601

**Statement:** When extraction cannot determine a relationship or property that belongs in the slice
model, the system MUST record an explicit unknown rather than inventing a definitive
edge or attribute from heuristics alone.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves honesty and aligns with ADR-L-0001 prohibition on probabilistic graph assertions.




### INV-0602

**Statement:** Unknowns MUST be first-order records in the slice documentation contract (queryable and
attributable), not only log lines or informal notes.
<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Ensures unknowns are visible to APIs, audits, and humans—not buried in logs.






## Decisions

### DEC-0601: Track extraction unknowns with the same rigor as known elements

**Rationale:**
Fabric MUST represent gaps explicitly so consumers can trust query results and
prioritize extractor work. Rejected alternatives: heuristic inference (hides
uncertainty), omitting elements (loses partial knowledge), vague low-confidence flags
(not actionable).


**Alternatives Considered:**

- **Heuristic inference for gaps**: Produces false positives and indistinguishable provenance versus deterministic extraction.

- **Omit elements when extraction is incomplete**: Loses partial information and visibility into gaps.

- **Whole-slice low-confidence flag only**: Too coarse to query, assert against, or prioritize fixes.


**Consequences:**

**Positive:**
- Honest, queryable representation of limits

**Negative:**
- Incomplete graphs and user education burden


### DEC-0602: Use categorized unknown records attached to slices

**Rationale:**
Unknowns SHOULD carry a stable category (e.g. opaque boundary, unsupported language,
incomplete extraction, manual assertion needed) and descriptive context so reporting
and APIs can filter and aggregate. Operational surfaces (HTTP APIs, event feeds) are
implementation details outside this ADR-L.



**Consequences:**

**Positive:**
- Gap visibility drives extractor prioritization

**Negative:**
- Requires consistent category vocabulary maintenance



## Gaps

### GAP-0601: Normative machine schema for unknown records in Architecture IR

**Impact:** medium<br>
**Blocking:** No





### GAP-0602: Cross-link to ADR-L-0009 when assertion precedence is machine-encoded

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0006 by ADR Architecture Kit*