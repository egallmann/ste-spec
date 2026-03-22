# Architecture IR — spec fragments (canonical)

This directory holds **normative, canonical** JSON for STE **spec IR fragments** published from `ste-spec` (for example component and invariant nodes and their relations).

## On-disk serialization

For reviewability and stable diffs, JSON in this directory is stored as:

- **UTF-8** encoding  
- **LF** newlines  
- **Indented** with **2 spaces**  
- **No** minified single-line blobs  

Fragment records carry their own `content_hash` values in `provenance.derivation_chain[]`; those hashes describe the **logical fragment payload** at publication time, not an undocumented alternate serialization of this file. If a verifier hashes the **entire file bytes**, it **MUST** use this on-disk convention or define an explicit canonicalization step.

## Files

- `spec-ir-fragments.json` — array of spec IR fragment objects (components, invariants, relations).

See also [`../README.md`](../README.md) for contract layout across `contracts/`.
