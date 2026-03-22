# STE Determinism and Canonical Identity (Integration Plane)

## Purpose

This document states **system-level** determinism requirements for Architecture
IR compilation and kernel boot identity. It does not restate algorithmic steps;
those live in the referenced IR contract bundle in `ste-kernel`.

---

## Conformance scope

**STE integration conformance** (interoperability with the Architecture IR path and
`ste-kernel`) **MUST** treat merge precedence, canonical serialization (JCS), and
compiled-array ordering as **fixed** by the kernel-owned IR contract—not as a
workspace-local or application-local preference.

**Workspace adoption** (how fully a team uses CEM, Cursor rules, or divergence
discipline) is separate: it **MUST NOT** be described as relaxing or replacing those
integration-plane MUSTs. A product **MAY** use different internal graphs for its own
purposes; it **MUST NOT** claim **STE kernel integration interoperability** if it alters
merge order, omits required adapters, or replaces canonical serialization rules
defined by the IR bundle.

---

## Pinning Architecture IR identity

Authoritative **`ir_version`** and **`schema_id`** values and co-required bundle paths
are recorded for human and CI drift checks in
`contracts/architecture-ir-kernel-contract-pin.json` (update when `ste-kernel` bumps
the bundle). Mechanical rules remain in `ste-kernel` as referenced below.

---

## Normative Requirements

### Deterministic compilation

**MUST:** Given the same adapter fragment inputs, adapter contract versions, and
merge configuration, `ste-kernel` MUST produce the same merged logical graph
prior to admission-only overlays.

### Canonical serialization

**MUST:** Canonical JSON serialization and hashing for IR identity MUST follow
**RFC 8785 (JCS)** over UTF-8 as required by the Architecture IR contract.

### Canonical IR identity

**MUST:** Entity and relationship `id` values and `document_id` MUST be derived
per the identity policy in the Architecture IR contract. **`assembled_at` MUST
NOT** double as a freshness or provenance authority.

### Stable merge order

**MUST:** Adapter merge precedence is **ADR → Spec → Runtime → Rules** (see
`ste-kernel/architecture-ir/architecture-ir.yaml`).

**MUST:** Compiled entity and relationship arrays MUST be sorted by `id` in
UTF-8 byte order where required by the IR contract.

### Non-inputs

**MUST NOT** affect canonical IR identity or `irSnapshot` inputs:

- wall clock time (except where explicitly recorded as non-identity metadata)
- random values
- process identifiers
- locale or timezone
- unordered filesystem enumeration where the contract fixes deterministic ordering instead

### Relationship to evidence and admission

**MUST:** `ArchitectureEvidence` freshness and bundle health inform admission
**projection** only; they MUST NOT redefine IR identity.

**MUST:** `KernelAdmissionAssessment` outcomes MAY vary with policy while IR
identity remains stable for fixed inputs.

---

## Referenced specifications

- `ste-kernel/documentation/ARCHITECTURE_IR.md`
- `ste-kernel/documentation/BOOT_SEQUENCE.md`
- `glossary.md` (terminology)

## Canon Status

This file is **canonical** for integration-plane determinism requirements in
`ste-spec`.
