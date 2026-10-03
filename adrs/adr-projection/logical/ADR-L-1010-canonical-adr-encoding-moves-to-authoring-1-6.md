<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: b2cc2419b141ff59f824fe75f5be399b5289a9dd16f7adfe8ce2587c78b8cfd7
rendered_hash: 6c57dd8cfab6c5c70b38e3f7576a6655200d9de888e7c18a6b4be2629b7de20d
-->

# ADR-L-1010: Canonical ADR Encoding Moves to Authoring 1.6

**Status:** proposed<br>
**Created:** 2026-10-03<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance<br>
**Tags:** encoding, authoring-1-6<br>
**Alias name:** canonical-adr-encoding-moves-to-authoring-1-6<br>

## Context

This proposed ADR records the encoding change for ste-spec canonical ADR
sources. It does not change the schema_version of any existing ADR, and it
does not add semantic authority.

The decisions below state only the locked encoding move: authoring 1.3 to
authoring 1.6, preservation of existing identities and structured semantic
content aside from that carrier and schema change, absence of
normative_propositions, exclusion of authoring 1.7 and ACC construction, and
unchanged ADR-L-0044 semantic authority.










## Decisions

### DEC-6983: Move ste-spec canonical ADR encoding from authoring 1.3 to authoring 1.6

**Rationale:**
ste-spec canonical ADR encoding moves from authoring 1.3 to authoring 1.6.




### DEC-6984: Preserve existing canonical identities and structured semantic content except for the approved carrier and schema change

**Rationale:**
Existing canonical identities and structured semantic content are preserved except for the approved carrier and schema change.




### DEC-6985: Leave normative_propositions absent and extract no propositions

**Rationale:**
The normative_propositions key remains absent. No proposition extraction occurs.




### DEC-6986: Do not adopt authoring 1.7 or ACC construction

**Rationale:**
Authoring 1.7 and ACC construction are not adopted by this migration.




### DEC-6987: Leave ADR-L-0044 semantic authority unchanged

**Rationale:**
ADR-L-0044 semantic authority remains unchanged.






---

*Generated from ADR-L-1010 by ADR Architecture Kit*