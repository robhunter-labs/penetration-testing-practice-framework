# 20.16 — Threat Modeling for Penetration Testing

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

**Component:** technical method · **Reader:** penetration tester, engagement lead, technical reviewer, or adopter tailoring a testing practice

## The job of this method

Threat modeling asks where a target's *design* may fail before the test is steered by a scanner result or a familiar checklist. A tester maps the system, marks changes in trust and authority, proposes ways a security property might fail, and turns the most useful hypotheses into authorized tests. The output is a better-directed engagement—not a list of findings.

This is threat modeling **as a penetration-testing method**. It can use an existing architecture or secure-design model, but does not replace the organization that owns product design, the software-development lifecycle, or its risk decisions. It does not authorize a new test. It does not establish a vulnerability until the test and human review support that conclusion.

Use the common framework [§20.1](20-1-method-framework.md) for the full engagement and finding decision. Use [§10.3](../10-engagement/10-3-scoping-map.md) to carry model-derived test needs into scope and rules of engagement. These are planned integration links until the full public set is assembled and checked.

## When to use it—and how much

Apply it before or early in execution when a new or materially changed target, complex workflow, privilege boundary, third-party integration, control assessment, or prior result makes design reasoning valuable. Refresh it when the target or evidence changes. An AI or agentic target deserves an explicit model of data, tool and action authority; that is a target-specific overlay, not a claim that the testing practice itself runs on AI agents.

Scale the record to the decision. One disputed authorization check may need a small boundary-and-hypothesis card. A system with several identities, data stores, integrations, and consequential actions may need a diagram, multiple hypotheses, and a review of untested paths. A large diagram is not evidence of a good model; a tiny card cannot support a claim about an entire architecture.

## Five steps from design to test

### 1. Decompose only what matters

Record the authorized target, its relevant version or state, actors and identities, assets, data, processes, stores, interfaces, dependencies, and security controls. Sketch data and action flows. A data-flow diagram, sequence, state table, or annotated architecture can all work. Keep sources, observation dates, and assumptions distinguishable.

The first question is simple: **what action or information are we trying to protect, and who is meant to control it?** If that answer is missing, ask the target owner or mark it uncertain; do not smuggle in a tester's expectation as a confirmed requirement.

### 2. Mark trust boundaries

Mark every material crossing where identity, privilege, ownership, tenant, data handling, control responsibility, or ability to act changes. “Internal” is not a trust decision. A boundary may exist inside one service when an ordinary user becomes an administrator, when one tenant's object is read through another's session, or when untrusted retrieved text is passed to an agent with tool access.

For each crossing, state the security property that should hold. For example: “Account A may read its own record, but not a record owned by Account B.” Bind the property to a requirement, design decision, local policy, stakeholder answer, or explicitly labeled tester expectation. A useful property names the subject, object, action, condition, and consequence of failure.

### 3. Enumerate falsifiable hypotheses

At each important boundary, ask how that property might fail. A hypothesis should name attacker capability and preconditions, the action or path, the suspected violation, and an observable result. Include a plausible benign explanation that the test must separate from the suspected flaw.

Technique catalogs can prompt this search. STRIDE, OWASP testing guidance, relevant CWE entries, MITRE ATT&CK or ATLAS, and target-specific references can expand coverage; they are not a substitute for understanding this target. Verify a catalog's current version and applicability when formally mapping a public claim. A label alone is not a tested weakness.

Distinguish implementation defects from design weaknesses without pretending the split is absolute. A scanner may expose a broken authorization symptom, but design reasoning is often needed to understand why that authorization boundary was misplaced or omitted.

### 4. Prioritize and design the test

Prioritize by plausible consequence, reachability, attacker preconditions, exposure, uncertainty, control strength, the engagement objective, and whether the test can be performed safely. A local risk scale may help order work; no impact-times-likelihood formula or score should be treated as universal or as a finding decision. Keep high-consequence uncertainties visible even when a neat numeric rank is unavailable.

For each selected hypothesis, record:

| Question | Minimum answer |
|---|---|
| Can we test it? | Authorized target, identity, method, environment, window, impact ceiling and stop condition—or the exact scope/RoE change needed. |
| What should happen? | The secure expectation and the failure behavior that would support the hypothesis. |
| What will separate causes? | A contrast in identity, object ownership, role, state, input, sequence, or control condition where safe and relevant. |
| What will we keep? | Raw and interpreted evidence, target state, collection context, data-handling rule, and limitation. |
| Who decides? | Qualified reviewer or local decision role, and the route for a disputed or unsafe result. |

A contrast is not mandatory when it is unsafe, impossible, or logically irrelevant; say what uncertainty remains instead of faking one. A hypothesis never expands testing authority by itself.

### 5. Document, test, and revise

The model should preserve the target and source context, boundary, security property, hypothesis, priority rationale, authorized test, expected evidence, actual result, human disposition, and untested conditions. A table or structured file is sufficient if another tester or reviewer can follow it. Machine-readable export is useful when a team has tooling, but no specific format or in-house tool is required to use this method.

Execution and final finding review belong to the engagement method. An observation can reject a hypothesis, expose a new boundary, support a candidate finding, or remain inconclusive. A tool or language model may propose hypotheses or organize evidence; it cannot confirm its own result. Update only the affected part of the model when new evidence, architecture, scope, or threat information changes the decision. Preserve material corrections instead of presenting a silently perfect history.

## A small worked example

Imagine an **authorized synthetic API assessment** with two test accounts and separate records. The API returns a record by identifier. The boundary is the ownership check between the authenticated caller and the requested record. The security property is that Account A cannot read Account B's record merely by knowing its identifier.

The hypothesis is that the service checks for a valid session but not object ownership. The safe test plan requests A's own record as a baseline, then B's test record using A's session, within the agreed environment and limits. A request under B's authorized session is a possible contrast. The tester records the exact account, token context, object ownership, API version, request, response, and state. If A receives B's data, the tester still checks for caching, account mix-up, test-fixture error, or unexpected authorization before proposing a finding. If ownership cannot be established, the result stays inconclusive. This is a model-to-test path, not a claim about a real target.

## Target-specific prompts

| Target | Boundaries and design questions worth considering |
|---|---|
| Web/API | Session and object ownership; role and function authorization; client/server trust; state-changing workflow; service-to-service and third-party authority. |
| AI/LLM application | User content versus instructions; retrieval and memory; prompt and model versus tool permissions; generated output versus downstream action; data and provider boundaries. |
| Tool-using or multi-agent system | Agent identity; delegated authority; tool credentials; inter-agent messages; memory and context persistence; human approval; cascading actions and rollback. |

These are prompts, not claims that every target has every path. This method references specific OWASP, MITRE and CSA catalogs and an internal targeting stage only as optional, currentness-checked sources; it does **not** claim that an internal tool or agentic testing workflow is deployed or needed by every adopter.

Threat-informed testing has a related but different job: intelligence helps choose which in-scope systems or behaviors deserve attention; this method reasons through *one target's design* to shape tests. Neither grants authority. The full-framework release must check this boundary against §20.15.

## Copyable model card

```text
Model / target / version:
Engagement and authorization reference:
Source facts and dates:
Assumptions and unresolved questions:
Actor, asset and action:
Trust or authority boundary:
Security property and its source:
Hypothesis, capability and preconditions:
Alternative explanation:
Priority reason and uncertainty:
Authorized test and safety limits:
Secure expectation / failure expectation:
Contrast or why none is suitable:
Evidence to collect and protect:
Observed result and limitations:
Human disposition and rationale:
Untested paths / refresh trigger:
```

An adopter binds its own authorization, depth triggers, reviewer roles, evidence store, retention, escalation and technique sources. A completed card is a reasoning aid; effective use is shown only when the model changes a test or review decision and its result can be traced back to current authorization and evidence.

## Public-release limitations

This is a draft, not a released standard or proof that any organization operates this method. Its worked example is synthetic. Catalog names and mappings require a separate current-primary-source check before use. Framework links, reader use, accessibility, and rights review remain open.
