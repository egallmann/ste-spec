# Internal Intelligence Surfaces

## Status

This document is **internal**, **non-public**, and **non-normative for external
compatibility**.

It records the role boundary for closed STE intelligence-bearing subsystems
without disclosing implementation details.

## Common Disclosure Rule

The following categories are prohibited from public disclosure unless later
promoted by an explicit public contract artifact:

- prompts
- heuristics
- ranking or weighting logic
- scoring formulas
- hidden orchestration behavior
- internal optimization strategies

## Internal Subsystems

### Conversation Compiler

- Role in lifecycle:
  transforms high-level architecture-facing requests or reasoning contexts into
  internal compile-ready control inputs
- Upstream dependencies:
  declared artifacts, architecture context, public contracts, internal operator
  intent
- Downstream outputs:
  internal compilation directives, candidate structured plans, private control
  signals
- Allowed public description:
  the system contains a compiler-like internal layer that prepares architecture
  work for downstream deterministic or intelligence-bearing stages
- Prohibited disclosure categories:
  prompts, heuristics, optimization strategy, hidden orchestration behavior

### Semantic Activation Engine

- Role in lifecycle:
  determines when private semantic activation is needed around architecture or
  governance tasks
- Upstream dependencies:
  architecture context, extracted signals, internal control conditions
- Downstream outputs:
  activation decisions or internal state transitions
- Allowed public description:
  an internal activation layer exists between context assembly and downstream
  reasoning/projection systems
- Prohibited disclosure categories:
  prompts, trigger heuristics, weighting logic, hidden orchestration behavior

### Constraint Projection Engine

- Role in lifecycle:
  projects architecture and governance context into internal constraint-bearing
  views used by higher-order reasoning or proposal systems
- Upstream dependencies:
  architecture state, rules/invariants, evidence, internal objectives
- Downstream outputs:
  internal projected constraints, structured candidate obligations, bounded
  problem frames
- Allowed public description:
  the system includes an internal projection stage that consumes architecture and
  governance context and emits constraint-bearing internal views
- Prohibited disclosure categories:
  heuristics, ranking logic, scoring formulas, private optimization strategy

### Adversarial Reasoning Engine

- Role in lifecycle:
  generates structured challenge, steelman, or adversarial scrutiny against
  proposals or interpretations
- Upstream dependencies:
  architecture context, candidate plans or proposals, rule and evidence inputs
- Downstream outputs:
  internal critique artifacts, challenge signals, escalation inputs
- Allowed public description:
  a private adversarial review layer may challenge candidate outputs before
  recommendation or action
- Prohibited disclosure categories:
  prompts, trigger heuristics, private challenge strategy, internal scoring

### EDR Scoring Engine

- Role in lifecycle:
  evaluates extracted design or evidence material using private confidence or
  quality signals
- Upstream dependencies:
  EDR-shaped inputs, evidence artifacts, extracted embodiment material
- Downstream outputs:
  private confidence or ranking signals, internal prioritization inputs
- Allowed public description:
  a private scoring layer may assess extracted or observed embodiment material
  before internal use
- Prohibited disclosure categories:
  scoring formulas, weighting logic, hidden feature selection, optimization
  strategy

### Graph Healing / Inference Engine

- Role in lifecycle:
  repairs, infers, or enriches internal graph-like state when explicit sources
  are incomplete
- Upstream dependencies:
  architecture graph state, evidence, unresolved gaps, internal inference
  context
- Downstream outputs:
  internal inferred links, healing suggestions, repair candidates
- Allowed public description:
  an internal inference layer may support repair or enrichment of incomplete
  graph state
- Prohibited disclosure categories:
  inference heuristics, repair policies, ranking logic, hidden orchestration

### Autonomous Orchestration Layer

- Role in lifecycle:
  coordinates internal sequencing among private intelligence-bearing subsystems
- Upstream dependencies:
  internal state, architecture context, control directives, private subsystem
  signals
- Downstream outputs:
  orchestration actions, internal scheduling or routing decisions
- Allowed public description:
  the system may contain an internal orchestration layer that sequences private
  intelligence-bearing components
- Prohibited disclosure categories:
  orchestration policy, prompts, optimization strategy, hidden prioritization

## Internal Use Rule

This document is intended for internal planning and architectural boundary
management only. It is not a public compatibility promise.
