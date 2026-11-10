# AI-Assisted and Agentic Penetration Testing — Operating Framework

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## At a glance

Terms used here are defined in the [Section 90 glossary](90-0-glossary.md).

Ask one question first:

> **Can this capability generate, change, validate, prioritize, or substantively support a finding?**

- **Yes:** it is on the testing path and enters the authority, tier, validation, evidence, and operating-control cascade.
- **No:** it is on the support path and remains governed by applicable development, data, access, records, and acceptable-use controls.

Then govern three independent axes:

1. **Output trust:** Is the finding supported and reproducible?
2. **Action containment:** What may the capability do, to what, with which identity and limits?
3. **Agent integrity:** Is the running system still the system that was evaluated, and can hostile input redirect it?

A passing answer on one axis cannot compensate for failure on another.

## Reader headlines

**Primary audience:** Penetration testers, engagement leads, AI-tool owners, technical reviewers, and program leaders accountable for findings produced with AI-assisted or agentic capability.

**Objective:** Make AI-enabled testing usable without losing human accountability, testing authority, evidence quality, scope discipline, or the ability to explain what the system actually did.

**Intended outcome:** Every AI-enabled engagement has a declared path, autonomy tier, operating posture, validation rule, accountable human, evidence trail, and correction route proportionate to the capability's real agency and consequence.

**This document defines:** The testing-versus-support seam, three governance axes, autonomy tiers, methodology transparency, finding validation (including severity, attack chains and validation capacity), operating authorization, guardrails, evidence, incident handling, and the handoff from capability readiness.

## Document administration

| Field | Detail |
|---|---|
| **Document** | 90.1 |
| **Type** | T2 — Standard |
| **Maintainer** | Framework maintainers |
| **Local approval authority** | Defined by the adopting organization |
| **Review trigger** | At least semiannually and on material model, tool, autonomy, validation, threat, data, or operating change |

The adopter supplies its own offices, systems, defaults, and approvals. This framework is a design input, not a claim of operating effectiveness.

> [!CAUTION]
> This framework grants no authority to test, deploy a tool, process data, connect to a model, or publish a finding. Local use requires program authority, a valid Delivery Authorization where applicable, an adopted per-tool procedure, and engagement-specific authorization.

## Where this fits

§00.3 supplies the authority boundary. §00.4 charters capability development. §90.3 governs build and readiness; its Delivery Authorization is the handoff into this operate-side framework. §90.2 binds the framework to one tool and posture. §90.4 holds adjustable local parameters without weakening fixed floors.

This document governs AI used to perform or substantively shape penetration testing. It does not govern every use of AI in a security team, the security assessment of an AI system as a target, or an adopter's enterprise AI lifecycle.

An assessment of an AI system as the *target* may also use an agentic testing tool. The target methodology and this tool-operating framework then both apply; neither replaces the other.

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
| **Execution principal** | The capability treated as a non-human workload identity: it acts through identities, credentials, tools, data paths, and permissions, and is governed by what it can do, not by its conversational interface (§10.1). |
| **Posture** | One specific configuration and deployment of the composite system: components and versions, where it runs, what it may reach, which identities it holds, and how it is bounded. |
| **Candidate** | A proposed finding, including the tool's own severity, before a qualified human has decided it. |
| **Full validation** | A qualified human establishes affected scope, behavior and impact from evidence they examined directly, whether from their own reproduction or from an independent replay (see the [glossary](90-0-glossary.md)). The human decides; reviewing the tool's narrative is not full validation. |
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

Words such as "substantial" and "most" are judged against observable behavior. Record, for the authorized posture: how often a human must approve (each action, each phase, or each run); whether the system may write and run its own code; whether it may exploit or act after exploitation; whether it may start sub-agents or run in parallel; and the longest period it may run without a human checkpoint. Those answers, not the product description, place the tier.

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

A qualified human shall decide whether every finding is accepted for delivery. AI may assist the work; it shall not be the accountable publication authority. Human decision is not the same as full manual reproduction of every intermediate tool suggestion; it is the accountable judgment that the evidence supports the claim.

A finding shall demonstrate affected scope, reproducible evidence, and security impact appropriate to the methodology. A label, vulnerability identifier, similarity match, or model assertion alone is not proof of exploitability. A validator working from fluent tool output watches for automation bias: excessive deference to automated systems, such as judging their output to be of higher quality than other sources without justification ([NIST AI 600-1 §2.7](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).

### 8.2 Minimum validation rules

- The tool's severity is a claim. A qualified human shall derive severity from the evidence at triage, and any change from the tool's severity shall be recorded with its reason. Downgrades are tracked as a measure (§90.5).
- Consequence for validation and sampling eligibility is the **triage band**: the higher of the tool's proposed severity and the human triage severity, until full validation settles it. A candidate that forms a step in an attack chain takes the chain's consequence (§8.5).
- Critical or otherwise highest-consequence findings shall receive full qualified-human validation.
- The first use of a material capability posture against a new target class shall receive full validation.
- Disputed, ambiguous, integrity-affected, special-scope, or safety-relevant findings shall receive full validation.
- Findings from a methodologically non-conformant or opaque posture shall receive full validation.
- A local sampling rule may apply only after a calibrating body of full validation supports it and §90.4 binds the rate, scope, owner, and rollback trigger. Calibration and sampling are done per stratum: posture × target class × vulnerability class × triage band (the higher of the tool's severity and the human triage severity). A calibrating body is a recorded, randomly selected set of fully validated candidates from one stratum, large enough to bound the failure rate at the level the adopter declares (§90.5 gives a method). A failure is any candidate where the reduced-depth decision on whether it is real, or on its severity band, would differ from full validation. What is sampled is direct reproduction of eligible candidates, chosen at random within the stratum; the human decision on every delivered finding is never sampled.
- Sampling never transfers accountability to the system and never waives evidence or peer-review requirements.

Finding validation and review of the **capability itself** are different jobs. Per-engagement validation asks whether a finding is real and supported. Independent or risk-based capability review asks whether the composite system, method, controls, and performance remain sound. An adopter shall bind both jobs to its own review authorities and cadence; a good finding does not prove the tool safe, and a reviewed tool does not make every finding correct.

### 8.3 Coverage assurance

Finding validation asks whether reported findings are real. Coverage assurance asks what the capability missed.

The program shall use proportionate parallel testing, seeded cases, ground-truth benchmarks, historical regression sets, or another independent method to evaluate false negatives. Where two independent methods are run on the same scope, the overlap between what each found supports an estimate of what both missed (a capture–recapture estimate, §90.5 §3); state its assumptions. A missing or dead answer key is reported as `unknown`, not as zero misses. Reported findings and coverage evidence shall not be blended into a single score that hides a material weakness.

### 8.4 Finding states

At minimum, records shall distinguish:

1. machine-proposed or candidate;
2. machine-rejected or suppressed by the capability (kept, not deleted, so misses stay visible);
3. merged into another candidate, or marked duplicate, with the link preserved;
4. not reviewed: no capacity (with the reason and the candidate's age);
5. human-validated or rejected;
6. accepted for engagement delivery;
7. published or otherwise communicated; and
8. corrected, withdrawn, or superseded.

Each candidate also carries the evidence it reached, using the §20.13 vocabulary, recorded as two parts: **repeatability** (*Observed*, then *Reproduced*, where independent replay counts as reproduction) and **impact** (*Demonstrated impact* or not). Anything beyond that is *Possible, not tested*. The claim shall not exceed what both parts support. State 4 is a recorded state, not a silent drop.

A clean-looking final report shall not erase the decision and correction trail.

### 8.5 Attack chains

When a capability proposes a chain, record it as a chain, not only as separate candidates. For each step, record the action, the evidence, and its repeatability and impact. The weakest proven step is the step lowest on either part; the chain's claimed impact shall not exceed it, and an unproven step makes the rest of the chain *Possible, not tested*. Merging duplicates shall not remove a step that a chain depends on.

Proving a chain in a live environment can mean re-running exploitation. That is testing, inside the engagement's authority, window and safety limits; a chain that needs an action outside them stays a hypothesis for owner triage. A system becoming relevant to a chain's impact does not bring it into scope.

### 8.6 Where automated checks run out

An oracle the tool cannot write to works best when the target leaves a mark that code can read: a crash a sanitizer reports, a callback confirmed to come from the target and carrying a one-time token, a flag planted for the test, or a script a headless browser confirms ran. Such a mark can move a candidate's repeatability to *Reproduced* and support its impact; it does not settle impact on its own (§8.4). A sanitizer crash shows memory corruption, not exploitability, and a script running in a test browser does not show it runs in a victim's context. Each mark is sharper with a negative control, such as a patched copy where the same action has to fail.

Three kinds of claim rarely leave a clean mark:

- **Chains.** Every step can be real and the chain still fail, or work only in an order the test never tried. Evidence is per step, then end to end (§8.5). In one study of 13 open-source LLM-based automated penetration-testing frameworks, only about one in six samples completed the chained-exploitation challenge ([Hackers or Hallucinators?, §5.6.1, Table 17](https://arxiv.org/abs/2604.05719)).
- **Authorization logic.** The oracle is two or more identities and a comparison, and it is only as good as the test's model of who should see what.
- **Impact and reachability.** A result against one host or a replica is not yet a finding in an environment. Whether a path reaches the target through that environment's segmentation and identity rules is a separate question, and a system becoming relevant to a chain does not bring it into scope (§8.5).

Live environments the practice does not control weaken every oracle: there is often no patched copy to compare against, outbound callbacks may be blocked, and timing is noisy.

An oracle that does not fire shows nothing. The claim shall stay at what other evidence supports (§8.4), and the oracle's part shall be recorded as `unknown`, not as a pass or a false positive.

### 8.7 The validation package

A validator can rule only on what reaches them. One way to hand over a candidate is a validation package: one versioned record per candidate, in six parts, each marked with where it came from. It is a pattern to tailor, set out in [*Proof Outside the Model*, §07](https://robhunterworks.com/writing/proof-outside-the-model/), and a proposal: whether it shortens review has not been measured (§90.5 §8).

| Part | What it holds |
|---|---|
| **1. Claim** | One sentence: the weakness, where it is, and what it allows. The tool's severity is recorded as the tool's (§8.2). |
| **2. Oracle output** | What a check outside the model observed (§8.6), or "no oracle", which leaves the claim at what other evidence supports (§8.4). |
| **3. Replay** | The exact request or script; the build or environment it ran against; the test identity, with credentials by reference (§30.3); the authorization it ran under; what it changed and cleaned up; and what sensitive data the evidence holds and how it is redacted. |
| **4. Controls** | The baseline (the legitimate request the claim should differ from); a negative control, built so the effect must not appear; and a positive control, built so the check must fire, behind any "not vulnerable" result. |
| **5. Expected difference** | What the validator should see if the claim holds, what they would see if it does not, and what would leave it unknown, all recorded before the replay runs. |
| **6. Retest** | The same check, kept for after the fix. It looks for the expected refusal, not only a different response, and names the build it ran against. |

**Provenance.** Each part should carry one label:

- *observed* (read from the target by an oracle, or by the validator in their own reproduction);
- *asserted* (stated by the tool);
- *decided* (ruled by a person); or
- `unknown` (nothing could check it).

*Proof Outside the Model* reserves *observed* for an oracle; this framework also counts the validator's own reproduction, in line with *full validation* (§2).

As a tool emits a package:

- the claim, the replay and the expected difference are *asserted*;
- the oracle output and the controls are *observed* only where a check returned a result, and otherwise `unknown`; and
- the retest is *asserted* until run through the retest route (§50.3 §3.4).

The ruling is *decided*. A model's confidence, or a second model agreeing with it, can order the queue; neither earns *observed*. `unknown` is a result with a reason, not a blank to fill. The label says where a part came from. It is separate from the evidence state in §8.4, which says how far the evidence reached.

**Four questions.** Ask them of every package, and record each answer on its own, because a single pass mark can hide which one failed:

1. Did it run?
2. Is the reasoning right?
3. Could someone else rerun it from the package alone?
4. Can a person act on it?

**Ruling.** The validator's ruling is one of four: *accepted*; *false positive*; *not enough evidence*; or *deferred to a named owner*. The first three are §20.1's accept, reject, and defer for more evidence or report as inconclusive; the fourth hands a question the validator cannot settle, such as whether a behavior is intended, to an owner recorded with the open question.

Accepted and false positive are the two sides of state 5 in §8.4. *Accepted* here means validated (state 5); acceptance for delivery is state 6. The other two leave the candidate in state 1 with the ruling, reason and any named owner recorded. It still counts in the backlog and maximum age (§9.4).

Merging, grouping and splitting are deduplication decisions (§90.5 §1), not rulings on whether a claim is real. *Not enough evidence* is not a false positive and should not be counted as one (§90.5 §2). A candidate nobody has reviewed has no ruling.

Each ruling should record its reason, for a dismissal as much as for an acceptance, with the person and the version of the package it was made on. If the evidence in any part changes, the ruling is reopened, not carried forward.

The script in a package comes from the tool, so a person reads it before running it, and replay against a live target is testing under the same authority as any other test (see *independent replay* in the [glossary](90-0-glossary.md)). A complete package is a better input to the decision in §8.1. It is not the decision.

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
- expected candidate volume, declared validator hours, and the backlog threshold for §9.4;
- validation and peer-review plan;
- transparency or communication requirement;
- deconfliction, stop, and incident contacts; and
- evidence and archival location.

Tool authorization shall not expand engagement scope, and engagement authorization shall not expand program authority.

### 9.3 Material change

Material changes shall be evaluated against §90.3. A change may be handled at the affected component when it does not alter shared behavior or risk. Program-wide reapproval is not required for an inconsequential local change, but a version label alone shall not conceal a changed model, tool, authority, data path, or decision behavior.

### 9.4 Validation capacity and backpressure

A capability can produce candidates faster than qualified people can validate them. Before a findings-producing run, the engagement shall declare the expected candidate volume (from evaluation or prior runs, or `unknown`) and the validator hours available.

- When unvalidated candidates exceed the declared backlog threshold, the run shall be slowed, paused, or narrowed. Validation shall not be thinned to keep pace.
- An unvalidated candidate at the highest consequence shall not wait beyond a locally declared maximum age; it is escalated through the engagement's real-time route.
- Candidates left unvalidated at the end of an engagement are recorded as such, with the reason, and are not delivered as findings or counted as coverage.

Capacity figures and maximum ages are local levers (§90.4), not defaults set by this framework.

Where a candidate is escalated before validation finishes, what the receiving program does is its decision; the item carries a "not yet validated" label and a named validator, and is not a delivered finding.

## 10. Operating guardrails

### 10.1 Least agency and action safety

Govern the capability as an execution principal. The system shall receive only the identities, tools, permissions, network paths, data, persistence, time, and cost needed for the authorized objective. Irreversible, destructive, production-touching, third-party, or high-impact actions require explicit human pre-authorization where the local authority model permits them at all.

### 10.2 Scope enforcement

The authorized target set shall be enforceable at the point of action. Ambiguous scope, unexpected redirects, shared infrastructure, newly discovered third parties, or conflicting target metadata shall stop or constrain the affected action pending human decision.

### 10.3 Credentials, data, and egress

Secrets shall be scoped, delivered, observed, rotated, and revoked through approved mechanisms. Restricted data shall not enter a model, provider, log, memory, or artifact store without explicit authority and a compatible handling path.

Network destinations and telemetry shall be declared. An uncontrolled egress path, changed provider term, or unapproved training/retention behavior is a material condition, not a footnote.

### 10.4 Runtime integrity

The program should use proportionate signatures, hashes, pinned manifests, isolated execution, tool allowlists, protected policies, output validation, external logs, and integrity canaries. No current in-model defense reliably stops prompt injection, so design controls that bound impact assuming injection succeeds: enforce limits outside the model, at identity, network, tool and action boundaries. Controls shall cover the decision-bearing composite system, not only the base model.

Pin model snapshots where the provider allows it. Where a hosted provider can change the model behind the same endpoint name, treat that endpoint as a source of uncontrolled change: record the identifier the provider reports for each run and treat an unexplained behavior shift as a material-change trigger.

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

**Integrity of agent-produced evidence.** A capability that can rewrite its own records can, by error or under injected instruction (§5.3), change the evidence a validator later relies on. Two proportionate controls address this:

1. The authoritative run log should be written to a store that the capability's own identity cannot modify or delete, so that the account of what it did does not rest on files it wrote.
2. A cryptographic digest of each raw evidence artifact should be computed outside the model, by the harness or the receiving store, and recorded in that log at capture, with the algorithm named, and re-checked before the artifact is relied on for validation and again at archival (§30.1).

A mismatch is an integrity concern under §5.3.

OWASP APTS (v0.1.0) states both as requirements for autonomous testing platforms ([Auditability](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/5_Auditability/README.md); [Reporting](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/8_Reporting/README.md)):

- APTS-AR-020, the agent runtime has no permission to write, modify, or delete the authoritative audit trail;
- APTS-AR-010, all evidence is hashed with SHA-256 or stronger and the algorithm is recorded with the hash; and
- APTS-RP-005, each finding's evidence carries its hash so a reviewer can verify it independently.

APTS also requires hash-chained, append-only logs at its first tier (APTS-AR-012) and recommends RFC 3161 trusted timestamps at its third (APTS-AR-013). This framework does not ask for either; an adopter may take them up where consequence warrants.

The limit: a matching digest shows that an artifact has not changed since the digest was recorded. It does not show that the artifact was accurate when captured, which remains the validator's question (§8), and a digest kept where the capability could rewrite it shows little (§40.3 makes the same point for evidence handoff).

### 10.6 Interruption, stop, and handoff

The §90.2 run card records how fast a stop takes effect and what happens to actions in flight. This section covers what the run record should hold once a stop, a pause, or a change of operator has happened. The OWASP APTS requirements cited below (v0.1.0) bind an autonomous testing platform; they are cited as published practice for the same moments, not as obligations of this framework.

**Three points.** Declare what a stop means at each:

- before an action is sent, when the orchestration can still withhold it;
- while it is in flight, when the target or another system may already have accepted it; and
- after it finishes, when what remains is cleanup.

Cleanup is a further action on the target, inside the engagement's authority, and can fail on its own.

**Three statements.** Keep *stop requested*, *stop acknowledged*, and *outcome observed* apart.

- A stop that was not acknowledged shall not be recorded as delivered. An unacknowledged stop is a failed stop (§12): use enforcement outside the tool, such as revoking its credentials or network path (§10.4).
- An action whose outcome was not observed shall be recorded as `unknown`, not as "did not happen". An `unknown` action is checked before any retry, so the same change is not made twice: against the run log and side-effect ledger (§90.2 §4) first, and against the target only where the stop authority allows that contact.

APTS states the first rule for its kill switch: "An unacknowledged kill instruction MUST NOT be treated as delivered" ([APTS-HO-008](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/3_Human_Oversight/README.md#apts-ho-008-immediate-kill-switch-with-state-dump)).

**What can outlive a stop.** Queued or scheduled actions, automatic retries, sub-agents and child processes, open sessions, credentials that are still valid, and resources the tool created off the target, which outlast a revoked credential unless removed separately (§90.2 §4). [APTS-SC-009](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/2_Safety_Controls/README.md#apts-sc-009-kill-switch) allows operations already dispatched to complete, then requires spawned processes and child agents to be terminated, temporary credentials revoked, and scheduled or queued actions cancelled.

The practice's record should let the next person see which of these were confirmed stopped and which were not. That record should be written as the run goes: each tool call is logged before it is sent and updated with its outcome, in the run record §10.5 requires.

**Handoff.** When a run passes to another operator, at a shift change or after a stop, the handoff record should carry:

- the run's state and autonomy tier;
- who now holds stop authority;
- pending approvals, which the incoming operator reviews again and does not inherit;
- open escalations and integrity concerns;
- candidates awaiting validation, with the backlog against its threshold (§9.4);
- sessions, credentials, and tools still active; and
- cleanup still owed.

The incoming operator is one the per-tool procedure already permits (§9.1, §13) and the run card names (§90.2 §4). The test of the record is whether the incoming operator can pick the run up from it without reading the full run transcript.

[APTS-HO-019](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/3_Human_Oversight/README.md#apts-ho-019-247-operational-continuity-and-shift-handoff), a SHOULD-level requirement for continuous operation, asks for a structured handoff of "active engagement state, pending approvals, open escalations, and suppression-rule status" and for stale approvals to expire; its informative Shift Handoff Template is one format. [APTS-HO-009](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/3_Human_Oversight/README.md#apts-ho-009-multi-operator-kill-switch-authority-and-handoff) requires a multi-operator platform to define who holds kill-switch authority and to handle shift handoffs; its verification items check that authority transfers at a handoff and that each transfer is logged.

**Resumption.** After a stop for a stop condition or incident (§12), resuming is a decision by the authority named in the engagement's rules of engagement (the rules-of-engagement worksheet, component 10.2, §6; §00.3 §5); an operator's own pause resumes within the run card. In both cases, before the run continues, re-confirm scope, window, and identities, and that the posture is the one authorized (§9.3). After a pause longer than its session timeout, [APTS-HO-006](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/3_Human_Oversight/README.md#apts-ho-006-graceful-pause-mechanism-with-state-preservation) requires a platform to re-establish connections and re-validate scope before continuing.

## 11. Attribution, credit, and performance measures

The engagement result may count as program output when it satisfies the same authorization, evidence, review, and delivery requirements as other engagements.

Individual or team credit shall reflect accountable work and shall not reward unvalidated volume. An adopter may use effort, responsibility, complexity, or another locally approved model. Any weight or sampling parameter belongs in §90.4, not in this durable framework.

**For adopters that use contractors:** performance credit and payment are different decisions. Document the actual testing, validation, and delivery responsibilities, and apply the governing contract or statement of work. Do not treat an agent-led run as a full manual engagement for invoicing solely because the final report looks similar.

Measures should include quality, coverage, correction, operator burden, time returned, cost, unsafe or refused actions, and the work AI did not perform. Under volume, also measure the validation queue: its depth, the age of unvalidated candidates by triage band, and time to validate by triage band. The draft annex §90.5 defines these measures with their denominators. The program shall not use finding count, engagement count, or tool utilization alone as proof of value.

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
| Validation | What counts as qualified validation, critical/highest consequence, first-of-kind, and calibrating evidence? What validation capacity and maximum age apply (§9.4)? |
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

## Version notes

- **2026-11-10.** Added §8.6 (where automated checks run out), §8.7 (the validation package), a §9.4 paragraph on candidates escalated before validation finishes, integrity of agent-produced evidence in §10.5, and §10.6 (interruption, stop, and handoff); §8.1 gained an automation-bias caution.
- **2026-11 revision.** After independent review: "At a glance" moved to the top; "posture", "candidate" and "full validation" defined, with a shared [glossary](90-0-glossary.md); tool severity treated as a claim a person re-derives; machine-rejected, merged and duplicate states added, with evidence states shared with §20.13; attack-chain records (§8.5) and validation capacity and backpressure (§9.4) added; sampling object stated once; observable tier criteria, hosted-model drift and injection-assumed containment added. No floor was weakened.
