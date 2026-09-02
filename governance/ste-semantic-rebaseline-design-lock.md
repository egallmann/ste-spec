# STE Semantic Re-Baseline Design-Lock Ledger

> **DESIGN-STATE LEDGER — This record tracks senior design locks for later review and promotion. It is not normative STE authority, an accepted ADR, a contract, an invariant, a schema, or an implementation instruction.**

## Purpose and authority status

This ledger records the current senior-design status of the normative semantic
tranche. It does not promote any item into accepted STE-SPEC authority and does
not amend the ADR corpus. Authority remains with accepted ADRs and their owning
contracts until a separately reviewed promotion occurs.

The deeper reasoning, source archaeology, evidence, alternatives, and unresolved
questions are recorded in the [STE Semantic Re-Baseline Design
Journal](ste-semantic-rebaseline-design-journal.md). That journal remains
nonnormative; this ledger is a compact design-state index, not a replacement
for it.

## FD-01 — Governed Reasoning-Space Shaping

**Status:** `LOCKED`

### Locked decision

STE treats computational reasoning as operation within an explicitly governed
semantic outcome space.

Applicable authoritative semantics shape that space in aggregate by requiring,
prohibiting, preferring, discouraging, or explicitly permitting outcomes.

STE does not define deterministic AI reasoning as requiring one identical textual
or implementation result. STE uses bounded-outcome determinism: independently
generated outcomes are acceptable when they remain within the applicable
authority, normative, and epistemic boundaries.

The semantic boundary used to shape reasoning SHOULD also provide the basis for
validating the resulting candidate.

Where applicable semantics can be mechanically reduced, validation may be
deterministic.

Where higher-order semantic interpretation is required, STE MUST use bounded,
evidence-bearing assessment rather than falsely representing semantic
interpretation as formal mathematical proof.

### Foundational semantic consequences

1. Normative force is an STE-wide semantic concept, not a
   `NormativeProposition`-specific concept.
2. The meaning of a normative force MUST remain semantically invariant across
   legitimate authoritative semantic carrier types.
3. Semantic entity type determines what kind of architectural meaning is
   represented; entity type MUST NOT redefine the meaning of the normative force
   itself.
4. Applicable normative semantics compose in aggregate to shape the reasoning
   space.
5. Hard normative semantics constrain the acceptable outcome space.
6. Preference-oriented normative semantics shape selection among otherwise
   acceptable outcomes.
7. Explicit permission semantics identify known-permitted regions of the
   applicable outcome space.
8. Normative force MUST NOT manufacture authority.
9. Normative force MUST NOT override epistemic boundaries or convert
   unknown/unsupported state into known or authoritative state.
10. Imperative-looking prose alone MUST NOT become governing normative semantics.
    Normative force governs only through admitted authoritative semantic
    structures.
11. Bounded-outcome determinism permits multiple materially different outcomes
    when all remain inside the governed acceptable semantic space.

### Relationship to CEM

The locked separation is:

- **FD-01 / normative semantics** governs **what** semantic outcome space
  reasoning may inhabit.
- **CEM** governs **how** bounded reasoning is conducted through its reasoning
  lifecycle.
- **Epistemic semantics** govern **what** the reasoner may legitimately claim to
  know.
- **Authority semantics** govern **which** semantics are competent to govern.

CEM historically named the governed-reasoning concept. The ADR corpus
subsequently evolved increasingly explicit normative and imperative semantics as
the practical mechanism used to shape acceptable reasoning outcomes.
`NormativeProposition` is a newer canonical semantic realization of that
mechanism; it is not the origin of the underlying STE theory.

### Reasoning / validation symmetry

```text
authoritative semantic state
            |
            v
   applicable semantics
       /           \
      v             v
shape reasoning   validate candidate
```

Validation capability forms a continuum: mechanically reducible contradiction
may receive deterministic validation; structured semantic incompatibility may
use graph/rule evaluation; and higher-order semantic incompatibility may use
bounded evidence-bearing AI assessment. STE does not claim that arbitrary
natural-language architecture can be mathematically proven consistent. More
explicit semantic structure can increase the portion of architecture that is
mechanically evaluable.

### Historical disposition

FD-01 is recorded as recovered and formalized STE doctrine, not as a newly
invented theory. The cautious lineage is:

```text
early normative / imperative STE practice
    -> CEM governed-reasoning model
    -> increasingly normative ADR corpus
    -> structured constraints / invariants
    -> canonical NormativeProposition
    -> explicit recognition of aggregate reasoning-space shaping
```

This is an approximate design lineage, not a claim of an exact historical
sequence. The Design Journal remains the detailed evidentiary record.

## FD-01-R1 — Formal Semantic Characterization of Governed Reasoning Space

**Parent:** FD-01 — Governed Reasoning-Space Shaping
**Status:** LOCKED REFINEMENT

FD-01 remains unchanged in its foundational claim: STE treats computational
reasoning as operation within an explicitly governed semantic outcome space and
defines determinism as bounded acceptable outcomes rather than identical
generated outputs.

### Complementary prose and formal semantics

For semantic concepts amenable to formal characterization, STE SHOULD define the
concept using complementary human-readable prose and formal semantics. Prose
communicates architectural intent and operational meaning; formal
characterization removes ambiguity, makes composition explicit, and exposes
mechanically evaluable consequences. Neither representation may silently
contradict or extend the other.

Formal notation MUST be used where it materially improves semantic precision or
evaluability, not merely to make a specification appear formal. The preferred
definition pattern is: human-readable definition; formal characterization;
architectural example; reasoning/composition consequence; validation
consequence.

### Hard-admissible reasoning space

Let \( \Omega \) be the universe of candidate outcomes available before
applicable semantic shaping. Let \(H = \{h_1,h_2,\ldots,h_n\}\) be the
applicable hard normative constraints, where each \(h\) induces an admissible
subset \(A_h \subseteq \Omega\). The hard-admissible reasoning space is:

$$
A = \bigcap_{h \in H} A_h
$$

A candidate \(x\) is hard-conformant only if \(x \in A\). Bounded-outcome
determinism therefore permits materially different outcomes
\(x_1,x_2,\ldots,x_n \in A\) when each remains inside the same applicable
semantic boundary. Determinism constrains the acceptable outcome space; it does
not require one textual, procedural, or implementation result.

### Preference semantics

Not every normative force changes membership in \(A\). A preference relation
\(\succ \subseteq A \times A\) orders otherwise hard-admissible candidates:
\(x \succ y\) means that \(x\) is normatively preferred to \(y\) in the
applicable context. Preference alone does not imply \(y \notin A\).

For a proposition \(P\), SHOULD(P) ordinarily means that, for materially
comparable \(x,y \in A\), \(P(x) \land \neg P(y) \Rightarrow x \succ y\),
subject to applicable competing concerns. SHOULD NOT(P) analogously prefers
\(\neg P\) without automatically making every P-satisfying candidate
hard-nonconformant.

### Explicit permission semantics

For proposition \(P\), define:

$$
A_P = \{x \in A \mid P(x)\}
$$

MAY(P) affirmatively establishes \(A_P\) as permitted with respect to \(P\). It
does not necessarily enlarge \(A\), and it is not equivalent to the absence of
prohibition:

$$
\mathrm{MAY}(P) \Rightarrow \neg\mathrm{MUST\ NOT}(P)
$$

but:

$$
\neg\mathrm{MUST\ NOT}(P) \not\Rightarrow \mathrm{MAY}(P)
$$

Explicit permission can therefore prevent over-constraint while preserving hard
restrictions.

### Semantic convergence and validation continuum

Where applicable hard semantics are mechanically reducible, \(A=\varnothing\)
means no candidate satisfies the complete applicable hard set. Simultaneously
applicable \(P\) and \(\neg P\) provide the canonical example:

$$
A_P \cap A_{\neg P} = \varnothing
$$

This is mechanically demonstrable non-convergence for that applicability
context. STE MUST NOT generalize that proof level to architectural semantics
that are not formally reducible. Validation remains a continuum:

1. mechanically reducible contradiction → deterministic validation;
2. structured semantic incompatibility → graph or rule evaluation;
3. higher-order semantic incompatibility → bounded, evidence-bearing semantic
   assessment.

Increasing explicit semantic structure SHOULD increase the portion of governed
reasoning space that can be evaluated mechanically. STE does not claim that
arbitrary natural-language architecture can be mathematically proven
consistent.

### Formalism integrity

STE MUST NOT introduce equations, formal notation, or logical expressions
merely to make specification content appear more rigorous, official,
mathematical, or impressive. Formal expressions are used only when they
materially improve semantic understanding, precision, composition, or
evaluability.

Every formal expression MUST hold within its stated assumptions and domain, and
non-trivial expressions MUST be locally interpretable. When equations are used,
the surrounding specification SHOULD provide:

1. the plain-language semantic claim;
2. the formal expression;
3. definitions for symbols, functions, relations, variables, and operators;
4. a plain-English reading;
5. a worked architectural example where useful;
6. semantic assumptions, boundary, and non-claim;
7. a validation consequence where useful.

STE MAY provide logical proofs when a proof materially establishes, clarifies,
or defends the semantic property. Formal expressions remain subject to
architectural challenge. When challenged, their assumptions, derivation,
domain, and validity MUST be defensible. An indefensible expression MUST be
corrected, narrowed, or removed; mathematical notation does not confer
authority or correctness.

## SD-01 — NormativeProposition

**Status:** LOCKED

NormativeProposition is a first-class canonical STE semantic entity for an
independently meaningful normative architectural proposition. It participates in
the common canonical identity model: UUIDv7 canonical identifier, typed
human-recognizable alias_id, and semantic alias_name.

For ADR-scoped NormativePropositions, current normative authority derives from
presence in the current effective authoritative ADR revision. An NP has no
independent proposed/accepted/deprecated/retired governance lifecycle. Removal
from the effective ADR removes it from current authority; historical ADR
revisions preserve prior normative state. Tombstones and mandatory NP-to-NP
supersedes/refines/coalescence lineage are not required. Materially different
normative meaning receives a new identity; editorial relocation or wording
changes may retain identity when semantic meaning is unchanged.

Modal wording alone does not create an NP. NP remains distinct from Invariant,
Rule, evidence, assessment, broad Constraint semantics, and future Requirement
semantics. Requirements remain a future first-class semantic family.

### SD-01 refinement — NP semantic materiality

An NP MUST contain independently meaningful normative semantics whose explicit
presence is materially capable of shaping the governed reasoning space. Before
admission, the semantic author/reasoner asks:

> Standing on its own as an explicit proposition, can this meaning materially
> affect what a competent reasoner understands to be required, prohibited,
> strongly preferred, strongly discouraged, or explicitly permitted?

If yes, the statement is eligible for NP admission. If no, it MUST NOT become
an NP merely because it contains normative or imperative wording. Explanatory
prose, rationale, navigation/organizational instructions, narrative statements,
and restatements without meaningful reasoning-space value remain outside the NP
set.

Semantic materiality does not require strict logical uniqueness. An NP MAY
specialize, reinforce, or concretize broader normative semantics when its
explicit presence materially improves reasoning-space shaping.

This admission-materiality test answers whether a canonical normative
proposition should exist. It does not answer which already-existing applicable
propositions should be assembled into a particular LLM reasoning task.
Task-specific reasoning-state formulation belongs to a separate
reasoning/CEM/system-component responsibility and MUST NOT be conflated with NP
admission.

## SD-02 — NormativeProposition / Invariant peer taxonomy

**Status:** LOCKED

NormativeProposition and Invariant are peer first-class normative semantic entity
types. They share common structural semantics where genuinely equivalent but
retain distinct type semantics. There is no ordinary NP-to-Invariant promotion
lifecycle.

Existing explicitly authored invariants remain Invariants. Existing scoped R###
or constraint-like architectural propositions conservatively migrate toward
NormativeProposition. Invariant status MUST NOT be inferred merely from modal
strength, importance, broad scope, or model interpretation. Material cross-type
evolution is a substantive architecture change, not an entity lifecycle state
transition.

## SD-03 — Global Normative Force Semantics

**Parent:** NM-01 — Normative Semantic Model
**Depends on:** FD-01 / FD-01-R1
**Status:** LOCKED

### Decision

STE defines these canonical global normative forces:

$$
\boxed{\mathrm{MUST}},\quad
\boxed{\mathrm{MUST\ NOT}},\quad
\boxed{\mathrm{SHOULD}},\quad
\boxed{\mathrm{SHOULD\ NOT}},\quad
\boxed{\mathrm{MAY}}
$$

Their meaning is global and MUST remain invariant across legitimate semantic
carrier types. A carrier determines what kind of architectural meaning is
expressed; it MUST NOT redefine the force's meaning. NormativeProposition is one
canonical carrier. Invariant, future Requirement semantics, contractual
semantics, and other governed families may participate where their type
semantics permit.

Tooling MAY derive secondary classifications or normalized representations, but
derived representations MUST preserve the canonical force and MUST NOT replace
or weaken it. A separate polarity dimension is not required: MUST NOT and
SHOULD NOT are complete forces, not positive force plus a reconstructed polarity
flag.

### Force meanings

| Force | Semantic role | Formal consequence |
|---|---|---|
| MUST | Hard positive admissibility: a conforming candidate satisfies \(P\). | \(A_{\mathrm{MUST}(P)}=\{x\in\Omega\mid P(x)\}\); \(x\in A\Rightarrow P(x)\). |
| MUST NOT | Hard exclusion: a conforming candidate satisfies \(\neg P\). | \(A_{\mathrm{MUST\ NOT}(P)}=\{x\in\Omega\mid\neg P(x)\}\); \(x\in A\Rightarrow\neg P(x)\). |
| SHOULD | Strong positive preference among otherwise admissible candidates. | \(P(x)\land\neg P(y)\Rightarrow x\succ y\), subject to competing concerns. |
| SHOULD NOT | Strong negative preference among otherwise admissible candidates. | \(\neg P(x)\land P(y)\Rightarrow x\succ y\), subject to competing concerns. |
| MAY | Explicit strong permission identifying a known-permitted region. | \(A_P=\{x\in A\mid P(x)\}\) is affirmatively permitted; \(P\) is not required. |

If compatible scope and authority make MUST(P) and MUST NOT(P) simultaneously
applicable, \(A_P\cap A_{\neg P}=\varnothing\). STE MUST expose this as
semantic divergence, not silently select a proposition by document order or
presentation position.

SHOULD and SHOULD NOT are strong expectations, not casual advice. Deviation may
remain admissible only with a defensible basis under applicable competing
concerns. Exact recording, waiver, exception, and competing-preference
resolution remain downstream decisions.

MAY is not mere non-prohibition. It positively communicates permitted
architectural freedom and can prevent a reasoner from over-generalizing nearby
restrictions. For example, Runtime MUST preserve canonical snapshot identity,
Derived state MUST NOT manufacture architectural authority, and Runtime MAY
maintain disposable local traversal indexes jointly express mandatory identity,
prohibited authority manufacture, and explicit freedom for disposable indexing.

### Aggregate composition and boundaries

The five forces compose into three semantic roles:

- hard admissibility: MUST, MUST NOT;
- strong preference: SHOULD, SHOULD NOT;
- explicit freedom: MAY.

Normative force MUST NOT manufacture authority, applicability, or epistemic
knowledge. It MUST NOT convert unknown or unsupported state into known or
authoritative facts. Imperative-looking prose outside an admitted governed
semantic structure does not acquire force merely because it uses one of these
words. Conflicts between simultaneously applicable forces MUST NOT be silently
resolved through document ordering.

### Explicit deferrals

SD-03 does not determine authority/effectivity composition, scope/applicability,
exception or waiver representation, cross-authority conflict precedence,
ADR-Kit authoring or normalized storage shape, Requirement-specific semantics,
Invariant-specific representation, validator implementation, or a universal
formal predicate language.

## SD-04 — Authority and Effectivity

**Status:** LOCKED

STE separates normative force, authority/competence, effectivity, and
applicability. They MUST NOT be collapsed. Authority is recognized competence
to establish governing semantic meaning for a bounded semantic domain and system
boundary. Semantic entities MUST NOT self-authorize, and normative strength
MUST NOT manufacture authority. Representation, persistence, copying,
normalization, projection, observation, inference, implementation, and graph
structure likewise MUST NOT manufacture architectural authority.

### Governing eligibility

The conceptual relation is:

$$
G(p,d,t)
\iff
\exists s\;[
s\text{ establishes }p
\land s\text{ is effective at }t
\land s\text{ has valid competence over }d\text{ at }t
]
$$

Here p is the semantic proposition, d the bounded semantic domain/system
boundary, t the relevant architectural state or time, s the authority-bearing
source state or revision, and G governing eligibility. This establishes
competent/effective eligibility, not concrete applicability.

For ADR-scoped semantic entities, governing participation derives from the
effective authority-bearing source state/revision; no duplicated NP lifecycle is
required.

### Authority composition

STE-SPEC is authoritative for the system-of-systems intent model and its
cross-system semantic boundaries. Individual STE systems retain local
architectural-intent authority within those boundaries; broader authority does
not imply detailed implementation authority. A local system MUST NOT manufacture
competence over cross-system semantics reserved to STE-SPEC.

The effective ADR corpus forms a composed authoritative intent-semantic model.
Relationships across ADR-L, ADR-PS, ADR-PC, Decision, Invariant,
NormativeProposition, and other admitted intent entities may be explicit or
validly derived. An LLM's plausible inference is not authoritative.

Runtime owns bounded observation, reconstruction, embodiment entities and
relationships, coverage, provenance, and derived assessment under its contracts.
Its semantic graph is not architectural-intent authority. STE MAY compose intent
and embodiment to produce linkage, realization/support, convergence, divergence,
coverage, unknown-state, and assessment semantics, but composition MUST NOT
transfer or union input authorities.

An STE enabling system can be governed by its own ADR corpus while providing
bounded semantic capability over another system; those roles remain distinct.
Delegated competence may narrow but cannot exceed upstream competence. Multiple
legitimate paths cannot manufacture new cross-domain competence by co-presence.
Conflicts among competent/effective semantics MUST NOT be silently resolved by
document order, ADR number, newest source, modal strength, implementation state,
or projection order. Unresolved real conflict is surfaced as semantic
divergence.

## SD-05 — Scope and Applicability

**Status:** LOCKED

SD-05 closes the authority/effectivity model rather than introducing an
independent theory. Scope bounds the contexts in which governed meaning can
potentially apply. It may be inherited from authoritative semantic context and
may be narrowed by more specific declarations, but it MUST NOT broaden
governing competence or manufacture authority.

Applicability evaluates already competent and effective meaning against a
concrete context. Meaning assessed as non-applicable does not govern that
context. Applicability MUST be grounded in declared or validly inherited scope
and contextual semantics. Textual similarity, document proximity, or
ungoverned model intuition MUST NOT manufacture applicability.

The applicability result preserves three epistemically distinct outcomes:

- APPLIES
- DOES_NOT_APPLY
- UNKNOWN

Insufficient contextual knowledge remains UNKNOWN. UNKNOWN MUST NOT be collapsed
into either APPLIES or DOES_NOT_APPLY. Exact downstream behavior while
applicability is UNKNOWN remains deferred.

Conceptually, the semantic set governing concrete context c at time/state t
contains propositions with competent/effective eligibility under SD-04 that are
assessed APPLIES under SD-05. This does not decide task-specific
reasoning-state assembly or which applicable propositions are selected for an
individual LLM invocation.

## Current normative tranche

| ID | Design item | Status | Context |
|---|---|---|---|
| FD-01 | Governed Reasoning-Space Shaping | `LOCKED` | STE-wide doctrine: applicable normative semantics collectively shape a bounded semantic outcome space, while epistemic and authority boundaries remain distinct. |
| FD-01-R1 | Formal Semantic Characterization | `LOCKED` | Formal treatment is complementary to prose when it materially improves semantic understanding, precision, composition, or evaluability; decorative mathematics is prohibited. |
| NM-01 | Normative Semantic Model | `TRANCHE LOCKED / COMPLETE` | FD-01, FD-01-R1, and SD-01 through SD-05 are senior-locked design state; no accepted authority promotion is implied. |
| SD-01 | NormativeProposition | `LOCKED` | Senior-locked semantic realization of normative meaning; detailed final authoring, authority/effectivity, scope, and representation decisions remain downstream. |
| SD-02 | NP / Invariant peer taxonomy | `LOCKED` | Senior-locked taxonomy relationship; this ledger records the status only and does not expand its final semantics. |
| SD-03 | Global normative force semantics | `LOCKED` | Canonical global forces are MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY; their meaning is carrier-invariant. Detailed applicability, authority, effectivity, exceptions, and implementation remain open. |
| SD-04 | Authority / effectivity | `LOCKED` | Competent/effective governing eligibility is distinct from force and applicability; semantic entities and derived carriers cannot self-authorize. |
| SD-05 | Scope / applicability | `LOCKED` | Scope bounds potential application; applicability yields APPLIES, DOES_NOT_APPLY, or UNKNOWN without deciding task-specific context selection. |

`LOCKED` records senior design disposition, not accepted architectural authority.
`OPEN` identifies intentionally unresolved downstream work outside this
completed tranche; it is not a defect in FD-01.

The foundational/normative semantic tranche is now `TRANCHE LOCKED / COMPLETE`.
These locks remain senior design convergence awaiting later controlled
promotion; they are not canonical STE-SPEC architectural authority.

## Explicit deferrals to preserve

The following remain deliberately unresolved:

- exact ADR-Kit authoring or normalized schemas;
- the full Requirement semantic model;
- exact Invariant representation mechanics;
- validator implementation;
- a universal predicate language;
- complete authority-precedence algebra;
- external intent-binding implementation;
- detailed applicability schema;
- waiver/exception mechanics;
- task-specific reasoning-state selection;
- intent/embodiment relationship vocabulary;
- convergence scoring algorithms;
- CEM lifecycle redesign.

No ADR, contract, schema, validator, Runtime artifact, Kernel artifact, or
implementation has been changed by recording this design-state lock.

## Checkpoint scope

This ledger is the first durable senior-design checkpoint for the semantic
re-baseline. Subsequent promotion work must cite this record, the deeper Design
Journal, and the authority-owning ADR/contract decisions that are eventually
accepted. Until then, all entries remain design state.
