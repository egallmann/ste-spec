<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 3e2157ebfe794f71b227711df7c3941775fff47f573355a001cd80420cdcd17d
rendered_hash: 0844b4af32f75addad99c1d6d49cf423fe0b0e1fa6471f38c45a76e05eb35288
-->

# ADR-L-1008: Decision Outcome Model

**Status:** proposed<br>
**Created:** 2026-03-28<br>
**Authors:** ste-spec<br>
**Domains:** governance, kernel<br>
**Tags:** outcomes, allow, deny<br>
**Alias name:** decision-outcome-model<br>

## Context

Caller-facing admission emits a small set of canonical outcomes. Each outcome carries
meaning for whether the **requested action** may execute, what remediation is required,
and how warnings differ from hard gates.

This model aligns with ADR-031: only ste-kernel emits caller-facing admission
semantics; ste-runtime remains evidence-only.








## Invariants

### INV-5071

**Statement:** DENY MUST prohibit execution of the requested_action; ALLOW MUST explicitly clear the
action subject to downstream enforcement surfaces; CONDITIONAL MUST require documented
preconditions before execution; WARNING MUST surface non-blocking findings without
implying allow unless paired with ALLOW or CONDITIONAL clearance.
<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** automated

**Rationale:**
Clients must interpret outcomes consistently for the same requested_action semantics.






## Decisions

### DEC-6871: Define ALLOW, DENY, CONDITIONAL, WARNING semantics for requested_action

**Rationale:**
Shared vocabulary prevents incompatible client interpretations.





### DEC-6872: Bind execution permission to outcome and action class jointly

**Rationale:**
Some informational actions never imply execution permission changes.







---

*Generated from ADR-L-1008 by ADR Architecture Kit*