<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: d99c20a4f8510a03c571bc89ca311cb6d887341d220b6c0d2d2d91a3ed37bae6
rendered_hash: b9d472f9e1809b9b0f760da36d9f384953b53d46f4de885af723c18e39e3f130
-->

# ADR-L-0022: Fail-Closed Semantics and Enforcement Scope

**Status:** accepted<br>
**Created:** 2025-12-23<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** gateway, enforcement<br>
**Tags:** fail-closed, enforcement<br>
**Alias name:** fail-closed-semantics-and-enforcement-scope<br>

## Context

Authoritative execution eligibility and canonical promotion require complete, successful
validation. Fail-closed halts authoritative actions when prerequisites cannot be verified;
it does not require total system unavailability. Non-authoritative inspection may continue
under explicit degraded labeling.

Legacy: `adrs/published/ADR-022-fail-closed-enforcement-scope.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1009** defines the
kernel decision contract; this ADR defines STE-system-wide fail-closed triggers and
non-bypass rules at the Gateway / promotion boundary.








## Invariants

### INV-2201

**Statement:** If any prerequisite for execution eligibility or canonical promotion cannot be fully
validated, the implementation MUST deny the authoritative action (fail closed).
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Matches eligibility and promotion algorithms that treat indeterminacy as denial.




### INV-2202

**Statement:** Read-only evaluation paths used while fail-closed is active MUST NOT approve execution
eligibility or canonical promotion and MUST surface degraded, non-authoritative status.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Prevents inspection modes from becoming shadow approval channels.






## Decisions

### DEC-2201: Apply fail-closed to execution eligibility and canonical promotion when validation is incomplete, failed, or indeterminate

**Rationale:**
Partial or best-effort validation would undermine determinism and authority scarcity;
authoritative actions require full verification.



**Consequences:**

**Positive:**
- Unambiguous correctness boundary

**Negative:**
- Stricter availability coupling for authoritative paths


### DEC-2202: Prohibit bypass of fail-closed via operator override, emergency modes, environment-specific relaxation, or best-effort execution

**Rationale:**
Any bypass introduces implicit trust and non-deterministic enforcement.



**Consequences:**

**Positive:**
- No hidden weakening of guarantees

**Negative:**
- No discretionary override at the enforcement boundary


### DEC-2203: Allow read-only inspection under fail-closed only when outputs are explicitly non-authoritative and audit-logged

**Rationale:**
Operators need diagnostics without granting execution or promotion.



**Consequences:**

**Positive:**
- Debuggability without correctness compromise

**Negative:**
- Requires clear degraded signaling in implementations



## Gaps

### GAP-2201: Operational SLAs and retry semantics remain out of band for this ADR-L

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0022 by ADR Architecture Kit*