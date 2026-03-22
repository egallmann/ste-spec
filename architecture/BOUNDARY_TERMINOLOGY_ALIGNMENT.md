# Boundary Terminology Alignment

This artifact aligns recommended architecture terminology for the open-core
versus closed-intelligence boundary. It does **not** force code renames in this
tranche.

| Existing / variant term | Recommended alignment | Boundary note |
|-------------------------|-----------------------|---------------|
| Rules Engine | Invariant Engine when the meaning is normative constraint execution | Preserve `rules-engine` where the repo means operational rule projection or catalog materialization. |
| Activation Engine | Semantic Activation Engine | Preferred when referring to intelligence-bearing activation behavior. |
| Projection Engine | Constraint Projection Engine | Preferred when referring to private projection behavior shaped by constraints. |
| Steelman Engine | Adversarial Reasoning Engine | Preferred when referring to challenge or steelman behavior as a private reasoning layer. |
| Kernel | Deterministic Validation Kernel | Preferred when emphasizing deterministic validation and admission behavior. |
| Conversation Engine | Architecture Compiler or Conversation Compiler | Preferred when referring to compiler-like internal reasoning preparation. |
| RECON | Extraction Compiler | Alignment note only; preserve `RECON` where it is already canonical in STE doctrine. |
| Architecture IR | Architecture Intermediate Representation | Canonical term remains unchanged. |

## Usage Note

Where current documents already use a stronger or canonical established term,
treat the alignment above as a recommendation for future architectural writing,
not as a mandatory immediate replacement.
