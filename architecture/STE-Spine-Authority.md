# STE Spine Authority

## Purpose and Scope

This document is normative supporting doctrine for authority categories and
boundary explanation across the STE Spine.

It preserves the accepted authority split already established by ADR-030,
ADR-031, ADR-035, ADR-038, INV-0001, and INV-0002.

## Authority Boundary

This document supports
[`../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`](../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md)
and uses ADR-040 for Spine-local terminology.

ADR-040 remains canonical for the Spine lifecycle and authority-transition
model. This document does not override that ADR or redefine the taxonomy
posture controlled by
[`../adrs/published/ADR-038-artifact-classification-and-versioning.md`](../adrs/published/ADR-038-artifact-classification-and-versioning.md).

## Core Model

| Authority type | Definition | Owned by repository | Artifact classes | Lifecycle stages | Can override | Cannot override |
| --- | --- | --- | --- | --- | --- | --- |
| Normative Authority | Intended behavior, rules, constraints, and doctrine published as accepted `ste-spec` authority. | `ste-spec` | Normative | Intent Definition, Governance Decision, Intent Update / Remediation | Orientation material, Internal notes, non-authoritative Reports, non-authoritative Derived artifacts | Observational facts already produced as evidence, kernel-emitted admission outputs within their boundary, implementation truth by merely asserting contrary prose outside accepted doctrine |
| Implementation Truth | Executable or operational source truth for how repositories behave. | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` | Implementation | Implementation, Runtime Execution | No normative authority; it may realize doctrine and supersede older implementation source in repository history | Normative Authority, Decision Authority, factual Evidence by reinterpretation |
| Proof Authority | Versioned proof inputs and expected outcomes used to verify behavior or replay determinism. | `ste-kernel`, `ste-runtime`, `ste-rules-library`, `adr-architecture-kit` | Proof Logic | Proof / Verification | Report outputs and local interpretive summaries derived from proof runs | Normative Authority, caller-facing admission decisions, factual runtime evidence |
| Derived Artifact (Non-Authoritative) | Generated outputs in the `Derived` artifact class, produced from authoritative inputs through defined processes. This class carries publication surfaces, compiled integration-state, caller-facing admission artifacts, and some projections. | Varies by producer; often `ste-kernel`, `adr-architecture-kit`, or repository-local generators | Derived | Publication / Integration Input, Architecture IR Compilation, Admission Decision, Assessment (Reports) | Nothing by default; explicit doctrine may designate a publication artifact or proof baseline exception without changing its default posture | Normative Authority, Implementation Truth, Observational Authority, Decision Authority |
| Observational Authority (Evidence) | Factual observation within the evidence boundary, including runtime bundle health and freshness. | `ste-runtime` and other explicitly defined evidence producers | Evidence | Observation (Evidence) | Interpretive reports that misstate the observed facts | Normative Authority, kernel admission authority, governance authority, implementation source truth |
| Interpretive Output (Reports) | Summaries, assessments, diffs, validation outputs, and review material derived from authoritative or observed inputs. | Proof, validation, execution, or governance tooling | Reports | Proof / Verification, Assessment (Reports), Governance Decision | Nothing automatically; it can inform governance but is not authoritative by itself | Normative Authority, Observational Authority, Decision Authority |
| Decision Authority (Admission) | Final caller-facing admission and eligibility semantics at the runtime/kernel handoff, carried by the derived admission artifact emitted by `ste-kernel`. | `ste-kernel` | Derived | Admission Decision | Caller-facing uncertainty about admission outcome at this boundary | Normative Authority in general doctrine, factual runtime evidence, governance authority outside the admission boundary |
| Governance Authority | Explicit review, override, remediation, and next-cycle intent steering under accepted governance doctrine. | `ste-spec` and governance-side consumers; `ste-rules-library` supplies rule logic but is not the normative store of all decisions | Normative, Reports, Internal | Governance Decision, Intent Update / Remediation | Internal plans, non-authoritative reports, unresolved review state once explicit governance action is taken | Accepted normative authority unless changed through accepted doctrine, factual evidence, kernel admission output as the caller-facing decision artifact |

## Interpretation Notes

| Question | Governed by | Effect |
| --- | --- | --- |
| Who owns truth within scope? | Authority category | Determines which surface is authoritative for that subject area or boundary |
| Does a state change transfer authority? | No | State affects readiness or applicability, not authority ownership |
| How can accepted intent change? | Accepted doctrine under governance authority | Governance may direct change, but reports or evidence do not change accepted intent by themselves |

- Normative authority governs intent and doctrine, but it does not rewrite
  factual evidence after the fact.
- Implementation truth realizes doctrine but does not override accepted
  normative doctrine.
- Proof authority determines proof inputs and expected outcomes, not caller-facing
  admission semantics.
- Derived artifacts remain non-authoritative unless explicit doctrine assigns a
  narrower exception posture such as publication artifact or deterministic proof
  baseline.
- `KernelAdmissionAssessment` is the derived admission artifact that carries
  caller-facing decision authority at the boundary. Report outputs about that
  decision remain interpretive.
- Reports and projections are non-authoritative. They may guide governance, but
  they do not replace accepted authority surfaces.
- Orientation artifacts are non-authoritative and indirect. They do not
  participate as public authority surfaces by default.
- Authority category, authority ownership, and current applicability are
  related but distinct terms in this model. State changes do not reassign
  authority ownership.

## Related Documents

- [`STE-Spine-Lifecycle.md`](./STE-Spine-Lifecycle.md)
- [`STE-Spine-Artifact-Mapping.md`](./STE-Spine-Artifact-Mapping.md)
- [`STE-Spine-State-Model.md`](./STE-Spine-State-Model.md)
- [`../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md`](../adrs/published/ADR-040-ste-spine-lifecycle-and-authority.md)
