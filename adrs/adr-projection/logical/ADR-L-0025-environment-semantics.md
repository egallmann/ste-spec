<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 1e2107af4c240106f14a86c46d26198f07a2aaca5d12579f3529743f7e2868f2
rendered_hash: 8ad34be6ee3347decac5c0a429cc6cf22b3c85672e966ba6f421352b99ada357
-->

# ADR-L-0025: Environment Semantics

**Status:** accepted<br>
**Created:** 2025-12-29<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** gateway, fabric<br>
**Tags:** environment, canonical-state<br>
**Alias name:** environment-semantics<br>

## Context

Environment is a mandatory, opaque identifier partitioning canonical state and
attestations. Fabric governance defines allowed values; Gateway enforces exact
case-sensitive equality between Context Bundle and Fabric Attestation; no inference,
defaults, aliases, or hierarchy in v1.

Legacy: `adrs/published/ADR-025-environment-semantics.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — environment is a
**STE-system canonical dimension** for eligibility; kernel documentation-state
environments (if any) are orthogonal unless explicitly bridged in a future ADR-L.








## Invariants

### INV-2501

**Statement:** Gateway MUST NOT infer, default, case-fold, pattern-match, or hierarchically interpret
environment identifiers for v1 eligibility; only exact equality on declared identifiers
is permitted.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves determinism claims for eligibility evaluation.






## Decisions

### DEC-2501: Treat environment as a primary canonical dimension with mandatory explicit identifiers in Fabric Attestations and Context Bundles

**Rationale:**
Prevents ambiguous canonical boundaries and cross-environment authorization mistakes.



**Consequences:**

**Positive:**
- Deterministic partition of canonical state

**Negative:**
- No silent defaults for environment


### DEC-2502: Enforce environment equality with exact case-sensitive string match at Gateway; deny on mismatch

**Rationale:**
Exact matching is falsifiable and implementation-neutral for v1.



**Consequences:**

**Positive:**
- Predictable interoperability

**Negative:**
- Naming discipline required across teams


### DEC-2503: Bind environment into signed Fabric Attestation content; prohibit inference from infrastructure or git metadata

**Rationale:**
Stops substitution and hidden derivation of scope.



**Consequences:**

**Positive:**
- Cryptographic binding of scope claims

**Negative:**
- Explicit configuration burden on callers



## Gaps

### GAP-2501: Future ADR-L for hierarchical environments, wildcards, or aliases if needed

**Impact:** <br>
**Blocking:** No






---

*Generated from ADR-L-0025 by ADR Architecture Kit*