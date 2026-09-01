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

## Current normative tranche

| ID | Design item | Status | Context |
|---|---|---|---|
| FD-01 | Governed Reasoning-Space Shaping | `LOCKED` | STE-wide doctrine: applicable normative semantics collectively shape a bounded semantic outcome space, while epistemic and authority boundaries remain distinct. |
| NM-01 | Normative Semantic Model | — | Current tranche grouping for the normative-semantic design work; no additional promotion is implied by this ledger. |
| SD-01 | NormativeProposition | `LOCKED` | Senior-locked semantic realization of normative meaning; detailed final authoring, authority/effectivity, scope, and representation decisions remain downstream. |
| SD-02 | NP / Invariant peer taxonomy | `LOCKED` | Senior-locked taxonomy relationship; this ledger records the status only and does not expand its final semantics. |
| SD-03 | Global normative force semantics | `OPEN` | Exact force vocabulary and cross-carrier semantics remain undecided. |
| SD-04 | Authority / effectivity | `OPEN` | Authority, lifecycle, effective-state, and conflict composition remain undecided. |
| SD-05 | Scope / applicability | `OPEN` | Scope resolution and applicability semantics remain undecided. |

`LOCKED` records senior design disposition, not accepted architectural authority.
`OPEN` records an intentionally unresolved downstream decision, not a defect in
FD-01.

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
