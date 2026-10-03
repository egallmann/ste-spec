<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: e118f12fb56c6040fbc0c4b332c1b1f54e2ad1b405684facdb685f529b8ff8e2
rendered_hash: 1e8d00dce6676db86fb446aa19c92e0423910772b79b079b93b1e38f46152ef5
-->

# ADR-L-0043: Context Domain and MVC Lifecycle Boundary

**Status:** proposed<br>
**Created:** 2026-05-30<br>
**Modified:** 2026-05-30<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** architecture-ir, contracts, context, mvc<br>
**Tags:** context-domain, graph-domain, linkage-surface, mvc, rss<br>
**Alias name:** context-domain-and-mvc-lifecycle-boundary<br>

## Context

STE is introducing an experimental model for task-scoped architectural context.
The model treats MVC as a task-scoped architectural reality bundle rather than
generic context reduction. RSS assembles the candidate architectural reality
surface from declared intent, Context Domains, Graph Domains, Linkage Surfaces,
Architecture IR snapshots, task context, and persona context-selection policy.

This ADR does not promote Context Domains into Architecture IR entity kinds and
does not authorize production MVC assembly. It records the boundary needed for
draft contract work under `contracts/graph-domain/`, `contracts/linkage-surface/`,
`contracts/context-domain/`, `contracts/persona/`, and `contracts/mvc/`.

Architecture IR remains the ste-spec-owned semantic authority per ADR-L-0035.
Contract authority remains in ste-spec per ADR-L-0030. Runtime/kernel split and
admission authority remain governed by ADR-L-0031, ADR-L-0041, INV-0001, and
INV-0002.








## Invariants

### INV-4301

**Statement:** Context Domain Definitions MUST NOT contain materialized selected entities,
relationships, evidence, constraints, or admission outcomes.
<br>
**Scope:** ste-spec<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Preserves the definition-versus-bundle boundary.




### INV-4302

**Statement:** Graph Domains and Linkage Surfaces MUST remain derived traversal and discovery
surfaces unless a relationship is independently established by an authoritative
artifact.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Prevents graph-authority drift.




### INV-4303

**Statement:** MVC-S MUST preserve stable source refs, selector version refs, topology metrics,
inclusion rationale, exclusion rationale, and negative space sufficient to
reproduce its fingerprint from the same declared inputs.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
RSS adaptive depth depends on MVC-S topology, so MVC-S identity must be reproducible.




### INV-4304

**Statement:** Deduplication MUST NOT collapse inclusion or exclusion rationale. All selector
paths and reasons that selected or excluded an item MUST remain available in
the materialized result.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Rationale preservation is required for composite persona sets, task overlays, and
CEM ablation.




### INV-4305

**Statement:** Runtime MAY emit factual candidate bundles, Graph Domains, Linkage Surfaces,
diagnostics, provenance, freshness, integrity, and MVC-S candidates, but MUST
NOT emit caller-facing admission decisions.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves the runtime/kernel admission boundary.






## Decisions

### DEC-4301: Define Context Domain Definitions as semantic view definitions and Context Domain Bundles as materialized instances

**Rationale:**
Keeping definitions declarative prevents ontology drift and prevents materialized
derived surfaces from being mistaken for authority.



**Consequences:**

**Positive:**
- Context Domain schemas can distinguish reusable selection intent from task-scoped materialization.
- CEM ablation can operate over materialized bundles without mutating domain definitions.

**Negative:**
- Consumers must handle an additional definition-versus-instance boundary.


### DEC-4302: Define Graph Domain Definitions and Linkage Surfaces as derived traversal inputs, not authority sources

**Rationale:**
Graph Domains and Linkage Surfaces improve structural discovery, but the authority
of any relationship still comes from ADRs, invariants, contracts, requirements,
embodiment records, or other accepted authoritative artifacts.



**Consequences:**

**Positive:**
- MVC assembly can become more structure-guided without moving authority into runtime graphs.
- Multiple linkage generation mechanisms can feed the same consumer contracts.

**Negative:**
- Linkage records require explicit provenance, integrity, freshness, and validation fields.


### DEC-4303: Split MVC into MVC-D, MVC-S, and MVC-M lifecycle contracts

**Rationale:**
The split separates declarative admissible context definition, candidate surface
assembly, and kernel-admitted materialization. This preserves reproducibility and
prevents runtime candidate generation from becoming caller-facing admission.



**Consequences:**

**Positive:**
- MVC-S can carry stable identity, topology metrics, source refs, selector refs, and rationale.
- Kernel admission can produce MVC-M without granting runtime admission authority.

**Negative:**
- Implementations must preserve rationale and identity across lifecycle transitions.


### DEC-4304: Treat Persona as Context Selection Policy rather than biography or projection-only policy

**Rationale:**
Personas select required and optional Context Domains, traversal objectives, projection
preferences, and rationale. Projection is only one dimension of persona behavior.



**Consequences:**

**Positive:**
- Composite persona MVCs can union and deduplicate requirements while preserving selector rationale.

**Negative:**
- Persona schemas must reject unconstrained narrative role descriptions as operational policy.



## Gaps

### GAP-4301: Promote or amend this ADR after draft schemas and fixtures demonstrate deterministic MVC-S construction and rationale-preserving deduplication

**Impact:** medium<br>
**Blocking:** No





### GAP-4302: Decide whether Context Domain and Graph Domain terms remain external contracts or later become Architecture IR semantic ontology extensions

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0043 by ADR Architecture Kit*