# Architecture IR — mechanical bundle and spec fragments (canonical)

This directory holds the **normative Architecture IR mechanical bundle** for
`Compiled_IR_Document` (`architecture-ir.schema.json`, `architecture-ir.yaml`,
split `entities/` and `relationships/` definitions, and `ARCHITECTURE_IR.md`),
plus **spec IR fragments** published from `ste-spec`.

## On-disk serialization

For reviewability and stable diffs, JSON in this directory is stored as:

- **UTF-8** encoding  
- **LF** newlines  
- **Indented** with **2 spaces**  
- **No** minified single-line blobs  

Fragment records carry their own `content_hash` values in `provenance.derivation_chain[]`; those hashes describe the **logical fragment payload** at publication time, not an undocumented alternate serialization of this file. If a verifier hashes the **entire file bytes**, it **MUST** use this on-disk convention or define an explicit canonicalization step.

## Files

- `architecture-ir.schema.json` — JSON Schema for `Compiled_IR_Document`.
- `architecture-ir.yaml` — merge and identity YAML bundle.
- `ARCHITECTURE_IR.md` — mechanical specification narrative.
- `entities/` and `relationships/` — split schema bundle inputs maintained with the YAML contract.
- `spec-ir-fragments.json` — array of spec IR fragment objects (components, invariants, relations).

`spec-ir-fragments.json` is a deterministic adapter input artifact for
`ste-kernel` merge. It is **not** a schema for a second fragment envelope and it
does not make `ste-spec` the compiler of merged IR.

See also [`../README.md`](../README.md) for contract layout across `contracts/`.
