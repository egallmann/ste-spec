<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: ca96c564001c9ac497f61206c07bf7f830f8f3512da896aad4faad0cc6520cf8
rendered_hash: 52b57da53d5aedf6e43229e34c7c7736a2421f86afec8bcbc47e5144a9ded443
-->

# ADR-L-0040: STE Spine Lifecycle and Authority

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, spine<br>
**Tags:** lifecycle, authority<br>
**Alias name:** ste-spine-lifecycle-and-authority<br>

## Context

Defines the canonical **Spine** lifecycle stages, system states, authority categories, and
precedence rules tying together ste-spec doctrine, implementation repos, publication,
Architecture IR compilation, kernel admission, runtime evidence, assessment, and
governance. Does not redefine ADR-L-0038 taxonomy, ADR-L-0035 ontology, ADR-L-0031
boundary, or ADR-L-0030 contract authority.

Legacy: `adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`.

**Reconciliation vs ADR-L-1001–1009:** **coexist-with-precedence** — the 100x series
formalizes kernel documentation contracts (actions, admission, posture, freshness, drift,
evidence, Golden, outcomes, decision contract). ADR-L-0040 is the **end-to-end Spine**
model that **uses** those contracts without merging their text.








## Invariants

### INV-4001

**Statement:** Supporting Spine documents in `architecture/` MUST explain or map ADR-L-0040 without
redefining Spine stages, authority ownership, or ADR-L-0038 taxonomy kinds.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Keeps supporting doctrine subordinate.






## Decisions

### DEC-4001: Define eleven canonical Spine lifecycle stages from Intent Definition through Intent Update and Remediation

**Rationale:**
Provides one explicit end-to-end vocabulary referenced across ste-spec and consumers.



**Consequences:**

**Positive:**
- Shared stage language

**Negative:**
- Narrower local lifecycles remain valid in their scopes


### DEC-4002: Document authority categories (normative, implementation truth, proof, derived, evidence, reports, admission, governance) without transferring ownership via state alone

**Rationale:**
Separates who governs truth from readiness states.



**Consequences:**

**Positive:**
- Clear enforcement and observation loci

**Negative:**
- Requires careful mapping in supporting doctrine


### DEC-4003: Establish precedence on apparent conflicts — ADR-L-0040 controls Spine lifecycle and authority transitions; ADR-L-0038 controls taxonomy and VCS posture; supporting `architecture/` doctrine is subordinate; analysis-only material is non-normative

**Rationale:**
Prevents accidental override via explanatory documents.



**Consequences:**

**Positive:**
- Deterministic interpretation order

**Negative:**
- Supporting docs must avoid contradictory claims



## Gaps

### GAP-4001: Visual projections (e.g. STE-Spine-Lifecycle.md) remain subordinate; regenerate when stages change

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0040 by ADR Architecture Kit*