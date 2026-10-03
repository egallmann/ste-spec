<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: a14a423b9faae809258e4ca7eb20ad4eacc726f5efa6f58545b67638ba17aee9
rendered_hash: b56acc4b0c2ee108d29a64a69b68bf7b70033a616832c062baa1745a56738f05
-->

# ADR-L-1006: Evidence Authority Model

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel, evidence<br>
**Tags:** evidence, authority<br>
**Alias name:** evidence-authority-model<br>

## Context

Runtime evidence is authoritative as **factual observation** within its contract, not as
a replacement for normative architecture declared in ste-spec and documentation-state.
When evidence contradicts IR or ADR meaning, the kernel MUST categorize contradiction as
drift or assessment finding; it MUST NOT silently rewrite normative sources.

Governance authority may authorize exceptions through explicit artifacts per ADR-040;
raw runtime truth does not override architecture by default.








## Invariants

### INV-5051

**Statement:** Evidence MUST NOT be interpreted as normative architecture authority; overrides MUST
flow from governance artifacts, not from raw observations alone.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Preserves documentation-state authority while still using factual runtime observations.






## Decisions

### DEC-6651: Enumerate authoritative evidence sources by contract family

**Rationale:**
Admission must know which observations count and under what provenance kinds.





### DEC-6652: Contradiction yields drift or assessment output, not silent IR mutation

**Rationale:**
Preserves documentation-state authority and auditability.






## Gaps

### GAP-5051: Cross-contract evidence bundle completeness rules

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-1006 by ADR Architecture Kit*