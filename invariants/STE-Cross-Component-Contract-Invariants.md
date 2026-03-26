# STE Cross-Component Contract Invariants

## Purpose

This document indexes the atomic invariants that govern the runtime-to-kernel
handoff.

**Filename note:** Files here use the **`INV-xxxx-*`** pattern as **cross-component
contract invariants** for kernel/runtime handoffs. That naming scheme is
**distinct** from **SYS-*** system invariants summarized in
[`STE-Invariant-Hierarchy.md`](STE-Invariant-Hierarchy.md); see also
[`glossary.md`](../glossary.md) (Invariant Hierarchy / System Invariants note).

## Canonical Invariants

- `INV-0001-runtime-evidence-factual-only.md`
- `INV-0002-kernel-final-admission-authority.md`
- `INV-0003-contract-version-required.md`
- `INV-0004-required-arrays-explicit.md`
- `INV-0005-unknown-freshness-explicit.md`
- `INV-0006-kernel-fails-closed-on-invalid-evidence.md`
- `INV-0007-closed-object-contract-discipline.md`
- `INV-0008-invalid-bundle-requires-error-diagnostics.md`
- `INV-0009-degraded-bundle-requires-diagnostic-context.md`
- `INV-0010-rule-projection-envelope-discipline.md` (draft scope; see file status)
- `INV-0011-kernel-fails-closed-on-unverifiable-execution-prerequisites.md`
- `INV-0012-evidence-must-reference-evaluated-subjects.md`

## Related Contracts

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
- `contracts/freshness-contract-mapping.md` (normative freshness layering)
- `contracts/architecture-ir/spec-ir-fragments.json`
- `contracts/architecture-ir/architecture-ir.schema.json`
- `contracts/architecture-ir-contract-pin.json`
- `contracts/rule-projection/` (draft rule projection envelope; pre-normative)
- `contracts/governance-decision-record/` (draft governance decision rows; pre-normative)

## Failure Layering

- `invariants/STE-Failure-Taxonomy-Boundaries.md`

## Related orientation

- `architecture/STE-System-Core.md`
