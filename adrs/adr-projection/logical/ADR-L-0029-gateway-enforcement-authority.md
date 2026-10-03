<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 6c5adbdfd5927dca6c5e951de833de1e500ada40fdfab0f8e3c13a9b8a3ccca7
rendered_hash: 90c5748bddfb35420f9ee57e1fcc1de086199900fc68c0fd9fb9abbbd320c2ee
-->

# ADR-L-0029: Gateway Enforcement Authority

**Status:** accepted<br>
**Created:** 2025-12-30<br>
**Modified:** 2026-03-29<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** gateway, governance<br>
**Tags:** enforcement, authority<br>
**Alias name:** gateway-enforcement-authority<br>

## Context

Gateway holds Enforcement Authority: verify ORG-signed material, consult trust registry,
evaluate eligibility prerequisites, emit ephemeral unsigned decisions. It is distinct
from ORG attestation authority which signs durable canonical artifacts.

Legacy: `adrs/published/ADR-029-gateway-enforcement-authority.md`.

**Reconciliation vs ADR-L-0019:** **merge** — ADR-L-0019 states ORG-scoped enforcement
without ORG attestation; this ADR names the **Enforcement Authority** kind explicitly for
trust-registry and specification alignment.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — kernel admission models
remain documentation-state focused; this ADR names the **production Gateway** authority
slice for STE eligibility.








## Invariants

### INV-2901

**Statement:** Gateway MUST NOT be modeled as holding ORG attestation authority to sign canonical
artifacts or Fabric Attestations; its authority is limited to verification and
enforcement per ADR-L-0019 and ADR-L-0028.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** audit

**Rationale:**
Preserves authority scarcity for canonical publishers.






## Decisions

### DEC-2901: Define Enforcement Authority as Gateway-specific verification and eligibility enforcement without canonical publishing or trust-registry mutation

**Rationale:**
Removes contradiction between ORG signing requirements and Gateway verifier role.



**Consequences:**

**Positive:**
- Clear trust-registry schema direction

**Negative:**
- Implementations must not label Gateway keys as ORG signing keys


### DEC-2902: Keep eligibility outcomes ephemeral and unsigned while retaining audit logs tied to signed inputs

**Rationale:**
Avoids false equivalence between point-in-time enforcement and durable canonical truth.



**Consequences:**

**Positive:**
- Smaller long-lived signing surface

**Negative:**
- Consumers cannot treat decisions as standalone attestations



## Gaps

### GAP-2901: Align specification section references (e.g. §6.1.5) with handbook and ISO-42010 views

**Impact:** low<br>
**Blocking:** No






---

*Generated from ADR-L-0029 by ADR Architecture Kit*