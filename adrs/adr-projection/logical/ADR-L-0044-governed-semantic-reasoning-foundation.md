<!--
integrity_schema_version: 1
generated: deterministic_projection_v1
artifact_kind: rendered_adr_markdown
generator_id: adr-projection-markdown
generator_version: 3
hash_algorithm: sha256
source_hash: 03dea5f9e2e4e2bd828761b664464d13d120511ca2258abdb2169e0f950d135d
rendered_hash: 8117af29a3b5b43106cb40b25ec9259e81fc19e736180e462f97ab0b4518d814
-->

# ADR-L-0044: Governed Semantic Reasoning Foundation

**Status:** accepted<br>
**Created:** 2026-09-02<br>
**Modified:** 2026-09-02<br>
**Authors:** Erik Gallmann, ste-spec<br>
**Domains:** governance, semantics, reasoning, architecture-ir<br>
**Tags:** bounded-reasoning, normative-semantics, authority, applicability<br>
**Alias name:** governed-semantic-reasoning-foundation<br>

## Context

This ADR promotes the first bounded semantic re-baseline tranche: FD-01,
FD-01-R1, and the NM-01 semantic contents represented by SD-01 through SD-05.
The senior design lock ledger and Design Journal are design evidence only; this
ADR is the accepted authority for the semantic foundation stated here.

CE-01 (Canonical Semantic Entity Model) remains locked design state and is not
promoted by this ADR. In particular, this ADR does not decide the relationship
among canonical semantic-record UUIDv7/alias identity, ADR-Kit normalized
representation, and compiled Architecture IR identifiers. No CE-01 identity
requirement or mechanical Architecture IR identity change is implied.

This ADR establishes semantic meaning and authority boundaries. Authoring,
normalized-model, schema, validator, Runtime, Kernel, CEM lifecycle, and
exception/waiver implementations remain governed by their owning surfaces and
the explicit deferrals below.








## Invariants

### INV-4401

**Statement:** A conforming reasoning outcome MUST remain within the applicable semantic, authority, normative, and epistemic boundaries; bounded-outcome determinism MUST NOT be interpreted as a requirement for one identical generated result.<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Preserves governed reasoning-space shaping while allowing bounded outcome diversity.



### INV-4402

**Statement:** STE MUST NOT introduce equations or formal notation merely for rhetorical effect, and every non-trivial formal expression MUST remain locally interpretable and defensible within its declared assumptions and domain.<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Mathematical notation does not confer authority or correctness.



### INV-4403

**Statement:** A NormativeProposition MUST contain independently meaningful normative semantics whose explicit presence is materially capable of shaping the governed reasoning space; modal or imperative wording alone MUST NOT admit an NP.<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Admission materiality distinguishes semantic propositions from explanation, navigation, organization, and non-shaping restatement.



### INV-4404

**Statement:** Normative force MUST retain the same meaning across legitimate semantic carrier types and MUST NOT manufacture authority, effectivity, applicability, or epistemic knowledge.<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Carrier type determines architectural meaning without redefining force semantics.



### INV-4405

**Statement:** For applicable hard constraints H over candidate universe Ω, each h MUST induce an admissible subset A_h and the hard-admissible space MUST be understood conceptually as A = intersection of all A_h; materially different candidates MAY both conform when each is a member of A.<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Makes hard admissibility, bounded determinism, and preference composition explicit
without claiming all architecture is formally reducible. Where mechanically
reducible hard semantics produce A = empty set, the bounded applicability context
has no convergent candidate. Validation remains a continuum: deterministic
contradiction checks, graph/rule evaluation for structured incompatibility, and
bounded evidence-bearing semantic assessment for higher-order incompatibility.




### INV-4406

**Statement:** Preference semantics MUST order otherwise hard-admissible candidates without automatically removing a non-preferred candidate from the hard-admissible space, and MAY(P) MUST be distinguished from mere absence of MUST NOT(P). MAY(P) implies absence of an applicable MUST NOT(P), but absence of MUST NOT(P) does not imply MAY(P).<br>
**Scope:** global<br>
**Enforcement:** must (design)<br>
**Verification:** manual

**Rationale:**
Preserves strong preference and explicit permission as distinct roles.



### INV-4407

**Statement:** Governing eligibility for proposition p over bounded domain d at relevant state or time t MUST require an authority-bearing source s that establishes p, is effective at t, and possesses valid competence over d at t; this eligibility relation MUST NOT be treated as concrete applicability. Representation, persistence, normalization, projection, observation, inference, implementation, or graph structure MUST NOT manufacture authority.<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Separates authority path and effectivity from case-specific applicability.



### INV-4408

**Statement:** Delegation MUST NOT amplify competence, co-present authority paths MUST NOT manufacture cross-domain competence, and unresolved conflicts among competent effective semantics MUST NOT be silently resolved by document order, recency, modal strength, implementation state, or projection order.<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Authority composition remains bounded and divergence remains visible.



### INV-4409

**Statement:** Applicability MUST yield APPLIES, DOES_NOT_APPLY, or UNKNOWN from declared or validly inherited scope and contextual semantics; insufficient contextual knowledge MUST remain UNKNOWN and MUST NOT be collapsed into either other outcome.<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Prevents textual similarity, proximity, or model intuition from manufacturing governing meaning.



### INV-4410

**Statement:** Runtime and other embodiment systems MUST NOT manufacture architectural intent authority from observation, reconstruction, provenance, coverage, evidence, persistence, projection, or derived assessment; composition MUST NOT transfer or union the authorities of intent and embodiment inputs.<br>
**Scope:** global<br>
**Enforcement:** must (policy)<br>
**Verification:** manual

**Rationale:**
Preserves the intent-versus-embodiment competence boundary.





## Decisions

### DEC-4401: Govern computational reasoning as operation within an explicitly governed semantic outcome space

**Rationale:**
Applicable authoritative semantics collectively shape acceptable outcomes by requiring, prohibiting, preferring, discouraging, or explicitly permitting outcomes while preserving separate authority and epistemic boundaries. FD-01 governs what semantic outcome space reasoning may inhabit; CEM governs how bounded reasoning is conducted through its lifecycle; epistemic semantics govern what may legitimately be claimed as known; and authority semantics govern which semantics are competent to govern.


**Consequences:**

**Positive:**
- Reasoning inputs and candidate acceptance have one explicit semantic boundary.
- Multiple materially different outcomes can remain conformant when bounded.

**Negative:**
- Higher-order semantic assessment remains evidence-bearing rather than theorem proof.


### DEC-4402: Define deterministic AI reasoning as bounded-outcome determinism

**Rationale:**
Determinism constrains the acceptable outcome space; it does not require one identical textual, procedural, or implementation result.


**Consequences:**

**Positive:**
- Independent reasoners may produce materially different conformant outcomes.
- Mechanical compilation and validation determinism remain separately expressible.

**Negative:**
- Consumers must evaluate authority, normative, and epistemic boundaries.


### DEC-4403: Use complementary prose and formal semantics when formal treatment materially improves precision or evaluability

**Rationale:**
Formal notation clarifies composition only when its assumptions and domain are
locally interpretable and defensible. When used, the specification should state
the plain-language claim, expression, symbol/operator definitions, plain-English
reading, useful worked example, semantic boundary/non-claim, and validation
consequence. Equations are not introduced for rhetorical effect; a challenged
expression must have defensible assumptions, derivation, domain, and validity or
be corrected, narrowed, or removed. For bounded reasoning, Ω denotes the
candidate-outcome universe, H the applicable hard constraints, each h ∈ H
induces A_h ⊆ Ω, and A = ⋂(h ∈ H) A_h is the hard-admissible outcome space.
Preference may order members of A without excluding them; explicit permission
identifies a permitted region. An empty A demonstrates non-convergence only
where those hard semantics are mechanically reducible.



**Consequences:**

**Positive:**
- Reducible semantic properties can expose mechanically evaluable consequences.

**Negative:**
- Formal expressions require explicit definitions, assumptions, and challenge.


### DEC-4404: Admit NormativeProposition as a first-class semantic type and carrier for independently meaningful normative architectural propositions

**Rationale:**
Independently meaningful normative meaning needs an explicit carrier whose
authority, force, scope, and provenance can be reasoned about without relying on
document position or modal wording alone. For ADR-scoped NPs, current authority
derives from presence in the effective authoritative ADR revision; no independent
NP governance lifecycle is required; removal removes current authority while
historical revisions preserve prior state. Tombstones and mandatory
supersedes/refines/coalescence lineage are not inherently required. Materially
changed meaning receives a new identity; editorial relocation or non-semantic
wording change may retain identity. NormativeProposition remains distinct from
Invariant, Rule, evidence, assessment, broad Constraint semantics, and future
Requirement semantics.



**Consequences:**

**Positive:**
- Normative meaning can be addressed and composed explicitly.
- Existing ADR authority remains the source of current NP authority.

**Negative:**
- Native authoring and normalized representation remain downstream work.


### DEC-4405: Preserve NormativeProposition and Invariant as peer semantic types

**Rationale:**
Semantic type determines architectural meaning; modal strength, importance, scope, or model interpretation cannot silently perform cross-type evolution.


**Consequences:**

**Positive:**
- Invariant, Rule, Constraint, evidence, assessment, and future Requirement remain distinct.

**Negative:**
- Cross-type evolution requires substantive architecture review.


### DEC-4406: Define global normative forces as MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY

**Rationale:**
One carrier-invariant vocabulary supports human understanding, reasoner steering,
semantic composition, and deterministic classification without a required polarity
flag. MUST establishes hard positive admissibility; MUST NOT establishes hard
exclusion; SHOULD is a strong positive expectation; SHOULD NOT is a strong negative
expectation; and MAY is explicit strong permission. SHOULD/SHOULD NOT are not
casual advice and permit defensible deviation without automatically making a
candidate hard-nonconformant.
MAY(P) implies absence of an applicable MUST NOT(P), but absence of MUST NOT(P)
does not imply MAY(P). MAY can therefore record positive permission without
enlarging the hard-admissible set.



**Consequences:**

**Positive:**
- Hard admissibility, preference, and explicit freedom are distinguishable.
- MAY can prevent over-constraint by recording positive permission.

**Negative:**
- Exception, waiver, and conflict-resolution mechanics remain downstream.


### DEC-4407: Separate normative force, authority, effectivity, and applicability

**Rationale:**
A proposition can be strongly expressed without being competent, effective, or
applicable to a concrete case. Conceptually, G(p,d,t) holds iff an
authority-bearing source s establishes proposition p, is effective at t, and has
valid competence over bounded domain d at t. G is governing eligibility, not
concrete applicability. STE-SPEC governs system-of-systems intent semantics and
cross-system boundaries; local STE systems retain bounded intent authority inside
those boundaries and MUST NOT manufacture competence over semantics reserved to
STE-SPEC. Explicitly established or validly derived semantic relationships
in an effective ADR corpus may compose, but plausible LLM inference alone does
not become authority. Representation, persistence, normalization, projection,
observation, inference, implementation, or graph structure do not manufacture
architectural authority.



**Consequences:**

**Positive:**
- Governing eligibility can be assessed without manufacturing authority.
- Scope and applicability remain explicit semantic dimensions.

**Negative:**
- Complete precedence and applicability schemas remain deferred.


### DEC-4408: Bound authority composition and delegation to legitimately possessed competence

**Rationale:**
Delegation may narrow competence but cannot amplify it; multiple authority paths
cannot manufacture cross-domain competence through co-presence; unresolved
competent/effective conflicts must remain visible rather than being ordered away
by document order, ADR number, recency, modal strength, implementation state, or
projection order. A future explicit composition rule may establish bounded
cross-domain composition.



**Consequences:**

**Positive:**
- Authority paths remain auditable and domain-bounded.

**Negative:**
- A future explicit cross-domain composition rule may still be required.


### DEC-4409: Evaluate applicability with APPLIES, DOES_NOT_APPLY, and UNKNOWN outcomes

**Rationale:**
Scope bounds contexts in which governed meaning can potentially apply; it may be
inherited and narrowed but must not broaden competence. Applicability evaluates
already competent/effective meaning against a concrete context and must arise from
declared or validly inherited scope/context semantics. Insufficient contextual
knowledge must not be converted into a positive or negative applicability claim.



**Consequences:**

**Positive:**
- Applicability remains grounded in declared or inherited scope and context.

**Negative:**
- Detailed context assembly and task-specific reasoning selection remain separate.


### DEC-4410: Preserve intent and embodiment as distinct competence domains

**Rationale:**
Runtime and other embodiment systems may provide bounded observation, provenance, coverage, evidence, and assessment without acquiring architectural-intent authority.


**Consequences:**

**Positive:**
- Intent/embodiment composition can support bounded assessment without authority union.

**Negative:**
- Cross-domain linkage and verdict semantics require later governed decisions.



## Gaps

### GAP-4401: Native authoring and normalized representation for NormativeProposition remain downstream and must preserve this semantic contract.

**Impact:** medium<br>
**Blocking:** No





### GAP-4402: Detailed exception/waiver mechanics, complete authority-precedence algebra, detailed applicability schema, task-specific reasoning-state selection, complete canonical relationship ontology, intent/embodiment relationship vocabulary, convergence scoring, CEM lifecycle redesign, full epistemic composition, exact Requirement semantics, exact future Invariant representation, native ADR-Kit or Runtime NP implementation, and validator mechanics remain downstream.

**Impact:** medium<br>
**Blocking:** No






---

*Generated from ADR-L-0044 by ADR Architecture Kit*