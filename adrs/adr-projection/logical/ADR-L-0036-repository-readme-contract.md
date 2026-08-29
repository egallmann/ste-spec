<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 2
hash_algorithm: sha256
source_hash: 2317a4e14ef42d61f4582fc90c10f5234dba0ac92d59fbe7163f31a8688bb5ac
rendered_hash: 00a24fa061b479635a187d07aad4312edd075e948f867fafb69c85cfe80c81b0
-->

# ADR-L-0036: Repository README Contract

**Status:** accepted  
**Created:** 2025-12-19  
**Modified:** 2026-03-29  
**Authors:** Erik Gallmann, ste-spec  
**Domains:** governance, documentation  
**Tags:** readme, boundaries  
**Alias name:** repository-readme-contract  

## Context

Every STE repository `README.md` MUST serve as a human-readable architectural boundary
and responsibility description. README is an orientation entry point, subordinate to ADRs,
contracts, invariants, and Architecture IR doctrine.

Legacy: `adrs/published/ADR-036-repository-readme-contract.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — kernel governance ADRs do
not define README structure; this ADR governs **repository human entrypoints** only.


## Relationship graph

```mermaid
flowchart LR
  n_01a04e96_1f5c_714a_aa37_80e9b4523045["INV-3601"]
  n_01a04e96_1f5c_7383_a21d_670b4848a89c["DEC-3601"]
  n_01a04e96_1f5c_78e0_823f_3c915d07acd6["ADR-L-0040"]
  n_01a04e96_1f5c_798e_953b_59dbf5d8cfec["ADR-L-0037"]
  n_01a04e96_1f5c_7bf8_893f_f5279ec1ec75["ADR-L-0038"]
  n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2["ADR-L-0036"]
  n_01a04e96_1f5c_714a_aa37_80e9b4523045 -->|"declared_in"| n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2
  n_01a04e96_1f5c_7383_a21d_670b4848a89c -->|"declared_in"| n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2
  n_01a04e96_1f5c_798e_953b_59dbf5d8cfec -->|"references"| n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2
  n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2 -->|"references"| n_01a04e96_1f5c_78e0_823f_3c915d07acd6
  n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2 -->|"references"| n_01a04e96_1f5c_798e_953b_59dbf5d8cfec
  n_01a04e96_1f5c_7fa8_a63c_a55b509dbca2 -->|"references"| n_01a04e96_1f5c_7bf8_893f_f5279ec1ec75
```

## Related ADRs

### ADR-L-0037 — Repository README Conformance and Reference Implementation

**Relationships:**
- 01a04e96-1f5c-798e-953b-59dbf5d8cfec -[:references]-> this ADR
- this ADR -[:references]-> 01a04e96-1f5c-798e-953b-59dbf5d8cfec

**Context:** Every STE repository MUST provide a README conforming to ADR-L-0036. README is an
Orientation artifact per ADR-L-0038: non-authoritative, should be versioned, cannot
introduce doctrine, and must cite normative sources for authority claims.

[Open projection](ADR-L-0037-repository-readme-conformance-and-reference-implementation.md)
### ADR-L-0038 — Artifact Taxonomy and Versioning Posture

**Relationships:**
- this ADR -[:references]-> 01a04e96-1f5c-7bf8-893f-f5279ec1ec75

**Context:** STE assigns each artifact a taxonomy **kind** per the ste-spec architecture document that
defines artifact taxonomy and versioning posture (under `architecture/`).
Version-control posture follows that kind, not repository or team preference.
This ADR is canonical for taxonomy and versioning posture; ADR-L-0040 maps kinds into
Spine stages without redefining the taxonomy.

[Open projection](ADR-L-0038-artifact-taxonomy-and-versioning-posture.md)
### ADR-L-0040 — STE Spine Lifecycle and Authority

**Relationships:**
- this ADR -[:references]-> 01a04e96-1f5c-78e0-823f-3c915d07acd6

**Context:** Defines the canonical **Spine** lifecycle stages, system states, authority categories, and
precedence rules tying together ste-spec doctrine, implementation repos, publication,
Architecture IR compilation, kernel admission, runtime evidence, assessment, and
governance. Does not redefine ADR-L-0038 taxonomy, ADR-L-0035 ontology, ADR-L-0031
boundary, or ADR-L-0030 contract authority.

[Open projection](ADR-L-0040-ste-spine-lifecycle-and-authority.md)





## Invariants

### INV-3601

**Statement:** When README content conflicts with a normative ADR, invariant, schema, contract, or
Architecture IR doctrine, the normative artifact MUST govern and README MUST be corrected.
  
**Scope:** global  
**Enforcement:** must (policy)  
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

**Impact:** low  
**Blocking:** No






---

*Generated from ADR-L-0036 by ADR Architecture Kit*