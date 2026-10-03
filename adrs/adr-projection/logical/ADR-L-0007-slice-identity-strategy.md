<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 5c17686380fd8c0025b66bcbe6fe4ac491d3d08e31f7c946cc04952150e45bc5
rendered_hash: ee4fa9427a0798952983b4fa1fa1f767096c657d4570a94a1858944e7ad141fd
-->

# ADR-L-0007: Slice Identity Strategy

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** extraction, documentation-state, recon<br>
**Tags:** identity, determinism, slices<br>
**Alias name:** slice-identity-strategy<br>

## Context

Slices require unique, stable, deterministic identifiers derived from **observable**
semantic anchors (contracts, paths, source paths, table names) rather than volatile
implementation labels alone.

Legacy human projection: `adrs/published/ADR-007-slice-identity-strategy.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — this ADR defines **Fabric
slice identity** for extraction and documentation-state; **Architecture IR** and
contract layers may define additional canonical identity rules. On conflict, IR
contract precedence for **IR element identity** is resolved in contract ADRs (e.g.
future migrated ADR-035); slice identity rules here remain authoritative for **extractor
output identity** unless explicitly superseded.








## Invariants

### INV-0701

**Statement:** Given the same source artifact inputs and extractor version, identity derivation for
a slice MUST be deterministic and reproducible.
<br>
**Scope:** global<br>
**Enforcement:** must (test)<br>
**Verification:** automated

**Rationale:**
Required for regression testing, environment diffs, and ADR-L-0001 determinism.




### INV-0702

**Statement:** Identity derivation MUST prefer observable contract anchors (routes, table names,
source paths, integration targets, config keys) over volatile implementation labels
when those anchors are available.
<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Reduces spurious identity churn on refactors that do not change consumer-visible contracts.






## Decisions

### DEC-0701: Derive slice identity per domain using observable semantic anchors

**Rationale:**
API endpoints use method plus normalized path; data entities prefer declared table or
schema-qualified names; graph elements use stable source paths; integration clients use service
or base identity; configuration uses stable keys. Identities are normalized
(lowercase, hyphenation) with explicit collision handling. This prioritizes **semantic
stability** over renames of functions or type names when observable anchors are
unchanged.


**Alternatives Considered:**

- **Content hash identity**: Unstable across refactors; not human-readable; breaks meaningful diffs.

- **User-annotated ids only**: Adoption friction and inconsistency; still needs fallback derivation.

- **Function or type name as sole identity**: Spurious churn on refactor; weak for multi-endpoint handlers.

- **UUID with persistent map**: Non-deterministic across environments without shared state.


**Consequences:**

**Positive:**
- Deterministic, debuggable identities aligned to consumer contracts

**Negative:**
- Extractor-specific domain logic and edge-case judgment


### DEC-0702: Define normalization and collision handling for derived identities

**Rationale:**
Normalize case and punctuation; avoid duplicate hyphens; disambiguate rare collisions
with explicit suffixes and warnings for manual review.



**Consequences:**

**Positive:**
- Predictable string forms across extractors

**Negative:**
- Requires consistent implementation and tests



## Gaps

### GAP-0701: Formal IR mapping when slice identity rules and IR ontology diverge

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0007 by ADR Architecture Kit*