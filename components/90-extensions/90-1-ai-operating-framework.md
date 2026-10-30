# AI-Assisted and Agentic Penetration Testing — Operating Framework

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## Reader headlines

**Primary audience:** Penetration testers, engagement leads, AI-tool owners, technical reviewers, and program leaders accountable for findings produced with AI-assisted or agentic capability.

**Objective:** Make AI-enabled testing usable without losing human accountability, testing authority, evidence quality, scope discipline, or the ability to explain what the system actually did.

**Intended outcome:** Every AI-enabled engagement has a declared path, autonomy tier, operating posture, validation rule, accountable human, evidence trail, and correction route proportionate to the capability's real agency and consequence.

**This document defines:** The testing-versus-support seam, execution-principal model, three governance axes, autonomy tiers, methodology transparency, finding validation, operating authorization, guardrails, evidence, incident handling, and the handoff from capability readiness.

## Document administration

| Field | Detail |
|---|---|
| **Document** | 90.1 |
| **Type** | T2 — Standard |
| **Maintainer** | Framework maintainers |
| **Local approval authority** | Defined by the adopting organization |
| **Review trigger** | At least semiannually and on material model, tool, autonomy, validation, threat, data, or operating change |

Organization-specific offices, systems, defaults, and open approvals from the originating practice have been replaced with adopter bindings; this framework is a design input, not a claim of operating effectiveness.

> [!CAUTION]
> This framework grants no authority to test, deploy a tool, process data, connect to a model, or publish a finding. Local use requires program authority, a valid Delivery Authorization where applicable, an adopted per-tool procedure, and engagement-specific authorization.

## Where this fits

§00.3 supplies the authority boundary. §00.4 charters capability development. §90.3 governs build and readiness; its Delivery Authorization is the handoff into this operate-side framework. §90.2 binds the framework to one tool and posture. §90.4 holds adjustable local parameters without weakening fixed floors.

This document governs AI used to perform or substantively shape penetration testing. It does not govern every use of AI in a security team, the security assessment of an AI system as a target, or an adopter's enterprise AI lifecycle.

An assessment of an AI system as the *target* may also use an agentic testing tool. The target methodology and this tool-operating framework then both apply; neither replaces the other.

## At a glance

Ask one question first:

> **Can this capability generate, change, validate, prioritize, or substantively support a finding?**

- **Yes:** it is on the testing path and enters the authority, tier, validation, evidence, and operating-control cascade.
- **No:** it is on the support path and remains governed by applicable development, data, access, records, and acceptable-use controls.

Then govern three independent axes:

1. **Output trust:** Is the finding supported and reproducible?
2. **Action containment:** What may the capability do, to what, with which identity and limits?
3. **Agent integrity:** Is the running system still the system that was evaluated, and can hostile input redirect it?

A passing answer on one axis cannot compensate for failure on another.

## 1. Purpose and scope

This framework applies when AI participates in authorized penetration-testing execution or in the decision-bearing finding pipeline.

It covers composite systems, including models, orchestration, prompts or policies, memory, tools, credentials, datasets, retrieval sources, adapters, and execution environments. Classification follows behavior and delegated authority rather than branding, vendor, open-source status, or whether one component is called an agent.

It does not authorize:

- testing outside approved targets, methods, identities, windows, or constraints;
- unreviewed findings or machine-only publication decisions;
- uncontrolled third-party processing, retention, training, or egress;
- operation beyond the delivered and approved posture;
- replacement of qualified professional judgment; or
- a claim that AI coverage is complete because the system found some vulnerabilities.

## 2. Defined terms

| Term | Meaning |
|---|---|
| **AI-assisted testing** | A human-directed testing activity in which AI recommends or produces bounded material for human use. |
| **Agentic testing** | Testing in which software plans or executes a multi-step action loop with delegated tools or authority. |
| **Execution principal** | A workload acting through identities, credentials, tools, data paths, and permissions; governed by what it can do, not by its conversational interface. |
| **Testing path** | AI use that can affect finding substance or the evidence relied upon for a finding. |
| **Support path** | AI use that assists administration or workflow without affecting finding substance. |
| **Finding substance** | The vulnerability claim, affected scope, exploitability, impact, severity, evidence, or decision to communicate the finding. |
| **Autonomy tier** | A classification of how much of the authorized testing loop the capability performs. |
| **Method transparency** | Sufficient evidence of what the capability attempted, how it mapped to the declared methodology, and what remained untested. |
| **Delivery Authorization** | The §90.3 decision allowing an exact findings-producing capability posture to enter bounded operation. |
| **Per-tool operating procedure** | The adopted §90.2 instance for one capability and deployment posture. |

## 3. Classify the path before the tool

### 3.1 Testing path

AI is on the testing path when it can:

- discover or propose vulnerabilities for delivery;
- select or execute test actions that produce evidence;
- alter exploitability, impact, affected scope, severity, or remediation meaning;
- validate or reject a candidate finding;
- combine evidence into a new security conclusion; or
- produce content a human substantially relies upon as a finding.

Testing-path use shall follow the remaining sections of this framework.

### 3.2 Support path

Support-path examples may include scheduling, approved-record assembly, deterministic formatting, routing, or administrative summaries that do not change finding substance.

Support classification requires a defined input and output boundary. If a support tool encounters unvalidated finding material, changes a security conclusion, or begins generating findings, the activity shall stop or be reclassified before output is relied upon.

### 3.3 The report-assembly seam

Formatting or assembling a finding a qualified human has already validated may remain support work. Generating or changing the vulnerability claim, evidence, exploitability, impact, severity, or remediation is testing work.

The absence of a recorded validation decision prevents the support classification. A convenient workflow label shall not downgrade the consequence of the output.

## 4. Build-to-operate handoff

Research, evaluation, and bounded proof occur under §00.4 and §90.3. A successful experiment does not create operating authority.

A findings-producing capability enters this framework only when Delivery Authorization identifies the exact capability and posture, operating limits, autonomy tier, per-tool procedure, validation rules, residual risk, material-change triggers, and accountable authority.

Direct adoption of an existing capability shall clear an equivalent readiness and safety record; purchasing or subscribing to a service is not Delivery Authorization.

## 5. Three-axis governance model

### 5.1 Output trust

The program shall determine whether finding evidence is accurate, reproducible, scoped, methodologically meaningful, and sufficient for the decision. It shall also measure what the capability may miss. Low false positives do not establish adequate coverage.

### 5.2 Action containment

The capability shall operate inside the intended-authority envelope authorized for the tool and the engagement. Enforcement should occur at identity, network, tool, data, and action boundaries—not only through natural-language instruction.

### 5.3 Agent integrity

The program shall protect or observe the decision-bearing composition and runtime. Relevant threats include substituted components, poisoned retrieval, prompt injection, malicious target output, tool-output forgery, memory contamination, unsafe replanning, and integrity loss after startup.

An integrity concern shall be recorded and may reduce evidence strength, stop the run, or require revalidation. Silence from a detector shall be reported as “not observed” or “integrity unverified” unless the evidence supports a stronger claim.

## 6. Autonomy tiers

Tier measures action autonomy, not the authority to decide what is published. A qualified human remains accountable for every delivered finding at every tier.

| Tier | Operating description | Human role | Minimum treatment |
|---|---|---|---|
| **0 — Assisted** | AI suggests content or actions; the tester directs each meaningful step | Directs, verifies, and decides | Normal methodology and evidence discipline; declare material AI use where required |
| **1 — Bounded component** | An agent performs one defined task inside a human-led engagement | Sets bounds, reviews output, integrates evidence, and decides | Per-tool procedure; bounded authority; full review of output relied upon |
| **2 — Agent-led** | The system performs substantial multi-step testing while a human supervises and validates | Authorizes run, monitors, validates findings, handles judgment and communication | Delivery Authorization; per-engagement approval; calibrated validation; coverage assurance; stronger containment/integrity controls |
| **3 — High-autonomy** | The system performs most of the testing loop with limited synchronous direction | Approves boundaries and remains responsible for every finding and stop decision | Tier-2 controls plus explicit high-autonomy decision, stronger monitoring, independent review, and additional local authority as consequence requires |

Classification shall use the highest material behavior available in the authorized posture, not the behavior demonstrated in a friendly example. A material autonomy increase requires reclassification and may require return to readiness evaluation.

Record the tier actually authorized and used **per engagement**. One capability can run in different modes across engagements; its general product label is not the engagement's classification. An adopter's model-risk or enterprise AI risk rank is a separate classification and must not be inferred from this autonomy tier.

## 7. Methodology transparency

An AI testing capability shall identify:

- the authorized methodology and target class;
- test areas attempted, skipped, refused, failed, or unavailable;
- the action and evidence chain for each candidate finding;
- where human judgment entered;
- any translation between tool output and the program's finding schema; and
- untested or weakly tested coverage.

An adopter may recognize external or internal methodologies through a maintained source and mapping process. Recognition shall not be inferred from marketing language, a tool name, or a list of vulnerability classes.

### 7.1 Conformant and non-conformant posture

For operating decisions, a capability may be treated as methodologically mapped only when current evidence shows how its behavior covers the declared method and how gaps are reported.

Where that evidence is missing or materially incomplete, every finding relied upon shall receive full qualified-human validation. The program shall not use sampling to compensate for an opaque or unbounded method.

For a targeted security-control assessment, assess conformance against the declared, applicable subset of the methodology and the control under test. A narrow assessment is not non-conformant merely because it did not run a full web, API, or infrastructure test. It must state what was in scope, what was not tested, and what evidence shows whether the control held or failed. A tool's narrated steps must be corroborated against captured actions and target evidence; fluent self-report is not a run log.

## 8. Finding validation

### 8.1 Fixed principle

A qualified human shall decide whether every finding is accepted for delivery. AI may assist the work; it shall not be the accountable publication authority.

A finding shall demonstrate affected scope, reproducible evidence, and security impact appropriate to the methodology. A label, vulnerability identifier, similarity match, or model assertion alone is not proof of exploitability.

### 8.2 Minimum validation rules

- Critical or otherwise highest-consequence findings shall receive full qualified-human validation.
- The first use of a material capability posture against a new target class shall receive full validation.
- Disputed, ambiguous, integrity-affected, special-scope, or safety-relevant findings shall receive full validation.
- Findings from a methodologically non-conformant or opaque posture shall receive full validation.
- A local sampling rule may apply only after a calibrating body of full validation supports it and §90.4 binds the rate, scope, owner, and rollback trigger.
- Sampling never transfers accountability to the system and never waives evidence or peer-review requirements.

Finding validation and review of the **capability itself** are different jobs. Per-engagement validation asks whether a finding is real and supported. Independent or risk-based capability review asks whether the composite system, method, controls, and performance remain sound. An adopter shall bind both jobs to its own review authorities and cadence; a good finding does not prove the tool safe, and a reviewed tool does not make every finding correct.

### 8.3 Coverage assurance

Finding validation asks whether reported findings are real. Coverage assurance asks what the capability missed.

The program shall use proportionate parallel testing, seeded cases, ground-truth benchmarks, historical regression sets, or another independent method to evaluate false negatives. Reported findings and coverage evidence shall not be blended into a single score that hides a material weakness.

### 8.4 Finding states

At minimum, records shall distinguish:

1. machine-proposed or candidate;
2. human-validated or rejected;
3. accepted for engagement delivery;
4. published or otherwise communicated; and
5. corrected, withdrawn, or superseded.

A clean-looking final report shall not erase the decision and correction trail.

## 9. Authorization and operating checks

### 9.1 Per-tool checks

Before findings-producing operation, the program shall verify:

- valid Delivery Authorization or equivalent adoption decision;
- current §90.2 operating procedure;
- exact capability composition and deployment posture;
- intended-authority envelope and enforcement evidence;
- permitted operators and required training;
- data, retention, egress, model, third-party, and credential disposition;
- methodology map, validation rule, and coverage-assurance plan;
- monitoring, spend bounds, stop, incident, correction, and rollback paths; and
- local AI, privacy, legal, risk, procurement, provider, and records obligations.

### 9.2 Per-engagement checks

The engagement authorization shall declare:

- capability and version/posture;
- autonomy tier and operating mode;
- targets, exclusions, accounts, data, tools, techniques, and window;
- permitted and prohibited actions;
- validating human and engagement lead;
- validation and peer-review plan;
- transparency or communication requirement;
- deconfliction, stop, and incident contacts; and
- evidence and archival location.

Tool authorization shall not expand engagement scope, and engagement authorization shall not expand program authority.

### 9.3 Material change

Material changes shall be evaluated against §90.3. A change may be handled at the affected component when it does not alter shared behavior or risk. Program-wide reapproval is not required for an inconsequential local change, but a version label alone shall not conceal a changed model, tool, authority, data path, or decision behavior.

## 10. Operating guardrails

### 10.1 Least agency and action safety

The system shall receive only the identities, tools, permissions, network paths, data, persistence, time, and cost needed for the authorized objective. Irreversible, destructive, production-touching, third-party, or high-impact actions require explicit human pre-authorization where the local authority model permits them at all.

### 10.2 Scope enforcement

The authorized target set shall be enforceable at the point of action. Ambiguous scope, unexpected redirects, shared infrastructure, newly discovered third parties, or conflicting target metadata shall stop or constrain the affected action pending human decision.

### 10.3 Credentials, data, and egress

Secrets shall be scoped, delivered, observed, rotated, and revoked through approved mechanisms. Restricted data shall not enter a model, provider, log, memory, or artifact store without explicit authority and a compatible handling path.

Network destinations and telemetry shall be declared. An uncontrolled egress path, changed provider term, or unapproved training/retention behavior is a material condition, not a footnote.

### 10.4 Runtime integrity

The program should use proportionate signatures, hashes, pinned manifests, isolated execution, tool allowlists, protected policies, prompt-injection defenses, output validation, external logs, and integrity canaries. Controls shall cover the decision-bearing composite system, not only the base model.

### 10.5 Evidence and records

For each run, preserve enough information to reconstruct:

- who and what initiated the run;
- the authorized scope and capability posture;
- model, orchestrator, tool, prompt/policy, adapter, and configuration identity;
- actions attempted and their outcomes;
- candidate findings and validation decisions;
- coverage limitations, refusals, errors, and abstentions;
- material costs and external calls;
- human interventions and approvals; and
- incidents, corrections, and final disposition.

Evidence shall follow applicable engagement-retention and disclosure rules. This framework does not create a competing record system.

## 11. Attribution, credit, and performance measures

The engagement result may count as program output when it satisfies the same authorization, evidence, review, and delivery requirements as other engagements.

Individual or team credit shall reflect accountable work and shall not reward unvalidated volume. An adopter may use effort, responsibility, complexity, or another locally approved model. Any weight or sampling parameter belongs in §90.4, not in this durable framework.

For contractor-delivered work, performance credit and payment are different decisions. Document the actual testing, validation, and delivery responsibilities, and apply the governing contract or statement of work. Do not treat an agent-led run as a full manual engagement for invoicing solely because the final report looks similar.

Measures should include quality, coverage, correction, operator burden, time returned, cost, unsafe or refused actions, and the work AI did not perform. The program shall not use finding count, engagement count, or tool utilization alone as proof of value.

## 12. Incident response and correction

The operator shall stop and preserve evidence when the capability:

- exceeds scope or authority;
- performs or attempts an unsafe or prohibited action;
- reveals or mishandles credentials or restricted data;
- shows suspected prompt injection, runtime substitution, poisoned context, or tool-output forgery;
- produces a material false finding or unexplained coverage regression;
- loses required logging, monitoring, cost bounding, or stop capability; or
- behaves outside the approved operating procedure.

The response shall coordinate with the adopting organization's incident, privacy, legal, asset, and vendor processes as applicable. The program shall assess affected engagements, correct or withdraw findings, notify relying parties when required, suspend the capability, and route material changes back through §90.3.

Separate a tool-caused incident from a security finding produced by the tool. Urgent, high-consequence findings still require the engagement's real-time escalation route; they must not wait silently for final report assembly. The accountable human decides what is substantiated and who must be notified under the engagement's authority.

## 13. Per-tool operating procedure

Every findings-producing capability shall have one current §90.2 instance that binds this framework to the actual composite system and deployment posture.

One procedure may cover multiple identical deployments only when their components, authority, data paths, controls, operators, and material-change behavior are genuinely shared. A new name shall not force a new procedure; a materially different posture shall not hide under an old one.

The procedure shall also name who may configure, operate, supervise, and stop the tool. Setup can create a different blast radius from running an already bounded engagement, so qualification should be demonstrated for each role. Offensive tooling remains a controlled asset: access, copies, credentials, egress, operator changes, and retirement need an owner and evidence. §30.4 supplies the broader tooling-OpSec companion.

### 13.1 Finding handoff

The program shall reconcile tool-specific finding labels to its maintained taxonomy and record the accepted finding in the system that issue owners and vulnerability-management partners actually use. Each delivered record needs affected scope, impact, severity rationale, exploitability evidence, remediation or next action, and the validation decision. Where the record's field model cannot carry an attack chain or richer evidence, preserve a linked or attached artifact rather than flattening away the reasoning. This framework does not prescribe a reporting product or automate acceptance of machine output.

## 14. Adoption profile

Before placing a tailored version In Force, the adopter shall bind:

| Binding | Local decision required |
|---|---|
| Authority | Which program and engagement authorities permit AI-assisted or agentic testing? |
| Enterprise interfaces | Which AI, model-risk, security, privacy, legal, data, procurement, records, and provider systems own related decisions? |
| Tier treatment | What additional review, monitoring, or authority applies to each autonomy tier? |
| Validation | What counts as qualified validation, critical/highest consequence, first-of-kind, and calibrating evidence? |
| Coverage assurance | Which independent methods and cadence reveal misses? |
| Tool custody | Where do approved procedures, manifests, authorizations, exceptions, and retirement records live? |
| Incident and correction | Who can stop use, revoke access, investigate, correct findings, and notify relying parties? |
| Transparency | What must be disclosed to engagement sponsors, customers, reviewers, or auditors? |
| Reporting handoff | Which taxonomy, issue record, real-time escalation route, and correction process receive accepted findings? |
| Operator qualification | Who may configure, run, supervise, stop, and retire each capability, and how is that demonstrated? |

An unbound field is an open adoption item. It shall not be replaced with a guessed default.

## 15. Assurance evidence

Evidence that this framework is operating may include:

- Delivery Authorizations and current per-tool procedures;
- engagement records that show tier, scope, operator, and validation decisions;
- full-validation calibration and coverage-assurance results;
- action logs tied to independently observed target evidence;
- scope, integrity, egress, stop, and cost-control tests;
- material-change reviews, suspensions, incidents, corrections, and retirements;
- measures showing quality, missed coverage, burden, and value; and
- independent review proportionate to autonomy and consequence.

Document presence or a successful demonstration does not establish operating effectiveness, comprehensive threat coverage, or safe deployment.
