# Public System Surfaces

## Purpose

This document inventories the public-compatible STE surfaces that external users
and compatible implementations may rely on.

It lists only surfaces that are safe to rely on as public schema, interface,
protocol, artifact-format, or runtime contracts. When a subsystem is
intelligence-bearing, this document references only its public interface layer.

## Public-Compatible Surface Inventory

| Name | Purpose | Status | Canonical inputs | Canonical outputs | Stability expectation | Classification |
|------|---------|--------|------------------|-------------------|-----------------------|----------------|
| ADR schema and templates | Structure architecture intent and ADR-authored records | Public | ADR author inputs, template fields, schema constraints | Valid ADR artifacts and related authoring records | Stable with versioned schema evolution | Schema |
| ADR-derived publication artifacts | Publish deterministic registries, manifests, indexes, and ADR-derived kernel inputs | Public | ADR corpora and invariant/decision declarations | Registries, manifests, architecture index, ADR-derived IR fragments | Stable publication surface, versioned by artifact/schema evolution | Artifact format |
| Architecture IR semantic specification | Define semantic ontology for entities, relationships, provenance, lifecycle, completeness, governance, evidence, gaps, overrides, remediation, and Architecture Index | Public | Published semantic definitions in `ste-spec` | Semantic compatibility contract | Stable semantic authority; changes require explicit spec updates | Schema |
| Architecture IR mechanical contract reference | Reference pinned compiled-document shape and version owned by `ste-kernel` | Public reference, interface-only | Pinned `ir_version`, referenced schema identifier | Mechanical contract identity and compatibility boundary | Stable by explicit pin; implementation owned outside `ste-spec` | Interface |
| Semantic graph entities and relationships | Provide public model terms for machine-oriented architecture state | Public | Declared architecture artifacts and semantic normalization rules | Published entities, relationships, and registries | Stable at the semantic layer; compiled realizations may be version-pinned | Artifact format |
| Decorators and explicit intent markers | Mark implementation or authored material with explicit architectural intent where published | Public where declared | Source annotations or declared intent markers | Explicit intent-bearing metadata or extracted artifacts | Stable only where already published as declared surfaces | Interface |
| Invariant definitions | Declare normative constraints and cross-component rules | Public | Normative doctrine, handoff invariants, declared rule text | Invariant artifacts and invariant references | Stable and versioned as normative doctrine | Artifact format |
| Rule declaration formats | Declare rule artifacts and rule metadata used for governance and evaluation | Public | Rule authoring inputs and published rule catalogs | Rule definitions, identifiers, manifests, or fragments | Stable where published; governance activation remains draft where marked | Artifact format |
| Rule evaluation result surfaces | Expose result envelopes or projected rule outputs where explicitly published | Draft / interface-only | Published rule material, projected evaluation input | Result envelopes, identifiers, attested projections where applicable | Draft where currently marked pre-normative; kernel rule evaluation may still be normative without promoting these envelopes | Interface |
| Kernel validation outputs | Publish deterministic validation or admission result contracts | Public | Validated booted integration-state and evidence inputs | Kernel validation output and `KernelAdmissionAssessment` | Stable contract surface once published | Runtime surface |
| ArchitectureEvidence / evidence schema | Define factual runtime evidence consumed by kernel evaluation | Public | Observed runtime/tooling state and evidence-producing systems | `ArchitectureEvidence` payloads | Stable contract surface | Schema |
| EDR-related schema surfaces | Describe extracted or observed embodiment records where architecture artifacts explicitly publish them | Draft / interface-only | Observed embodiment or extracted design material | EDR-shaped records or evidence artifacts where declared | Public only if explicitly published; otherwise draft or internal | Artifact format |
| Provider proposal schema surfaces | Structure external/provider-submitted proposal envelopes where architecture artifacts define them | Draft / interface-only | Provider proposal metadata, signatures, proposed changes | Proposal envelopes and validation-ready records | Draft until promoted into normative published contracts | Protocol |

## Notes

- Public compatibility depends on the declared surface, not on hidden internal
  implementation strategy.
- Draft governance and projection artifacts remain draft even if they are named
  here.
- When a surface is listed as interface-only, consumers may rely on the declared
  envelope or lifecycle role but not on private decision logic behind it.

## Canon Status

This file is canonical for the inventory of public-compatible STE system
surfaces.
