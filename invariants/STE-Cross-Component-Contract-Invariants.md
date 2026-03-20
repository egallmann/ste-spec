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

## Related Contracts

- `contracts/architecture-evidence.schema.json`
- `contracts/kernel-admission-assessment.schema.json`
