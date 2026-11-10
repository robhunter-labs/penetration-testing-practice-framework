# 90.0 — Section 90 Glossary

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

**Component:** shared vocabulary for §90.1–§90.5 and the evidence states in §20.13
**Reader:** anyone opening the AI and R&D extensions for the first time

## Why this page comes first

The AI extensions reuse a small set of terms. Each term is defined here, in the order a reader usually meets it. Components may repeat a definition for convenience, or add a narrower meaning for their own use; where they narrow it, they say so, and this page stays the default.

## Terms

| Term | Plain definition |
|---|---|
| **Engagement** | One authorized penetration test of defined targets. |
| **Scope / rules of engagement** | What may be tested, how, when, and by whom (§10.1, §10.2). |
| **Adopter** | The organization tailoring this framework for its own use. |
| **AI as target vs AI as tool** | Testing an AI system (§20.13) versus using AI to do the testing (§90.1–§90.5). |
| **AI-assisted testing** | AI suggests content or actions; a person directs each meaningful step. |
| **Agentic testing** | Software plans and carries out multi-step actions itself, using delegated tools or authority. |
| **Composite system** | The model plus its orchestration, prompts or policies, memory, tools, credentials, retrieval sources, adapters and network access. It is what gets classified, not the product name. |
| **Posture** | One specific configuration and deployment of a composite system: its components and versions, where it runs, what it may reach, which identities it holds, and how it is bounded. A materially different posture is a different thing to evaluate and authorize. |
| **Configuration digest** | A cryptographic fingerprint over the posture's decision-bearing parts (see §90.2 §1). A version label alone is not a digest. |
| **Testing path / support path** | Whether the AI can create, change, validate, prioritize or substantively support a finding (testing path), or only helps with administration (support path). |
| **Finding substance** | The vulnerability claim, affected scope, exploitability, impact, severity, evidence, or the decision to communicate it. |
| **Autonomy tier** | 0 to 3: how much of the authorized testing loop the AI performs (§90.1 §6). |
| **Intended-authority envelope** | The written limits on what a capability may touch and do: targets, actions, identities, data, network reach, persistence, time and cost (§90.3 §6.1). |
| **Least agency** | Give the capability only the access and autonomy the task needs. |
| **Prompt injection** | Content the AI reads that changes what it does. *Direct* when typed by a user; *indirect* when hidden in material the AI retrieves or is shown, including target output. |
| **Agent integrity** | Whether the running system is still the one that was evaluated, and whether hostile input can redirect it. |
| **Readiness stage** | An evidence checkpoint between an idea and real use (§90.3 §4). |
| **Delivery Authorization** | The single recorded decision allowing an exact findings-producing posture into bounded engagement use (§90.3 §9). |
| **Candidate** | Something a tool or tester proposes as a finding, including the tool's own severity, before a qualified person has decided it. A reason to look, not a conclusion. |
| **Finding** | A candidate that a qualified person has validated and accepted for delivery. |
| **Validation** | The work that turns a candidate into a finding, or rules it out. |
| **Full validation** | A qualified person establishes the finding's affected scope, behavior and impact from evidence they have examined directly. The evidence may come from the person's own reproduction or from an independent replay (below); in either case the person decides. It is not a review of the tool's narrative. |
| **Independent replay** | Re-running a candidate's request or action under control, by a verifier that does not share the finding tool's context or memory, judged against an oracle the tool cannot write to (for example an out-of-band callback, a planted canary, or target state observed by something other than the tool). Replay against a live target is testing and needs the same authority. |
| **Qualified human validation** | Validation by a person the adopter has authorized and judged competent for that target class and finding type. |
| **Evidence state** | How far a candidate's evidence has reached, recorded as two parts (§20.13): **repeatability** (*Observed*, then *Reproduced*) and **impact** (*Demonstrated impact* or not). Anything further is *Possible, not tested*. A claim never exceeds what both parts support. |
| **Tool severity / validated severity** | The severity the tool proposes (a claim) versus the severity a qualified person derives from the evidence (the decision). |
| **Triage band** | The higher of the tool's severity and the human triage severity, used for validation depth and sampling eligibility until full validation settles the severity. |
| **Attack chain** | Several weaknesses used together, each step enabling the next. Each step records its own repeatability and impact; the chain's claimed impact never exceeds its weakest proven step, the step lowest on either part (§90.1 §8.5). |
| **Sampling** | Directly validating only a randomly selected subset of eligible candidates within a stratum, allowed only after full validation has earned it (§90.4 lever 1, §90.5). The sampled object is always the direct reproduction of candidates, never the human decision to deliver. A sampling *failure* is a candidate where the reduced-depth decision on reality or severity band would differ from full validation. |
| **Validation capacity** | The qualified validator hours available for an engagement or period, compared with the candidates a run is expected to produce. |
| **Backpressure** | Slowing, pausing or narrowing a run when unvalidated candidates exceed the declared backlog threshold (§90.1 §9.4). |
| **Ground truth / answer key (oracle)** | Independent knowledge of what should be found, refused or changed. A *living* answer key is current and checked; a *stale* one has not been checked since the target or method changed; a *dead* one no longer reflects reality or failed its self-test. Results that depend on a dead key are `unknown`. |
| **Oracle (check)** | A check whose answer comes from outside the model, read by code the tool did not write and cannot change: a sanitizer report, a callback confirmed to come from the target, a planted flag, or execution a browser confirms (§90.1 §8.6). Distinct from an answer key, which says what should be found. Some passages also use *oracle* for an answer key (row above; §90.3 §2), and a *living oracle* (§90.4) is a living answer key; elsewhere in Section 90, *oracle* means this check. |
| **Merge / group** | A *merge* says two candidates are the same exposure: the same weakness at the same affected instance. A *group* keeps distinct affected instances that share a root cause or a fix under one unique issue, each with its own evidence or marked inferred (§90.5 §1). |
| **Validation package** | One versioned record per candidate, in six parts (claim, oracle output, replay, controls, expected difference, retest), each labeled *observed*, *asserted*, *decided* or `unknown`, on which a qualified person rules (§90.1 §8.7). The label says where a part came from; the evidence state says how far the evidence reached. |
| **False positive / miss; coverage assurance** | A reported candidate that is not real versus a real issue the capability did not report; coverage assurance is the separate job of estimating misses. |
| **Material change** | Any change that can alter behavior, authority, risk or the validity of earlier evidence, and so requires re-evaluation. |
| **Floor vs lever** | A rule no local setting can waive, versus a local setting chosen within it (§90.4). |

## Reading order

1. §90.1 "At a glance", its defined terms and its autonomy tiers.
2. §90.3, starting from its worked example (§7.4).
3. The rest of §90.1.
4. §90.2.
5. §90.4, then the draft measurement annex §90.5.
6. §20.13, as a separate track: it covers testing AI systems, not testing with AI.

## Version notes

- **2026-11-10.** Added *merge / group* and *validation package*.
- **2026-11-08.** Added *oracle (check)*.
- **2026-11 — new.** Added as the shared vocabulary for Section 90 after independent review found key terms used before, or without, definition.
