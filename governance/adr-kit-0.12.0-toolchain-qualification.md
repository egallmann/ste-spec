# ADR-Kit 0.12.0 toolchain qualification

Operational evidence for Tranche 1 of the ste-spec rebaseline. This note is not
architectural authority. It does not change ADR meaning, identity, or schema.

Basis: `feature/ste-semantic-rebaseline-design-journal` at
`e21b8409f09d01be419db09d979ce924a92e3777`.

## Tooling

- Pin: `adr-architecture-kit==0.12.0` in `requirements-dev.txt`.
- Installed from the published wheel `adr_architecture_kit-0.12.0-py3-none-any.whl`.
- `adr, version 0.12.0`.
- Interpreter: Python 3.14.7, isolated virtual environment outside this
  repository. The environment's previous editable ADR-Kit 0.11.1 checkout was
  not used.
- The local dirty ADR-Kit worktree was not the qualification basis. Git tag
  `v0.12.0` still peels to `bfe24ef159132d18fb8896d43febae6a7c1471f9`.

## Commands and results

`python scripts/adr_governance.py` under the 0.12.0 environment:

| Step | Result |
| --- | --- |
| `adr validate-project-metadata --scope .` | exit success; `PROJECT.yaml valid` |
| `adr validate --scope . --cross-references --mode complete` | `All 40 files valid`; `Cross-references valid` |
| `adr validate-generated-docs --scope .` before regeneration | projections `source_hash_mismatch`; manifest, architecture graph, and entity registry `hashes_match` |
| `adr compile --scope . --emit registries,manifest,markdown --timestamp 2026-05-30T18:44:57Z --mode normal` | success; deprecation warning that `adr compile` is not the runtime compiler of record |
| `adr validate-generated-docs --scope .` after regeneration | hashes match |
| `scripts/run_local_contract_checks.py` | 0 broken internal links; 24 pytest passed |

The second full governance run exited 0.

## Source proof

- Logical ADR count: 40.
- Schema histogram: `{1.3: 40}`.
- Logical source tree hash, unchanged from before the pin:
  `7c346a547d1b64cf680b6e5fae412d67fa09966f280e32bc623c233b0dc6f2c5`.
- `PROJECT.yaml` was not edited. Metadata validation accepted
  `project.type: specification`.

## Generated-artifact classification

Harmless toolchain projection churn. No canonical ADR field changed.

- Forty markdown projections: integrity `source_hash` / `rendered_hash` refreshed;
  metadata lines use `<br>` instead of trailing spaces; the embedded
  `Relationship graph` and `Related ADRs` sections are omitted. After removing
  those sections and the line-break markup, each ADR's own context, decisions,
  invariants, and gaps match the previous projection.
- `adrs/index/decision-registry.yaml` (104 entities),
  `adrs/index/entity-registry.yaml` (215), and
  `adrs/index/invariant-registry.yaml` (71): same ids and same core fields.
  The only addition is seven empty relationship slots:
  `consumes_interface`, `depends_on`, `calls`, `publishes_to`,
  `subscribes_to`, `reads_from`, `writes_to`. None of those slots contain edges.
- Manifest, architecture graph, and `adrs/entities/registry.yaml` were already
  fresh and were not rewritten.

`adr compile` also wrote an untracked `SYSTEM-OVERVIEW.md`. That file was not
previously committed. It was removed and is not part of this qualification
commit, because it is a new overview document rather than a refresh of an
existing derived surface.

Internal markdown link targets fell from 645 to 383 after the related-ADR
embeds were omitted. The link check still reports 0 broken targets.

## Gate 1 runtime alignment

The published ADR-Kit 0.12.0 package declares `Requires-Python: >=3.14`.
Local qualification used Python 3.14.7. During Gate 1 cleanup,
`.github/workflows/adr-governance.yml` was changed from Python 3.13 to the
3.14 line so the automated governance job can install that pin. Triggers,
checkout, `requirements-dev.txt` installation, and
`python scripts/adr_governance.py` were left unchanged.
