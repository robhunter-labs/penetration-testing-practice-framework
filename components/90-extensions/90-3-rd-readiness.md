# 90.3 — R&D Build and Readiness for AI Testing Capability

**§90.3 · R&D build & readiness for AI testing capability · Penetration Testing Practice Framework**

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## Reader headlines

**Primary audience:** Penetration-testing capability leads, technical builders, evaluators, safety reviewers, and leaders who decide whether an experimental capability may move into operational use.

**Objective:** Let a team investigate an AI-assisted or agentic testing capability inside a bounded R&D lane while making safety, measurement, authority, and the handoff to real engagement work unmistakable.

**Intended outcome:** A capability candidate is rejected, continued, adopted, adapted, built, or authorized from recorded evidence—not momentum, novelty, a successful demo, or tool provenance.

**This document defines:** The readiness stages, smallest-useful experiment, safety evaluation, intended-authority envelope, evaluation discipline, adopt-before-build decision, Delivery Authorization, rollback triggers, and evidence needed to move from research to operation.

## Document administration

| Field | Detail |
|---|---|
| **Document** | 90.3 |
| **Status** | Published framework component; local adoption is a separate decision. |
| **Type** | Standard |
| **Maintainer** | Framework maintainers |
| **Local approval authority** | Defined by the adopting organization |
| **Review trigger** | At least annually and on material capability, autonomy, threat, evidence, deployment, or authority change |

> [!CAUTION]
> This standard grants no authority to acquire, build, connect, deploy, or use a capability against a real target. An adopter shall bind its own R&D authority, environment, data rules, procurement route, independent reviewer, and operational approval before relying on a tailored version.

## Where this fits

§00.4 charters the capability-development lane. This standard makes its build and readiness mechanics usable. §90.1 governs a findings-producing AI capability after Delivery Authorization. §90.2 binds the resulting controls to one tool and deployment posture.

This standard governs evidence-building before operation. It is not a testing methodology, procurement approval, production change process, per-engagement authorization, or substitute for the adopting organization's software, AI, data, privacy, safety, and third-party governance.

The boundary is:

> **Readiness work establishes what the program knows. Delivery Authorization permits a declared capability to enter a bounded operating path.**

## At a glance

1. Start with a mission gap and a relying consumer.
2. Screen the smallest plausible option before building infrastructure around it.
3. Evaluate safety and intended authority before granting meaningful agency.
4. Prove the candidate on bounded targets with declared measures and negative cases.
5. Prefer adoption or adaptation when it meets the need.
6. Use one Delivery Authorization to cross from evidence-building to findings-producing operation.
7. Step back, contain, correct, or retire when the capability or its evidence changes.

Readiness stages are not repeated approval ceremonies. A sandbox is an environment, not a stage. A demo is evidence, not authorization.

## 1. Purpose and scope

This standard defines a proportionate path for evaluating AI-assisted, tool-using, or agentic penetration-testing capability. Conventional automation or advisory tools may be comparators or support-path candidates; their inclusion here does not turn every script or prompt into a controlled AI program.

It applies when a candidate may materially affect:

- how authorized testing is performed;
- what evidence or findings are produced;
- the privileges, credentials, data, tools, or network reach delegated to software;
- the safety, reproducibility, or defensibility of testing; or
- a recurring program workflow that warrants controlled adoption.

It does not require every script, prompt, note, or disposable experiment to become a controlled program artifact. Control shall attach to the smallest object that carries durable risk or decision value.

## 2. Defined terms

| Term | Meaning |
|---|---|
| **Capability** | A repeatable program ability that supports or performs authorized work. |
| **Capability candidate** | A tool, model, technique, automation, workflow, or composite system under evaluation. |
| **Readiness stage** | An evidence-bearing state used to decide what the program may learn next. |
| **Sandbox** | An isolated environment used by one or more readiness stages; not an approval state. |
| **Testing path** | A capability whose output may create, change, validate, prioritize, or substantively support an engagement finding. |
| **Support path** | A capability that assists work without generating or changing the substance of findings. |
| **Intended-authority envelope** | The explicit limit on the identities, actions, tools, targets, data, network reach, persistence, time, and cost delegated to a capability. |
| **Delivery Authorization** | The recorded decision that a declared findings-producing capability and posture may enter bounded engagement use under operating controls. |
| **Evaluation bench** | A separated set of targets, cases, answer keys, measures, and scoring logic used to test a candidate. |
| **Ground truth** | Evidence independent of the candidate that establishes what should be found, refused, or changed. |
| **Material change** | A change that can alter capability, authority, risk, evidence validity, or operating behavior. |

## 3. Operating principles

1. **Mission before machinery.** Name the capability gap, decision, and relying consumer before selecting a tool, model, or architecture.
2. **Adopt before build.** Evaluate existing options before accepting the continuing cost of a fork or internal build.
3. **Contain first.** Unknown capability begins with minimum trust, synthetic or controlled data, limited reach, observable behavior, and explicit stop conditions.
4. **Measure before belief.** Pre-register the important acceptance, rejection, and comparison rules before seeing the result.
5. **Origin is not readiness.** Commercial, open-source, internal, forked, and AI-authored candidates enter through the same consequence-based evidence path.
6. **Least agency.** Increase autonomy, privilege, data access, network reach, persistence, and cost only when the next experiment requires them.
7. **One operational handoff.** Screening and evaluation help the team know; Delivery Authorization is the findings-producing operating decision.
8. **Controls live at the lowest effective layer.** A component or configuration change stays local unless it changes shared authority, infrastructure, or operational risk.
9. **Failure must be observable.** A capability without meaningful logs, stop behavior, rollback, correction, and retirement paths is not ready for trust.
10. **Uncertainty remains visible.** A missing answer, untested class, or unverified claim shall not become a zero, a pass, or a clean-looking audit trail.

## 4. Readiness model

| State | Decision answered | Minimum evidence | Allowed next move |
|---|---|---|---|
| **Need framed** | What capability and consumer justify work? | Problem, intended outcome, constraints, non-goals, and stop rule | Screen candidates or close the need |
| **Screened** | Is the candidate plausible and permissible to evaluate? | Identity, provenance, license/terms, architecture sketch, data/egress needs, and known blockers | Reject or enter safety evaluation |
| **Safety evaluated** | Can the next bounded test run without exceeding declared authority? | Intended-authority envelope, containment proof, abuse cases, dependency posture, stop/rollback evidence | Reject, correct, or run bounded proof |
| **Bounded proof** | Does the candidate produce useful evidence under declared conditions? | Ground truth, actual-consumer run, negative cases, measured results, limitations, and reproducibility evidence | Reject, continue, adopt, adapt, or propose build |
| **Delivery authorized** | May this exact capability posture enter findings-producing engagement use? | Independent decision, operating procedure, scope of authorization, residual risk, monitoring, expiry/review trigger, and rollback | Enter §90.1 operating controls |

### 4.1 Stages are evidence states

An adopter may combine or repeat readiness work when risk and learning justify it. The model shall not create a separate executive approval for every experiment by default.

Approval attaches to actual authority and consequence. Examples include acquiring a paid service, connecting to a protected network, using restricted data, granting high-impact actions, or crossing into findings-producing use. Where another organizational process already owns that decision, this standard shall reference and reuse it rather than build a competing gate.

### 4.2 Support-path release

A support capability that cannot generate or alter finding substance does not enter the §90.1 testing cascade merely because it uses AI. It shall still satisfy applicable secure-development, data, access, records, change, and acceptable-use controls.

If its behavior changes so that it can create or modify finding substance, it shall be reclassified and may not continue under the support-path exception.

## 5. Start with the smallest useful experiment

The first experiment should answer one consequential uncertainty with the least apparatus that can produce credible evidence.

A lean initial proof should normally use:

- one declared capability question;
- one or a small number of candidates;
- synthetic, deliberately vulnerable, or otherwise controlled targets;
- minimum privileges and deny-by-default connectivity;
- a frozen manifest of the candidate and its configuration;
- a known-answer or independently observable outcome;
- a bounded time, action, and cost budget; and
- one continue, change, or stop decision.

A heavier lab, full automation, broad inventory, or permanent platform must be earned by repeated use, material consequence, or a decision that the lighter path cannot support. Tooling sophistication shall not become a proxy for readiness.

### 5.1 One useful containment pattern—and what it cannot promise

This guide describes two network states: **A**, isolated evaluation with simulated or blocked external services; and **B**, a separately reviewed, logged, allowlisted connection to a named nonproduction environment. An adopter may implement those states with different technology, but should preserve the decision they expose. State A tests behavior under isolation. A State-A disposition does **not** certify State-B behavior or grant a live-target route. State B needs its own data-flow, network, target-owner, privacy and deconfliction decisions where applicable. A system owner's “nonproduction” attestation is useful context, not independent proof that no production dependency or data can be reached.

A particular type-2 hypervisor, two-VM, build-as-code and managed-host setup is **one local implementation**, not a portable recipe. A host with real credentials and corporate reach makes guest escape consequential. A local design should record what the host can reach, what the candidate can reach, how the egress detector is self-tested, where evidence persists after a snapshot revert, and which events ground the experiment. A smaller host-only synthetic proof can be right for an early decision; a mature two-environment apparatus is earned when its distinct safety or reproducibility value is demonstrated. Neither setup is described as containment guaranteed.

## 6. Safety evaluation

Before a candidate receives meaningful action authority, the evaluator shall examine at least:

| Concern | Required question |
|---|---|
| Candidate identity | What exact version, image, model, prompt set, configuration, adapter, and tool bundle is being evaluated? |
| Provenance and supply chain | Where did each decision-bearing component come from, under what license or terms, and how is its integrity checked? |
| Data and egress | What data can enter or leave, through which endpoints, and is training, retention, telemetry, or third-party processing involved? |
| Credentials and secrets | Which identities or secrets are available, how are they scoped, and can the candidate reveal, persist, or misuse them? |
| Action reach | What can the candidate read, write, execute, alter, delete, purchase, publish, or contact? |
| Target and scope | How is the authorized target represented at the point of action, and what happens when scope is ambiguous? |
| Agent integrity | How can prompt injection, poisoned context, malicious output, tool substitution, or runtime mutation change behavior? |
| Failure and containment | Can the evaluator stop the run, preserve evidence, revoke access, restore state, and detect a fail-open? |
| Evidence quality | Are outputs reproducible, attributable, time-bound, and distinguishable from the candidate's own claims? |
| Cost and abuse | What bounds compute, model calls, tool invocations, time, storage, and externally billable actions? |

### 6.0 The tool is an untrusted actor, not only a package

Treat a candidate offensive agent as both potentially evasive software and an actor that can choose actions. That is the useful threat-modeling move. Evaluate at least: environment-aware behavior; delayed behavior beyond a short observation window; guest-to-host or container-to-host escape; credential access; undisclosed destinations; prompt injection from the target being tested; and out-of-scope or destructive action taken without an explicit order.

No finite lab run proves a tool safe in every later environment. A sinkhole can observe and route an attempted connection without preventing the information content of the attempt; a synthetic target may elicit different behavior from a live nonproduction one; a hypervisor or host boundary may fail. Name the residual risk and the person accepting it for the *next bounded use*. “Not observed in these runs” is a narrower and more honest result than “safe.”

Build the safety examination from four independent lenses:

1. **Static and supply-chain review:** identity, pinned dependencies, install/build hooks, dangerous primitives, obfuscation, provider endpoints, license and update path. A scanner report is an input, not ground truth about every behavior.
2. **Instrumented dynamic run:** observe process, file, network and credential access while the candidate acts on a synthetic target with no unapproved real egress. Include a detector self-test that would expose a blind packet or event capture path.
3. **Adversarial target behavior:** offer injection-bearing target content, an out-of-scope pivot, and a destructive opportunity; record whether the tool refuses, stops, seeks authorization, or acts. Treat the target's content as data, not instructions.
4. **Repeated and changed-condition runs:** vary conditions enough to discover unstable or delayed behavior; report the actual number of runs and the worst observed action. Do not use a zero-incident count from a dead or narrow detector as a safety score.

A qualified human signs a **bounded safety disposition**—proceed to the named next experiment, proceed with conditions, or reject/stop—against the instrumented evidence and its blind spots. An LLM may help summarize source and telemetry but cannot sign or upgrade its own safety verdict, particularly when it reads attacker-controlled input. Credential access, unexplained egress, containment failure, or authority-envelope exceedance stops the affected run and triggers the local response; the consequence is judged from observation, not an automatic one-size-fits-all incident label.

### 6.1 Intended-authority envelope

The envelope is the explicit specification to compare with observed behavior. Its important limits should also have preventive or stopping controls close to the action where feasible, not merely a prompt. It shall declare:

- permitted targets and exclusions;
- permitted actions, tools, and protocols;
- identity, role, and privilege limits;
- readable and writable data classes;
- network and endpoint allowlists or deny rules;
- persistence, memory, and artifact-retention limits;
- human pre-authorization points for irreversible or high-impact actions;
- time, iteration, rate, and cost bounds;
- stop conditions and the role empowered to stop; and
- evidence proving that enforcement was active.

An observed envelope exceedance stops the current run. It is not deferred to a later readiness decision.

The envelope is a *specification and a detectable comparison*, not by itself a preventive control. Enforce limits at the network, identity, tool, policy and action layers that actually govern behavior, then verify those controls under a known-bad attempt. If an observed action violates the intended envelope at screening, safety evaluation, or bounded proof, stop there; do not postpone the breach until Delivery Authorization.

### 6.2 Composition evidence at the lowest useful object

The program shall be able to identify the deployable or decision-bearing unit that is evaluated and later authorized. It should inherit valid upstream SBOM, ML-BOM, provenance, signature, or vendor evidence when available.

This standard does not require a manual, program-wide living BOM for every experiment. Composition depth shall increase when the candidate is materially modified, broadly reused, distributed, granted privileged or autonomous action, exposed to sensitive data, or used to generate accepted findings.

## 7. Evaluation and benchmark discipline

The evaluation shall separate the candidate from the truth used to judge it.

### 7.1 Evaluation contract

Before the decision-bearing run, record:

- the actual consumer and decision;
- the candidate identity and comparison set;
- target strata and what each stratum proves;
- ground truth and how it is protected from the candidate;
- accepted output schema and abstention behavior;
- pass, fail, and stop thresholds;
- positive and negative cases;
- repeatability or replay rule;
- treatment of false positives, false negatives, unsupported claims, and unsafe actions; and
- how uncertainty and untested coverage will be reported.

### 7.2 Measures

Measure the failure modes that matter to the mission. For a discovery capability this will normally include precision, recall or another missed-coverage measure, false-positive rate, verification depth, reproducibility, unsafe-action rate, abstention, cost, and operator burden.

No single score shall decide alone. The decision record shall preserve material contradictions—for example, high discovery with unsafe action reach, low false-positive rate with poor recall, or strong synthetic performance with an unmeasured real-environment gap.

Keep synthetic, deliberately vulnerable, and authorized nonproduction results **separate**. A synthetic suite can show whether cases are found under known conditions; it may be a poor predictor of a different application's architecture, data or controls. A nonproduction proof adds realism but only within that environment's actual authority and observable truth. Do not blend them into one flattering headline. Precision, recall or false-positive/false-negative rates require a living, independent answer key and a stated denominator; where the answer key is incomplete or a detector fails its self-test, report `unknown` rather than a manufactured zero. Report abstentions and untested cases alongside successes.

For a comparison or adopt-versus-build decision, fix the candidates, target strata, primary metric, safety stop, cost model and decision margin *before* reading the results. No single architecture—one agent, planner/executor, specialist agents or a deterministic pipeline—wins by name. A specific score formula and adapter limits are a local bench design; a public adopter must specify and verify its own measurement contract rather than inherit numbers without the corresponding oracle.

### 7.3 Evidence strength

Candidate-generated narration is not ground truth. Stronger evidence includes independently observable target state, deterministic replay, external logs, signed or hashed manifests, controlled seeds, and review by a person who did not build the decision-bearing behavior.

An evaluation may say “not observed” or “insufficient evidence.” It shall not say “safe,” “clean,” or “complete” merely because a detector remained silent.

### 7.4 A bounded first run (fictional)

A team wants to know whether a tool can identify a known authorization weakness without acting outside scope. It records the candidate version and configured model/tool stack, chooses a local deliberately vulnerable API fixture with an independent answer key, and locks one positive case, one negative case, a target-origin prompt-injection attempt, a prohibited network destination and a stop condition. In State A, the operator proves the egress detector detects a known-bad attempt before relying on it, then runs the candidate under observation. The reviewer compares raw requests and target state with the answer key, records false claims and missed cases, and signs a bounded **continue/change/stop** disposition. Nothing about that run permits connecting the tool to an organizational application or counting its output as an engagement finding. A later State-B nonproduction proof and Delivery Authorization are separate decisions.

## 8. Adopt, adapt, build, or stop

Adoption is the default comparison, not the automatic outcome.

Before committing to an internal build or long-lived fork, the decision maker shall compare at least:

- mission effectiveness and coverage;
- safety and governability;
- integration and operator burden;
- inspectability and correction speed;
- licensing, provenance, and supply-chain posture;
- recurring compute, service, support, and maintenance cost;
- portability and exit cost; and
- the consequence of doing nothing.

A build decision shall be explicit and separate from successful experimentation. It shall identify the capability gap external options did not meet, the evidence supporting the decision, the maintained execution model, the accountable owner, and the expected continuing cost.

Architecture shall follow evidence. A single agent, planner/executor, specialist swarm, deterministic pipeline, or hybrid may be appropriate. Tool protocols and model interfaces are components, not architectures by themselves.

## 9. Delivery Authorization

Delivery Authorization is the one framework decision that transfers a findings-producing capability from readiness work into bounded operational use.

The record shall identify:

1. the capability and exact operating posture authorized;
2. the testing path and permitted engagement classes;
3. the autonomy tier under §90.1;
4. the operating procedure under §90.2;
5. the approving role and its local authority basis;
6. the evidence and residual risks relied upon;
7. required operators, validation, monitoring, data, and environment controls;
8. prohibited uses and additional-authorization triggers;
9. material-change, review, expiry, suspension, and revocation conditions; and
10. the rollback or containment path.

The authorization shall not expand program authority or an engagement's rules of engagement. A capability may be ready and still not be permitted on a particular target.

## 10. Material change, regression, and revocation

A material change shall step the candidate back to the earliest readiness state whose evidence may no longer be valid. Triggers commonly include:

- a new model, tool, image, dependency, adapter, prompt policy, or execution architecture;
- changed privileges, network reach, data classes, persistence, or target type;
- a failed regression or reproducibility run;
- an integrity, injection, egress, scope, or unsafe-action event;
- a changed provider term, license, vulnerability, or external dependency;
- unexplained drift in precision, recall, abstention, cost, or operator burden; or
- a finding correction or incident that challenges the authorization basis.

Delivery Authorization shall be suspendable and revocable. Operational use shall not continue while a material safety or authority question is unresolved.

## 11. Required records

The readiness record should be as small as possible while preserving the decision:

- capability-need statement;
- candidate and provenance manifest;
- safety evaluation and intended-authority envelope;
- evaluation contract, raw results, and negative cases;
- adopt/adapt/build/stop decision;
- material exceptions and compensating controls;
- Delivery Authorization where applicable;
- per-tool operating procedure;
- change, regression, incident, correction, and retirement records; and
- lessons that alter the evaluation method or durable control set.

The program shall not reconstruct approvals, dates, runs, or evidence after the fact. Missing evidence remains missing.

## 12. Adoption profile

Before placing a tailored version In Force, the adopter shall bind:

| Binding | Local decision required |
|---|---|
| R&D authority | Who may conduct which classes of contained evaluation? |
| Environments | Which environments, targets, data, identities, and network paths are permitted? |
| Review independence | Who supplies the decision-bearing independent review? |
| Procurement/build authority | Which existing systems own spend, acquisition, fork, and long-term build commitments? |
| Delivery authority | Who may authorize findings-producing use, for which engagement classes? |
| Evidence store | Where do manifests, results, decisions, exceptions, and incidents live? |
| Material-change triggers | Which changes require regression, reauthorization, suspension, or retirement? |
| Operating link | How do §90.1 and §90.2 become binding after delivery? |

An unbound field is an open adoption item, not implied authority.

## 13. Assurance evidence

Evidence that this standard is operating may include:

- rejected candidates and stop decisions, not only successful pilots;
- tests that demonstrate envelope enforcement and fail-closed behavior;
- evaluation results with ground truth, negative cases, and limitations;
- decisions that adopted an external option or declined to build;
- Delivery Authorizations that name exact postures and expiry conditions;
- material changes that visibly stepped a capability back;
- incidents, corrections, suspensions, and retirements; and
- measured R&D lead time and governance burden without hiding safety failures.

Document presence establishes only that the control is defined. It does not establish that a capability is safe, effective, authorized, or operating.
