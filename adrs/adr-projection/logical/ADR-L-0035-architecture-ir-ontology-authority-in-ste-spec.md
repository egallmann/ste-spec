<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 2d5c52561e8d7f8d34323962d499289e270371852886fe907f0472477f910c51
rendered_hash: d04d9e4ad5642349528df6be8a620e84c13df033a6a0af3b536fd22731ba0aef
-->

# ADR-L-0035: Architecture IR Ontology Authority in ste-spec

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-09-02<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** architecture-ir, contracts<br>
**Tags:** ontology, semantics<br>
**Alias name:** architecture-ir-ontology-authority-in-ste-spec<br>

## Context

`architecture/STE-Architecture-Intermediate-Representation.md` is the canonical **semantic**
specification of Architecture IR. Mechanical JSON Schema and compiled enumerations publish
under `contracts/architecture-ir/` per the contract pin. ste-kernel consumes the bundle;
it does not own normative mechanical definitions. Compiler roles are further constrained
by ADR-L-0041.

Legacy: `adrs/published/ADR-035-architecture-ir-ontology-authority.md`.

**Reconciliation vs ADR-L-1006:** **coexist-with-precedence** — evidence authority governs
evidentiary artifacts; this ADR governs **Architecture IR meaning** versus mechanical enums.
**Reconciliation vs ADR-L-0044:** **coexist-with-precedence** — ADR-L-0044 establishes cross-cutting governed-reasoning and normative semantic meaning; this ADR remains the authority for semantic Architecture IR ontology and mechanical realization boundaries. No CE-01 identity or compiled IR identity change is implied.








## Invariants

### INV-3501

**Statement:** Extensions to mechanical Architecture IR enumerations MUST be ste-spec contract changes
with pin discipline; semantic additions MAY land in ste-spec prose first with explicit
realization notes.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves ADR-L-0035 as ontology and mechanical authority anchor.






## Decisions

### DEC-3501: Keep semantic Architecture IR authority in ste-spec prose; keep mechanical schemas and pins in ste-spec contracts

**Rationale:**
Prevents conflating JSON `kind` enums with the full ontology and avoids duplicate schema authority in kernel repos.



**Consequences:**

**Positive:**
- Single cross-repo vocabulary reference

**Negative:**
- Requires disciplined ir_version and schema_id updates



## Gaps

### GAP-3501: Registry surfaces and adapter projections should cite both prose ontology and mechanical pin

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0035 by ADR Architecture Kit*