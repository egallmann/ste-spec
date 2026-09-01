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

## Current normative tranche

| ID | Design item | Status | Context |
|---|---|---|---|
| FD-01 | Governed Reasoning-Space Shaping | `LOCKED` | STE-wide doctrine: applicable normative semantics collectively shape a bounded semantic outcome space, while epistemic and authority boundaries remain distinct. |
| NM-01 | Normative Semantic Model | — | Current tranche grouping for the normative-semantic design work; no additional promotion is implied by this ledger. |
| SD-01 | NormativeProposition | `LOCKED` | Senior-locked semantic realization of normative meaning; detailed final authoring, authority/effectivity, scope, and representation decisions remain downstream. |
| SD-02 | NP / Invariant peer taxonomy | `LOCKED` | Senior-locked taxonomy relationship; this ledger records the status only and does not expand its final semantics. |
| SD-03 | Global normative force semantics | `LOCKED` | Canonical global forces are MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY; their meaning is carrier-invariant. Detailed applicability, authority, effectivity, exceptions, and implementation remain open. |
| SD-04 | Authority / effectivity | `OPEN` | Authority, lifecycle, effective-state, and conflict composition remain undecided. |
| SD-05 | Scope / applicability | `OPEN` | Scope resolution and applicability semantics remain undecided. |

`LOCKED` records senior design disposition, not accepted architectural authority.
`OPEN` records an intentionally unresolved downstream decision, not a defect in
FD-01.

FD-01-R1 resolves the previously open force-vocabulary question through SD-03;
this refinement does not alter FD-01's foundational claim or promote either
design item into accepted architecture.

## Explicitly deferred by FD-01

FD-01 does not decide:

- the exact canonical normative-force vocabulary;
- `NormativeProposition` authoring syntax;
- authority/effectivity composition;
- scope/applicability semantics;
- exception or waiver semantics;
- Invariant-specific realization details;
- Requirement semantics;
- ADR-Kit representation or normalization;
- validator implementation;
- a formal predicate language;
- CEM lifecycle redesign.

No ADR, contract, schema, validator, Runtime artifact, Kernel artifact, or
implementation has been changed by recording this design-state lock.

## Checkpoint scope

This ledger is the first durable senior-design checkpoint for the semantic
re-baseline. Subsequent promotion work must cite this record, the deeper Design
Journal, and the authority-owning ADR/contract decisions that are eventually
accepted. Until then, all entries remain design state.
