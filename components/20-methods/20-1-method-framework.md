# 20.1 — Penetration-testing method framework

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

This is an organization-neutral framework component. It is not an accreditation bar, permission to test, or evidence that any adopter operates these practices. Domain guides and templates named here are not represented as public until released and linked from an exact public index.

## What this component helps a team do

Use one coherent method to connect a permitted test to a defensible result without pretending that every target needs the same procedure. A team adopting this component should be able to answer five questions for a particular engagement:

1. What decision or security property is the test meant to inform?
2. Who authorized which target, identities, techniques, conditions, and limits?
3. Which domain method and test hypotheses suit that target?
4. What was observed, what was not established, and who challenged the interpretation?
5. How did the result reach the people who can act on it, and what changes before the next test?

The answers should be proportional to the engagement. A small, bounded retest need not produce a large design dossier. A complex system with several trust boundaries needs more than a checklist and a broad asset name.

This component is the umbrella. It does not replace the web, API, network, database, mobile, physical, secure-code, AI-target, or other tactical methods; the public library should link each available guide by version and mark missing domains plainly. It does not own vulnerability-management policy, incident response, legal authorization, risk acceptance, or another team's system of record.

## Choose the entry that matches your job

- **Building or improving a practice?** Use the engagement path below to expose the decisions your team already makes, then complete the local adoption profile. You do not need to adopt every supporting document before improving one handoff.
- **Planning or performing a test?** Start with the authorized target and the engagement design record, then use the current domain guide for technical depth. The umbrella keeps scope, safety, evidence, and review attached to that work.
- **Reviewing a result?** Start with the evidence and finding-decision sections. Follow one report claim backward to the test condition and authorization, then check what remains uncertain or untested.

If your question is solely about a post-test technical consultation or retest request, the separate consulting-service guide is the more direct entry. This umbrella explains how that service connects to the engagement; it does not duplicate its operating instructions.

## The engagement path

`select → authorize → scope → prepare → model → test → capture → review → communicate → retest → learn`

This is a reasoning path, not a mandate that every local workflow use eleven separate approvals or systems. A team may combine steps if it preserves the decisions and their evidence. Each step has a useful output and a boundary that cannot be skipped by renaming it.

| Move | Decision or output | Boundary to preserve |
|---|---|---|
| Select | Why this target and why now: obligation, change, exposure, prior result, business need, or another named driver | Selection does not authorize action. |
| Authorize | Who permits testing, for which targets and methods, under which constraints | A tool approval does not enlarge the engagement. |
| Scope | Exact systems, interfaces, environments, identities, workflows, exclusions, dependencies, and test conditions | A broad product name may hide a third party or a different production system. |
| Prepare | Access, test data, safe environment, contact and stop path, evidence location, time-sensitive coordination | Missing prerequisites become visible limitations, not silent coverage claims. |
| Model | The assets, trust boundaries, attacker capabilities, and security properties that matter | A threat catalog suggests questions; it does not establish local risk. |
| Test | Chosen domain method, hypotheses, safe actions, contrasts, and notes on untested paths | Professional exploration stays inside authorization; new impact or scope requires a new decision. |
| Capture | Reproducible observation with target, identity, state, action, result, and limitations | Tool output is not yet an accepted finding. |
| Review | Qualified technical judgment on truth, affected scope, consequence, uncertainty, and severity | Review can reject, merge, split, or request more evidence; disagreement is recorded. |
| Communicate | Report and conversation with the people who need to understand and act | Observed fact, inference, limit, and recommendation remain distinct. |
| Retest | Fresh test of the condition that supported the original finding | A ticket, version change, or inability to reproduce is not automatically proof of a fix. |
| Learn | The smallest justified update to scope prompts, a test, a method, preparation, review, or training | A single local exception need not become a program rule. |

The record can be one connected engagement package or several linked artifacts. The shape matters less than the ability to reconstruct the decisions.

### The smallest useful engagement record

Before testing, capture one connected record with these decisions. A team can place the fields in an existing intake, ticket, rules-of-engagement document, or brief; this is not a mandate for a new system.

| Decision | Write enough to answer | If missing |
|---|---|---|
| Purpose | What question will this test help answer, and for whom? | The test can become a collection of tool results without a relying decision. |
| Authority | Who permitted this target, environment, identities, methods, and impact ceiling? Where is the current record? | Do not treat selection, access, or prior permission as authorization. |
| Target model | Which components, workflows, users, data, trust boundaries, and dependencies matter? | Scope may look precise while hiding the actual path under test. |
| Test approach | Which domain method and hypotheses will be used, and what counts as meaningful evidence? | Coverage becomes a checklist claim rather than a test design. |
| Operating conditions | Are access, test data, monitoring, contacts, stop conditions, and evidence handling ready? | A missing prerequisite becomes a recorded limitation or a decision to pause. |
| Review and delivery | Who can challenge a candidate finding, who receives urgent notice, and where will the report and retest land? | The result can be technically correct yet unusable by the people who need it. |

The first pass can be short. Deepen the entries when target complexity, uncertainty, sensitive data, production impact, third-party reach, or the consequence of a wrong conclusion makes a short answer unsafe. The size of the record should follow the decision, not the size of the organization.

## Design the test from the target

The engagement's objective comes before its tool list. For each material test path, the tester can make a short test-design note:

> **Target and authorized identity:** Which component and role are being exercised?  
> **Property:** What should remain true?  
> **Hypothesis:** What action could violate it?  
> **Expected contrast:** What would a secure and an insecure result look like?  
> **Evidence:** What must be captured to decide?  
> **Safety:** What action would exceed the permitted impact or cross scope?  
> **Method source:** Which current domain guide or other source informs the technique?

That note is most useful where the result is ambiguous, consequential, novel, or likely to be challenged. Routine checks may be grouped. The method should record why a meaningful path was skipped or blocked, not force a form for every probe.

### One worked thread: an API ownership boundary

Suppose an authorized test includes a synthetic customer-record API, one nonproduction environment, and two test accounts that own separate records. The question is whether Account A can read Account B's object by changing an identifier. The scope record names the API version, endpoint, accounts, allowed test data, rate limit, and who to contact if the request reaches an unexpected service. Those are example fields, not a model authorization for anyone else's API.

The tester records the expected property: an account may read its own permitted object but not another account's. A baseline request under Account A succeeds for A's object. A request for B's object under A's session appears to return B's data. That is an observation worth pursuing, not yet a delivered finding. The tester checks token and account identity, object ownership, response provenance, caching, and whether the data is actually sensitive and in scope. A contrast under B's authorized session helps establish what changed with identity. If one of these facts cannot be resolved, the result remains a candidate or an inconclusive observation.

When the evidence holds, the reviewer can trace the conclusion to the requests, identities, target state, and authorization. The report can describe the affected path, reproduction conditions, impact, and limits. A later retest repeats the access boundary against the changed system. If the route is no longer reproducible but the environment or identity differs, the retest says so rather than silently calling the issue fixed.

The API field guide should carry the endpoint-discovery, authorization-testing, and protocol-specific depth. This umbrella carries the decisions and evidence relationship that would also matter in a database, cloud, or physical assessment.

## Evidence is a trail, not a screenshot quota

A finding candidate should preserve what acted against what: target version and state, identity and privilege, request or action, observed response, relevant control condition, reproduction path, and any cleanup or data-handling limitation. A screenshot may help a reader, but it rarely carries that context alone.

The review should keep these classes separate:

- a source fact from code, configuration, design, or documentation;
- a direct observation from the authorized test;
- output or interpretation from a tool or model;
- a hypothesis about why the behavior occurred;
- a finding accepted by a qualified reviewer for the next communication state; and
- a priority or risk decision made with local business context.

Neither a recognized weakness label nor a severity score substitutes for the local observation. The final report should tell its reader what the test supports and what it cannot: scope, perspective, work completed, material limitations, untested conditions, and the evidence behind each accepted finding. A negative test result is bounded evidence about the conditions tested, not proof that the system has no weakness.

### A finding decision a second person can inspect

For each material candidate, record a compact disposition: **accept, reject, merge, split, defer for more evidence, or report as inconclusive**. Preserve the reason. A reviewer should be able to answer which identity and target state produced the observation, what secure contrast was attempted, what alternative explanations were considered, whether the behavior is inside scope, and what consequence was actually demonstrated. A severity score can accompany that decision, but it cannot make it.

Do not smooth disagreement out of the trail. If the tester sees an authorization flaw and the reviewer suspects a test-data artifact, the next action is a bounded discriminating test or a stated uncertainty—not a prettier report sentence. This is especially important when a tool or agent generated the candidate, because the volume and confidence of generated text can make an unverified result look complete.

The report's coverage note should use ordinary language: what was tested, from which perspective, what was blocked or partial, and what the result does *not* establish. That note protects both the reader and the tester from a broader assurance claim than the work earned.

## People and handoffs are part of the method

The tester owns technical judgment on the test path, but they should not need to be the only person who can understand the result. A practice needs a way to peer-review difficult findings, escalate unsafe or disputed conditions, preserve the record, explain the result to the target owner, and support a legitimate retest after the engagement window.

Who performs each step depends on team size and consequence. A small practice may rotate qualified reviewers and consulting responsibility. A larger one may have dedicated capacity. This framework specifies the questions and handoffs; an adopter decides staffing, coverage, escalation, service expectations, and systems of record. When a finding indicates a broader pattern or a critical condition, the right response may involve security architecture, vulnerability management, incident response, business ownership, and others under local authority. The penetration-testing team does not silently inherit all those decisions.

Records should be protected, access-controlled, and retrievable under the adopter's policy. The public framework cannot set a universal retention period, storage system, notification tree, or release authority.

## Adapt the method without losing its spine

A team should record its local bindings once, in a short adoption profile. At minimum: testing authority and engagement authorization; scope and rules-of-engagement record; supported test domains; qualified testing and review roles; production and safety limits; evidence protection and retention; reporting and correction path; retest and local closure ownership; and a maintainer for method changes. If the team cannot identify one of these, that is a design question to resolve locally—not permission supplied by this document.

Two teams may satisfy those decisions differently. In a small practice, one tester may own the engagement and a qualified colleague may perform the review; consulting duty can rotate. In a larger enterprise, intake, scheduling, technical review, records, urgent response, and post-test support may have distinct owners and systems. Neither staffing shape is the framework's default. The common requirement is that a relying reader can identify who made each consequential decision and where the evidence went.

A practical adoption exercise is to take one recent or synthetic engagement and mark each handoff on the path above. For every move, ask **who decided, what record carried it, what a second person could verify, and what would happen if the normal owner were unavailable**. Keep the components that resolve a real ambiguity. Tailor or omit examples that add ceremony without improving the decision. Record an omission that narrows coverage or assurance; do not bury it in a local copy of the method.

The domain methods provide the technical depth. Existing industry material should be used by name and version where a test depends on it. CREST's programme guidance, OWASP testing guides, PTES, NIST SP 800-115, threat knowledge bases, and severity systems each serve different jobs. The Open Practice Framework is an adaptable implementation reference among them, not their replacement or an endorsement from them. A source list also does not prove coverage; the engagement record must show what was done.

The public index should make status obvious. A released guide is not the same as a private draft; an illustrative template is not a requirement; an old tool recipe should not silently remain current. Report errors and update the smallest affected component, with a visible version note when a reader's decision would change.

## Next extension: AI-infused testing

The baseline above describes a human-led practice. It applies whether a tester uses manual tools, scripts, scanners, or no AI at all. Two separate future-facing questions belong beside it:

1. **AI as a target:** what changes when the system under test uses models, retrieval, agent tools, generated content, or automated decisions? A target-specific method must address those attack surfaces without assuming every engagement contains them.
2. **AI as a testing capability:** what may an assisted or agentic tool read, propose, execute, capture, and send? What local authorization, isolation, monitoring, evidence, data handling, validation, and stop controls make that use defensible?

Neither question turns an agent's output into a finding. A versioned AI overlay can propose faster preparation and test exploration, while preserving human authority over accepted findings and all impact-bearing decisions. Its claims about speed, quality, cost, and staffing need observed measurements and comparison with the human-led baseline. No deployment or superiority claim is made here.

## Worked reader route

The [synthetic API engagement](../../examples/api-engagement/README.md) joins this umbrella to a bounded authority and scope, two identity contexts, an API-specific method, a test-design and evidence example, an untested question, a review decision, a report handoff, and a retest condition. It is a paper walkthrough, not an executed test or proof that an adopter's local practice works. Use it to challenge whether each component gives a tester, lead, or reviewer a decision they can follow without silently inventing authority.

### Copyable engagement thread card (illustrative)

Use this as a prompt in an existing record, not as a substitute for local approval or a domain method.

| Field | This engagement |
|---|---|
| Question and relying decision |  |
| Authorization record and accountable authority |  |
| Target, environment, identities, and explicit exclusions |  |
| Material trust boundaries and security properties |  |
| Domain method and planned test paths |  |
| Access, data, communication, safety, and stop conditions |  |
| Evidence location and reviewer |  |
| Candidate result and alternative explanations |  |
| Finding disposition and stated uncertainty |  |
| Report audience, urgent route, and retest path |  |
| Limitation or lesson for the next engagement |  |

The card earns its space only if it helps someone make or challenge a decision. An adopter may remove fields already carried reliably elsewhere, but should preserve the link between authorization, test, evidence, conclusion, and handoff.
