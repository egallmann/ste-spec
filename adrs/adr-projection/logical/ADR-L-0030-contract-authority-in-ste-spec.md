<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 2
hash_algorithm: sha256
source_hash: 848818a89cafae057e4ff7ddc81cfcec0809d8dfd79c6a40f0453ff42e41e415
rendered_hash: b58ca38a7f7fc0cb2ff9bfc88ac6c0783fb94af3a22cd6788dea44ebc49dcdf5
-->

# ADR-L-0030: Contract Authority in ste-spec

**Status:** accepted  
**Created:** 2025-12-19  
**Modified:** 2026-03-29  
**Authors:** Erik Gallmann, ste-spec  
**Domains:** contracts, governance  
**Tags:** contracts, ste-spec  
**Alias name:** contract-authority-in-ste-spec  

## Context

Cross-repository handoff contracts are governed in **ste-spec**: shape in `contracts/`,
rules in `invariants/`, rationale in ADRs. Runtime and kernel repos remain subordinate
implementation surfaces.

Legacy: `adrs/published/ADR-030-contract-authority-in-ste-spec.md`.

**Reconciliation vs ADR-L-100x:** **coexist-with-precedence** — **ADR-L-1002** defines
admission semantics at the kernel documentation layer; this ADR asserts **ste-spec
ownership of interchange contracts** that admission consumes.


## Relationship graph

```mermaid
flowchart LR
  n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6["ADR-L-0030"]
  n_01a04e96_1f5b_76a7_9f3e_74a771a33e46["ADR-L-0034"]
  n_01a04e96_1f5b_7c56_bc3f_75fbbc94d42b["ADR-L-0031"]
  n_01a04e96_1f5b_7c87_8a1f_093dbd20805a["INV-3001"]
  n_01a04e96_1f5b_7ded_b337_01c79d48c692["DEC-3001"]
  n_01a04e96_1f5c_7116_883f_0badde97c759["ADR-L-0042"]
  n_01a04e96_1f5c_72a7_8a1b_81cf44933af3["ADR-L-0043"]
  n_01a04e96_1f5c_73c9_ad1f_df05ef43cae1["ADR-L-1002"]
  n_01a04e96_1f5c_78e0_823f_3c915d07acd6["ADR-L-0040"]
  n_01a04e96_1f5c_7e5b_9837_1dea58886565["ADR-L-0041"]
  n_01a04e96_1f5c_7fd4_bf3e_ddca6103eae1["ADR-L-0035"]
  n_01a06490_5b3c_76c0_9da2_abc5d28f8970["ADR-L-0044"]
  n_01a04e96_1f5b_7c87_8a1f_093dbd20805a -->|"declared_in"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5b_7ded_b337_01c79d48c692 -->|"declared_in"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6 -->|"references"| n_01a04e96_1f5b_7c56_bc3f_75fbbc94d42b
  n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6 -->|"references"| n_01a04e96_1f5c_73c9_ad1f_df05ef43cae1
  n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6 -->|"references"| n_01a04e96_1f5c_78e0_823f_3c915d07acd6
  n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6 -->|"references"| n_01a04e96_1f5c_7e5b_9837_1dea58886565
  n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6 -->|"references"| n_01a04e96_1f5c_7fd4_bf3e_ddca6103eae1
  n_01a04e96_1f5b_76a7_9f3e_74a771a33e46 -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5b_7c56_bc3f_75fbbc94d42b -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5c_7116_883f_0badde97c759 -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5c_72a7_8a1b_81cf44933af3 -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5c_78e0_823f_3c915d07acd6 -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a04e96_1f5c_7e5b_9837_1dea58886565 -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
  n_01a06490_5b3c_76c0_9da2_abc5d28f8970 -->|"references"| n_01a04e96_1f5b_752a_bb27_9bfbb872ffc6
```

## Related ADRs

### ADR-L-0031 — Runtime and Kernel Responsibility Boundary

**Relationships:**
- 01a04e96-1f5b-7c56-bc3f-75fbbc94d42b -[:references]-> this ADR
- this ADR -[:references]-> 01a04e96-1f5b-7c56-bc3f-75fbbc94d42b

**Context:** **ste-runtime** produces factual evidence only. **ste-kernel** is the caller-facing
admission authority at the evaluated System Instance boundary (explicit environment and
evaluation scope).

[Open projection](ADR-L-0031-runtime-and-kernel-responsibility-boundary.md)
### ADR-L-0034 — Rule Projection Envelope Authority

**Relationships:**
- 01a04e96-1f5b-76a7-9f3e-74a771a33e46 -[:references]-> this ADR

**Context:** ste-spec will own the interchange envelope for ADR-bound rule projections and related
attestations under `contracts/rule-projection/` when promoted from draft. Semantic rules
live in `invariants/` (e.g. INV-0010). ste-kernel must not be treated as authoritative
signer or compiler of rule text for these envelopes.

[Open projection](ADR-L-0034-rule-projection-envelope-authority.md)
### ADR-L-0035 — Architecture IR Ontology Authority in ste-spec

**Relationships:**
- this ADR -[:references]-> 01a04e96-1f5c-7fd4-bf3e-ddca6103eae1

**Context:** `architecture/STE-Architecture-Intermediate-Representation.md` is the canonical **semantic**
specification of Architecture IR. Mechanical JSON Schema and compiled enumerations publish
under `contracts/architecture-ir/` per the contract pin. ste-kernel consumes the bundle;
it does not own normative mechanical definitions. Compiler roles are further constrained
by ADR-L-0041.

[Open projection](ADR-L-0035-architecture-ir-ontology-authority-in-ste-spec.md)
### ADR-L-0040 — STE Spine Lifecycle and Authority

**Relationships:**
- 01a04e96-1f5c-78e0-823f-3c915d07acd6 -[:references]-> this ADR
- this ADR -[:references]-> 01a04e96-1f5c-78e0-823f-3c915d07acd6

**Context:** Defines the canonical **Spine** lifecycle stages, system states, authority categories, and
precedence rules tying together ste-spec doctrine, implementation repos, publication,
Architecture IR compilation, kernel admission, runtime evidence, assessment, and
governance. Does not redefine ADR-L-0038 taxonomy, ADR-L-0035 ontology, ADR-L-0031
boundary, or ADR-L-0030 contract authority.

[Open projection](ADR-L-0040-ste-spine-lifecycle-and-authority.md)
### ADR-L-0041 — Compiler, Evidence, and Merge Authority

**Relationships:**
- 01a04e96-1f5c-7e5b-9837-1dea58886565 -[:references]-> this ADR
- this ADR -[:references]-> 01a04e96-1f5c-7e5b-9837-1dea58886565

**Context:** Non-overlapping compiler roles: **adr-architecture-kit** is the authoring compiler for
ADR registries/manifest/rendered views (not a second compiler-of-record for
`ArchitectureEvidence` or normative `Compiled_IR_Document`). **ste-runtime** is runtime
evidence compiler of record. **ste-kernel** merges publication fragments, validates IR,
and emits `KernelAdmissionAssessment` while consuming ste-spec contracts.

[Open projection](ADR-L-0041-compiler-evidence-and-merge-authority.md)
### ADR-L-0042 — Open Standards and Closed Intelligence Boundary

**Relationships:**
- 01a04e96-1f5c-7116-883f-0badde97c759 -[:references]-> this ADR

**Context:** STE adopts **open standards plus closed intelligence**: public specifications define
compatible artifact formats, schemas, interfaces, and deterministic validation surfaces;
proprietary reasoning may remain behind those interfaces.

[Open projection](ADR-L-0042-open-standards-and-closed-intelligence-boundary.md)
### ADR-L-0043 — Context Domain and MVC Lifecycle Boundary

**Relationships:**
- 01a04e96-1f5c-72a7-8a1b-81cf44933af3 -[:references]-> this ADR

**Context:** STE is introducing an experimental model for task-scoped architectural context.
The model treats MVC as a task-scoped architectural reality bundle rather than
generic context reduction. RSS assembles the candidate architectural reality
surface from declared intent, Context Domains, Graph Domains, Linkage Surfaces,
Architecture IR snapshots, task context, and persona context-selection policy.

[Open projection](ADR-L-0043-context-domain-and-mvc-lifecycle-boundary.md)
### ADR-L-0044 — Governed Semantic Reasoning Foundation

**Relationships:**
- 01a06490-5b3c-76c0-9da2-abc5d28f8970 -[:references]-> this ADR

**Context:** This ADR promotes the first bounded semantic re-baseline tranche: FD-01,
FD-01-R1, and the NM-01 semantic contents represented by SD-01 through SD-05.
The senior design lock ledger and Design Journal are design evidence only; this
ADR is the accepted authority for the semantic foundation stated here.

[Open projection](ADR-L-0044-governed-semantic-reasoning-foundation.md)
### ADR-L-1002 — Architecture Admission Model

**Relationships:**
- this ADR -[:references]-> 01a04e96-1f5c-73c9-ad1f-df05ef43cae1

**Context:** Admission decides whether a **requested action** may proceed under declared
architecture truth (IR), factual evidence, governance posture, and active rules.
This ADR-L defines the semantic meaning of allowed, denied, conditional, and warned
admission postures and the **input closure** required to reach a decision.

[Open projection](ADR-L-1002-architecture-admission-model.md)





## Invariants

### INV-3001

**Statement:** Runtime and kernel repositories MUST NOT treat repo-local types, tests, or informal
prose as authoritative over ste-spec `contracts/` and published invariants for the
same handoff surfaces.
  
**Scope:** global  
**Enforcement:** must (policy)  
**Verification:** audit

**Rationale:**
Preserves ADR-L-0030 as the contract authority anchor.






## Decisions

### DEC-3001: Govern cross-repository handoff contract shape in ste-spec `contracts/` and rules in `invariants/`

**Rationale:**
Single normative source for payload structure, semantic rules, and architectural intent
at the runtime/kernel boundary.



**Consequences:**

**Positive:**
- No parallel shadow contract authority in consumer repos

**Negative:**
- Contract evolution requires coordinated ste-spec changes



## Gaps

### GAP-3001: Enumerate every handoff contract family in Architecture IR when catalogs mature

**Impact:** low  
**Blocking:** No






---

*Generated from ADR-L-0030 by ADR Architecture Kit*