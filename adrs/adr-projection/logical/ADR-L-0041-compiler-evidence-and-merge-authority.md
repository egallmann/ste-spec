<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 89f40fb872aac2765aea35705e49d2d5625294f17fe87d8a04cc60b8aae783d5
rendered_hash: 18cf69a3b0dff3e30db003a4f3505bd3aa92305f4fd938d0fab97ac56d451a62
-->

# ADR-L-0041: Compiler, Evidence, and Merge Authority

**Status:** accepted<br>
**Created:** 2025-12-19<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** compilation, governance<br>
**Tags:** compiler, evidence, kernel<br>
**Alias name:** compiler-evidence-and-merge-authority<br>

## Context

Non-overlapping compiler roles: **adr-architecture-kit** is the authoring compiler for
ADR registries/manifest/rendered views (not a second compiler-of-record for
`ArchitectureEvidence` or normative `Compiled_IR_Document`). **ste-runtime** is runtime
evidence compiler of record. **ste-kernel** merges publication fragments, validates IR,
and emits `KernelAdmissionAssessment` while consuming ste-spec contracts.

Legacy: `adrs/published/ADR-041-compiler-and-merge-authority.md`.

**Reconciliation vs ADR-L-1004:** **coexist-with-precedence** — freshness semantics govern
evidence timing; this ADR assigns **who may compile** named artifact families.

**Reconciliation vs ADR-L-1005:** **coexist-with-precedence** — drift detection consumes
compiled views; compiler-of-record boundaries prevent ambiguous duplicate compile stacks.

**Runtime compiler of record:** **ste-runtime** `COMPILER-AUTHORITY.md` — use
`ste architecture compile --project-root <repo-root>` (see **MIGRATION-INVENTORY.md** Phase 5
for a recorded example command and artifact paths).








## Invariants

### INV-4101

**Statement:** Repositories MUST NOT maintain a second authoritative compile path that redefines ste-spec
contract shapes for `ArchitectureEvidence` or normative Architecture IR schema without an
explicit superseding ADR-L.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves single normative shape targets for fail-closed enforcement.






## Decisions

### DEC-4101: Assign authoring-time ADR compilation to adr-architecture-kit without claiming runtime ArchitectureEvidence or normative Compiled_IR_Document compiler-of-record roles

**Rationale:**
Prevents parallel truth compilers for the same interchange contracts.



**Consequences:**

**Positive:**
- Clear golden parity versus production compile paths

**Negative:**
- Contributors must use the right tool per task


### DEC-4102: Assign ArchitectureEvidence compilation to ste-runtime; assign IR merge, validation, and admission assessment emission to ste-kernel

**Rationale:**
Keeps evidence factual and kernel decision-bearing per ADR-L-0031.



**Consequences:**

**Positive:**
- Aligns repos with Spine enforcement story

**Negative:**
- Documentation must stay synchronized across three repos



## Gaps

### GAP-4101: Keep ste-runtime CLI install docs aligned when global `ste` npm shim diverges from workspace builds

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0041 by ADR Architecture Kit*