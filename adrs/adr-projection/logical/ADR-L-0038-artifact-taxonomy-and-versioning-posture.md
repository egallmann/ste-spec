<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: e9a4e8f0ca09ae6e2566a14389783fe5ec05484f55e8777b1fef2fe32a248b5b
rendered_hash: 759394b7c467f7ec6dc08a2dddca365ab756773dab3a6b96a873eebe475d6340
-->

# ADR-L-0038: Artifact Taxonomy and Versioning Posture

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, taxonomy<br>
**Tags:** artifacts, versioning<br>
**Alias name:** artifact-taxonomy-and-versioning-posture<br>

## Context

STE assigns each artifact a taxonomy **kind** per the ste-spec architecture document that
defines artifact taxonomy and versioning posture (under `architecture/`).
Version-control posture follows that kind, not repository or team preference.
This ADR is canonical for taxonomy and versioning posture; ADR-L-0040 maps kinds into
Spine stages without redefining the taxonomy.

Legacy: ste-spec published **ADR-038** (markdown under `adrs/published/`).

**Reconciliation vs ADR-L-1003 / ADR-L-1007:** **coexist-with-precedence** — governance
posture and Golden models reference artifact participation; ADR-L-0038 remains the
**taxonomy and VCS posture** authority.








## Invariants

### INV-3801

**Statement:** Repositories MUST apply the ste-spec architecture doctrine that defines artifact taxonomy
kinds and versioning posture when determining version-control treatment for STE artifacts.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Makes the taxonomy document enforceable via ADR-L.




### INV-3802

**Statement:** Spine doctrine and lifecycle projections MUST NOT introduce new top-level taxonomy
kinds or alter VCS posture established in ADR-L-0038 without amending this ADR-L.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves precedence versus ADR-L-0040.






## Decisions

### DEC-3801: Adopt STE artifact taxonomy kinds (Normative, Implementation, Proof Logic, Derived, Evidence, Reports, Orientation, Internal) with documented VCS posture per architecture doctrine

**Rationale:**
Prevents repositories from drifting on what is source truth versus regenerable output.



**Consequences:**

**Positive:**
- Shared reproducibility expectations

**Negative:**
- Requires discipline when assigning kinds to new outputs


### DEC-3802: Separate version-control posture from normative authority; committing generated artifacts does not make them authoritative

**Rationale:**
Avoids equating git presence with governance authority.



**Consequences:**

**Positive:**
- Clear authority versus storage distinction

**Negative:**
- Requires contributor education



## Gaps

### GAP-3801: Publication artifact exceptions remain labeled in doctrine; track in handbook index

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0038 by ADR Architecture Kit*