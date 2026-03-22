# STE Cross-Component Contract Invariants

## Purpose

This document indexes the atomic invariants that govern the runtime-to-kernel
handoff.

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

## Related Contracts

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
- `contracts/architecture-ir/spec-ir-fragments.json`
- `contracts/rule-projection/` (draft rule projection envelope; pre-normative)
- `contracts/governance-decision-record/` (draft governance decision rows; pre-normative)

## Failure Layering

- `invariants/STE-Failure-Taxonomy-Boundaries.md`

## Related orientation

- `architecture/STE-System-Core.md`
