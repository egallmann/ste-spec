# ste-spec ADR migration inventory

Authoritative legacy markdown for numbered ADRs: `adrs/published/`. Machine-canonical Logical ADRs: `adrs/logical/*.yaml`. Generated human projections: `adrs/rendered/*.md` and `adrs/manifest.yaml` (regenerate via **adr-architecture-kit**; do not hand-edit the manifest).

This inventory records the **ste-spec `adrs/published/` → machine ADR-L** migration. All numbered published ADRs listed below are migrated unless explicitly marked otherwise; regenerate projections with **adr-architecture-kit** (`adr compile`, graph emit) after YAML edits.

**Numeric IDs (ste-spec convention):** Legacy **`ADR-NNN`** (three-digit published number) maps to machine **`ADR-L-0NNN`** (four digits, zero-padded). Nested **DEC**, **INV**, and **GAP** ids on that ADR use an **`NNxx` block** where **`NN`** is the two-digit legacy index (e.g. ADR-006 → `DEC-0601`, `INV-0601`; ADR-001 → `DEC-0101`). The separate **ADR-L-1001–1009** kernel governance series uses unrelated blocks (`DEC-61xx`, `INV-50xx`, …). Do not allocate a single global DEC counter across unrelated ADRs. The **adr-architecture-kit** repo has its own **ADR-L-0001** (different scope); **ste-spec** validation only includes `ste-spec/adrs/`.

**Convergence (vs ADR-L-100x):** When a migrated `published/` ADR overlaps kernel governance semantics, record reconciliation in **`related_adrs`**, a short note in YAML **`context`**, and the table below (**Reconciliation vs ADR-L-100x**). Use one explicit outcome: **merge**, **supersede**, or **coexist-with-precedence**. Never resolve conflicts silently.

## Machine Logical ADRs already canonical in ste-spec

| Machine ADR ID | Title | Legacy published ID | Overlap / cross-links |
| --- | --- | --- | --- |
| ADR-L-0001 | Deterministic Extraction Over ML-Based Inference | **ADR-001** (migrated) | Uses `DEC-01xx` / `INV-01xx` / `GAP-01xx`. `related_adrs`: 0006–0009. |
| ADR-L-0006 | Explicit Unknowns Over Inference | **ADR-006** (migrated) | **coexist-with-precedence** vs ADR-L-100x; see YAML `context`. |
| ADR-L-0007 | Slice Identity Strategy | **ADR-007** (migrated) | **coexist-with-precedence** vs IR ontology; see YAML `context`. |
| ADR-L-0008 | Correctness and Consistency Contract | **ADR-008** (migrated) | **coexist-with-precedence** vs ADR-L-1006 / ADR-L-1009; `related_adrs` includes 0009. |
| ADR-L-0009 | Assertion Precedence Model | **ADR-009** (migrated) | **coexist-with-precedence** vs ADR-L-1002 / ADR-L-1009; see YAML `context`. |
| ADR-L-0019–0029 | Gateway / signing / trust / fail-closed / validation / contracts / environment / scope / Fabric boundary / enforcement authority | **ADR-019–029** (migrated) | **coexist-with-precedence** vs ADR-L-1002 / ADR-L-1009 where noted; ADR-L-0023 **merges** timing with ADR-L-0026 on conflict verification. |
| ADR-L-0030 | Contract Authority in ste-spec | **ADR-030** (migrated) | **coexist-with-precedence** vs ADR-L-1002. |
| ADR-L-0031 | Runtime and Kernel Responsibility Boundary | **ADR-031** (migrated) | **merge** with ADR-L-1001 / ADR-L-1002 themes; `related_adrs` wired. |
| ADR-L-0032 | Fail-Closed Enforcement Model | **ADR-032** (migrated) | **merge** with ADR-L-1009; **coexist-with-precedence** vs ADR-L-0022 (STE Gateway story). |
| ADR-L-0033 | Closed-Object Discipline | **ADR-033** (migrated) | **coexist-with-precedence** vs ADR-L-1002. |
| ADR-L-0034 | Rule Projection Envelope Authority | **ADR-034** (migrated, proposed) | **coexist-with-precedence** vs ADR-L-1008. |
| ADR-L-0035 | Architecture IR Ontology Authority | **ADR-035** (migrated) | **coexist-with-precedence** vs ADR-L-1006. |
| ADR-L-0036 | Repository README Contract | **ADR-036** (migrated) | **coexist-with-precedence** vs ADR-L-100x (orthogonal README governance). |
| ADR-L-0037 | Repository README Conformance | **ADR-037** (migrated) | Same as ADR-L-0036. |
| ADR-L-0038 | Artifact Taxonomy and Versioning Posture | **ADR-038** (migrated) | **coexist-with-precedence** vs ADR-L-1003 / ADR-L-1007. |
| ADR-L-0039 | Structured Diagram Format (Mermaid) | **ADR-039** (migrated) | **coexist-with-precedence** vs ADR-L-0040 (Spine vs diagram format). |
| ADR-L-0040 | STE Spine Lifecycle and Authority | **ADR-040** (migrated) | **coexist-with-precedence** vs ADR-L-1001–1009; end-to-end Spine model. |
| ADR-L-0041 | Compiler, Evidence, and Merge Authority | **ADR-041** (migrated) | **coexist-with-precedence** vs ADR-L-1004 / ADR-L-1005. |
| ADR-L-0042 | Open Standards and Closed Intelligence Boundary | **`ARCHITECTURE_BOUNDARY_DECISION.md`** (migrated) | Non-numbered legacy note; see `architecture/OPEN_CLOSED_BOUNDARY.md` prose. |
| ADR-L-1001 | Architecture Action Model | — | `related_adrs`: **ADR-L-0031**, **ADR-L-0040**, 1002, 1009. |
| ADR-L-1002 | Architecture Admission Model | — | Admission / allow-deny semantics. |
| ADR-L-1003 | Governance Posture State Model | — | Posture / golden / experimental. |
| ADR-L-1004 | Architecture Freshness Model | — | Freshness semantics for documentation-state. |
| ADR-L-1005 | Architecture Drift Model | — | Drift vs normative architecture. |
| ADR-L-1006 | Evidence Authority Model | — | Evidence vs normative IR. |
| ADR-L-1007 | Golden System Model | — | Golden system posture. |
| ADR-L-1008 | Decision Outcome Model | — | Decision outcomes vocabulary. |
| ADR-L-1009 | Kernel Decision Contract | — | `related_adrs`: **ADR-L-0031**, **ADR-L-0032**, 1001, 1002, 1008. |

**Overlap rule of thumb:** For each overlap above, reconciliation is explicit in YAML **`context`** and/or **`related_adrs`**. Prefer **coexist-with-precedence** unless a **merge** statement is documented (for example ADR-L-0031 vs ADR-L-1001, ADR-L-0032 vs ADR-L-1009, ADR-L-0023 vs ADR-L-0026).

## Legacy `adrs/published/` migration table

| Markdown ADR ID | Title (short) | Classification | Target machine ADR id | Reconciliation vs ADR-L-100x | Notes |
| --- | --- | --- | --- | --- | --- |
| ADR-001 | Deterministic extraction | ADR-L | **ADR-L-0001** | *N/A* (extraction doctrine) | **Done.** |
| ADR-006 | Explicit unknowns | ADR-L | **ADR-L-0006** | **coexist-with-precedence** — complements ADR-L-1005 (drift) / evidence models; unknowns are extraction documentation-state, not kernel admission. | **Done.** |
| ADR-007 | Slice identity strategy | ADR-L | **ADR-L-0007** | **coexist-with-precedence** — identity for slices vs IR identity rules in contracts; no merge required unless duplicate invariant is found. | **Done.** |
| ADR-008 | Correctness / consistency contract | ADR-L | **ADR-L-0008** | **coexist-with-precedence** — query/consistency semantics overlap themes with ADR-L-1006 (evidence) / ADR-L-1009 (contracts); ste-spec truth model for Fabric queries. | **Done.** |
| ADR-009 | Assertion precedence model | ADR-L | **ADR-L-0009** | **coexist-with-precedence** — ADR-L-1002 / ADR-L-1009 at kernel boundary. | **Done.** |
| ADR-019 | Gateway authority and signing | ADR-L | **ADR-L-0019** | **coexist-with-precedence** — ADR-L-1002 / ADR-L-1009. | **Done.** |
| ADR-020 | ORG-level signing scope | ADR-L | **ADR-L-0020** | **coexist-with-precedence** — ADR-L-1009. | **Done.** |
| ADR-021 | Gateway trust verification | ADR-L | **ADR-L-0021** | **coexist-with-precedence** — ADR-L-1009. | **Done.** |
| ADR-022 | Fail-closed enforcement scope | ADR-L | **ADR-L-0022** | **coexist-with-precedence** — ADR-L-1009 (kernel) vs STE Gateway narrative. | **Done.** |
| ADR-023 | Validation timing and responsibility | ADR-L | **ADR-L-0023** | **coexist-with-precedence** — ADR-L-1002 / ADR-L-1009; **merge** with ADR-L-0026 on conflict verification meaning. | **Done.** |
| ADR-024 | Cross-component contracts | ADR-L | **ADR-L-0024** | **coexist-with-precedence** — ADR-L-1009. | **Done.** |
| ADR-025 | Environment semantics | ADR-L | **ADR-L-0025** | **coexist-with-precedence** — orthogonal kernel documentation-state unless bridged later. | **Done.** |
| ADR-026 | Invariant conflict detection semantics | ADR-L | **ADR-L-0026** | **coexist-with-precedence** — ADR-L-1006; **merge** with ADR-L-0023. | **Done.** |
| ADR-027 | Scope semantics and versioning | ADR-L | **ADR-L-0027** | **coexist-with-precedence** — ADR-L-1002 / ADR-L-1009. | **Done.** |
| ADR-028 | Fabric and Gateway authority boundaries | ADR-L | **ADR-L-0028** | **coexist-with-precedence** — ADR-L-1001 / ADR-L-1009. | **Done.** |
| ADR-029 | Gateway enforcement authority | ADR-L | **ADR-L-0029** | **merge** — names Enforcement Authority; **coexist-with-precedence** — ADR-L-1002 / ADR-L-1009. | **Done.** |
| ADR-030 | Contract authority in ste-spec | ADR-L | **ADR-L-0030** | **coexist-with-precedence** — ADR-L-1002. | **Done.** |
| ADR-031 | Runtime/kernel responsibility boundary | ADR-L | **ADR-L-0031** | **merge** — ADR-L-1001 / ADR-L-1002. | **Done.** |
| ADR-032 | Fail-closed enforcement model | ADR-L | **ADR-L-0032** | **merge** — ADR-L-1009; **coexist-with-precedence** — ADR-L-0022. | **Done.** |
| ADR-033 | Closed-object discipline | ADR-L | **ADR-L-0033** | **coexist-with-precedence** — ADR-L-1002. | **Done.** |
| ADR-034 | Rule projection envelope authority | ADR-L | **ADR-L-0034** (proposed) | **coexist-with-precedence** — ADR-L-1008. | **Done.** |
| ADR-035 | Architecture IR ontology authority | ADR-L | **ADR-L-0035** | **coexist-with-precedence** — ADR-L-1006. | **Done.** |
| ADR-036 | Repository README contract | ADR-L | **ADR-L-0036** | **coexist-with-precedence** — orthogonal to 100x kernel contracts. | **Done.** |
| ADR-037 | README conformance / reference impl | ADR-L | **ADR-L-0037** | **coexist-with-precedence** — orthogonal. | **Done.** |
| ADR-038 | Artifact taxonomy and versioning | ADR-L | **ADR-L-0038** | **coexist-with-precedence** — ADR-L-1003 / ADR-L-1007. | **Done.** |
| ADR-039 | Structured diagram format (Mermaid) | ADR-L | **ADR-L-0039** | **coexist-with-precedence** — ADR-L-0040. | **Done.** |
| ADR-040 | STE Spine lifecycle and authority | ADR-L | **ADR-L-0040** | **coexist-with-precedence** — ADR-L-1001–1009 (Spine uses kernel contracts). | **Done.** |
| ADR-041 | Compiler and merge authority | ADR-L | **ADR-L-0041** | **coexist-with-precedence** — ADR-L-1004 / ADR-L-1005. | **Done.** |
| *other* | `ARCHITECTURE_BOUNDARY_DECISION.md` | ADR-L | **ADR-L-0042** | **coexist-with-precedence** — supporting `architecture/` notes. | **Done.** |

## Phase 5 scope: normative spec vs runtime compiler (kernel consumption)

- **ste-spec** holds **normative** architecture decisions as schema-valid YAML (ADR-L / future ADR-PS / ADR-PC under `ste-spec/adrs/`) and supporting prose (`execution/`, `architecture/`, `contracts/`, etc.). Completing migration means **published ADR intent** is reachable in machine form without contradicting the YAML.
- **adr-architecture-kit** is the **authoring** toolkit: validate, render markdown, and emit registries/manifest/graph via `adr compile` with `--emit registries,manifest,markdown,graph` (from the kit repo: `python -m adr_kit.cli.main …`). The kit CLI may print a deprecation notice: **runtime-facing compilation of record** for machine artifacts is **ste-runtime** — see **ste-runtime** `COMPILER-AUTHORITY.md`.
- **Normative runtime compile command (ste-runtime):** from a project root that contains `PROJECT.yaml` and `adrs/`, run `ste architecture compile --project-root <repo-root>` (or invoke the built CLI: `node <ste-runtime>/dist/cli/index.js architecture compile --project-root <repo-root>`). **Recorded verification (2026-03-29):** full compile succeeded for `C:\Users\Erik\Documents\Projects\STE-workspace\ste-spec`, writing registries and `adrs/manifest.yaml` under `ste-spec/adrs/` (then **adr compile** was re-run with graph emit to restore authoring golden hashes for `validate-generated-docs`).
- **Kernel-relevant** semantics must exist as **ADR-L or ADR-PS** (or explicit cross-links to **ste-kernel** `adrs/physical-system/` where the kernel owns physical-system boundaries). ste-spec ADR-L-100x + future migrated legacy ADRs should **not** leave admission, fail-closed, or IR authority **only** in legacy markdown once migration completes.
- **Prose outside `adrs/published/`** (e.g. `execution/STE-Kernel-Execution-Model.md`) may remain normative **supporting** material. After migration, either: (1) keep as subordinate prose with explicit precedence pointers, or (2) progressively extract remaining normative bullets into ADR-L/PS/PC. Phase 5 “no governance only in prose” is **repository-wide** only if you adopt option (2); otherwise interpret Phase 5 as **no governance only in legacy published markdown**.

## Pilot human gate (ADR-001 → ADR-L-0001)

Complete before batch-migrating further legacy ADRs.

1. **Semantic parity:** Compare [`published/ADR-001-deterministic-extraction.md`](published/ADR-001-deterministic-extraction.md) with [`logical/ADR-L-0001-deterministic-extraction.yaml`](logical/ADR-L-0001-deterministic-extraction.yaml) and [`rendered/ADR-L-0001.md`](rendered/ADR-L-0001.md). Confirm no weakening or unintended narrowing of prohibitions (ML/graph, NL translation boundary, unknowns).
2. **Layering:** Confirm **ADR-L** is the right type (logical extraction doctrine, not ste-runtime component implementation). If physical deployment belongs elsewhere, note for ADR-PS/PC follow-up.
3. **Cross-references:** **ADR-L-0001** lists **ADR-L-0006**, **ADR-L-0007**, **ADR-L-0008**, **ADR-L-0009** in `related_adrs`. **GAP-0101** now tracks Architecture IR assertion payload alignment (low impact).
4. **Tooling:** From **adr-architecture-kit** repo: `adr validate --scope <ste-spec> --cross-references`, then `adr compile --scope <ste-spec> --emit registries,manifest,markdown,graph`, then `adr validate-generated-docs --scope <ste-spec>`.
5. **Plan refinement:** Record template tweaks (decision vs invariant split, handling of “Implementation Notes”, performance SLOs in gaps vs NFRs) and apply to the next legacy ADR.

When this gate is satisfied, update remaining rows in the legacy table above and proceed one ADR at a time or in small batches.
