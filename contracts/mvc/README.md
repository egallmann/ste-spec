# MVC contracts (draft)

**Status:** Draft / pre-normative. This folder sketches MVC-D, MVC-S, and MVC-M
contracts for MVC evolution experiments. Until promoted by ADR and indexed in
the cross-component contract inventory, consumers must not treat these shapes
as stable interchange.

MVC is a task-scoped architectural reality bundle: the smallest faithful
representation of the portion of modeled architectural reality required to
answer a declared question.

- MVC-D is the declarative admissible context definition.
- MVC-S is the deterministic candidate task-relevant architectural reality
  surface prior to admission.
- MVC-M is the admitted, bounded, materialized architectural reality surface.

Runtime may produce factual candidate surfaces and bundles. Kernel owns
caller-facing admission.

## Files

- `mvc-definition.schema.json` - draft schema for MVC-D.
- `mvc-snapshot.schema.json` - draft schema for MVC-S.
- `mvc-materialization-result.schema.json` - draft schema for MVC-M.

## Related

- `contracts/context-domain/`
- `contracts/graph-domain/`
- `contracts/linkage-surface/`
- `contracts/kernel-admission-assessment.schema.json`

## Conceptual background (handbook, not normative)

These draft schemas do not include research illustrations or experimental methodology.
For the MVC assembly pipeline diagram, representation-ceiling thesis, and research
program methodology, see the handbook research library in sibling repo `ste-handbook`:

- `ste-handbook/14-research/research/mvc/README.md` — canonical home for the assembly-pipeline illustration
- `ste-handbook/14-research/research/mvc/thesis/README.md` — thesis publication lineage
- `ste-handbook/14-research/research/mvc/thesis/mvc-representation-ceiling-thesis.md` — published thesis
