# ADR Governance Baseline

> Operational measurement recorded for migration planning on 2026-08-29. This
> file is not an architectural authority artifact and does not change ADR
> meaning or identity.

## Tooling and scope

- Repository base: `a096e4e` (`origin/develop`).
- ADR Architecture Kit: `0.7.0`, the current tagged release used for this
  baseline.
- Canonical local entrypoint: `python scripts/adr_governance.py` after
  `python -m pip install -r requirements-dev.txt`.
- Generated-document freshness is intentionally excluded while the legacy
  `adrs/rendered/` projection layout remains in place.

## Unchanged corpus measurement

| Measure | Value |
| --- | ---: |
| Logical ADR source files | 39 |
| Source schema version | 39 at `1.0` |
| Accepted / proposed ADRs | 28 / 11 |
| Authored decisions | 94 |
| Authored invariants | 61 |
| Authored gaps | 41 |
| Authored constraints, capabilities, components, boundaries | 0 in logical sources |
| Generated manifest entities | 135 |
| Generated relationship-registry edges | 327 |

`adr validate --scope . --cross-references --mode complete` passed for all 39
files. The repository Markdown-link check passed with 329 path targets, and
the pytest suite passed with 24 tests.

`adr validate-project-metadata --scope .` fails closed because the v1.0
`PROJECT.yaml` value `project.type: specification` is not accepted by ADR-Kit
0.7.0's project-metadata model (`service`, `library`, `platform`, `system`, or
`tool`). This is a **LEGACY SCHEMA LIMITATION**; the corpus and the validator
were not weakened or edited to hide it.

## v1.3 identity-migration preflight

The official command completed in plan-only mode:

```text
adr migrate-identity-v13 --scope . --plan-out <ignored temporary path>
```

The candidate map is deliberately ignored and contains no tracked canonical
identity. It contains 194 entries: 39 ADRs, 94 decisions, and 61 invariants.
Every entry preserves its current alias as `alias_id`. The map is unsealed,
with no source-owner or external-provider queues and no unsupported-shape,
collision, or baseline-fingerprint diagnostic emitted by the successful
preflight.

The tool classifies 159 entries as mechanical and 35 as `review_required`.
All 35 are decision alias-name conflicts caused by the current sources'
non-unique decision presentation name. Their alias IDs are:

- `ADR-L-0021`: `DEC-2102`
- `ADR-L-0022`: `DEC-2201`, `DEC-2202`, `DEC-2203`
- `ADR-L-0023`: `DEC-2301`, `DEC-2302`, `DEC-2303`
- `ADR-L-0024`: `DEC-2401`, `DEC-2402`, `DEC-2403`
- `ADR-L-0025`: `DEC-2501`, `DEC-2503`
- `ADR-L-0026`: `DEC-2601`, `DEC-2602`, `DEC-2603`
- `ADR-L-0027`: `DEC-2701`, `DEC-2703`
- `ADR-L-0028`: `DEC-2801`, `DEC-2802`
- `ADR-L-0029`: `DEC-2901`, `DEC-2902`
- `ADR-L-0032`: `DEC-3201`
- `ADR-L-0034`: `DEC-3402`
- `ADR-L-0035`: `DEC-3501`
- `ADR-L-0036`: `DEC-3601`
- `ADR-L-0038`: `DEC-3801`, `DEC-3802`
- `ADR-L-0040`: `DEC-4001`, `DEC-4002`, `DEC-4003`
- `ADR-L-0041`: `DEC-4101`, `DEC-4102`
- `ADR-L-0042`: `DEC-4201`
- `ADR-L-0043`: `DEC-4301`, `DEC-4302`

Because those entries remain pending in the alias-conflicts judgment queue,
the map cannot be sealed or applied without reviewer decisions. Source
cross-references would be rewritten by the sealed-map apply operation; the
public preflight emits no separate rewrite total. The existing derived
relationship registry contains 327 edges, providing a later replay/parity
comparison baseline.
