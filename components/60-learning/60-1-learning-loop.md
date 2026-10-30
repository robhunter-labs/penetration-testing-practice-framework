# Learning That Changes the Practice

**§60.1 · Practice learning & continuous-improvement loop · Penetration Testing Practice Framework**

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

An excellent report can be reviewed and delivered without changing what the next engagement does. This guide is for the other job: turning a useful observation about the *practice* into a decision, a tested change when warranted, and a record someone else can follow. It does not replace incident response, report quality review, or an adopter's change authority.

## Use this when

A tester, reviewer, practice lead, partner, metric, retrospective, incident review, or external development exposes a possible improvement to a method, template, tool, training exercise, or handoff. A finding in one report is not automatically a practice defect. Conversely, a dangerous method instruction may need immediate containment rather than waiting for a scheduled retrospective.

This is a pattern to tailor, not a prescribed meeting cadence, staffing model, ticket system, escalation interval, or accreditation claim. The adopter chooses who can approve and release changes, where restricted records live, and which events demand urgent action.

## The loop in six decisions

| Decision | Ask | Minimum record that survives the handoff |
|---|---|---|
| 1. Capture | What was observed, by whom, in which bounded context? | A short description, source pointer, date or version, and sensitivity label. Keep client and personnel detail in their authorized store, not in a broadly shared improvement log. |
| 2. Triage | Is there an active safety, scope, evidence-integrity, or delivery problem? | Route urgent containment to the adopter's existing authority and incident paths. Record the handoff; do not make this guide the incident commander. |
| 3. Diagnose | Is the cause a method, local execution, training, tooling, or an unresolved question? What else could explain it? | Hypothesis, evidence, affected component or workflow, counterexample, and the person who will decide the disposition. |
| 4. Decide | Change, test a proposal, seek more evidence, accept a local exception, or make no change? | Decision, reason, accountable owner, target component, and conditions that would reopen it. “No change” is a legitimate, visible result—not a silently closed suggestion. |
| 5. Implement and verify | Did the approved change actually reach the intended consumer? | Versioned change or artifact link, approver/reviewer where required, a focused consumer check, limitations, and a rollback or correction route. An edited file alone does not prove improvement. |
| 6. Revisit | Did it help, introduce a new failure, or age out? | Outcome at an adopter-chosen review point, feedback from the next relevant use, and any follow-on item. Keep unresolved work visible. |

The change can land in a method, rules of engagement, scoping form, evidence practice, report template, training, tooling, or a partner handoff. The right landing place follows the diagnosed cause, not the source of the complaint. A report correction still follows the report's own correction route; this loop captures the broader practice lesson, if one exists.

## A small record you can adopt

Use an existing issue system or a simple table. The fields matter more than the product.

| Field | What to record |
|---|---|
| ID and source | A stable local key; retro, incident review, tester observation, peer review, metric, partner feedback, or external source. |
| Observation and protected pointer | What happened, with a reference to restricted evidence rather than copied secrets or client data. |
| Proposed change and alternate explanation | The smallest plausible improvement and what would make it unnecessary or wrong. |
| Target and owner | The method, form, tool, training, or handoff; one accountable decision owner. |
| Disposition and state | `new`, `investigating`, `decided-no-change`, `approved`, `in-change`, `verification-needed`, or `closed-verified`, adapted to local workflow. |
| Decision and release proof | Reason, approval when locally required, changed version/link, consumer check, remaining limitation, and correction route. |
| Revisit trigger | A next relevant engagement, reference change, repeated signal, or locally chosen review point. |

Do not mark an item `closed-verified` merely because a meeting ended, a ticket moved, or a change was merged. If the change was made but its effect has not been observed, `verification-needed` is the honest state. A rejected or no-change item can close with the decision and reopen condition; it does not masquerade as implemented improvement.

## Worked example: an API ownership fixture

*Fictional example; it describes no real engagement or deployed practice.* A two-account API test returns a record to the other account, but the test packet does not establish whether the record was intentionally shared. The reviewer withholds a broken-object-authorization finding because the missing ownership rule makes the interpretation inconclusive. That is a sound report decision, not a failure to find enough vulnerabilities.

The team records a separate practice question: did the scoping form ask the service owner for an explicit unshared-record fixture and the identity/ownership mapping needed for the planned contrast? A useful improvement item might look like this:

| Field | Fictional entry |
|---|---|
| Source | Reviewer challenge of the synthetic API test; restricted evidence pointer `E-SYN-3`. |
| Hypothesis | The form allowed “two accounts supplied” to stand in for a confirmed ownership rule. |
| Alternative | The form already asked; the owner response was omitted during this engagement. Check the actual completed form before changing the template. |
| Decision | If the question was absent, add a conditional fixture/ownership prompt to §10.4 and clarify the precondition in §20.3. If it was present, address execution or review instead. |
| Consumer check | Have a tester plan both an allowed and denied read using a fictional, explicitly unshared fixture; have a reviewer identify the missing fact when the fixture is withheld. |
| Closure | Link the approved form/method versions and the check result. The test finding remains inconclusive until authorized evidence resolves it; changing a template does not retroactively validate it. |

That is one possible improvement, not a mandate to collect real customer records in a public worksheet. The example shows the boundary between a per-engagement evidence decision (§30.1 and §30.5) and a change to how future work is prepared.

## Decide what deserves a review

An adopter can use post-engagement reflection, incident learning, peer-review patterns, metrics, external technical change, and direct tester or partner suggestions. Decide locally which events trigger a structured review and how routine work is sampled. A small practice may use a lightweight discussion and one owned record; a larger or higher-volume practice may need a staffed review lane and trend analysis. Neither scale earns a universal percentage or timetable.

Look for repeated friction, but do not make a fixed count the definition of a theme. One high-consequence method error may deserve immediate action; several similar complaints may have different causes. When a measurement from §40.9 prompts an item, preserve its denominator and caveats before treating a trend as an explanation. When an incident or near miss prompts it, use the authorized incident route first and carry only the improvement decision into this record.

## Interfaces and limits

- **Before the test:** §10.1–10.4 frame the engagement and collect locally approved scope facts; §00.3 and §10.2 retain authorization authority. This guide grants none.
- **During the test:** §20.1 and a relevant domain method such as §20.3 govern the selected work. A live safety or scope issue takes their stop/escalation route, not a future-retro queue.
- **After the test:** §30.1 keeps the protected engagement record; §30.5 governs report review and correction. §60.1 may propose a change to either, but cannot rewrite their evidence or approval history.
- **Practice stewardship:** §00.1 and the public component index §00.2 will identify released versions and correction paths; §40.9 may provide a signal, not proof of causation. These links must resolve to actual released counterparts before this guide is released.

The framework's presence is not evidence that any adopter runs this loop. An adopter should describe what it has implemented, what remains a proposal, and what local law, contract, privacy, or organizational policy changes the route. This guide's own technical and process assumptions should be revisited when those sources or a real consumer challenge them.
