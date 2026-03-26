# Architecture IR mechanical specification (`ste-spec`)

## Purpose

The Architecture IR is the single canonical graph `ste-kernel` merges and validates after deterministic adapter publication.
It is a compiled artifact contract, not an alternate authoring surface. Canonical
architecture state still lives in repository artifacts such as ADRs, invariants,
manifests, rules, and schemas. The IR is the deterministic merge product of
external adapters:

- `ADRAdapter` from `adr-architecture-kit`
- `SpecAdapter` from `ste-spec`
- `RuntimeAdapter` from `ste-runtime`
- `RulesAdapter` from `ste-rules-library`

The kernel must not treat graph projections or other derived state as
authoritative.

## Authority and Decision References

ADRs are the decision authority for Architecture IR layering, provenance, and
conformance boundaries. This document explains the mechanical contract for kernel implementers and integrators. Normative authority for the bundle lives in `ste-spec` (`contracts/architecture-ir/`); `ste-kernel` consumes this contract.

- `ADR-L-0008`
- `ADR-L-0009`
- `ADR-L-0010`
- `ADR-L-0011`
- `ADR-L-0012`

## Execution Gate

The Architecture IR is not complete unless the following three artifacts remain
aligned:

- `architecture-ir.schema.json` (this directory)
- `architecture-ir.yaml` (this directory)
- `ARCHITECTURE_IR.md` (this file)

No downstream implementation work is complete until this gate is satisfied.

## Deterministic Hardening Addendum

### 1. Identity specification

Every entity and relationship id is produced by a documented pure function over
normalized adapter inputs. The `namespace` value is required in every
`payload_for_id` definition. IDs must be stable across recompilation of identical
inputs and must not depend on `ir_version` or `assembled_at`.

Normalization rules:

- Strings are UTF-8.
- Trim surrounding whitespace before hashing.
- Lowercase only fields whose local rule explicitly requires it, such as
  `capability.slug`.
- Composite payloads are serialized with RFC 8785 JSON Canonicalization Scheme.
- Relationship payloads include `namespace`, `type`, `from_id`, and `to_id`.

ID families:

- `capability:{slug-or-hash}`
- `decision:{adr_id-or-decision_key}`
- `component:{name-or-hash}`
- `invariant:{invariant_key-or-hash}`
- `rule:{rule_id}:{version}` or a stable hash equivalent
- `evidence:{evidence_type}:{payload_hash}`
- `rel:{type}:{from_id}:{to_id}` or a stable hash equivalent when needed

#### Canonical `payload_for_id` definitions

Entity and relationship IDs use these canonical identity payloads before
prefixing or hashing:

| Kind | `payload_for_id` fields | Normalization and precedence |
| --- | --- | --- |
| `capability` | `namespace`, `slug` | `slug` trimmed, lowercased, UTF-8; if an upstream source cannot supply a stable slug, hash `{ namespace, title, description }` after trimming each field |
| `decision` | `namespace`, `adr_id` or fallback `decision_key` | Use `adr_id` when present; fallback to `decision_key` only when `adr_id` is absent; both trimmed, UTF-8, case preserved except any upstream canonical ADR casing rule |
| `component` | `namespace`, `name`, `type` | Trim fields, preserve case for `name`, lowercase `type` only if upstream contract requires it |
| `invariant` | `namespace`, `invariant_key` or fallback normalized statement object | Prefer `invariant_key`; fallback hash uses `{ namespace, statement, scope, enforcement_level, enforcement_mechanism, verification_method }` |
| `rule` | `namespace`, `rule_id`, `version` | Trim all fields; preserve case unless the producer contract explicitly narrows it |
| `evidence` | `namespace`, `evidence_type`, `payload_ref` | `payload_ref` is the canonical content hash of normalized evidence source material |
| Relationship | `namespace`, `type`, `from_id`, `to_id` | `metadata` never participates in identity in `0.1.0` |

#### Hash and prefix rules

- Hash family is `sha256`, rendered as 64 lowercase hex characters.
- Hash inputs are RFC 8785 JCS canonical JSON encoded as UTF-8 bytes.
- Prefixes are semantic and stable:
  - `capability:`
  - `decision:`
  - `component:`
  - `invariant:`
  - `rule:`
  - `evidence:`
  - `rel:`
- When a human-readable stable key exists, the prefixed identifier may embed that
  key directly instead of an opaque hash, provided it still derives from the
  canonical payload above and remains unique within `namespace`.

### 2. Canonical serialization

Canonical serialization is part of the kernel IR contract. All hashing uses RFC
8785 JCS over UTF-8. There is no alternate serializer.

Rules:

- Canonical bytes are UTF-8 only.
- Object keys are canonically ordered by JCS.
- Compiled entity arrays are sorted by `id` in UTF-8 byte order.
- Compiled relationship arrays are sorted by `id` in UTF-8 byte order.
- File-system enumeration order must never affect the compiled output.
- Booleans and numbers use canonical JSON formatting only.
- Optional keys are omitted rather than populated with `null`.
- Forbidden `null` values fail validation; they are not silently normalized at
  merge time.
- `document_id` hashes the full document graph plus required envelope fields,
  excluding `document_id` and `assembled_at`.
- `canonicalHash` is `sha256(canonicalBytes)`.
- Root `extensions` are omitted entirely while the allowlist is empty.

### 3. Merge contract

Adapter precedence is fixed:

1. ADR
2. Spec
3. Runtime
4. Rules

Conflict handling:

- Deduplicate strictly by `id`.
- Same `id` plus identical normalized record content is allowed and coalesced
  deterministically.
- Same `id` plus different content from a lower-precedence adapter is resolved by
  first-defined-wins in precedence order.
- Same `id` plus different content at the same precedence is a hard failure.
- Same `id` plus different record kind or relationship category is a hard
  failure.
- Replace arrays atomically unless a future schema version documents a finer rule.
- Fail merge when any incoming entity or relationship record omits `provenance`.
- Conflicting provenance for the same surviving field is a hard failure unless
  resolved by the same explicit precedence rule.
- Resolve freshness conflicts with the same precedence rule. No ad hoc tie-breaks.

Merged provenance behavior:

- Single-contributor records may pass through source provenance unchanged.
- Multi-contributor records use `source.adapter: kernel_merge`.
- `derivation_chain` concatenates contributor chains in deterministic adapter and
  step order.
- `last_updated` is the maximum contributor instant, serialized as RFC 3339 UTC
  with millisecond precision and trailing `Z`.

### 4. Required graph invariants

Validators must fail, not warn, when any of the following are violated:

- Every `decision` has at least one `decision_supports_capability` edge.
- Every `component` has at least one `component_implements_decision` edge.
- Every `evidence` has at least one `evidence_supports_component` edge.

### 5. Provenance rules

`provenance` is required on every entity and every relationship.

`derivation_chain` rules:

- Steps are contiguous from `0` to `n - 1`.
- `step` equals the array index.
- `content_hash` is the JCS hash of the immediate adapter source fragment.
- `adapter_schema_version` records the producer-side contract version.

### 6. Schema strictness and extensions

- Root schema is closed with `additionalProperties: false`.
- Every entity and relationship record is closed with
  `additionalProperties: false`.
- Root `extensions` are disabled in `0.1.0` because
  `architecture-ir.yaml` sets `extension_allowlist: []`.
- A future version may add `extensions` only when the allowlist is non-empty and
  the schema defines every allowed key's shape.
- Extensions must never alter `id`, `kind`, merge semantics, or graph invariants.

## Envelope

The compiled document requires:

- `ir_version`
- `schema_id`
- `document_id`
- `assembled_at`
- `namespace`
- `entities`
- `relationships`

`assembled_at` is informational and must not be reused as freshness or
provenance state.

## Entity kinds

### `capability`

Represents an externally meaningful ability or architectural outcome.

Required fields:

- `id`
- `kind: capability`
- `slug`
- `title`
- `description`
- `status`
- `provenance`

### `decision`

Represents a recorded architecture decision, usually ADR-backed.

Required fields:

- `id`
- `kind: decision`
- `status`
- `authority_tier`
- `summary`
- `provenance`

Optional fields:

- `adr_id`
- `decision_key`
- `supersedes`
- `validation_profile`

Identity rule:

- At least one of `adr_id` or `decision_key` is required.
- When both are present, `adr_id` is the primary identity source and
  `decision_key` is an additional stable locator.
- `id` must be derived from `namespace + adr_id` when `adr_id` exists, otherwise
  from `namespace + decision_key`.

### `component`

Represents a deployable or logical building block.

Required fields:

- `id`
- `kind: component`
- `name`
- `type`
- `provenance`

Optional fields:

- `boundary`
- `owners`
- `external_refs`

### `invariant`

Represents a normative architecture constraint.

Required fields:

- `id`
- `kind: invariant`
- `invariant_key`
- `statement`
- `scope`
- `enforcement_level`
- `enforcement_mechanism`
- `verification_method`
- `provenance`

### `rule`

Represents an executable governance rule.

Required fields:

- `id`
- `kind: rule`
- `rule_id`
- `rule_pack_id`
- `version`
- `severity`
- `provenance`

Optional fields:

- `applies_when`

### `evidence`

Represents an observable artifact or measurement supporting truth claims.

Required fields:

- `id`
- `kind: evidence`
- `evidence_type`
- `payload_ref`
- `summary`
- `freshness`
- `provenance`

`freshness` contains:

- `freshness_class`
- `observed_at`
- optional `last_reconciled`

## Relationship kinds

The Architecture IR fixes exactly five relationship types:

- `decision_supports_capability`
- `component_implements_decision`
- `invariant_constrains_component`
- `rule_evaluates_decision`
- `evidence_supports_component`

Each relationship record requires:

- `id`
- `type`
- `from_id`
- `to_id`
- `provenance`

Optional `metadata` may contain non-null scalar, object, or array values.

## Adapter mapping rules

### ADR to IR

- ADR decisions map to `decision`.
- ADR-expressed capabilities map to `capability`.
- ADR-described logical or physical building blocks map to `component`.
- ADR invariants map to `invariant`.
- Decision identity uses `adr_id` first when present; `decision_key` is only a
  fallback when ADR material lacks a stable ADR identifier.
- ADR relationship registry values project into the fixed kernel edge set:

| adr-kit relationship type | IR edge |
| --- | --- |
| `supports` | `decision_supports_capability` when source is a decision and target is a capability |
| `implemented_by` | `component_implements_decision` with direction normalized to component -> decision |
| `constrains` | `invariant_constrains_component` |
| `evaluates` | `rule_evaluates_decision` |
| `supports_component` | `evidence_supports_component` |

If adr-kit emits a richer type vocabulary, the adapter must collapse or expand it
deterministically into one of the five IR edges above.

### Runtime to IR

- Runtime evidence snapshots map to `evidence`.
- Runtime bundle freshness maps to `evidence.freshness`.
- Runtime component references map to `component` and
  `evidence_supports_component`.
- Existing `src/admission/types.ts` runtime evidence types are downstream views,
  not canonical state.

Deterministic runtime rules:

- `payload_ref` is `sha256:` plus the lowercase hex hash of the normalized
  runtime evidence payload serialized with RFC 8785 JCS over UTF-8.
- If the runtime source already includes a canonical content hash with equivalent
  semantics, adapters may reuse it only when it exactly matches this rule.
- `observed_at` is required in compiled IR. When the runtime source omits it, the
  adapter must use deterministic assembly time for the fragment and record the
  fallback operation in `provenance.derivation_chain`.
- If runtime evidence names concrete components, emit one
  `evidence_supports_component` relationship per referenced component.
- If runtime evidence is bundle-level only, bind the evidence to the namespace
  singleton `component:architecture_graph` so component linkage remains
  deterministic and explicit rather than implied.

### Spec to IR

- Normative schemas and catalogs map primarily to `invariant`.
- Spec-owned executable checks may map to `rule`.
- Spec-defined architecture elements may map to `component` or `capability`.
- When Spec and ADR both describe the same record id, ADR wins by precedence.

Ownership and precedence rule:

- Spec owns normalized architecture data and enforcement metadata.
- Rules-library owns executable governance checks when rule execution semantics
  originate in `ste-rules-library`.
- If Spec describes policy data but not execution behavior, map to `invariant`
  rather than `rule`.
- If both Spec and Rules contribute the same `rule` id, Rules wins for executable
  semantics and Spec may only contribute supplementary metadata through
  deterministic merge precedence.

### Rules to IR

- Rules-library manifests map to `rule`.
- Rules target decisions through `rule_evaluates_decision`.
- Component-targeting governance must still anchor through decisions or
  invariants until a future schema version introduces another edge type.

## Minimal compiled example

```yaml
ir_version: "0.1.0"
schema_id: "https://ste-kernel.local/schema/architecture-ir/0.1.0/architecture-ir.schema.json"
document_id: "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
assembled_at: "2026-03-20T12:00:00.000Z"
namespace: "repo:ste-kernel:branch:main"
entities:
  capabilities:
    - id: "capability:normalized-arch-graph"
      kind: capability
      slug: "normalized-arch-graph"
      title: "Normalized architecture graph"
      description: "A canonical graph the kernel can reason over."
      status: accepted
      provenance: &p
        source:
          adapter: adr
          artifact_uri: "repo://ste-kernel/adrs/logical/ADR-L-0008"
          artifact_kind: "adr"
        last_updated: "2026-03-20T12:00:00.000Z"
        derivation_chain:
          - step: 0
            adapter: adr
            operation: "parse_manifest"
            input_ref: "repo://ste-kernel/adrs/manifest.yaml"
            adapter_schema_version: "1.0.0"
            content_hash: "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  decisions:
    - id: "decision:ADR-L-0008"
      kind: decision
      adr_id: "ADR-L-0008"
      decision_key: "kernel-ir-layering-and-explicit-consumption"
      status: promoted
      authority_tier: promoted
      summary: "Use a kernel-normalized architecture IR."
      provenance: *p
  components:
    - id: "component:ste-kernel"
      kind: component
      name: "ste-kernel"
      type: service
      provenance: *p
  invariants:
    - id: "invariant:ir-authority"
      kind: invariant
      invariant_key: "ir-authority"
      statement: "Kernel reasoning consumes compiled IR, not raw sibling repo state."
      scope: "global"
      enforcement_level: must
      enforcement_mechanism: runtime
      verification_method: automated
      provenance: *p
  rules:
    - id: "rule:admission-profile:1.0.0"
      kind: rule
      rule_id: "admission-profile"
      rule_pack_id: "ste-rules-library/core"
      version: "1.0.0"
      severity: warning
      provenance: *p
  evidences:
    - id: "evidence:runtime_architecture_bundle:abc123"
      kind: evidence
      evidence_type: runtime_architecture_bundle
      payload_ref: "sha256:abc123"
      summary: "Current runtime architecture bundle."
      freshness:
        freshness_class: current
        observed_at: "2026-03-20T11:59:00.000Z"
      provenance: *p
relationships:
  decision_supports_capability:
    - id: "rel:decision_supports_capability:ADR-L-0008:normalized-arch-graph"
      type: decision_supports_capability
      from_id: "decision:ADR-L-0008"
      to_id: "capability:normalized-arch-graph"
      provenance: *p
  component_implements_decision:
    - id: "rel:component_implements_decision:ste-kernel:ADR-L-0008"
      type: component_implements_decision
      from_id: "component:ste-kernel"
      to_id: "decision:ADR-L-0008"
      provenance: *p
  invariant_constrains_component:
    - id: "rel:invariant_constrains_component:ir-authority:ste-kernel"
      type: invariant_constrains_component
      from_id: "invariant:ir-authority"
      to_id: "component:ste-kernel"
      provenance: *p
  rule_evaluates_decision:
    - id: "rel:rule_evaluates_decision:admission-profile:ADR-L-0008"
      type: rule_evaluates_decision
      from_id: "rule:admission-profile:1.0.0"
      to_id: "decision:ADR-L-0008"
      provenance: *p
  evidence_supports_component:
    - id: "rel:evidence_supports_component:abc123:ste-kernel"
      type: evidence_supports_component
      from_id: "evidence:runtime_architecture_bundle:abc123"
      to_id: "component:ste-kernel"
      provenance: *p
```

## Validation expectations

Schema validation must reject:

- unknown root or record properties
- missing `provenance`
- `null` values anywhere in the document
- invalid id prefixes or malformed `document_id`

Additional validators must reject:

- out-of-order or gapped `derivation_chain.step` values
- duplicate ids inside any entity or relationship array
- required graph invariant failures
- unsorted compiled arrays
- a `decision` that contains neither `adr_id` nor `decision_key`
- root `extensions` when `extension_allowlist` is empty

## Post-Compilation Assessment

Compiled IR diff, drift classification, EDR scoring, and architecture assessment
reports are downstream kernel analysis layers. They do not alter fragment
formats, merge semantics, canonical serialization, or admission contracts.

Rules:

- Compiled IR diff compares canonical compiled documents only.
- Diff never treats source file formatting or `assembled_at` as semantic change.
- Drift classification operates over a validated compiled document, an
  ADR-preferred intended baseline derived from that document, and
  `ArchitectureEvidence`.
- EDR scoring is deterministic, integer-only, and derived from explicit kernel
  rules rather than heuristic inference.
- Reports may embed admission, but they must reuse existing admission logic
  rather than reinterpret policy at the assessment layer.

## Maintenance

There is currently no schema generator in `ste-kernel`; the schema is manually
maintained. If a generator is introduced later, schema descriptions and this
document must remain aligned.

