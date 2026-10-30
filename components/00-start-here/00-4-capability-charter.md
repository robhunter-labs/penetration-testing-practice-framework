# Developing the Next Testing Capability

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A penetration-testing practice needs to improve its methods and tools without letting a promising experiment quietly become trusted delivery machinery. This charter gives a practice lead and capability builder a usable boundary: research is one kind of work; using a capability to influence a real engagement is another.

It is an adaptable capability-development pattern, not permission to acquire a tool, access a network, test a system, use customer data, publish a finding, or operate an AI agent. Those decisions belong to the adopter's accountable authorities and to the particular engagement.

## The two jobs

1. **Deliver credible testing.** The practice's central work is authorized testing, careful validation, clear reporting, and useful handoffs. People, methods, evidence, and review matter more than the novelty of a tool.
2. **Develop capability that improves that work.** The practice can investigate new tools, techniques, environments, and support workflows—including conventional automation and AI-assisted or agentic approaches—when they address a real testing or operating need. This is a supporting investment, not an independent product mission.

An adopter should state its own mandate, decision owners, resource limits, and research environments before using this pattern. A public framework cannot confer those powers.

## Begin with a capability question

Describe the work that is difficult now, who relies on a better result, and how improvement would be recognized. Separate three possible outputs:

| Lane | What it may do | Boundary to watch |
|---|---|---|
| **Testing capability** | Select or execute test actions, affect target state, produce engagement evidence, assist validation, or contribute to a reported finding. | Requires a capability-to-delivery decision before operational use, plus the particular engagement's scope and rules. Tool output does not validate itself. |
| **Support capability** | Help with intake, scoping preparation, documentation, scheduling, evidence organization, or report drafting without deciding tests or findings. | Still needs applicable security, data, software, and change controls. Reclassify if its actual use starts directing testing or determining conclusions. |
| **Tradecraft research** | Explore a test idea, threat hypothesis, method extension, or evaluation approach. | Research results are not automatically approved methods or engagement findings. |

Classify by *observed behavior and intended use*, not by a product name or whether AI helped write its code. A report-formatting assistant that only rearranges supplied text can be a support capability; an agent that chooses API actions, uses credentials, or asserts vulnerabilities is on the testing path even if marketed as an assistant. An automation can move lanes when its permissions or use change.

## Research-to-delivery path

The stages below are a decision aid. They do not replace any local approval required for acquisition, data, network reach, non-production access, or operational deployment. The sandbox is an environment, not a magic approval state.

| Step | Question | Evidence or disposition |
|---|---|---|
| 1. Frame and screen | What capability is missing? Which existing options deserve a fair comparison? Is the candidate's origin, license, behavior, and dependency surface understandable enough to evaluate? | Named consumer and success question; candidate/version; reject, compare, or admit to bounded evaluation. |
| 2. Observe safety in isolation | What does the candidate actually access, write, call, retain, or send? What happens when it fails or receives hostile input? | Instrumented observations, constraints, negative cases, stop path, and a decision to reject, constrain, or continue. Unknown code does not gain production reach by being open source. |
| 3. Test against known cases | Does it perform the claimed task under a reproducible, independently checkable test? What false alarms or misses matter? | Declared cases and expected results, measurement limits, operator burden, and comparison with the strongest viable adopt/adapt/build alternative. |
| 4. Prove a bounded use | Can it work on an explicitly authorized non-production surface without breaking scope, safety, or evidence rules? | Exact authorization and target; configuration; observations; deviations; decision to iterate, stop, or request operational use. Non-production does not imply permission. |
| 5. Authorize delivery | Under which exact version, configuration, target class, autonomy, people, data, and conditions may this testing capability be used in real engagements? | A local accountable decision with evidence, limits, human validation, monitoring, stop/rollback, update triggers, and effective state. Separate engagement authorization still applies. |

A team may revisit a step or stop. Stage completion is evidence about readiness, not an automatic license to advance. “It worked in a lab” and “a human looked at the output” do not answer the delivery question by themselves.

## Adopt, adapt, build—or decline

The sourcing choice is distinct from readiness. A built tool and an adopted tool both need evaluation; a familiar vendor does not inherit trust. Start with existing options because building creates maintenance obligations, but do not make “adopt” an unexamined rule. A fork or new build may be justified by measured capability, integration, control, transparency, maintainability, or other local constraints.

For a consequential choice, record the strongest viable alternatives, the same test cases and measures, safety and legal constraints, ownership cost, and the result that would change the decision. Keep the answer key or judging method separate enough that a candidate cannot define its own success. Record what remains unknown. Cost, license, provenance, and supportability are part of the decision—not afterthoughts and not substitutes for technical performance.

## The capability-to-delivery decision card

Complete this locally for a *testing* capability. It is not a universal approval form, and a support tool may need a different operational decision under local policy.

| Decision field | Local answer |
|---|---|
| Capability and relying engagement use |  |
| Exact version, configuration, dependencies, model or rules, and origin |  |
| Authorized action reach, target classes, data, credentials, network, and persistence |  |
| Evaluation cases, observed results, false alarms/misses, unsafe behavior, and limitations |  |
| Qualified operator, independent challenge, human finding-validation responsibility |  |
| Monitoring, stop, incident, rollback, update and retirement triggers |  |
| Permitted, conditional, and prohibited uses; residual risk and owner |  |
| Local authorizer, decision, effective version/state, and evidence pointers |  |
| Relationship to engagement authorization and reporting review |  |

An independent challenge should be proportionate to the consequence and strong enough to reject the candidate. The operator should not be the sole witness to a claim that the tool is safe or its findings sound. A changed model, connector, permission, action policy, data path, or target class can invalidate the original decision; re-evaluate what changed rather than silently inheriting approval.

## Two changes of lane

*Fictional examples; neither describes an operational deployment.*

- A local assistant first formats a tester's already-written notes. It has no target access and does not decide findings. It belongs on the support path, subject to local data and software controls. Later, it begins proposing severity and inserting unreviewed report language. Its use has changed; a practice lead reclassifies and reviews the evidence and human-control boundary before relying on it.
- An API-testing agent performs well in synthetic cases but uses a credential outside the declared test identity during a non-production trial. The team stops the trial, preserves the restricted evidence, and follows its incident/safety route. That observation is not cured by a high benchmark score or by a later prompt change. A new bounded evaluation and accountable decision would be needed before any delivery request.

## Interfaces and limits

- **§00.3, §10.1 and §10.2** hold the authority, scope, and engagement rules. This charter adds no testing permission.
- **§90.3** carries build, bench, safety, and readiness decisions; **§90.1** addresses AI-assisted and agentic operation. Use them with this charter. Their presence in the framework does not mean an adopter has deployed either capability.
- **§20.1 and domain methods** govern human-led testing; **§30.5** governs the reviewed report. A capability does not replace either method or finding accountability.
- **§60.1** receives lessons from real use or failed evaluation and routes a justified change back to the smallest responsible component.

The framework provides an inspectable pattern; it cannot attest that any adopter has staffed, approved, tested, or operated this capability lane. A maintainer should revise this component when its source assumptions, connected methods, technologies, or a real consumer challenge change.
