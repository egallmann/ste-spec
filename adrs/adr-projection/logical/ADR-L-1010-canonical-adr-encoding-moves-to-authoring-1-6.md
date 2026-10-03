<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: bb85f23fa3efe53963a8eab82297af3afc73442baf6637c5c403b43a1abf6ad5
rendered_hash: e76ed43574be9b8808eeedc52acab116f5b5d5d7792eabeb7240cae72f16b813
-->

# ADR-L-1010: Canonical ADR Encoding Moves to Authoring 1.6

**Status:** accepted<br>
**Created:** 2026-10-03<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance<br>
**Tags:** encoding, authoring-1-6<br>
**Alias name:** canonical-adr-encoding-moves-to-authoring-1-6<br>

## Context

This proposed ADR records the encoding change for ste-spec canonical ADR
sources. It does not change the schema_version of any existing ADR. This ADR
does not alter existing semantic doctrine or the authority of existing
semantic content.

The decisions below state only the locked encoding move: authoring 1.3 to
authoring 1.6, preservation of existing identities and structured semantic
content, with the only canonical-source transformation being the
schema_version change from 1.3 to 1.6, absence of normative_propositions,
exclusion of authoring 1.7 and ACC construction, and unchanged ADR-L-0044
semantic authority.










## Decisions

### DEC-6983: Move ste-spec canonical ADR encoding from authoring 1.3 to authoring 1.6

**Rationale:**
ste-spec canonical ADR encoding moves from authoring 1.3 to authoring 1.6.




### DEC-6984: Preserve canonical identities and structured semantic content except for the schema_version change

**Rationale:**
The migration changes only schema_version from 1.3 to 1.6. No other canonical source field or semantic content is changed unless separately reviewed and authorized.




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