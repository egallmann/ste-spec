# ADR-041: Compiler, Evidence, and Merge Authority

## Status

Accepted

## Context

STE spans multiple repositories. Without an explicit **compiler-of-record** and
**merge authority** model, teams can accidentally introduce parallel “truth
compilers” for the same artifact classes, or confuse **authoring-time**
compilation with **runtime evidence** and **kernel merge** responsibilities.

Related accepted decisions:

- [`ADR-031-runtime-kernel-responsibility-boundary.md`](ADR-031-runtime-kernel-responsibility-boundary.md)
  (`ste-runtime` evidence-only; `ste-kernel` admission authority)
- [`ADR-035-architecture-ir-ontology-authority.md`](ADR-035-architecture-ir-ontology-authority.md)
  (semantic vs mechanical Architecture IR authority in `ste-spec`)

## Decision

STE assigns **non-overlapping** compiler and merge roles:

1. **`adr-architecture-kit` (authoring compiler).** Compiles contributor ADR
   sources into **authoring-time** outputs (for example registries, manifest,
   rendered views). Internal structures such as **`ArchModel`** are **not** a
   cross-repository interchange contract. The kit **MUST NOT** claim a second
   **compiler-of-record** role for **`ArchitectureEvidence`** or for the
   normative **`Compiled_IR_Document`** JSON Schema published under
   `ste-spec/contracts/architecture-ir/`.

2. **`ste-runtime` (runtime evidence compiler of record).** Produces factual,
   schema-governed **`ArchitectureEvidence`** (and any other **ste-spec**
   runtime evidence contracts). Runtime evidence is **non-decision-bearing** at
   the handoff boundary.

3. **`ste-kernel` (merge + admission authority).** Loads adapter **publication
   surfaces**, deterministically merges fragments into **`Compiled_IR_Document`**,
   validates against the **ste-spec** Architecture IR schema, and emits
   **`KernelAdmissionAssessment`**. The kernel **consumes** normative contracts
   from **`ste-spec`**; it does not redefine them.

**MUST NOT:** Maintain a second authoritative pipeline that redefines the same
ste-spec contract shapes for **`ArchitectureEvidence`** or the normative
Architecture IR schema without an explicit superseding ADR.

## Lifecycle Placement in the STE Spine

This ADR applies across **Intent Definition** (authoring), **Publication /
Integration Input** (fragments and evidence), **Architecture IR Compilation**
(merge and validate), and **Admission Decision** (kernel output).

## Relationship to Enforcement Model

This ADR does not change enforcement mechanics; it constrains **who may claim
compiler or contract authority** for named artifact classes so fail-closed
enforcement has a single normative shape to target.

## Rationale

- Prevents ambiguous “two compilers of record” failures for the same contract.
- Keeps runtime evidence factual and kernel admission decision-bearing, per ADR-031.
- Aligns mechanical Architecture IR authority with `ste-spec`, per ADR-035.

## Consequences

- Repository READMEs and integration docs **SHOULD** describe their role using
  the terms above.
- Changes to normative Architecture IR mechanics **MUST** land in **`ste-spec`**
  (with pin updates), not only in **`ste-kernel`**.
