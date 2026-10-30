# Penetration Testing Consulting Guidebook

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## Reader headlines

**Primary audience:** Penetration testers assigned to consulting duty; the technical and program leaders who staff and support them; and organizations adapting a post-test consulting service.

**Objective:** Give the tester a reliable route from a post-test question to a researched answer, technical review, formal workflow, partner, or escalation—without making the finding author the permanent help desk.

**Intended outcome:** Customers know where to ask and what to do next. Testers can cover one another, keep findings technically sound, and protect scheduled testing from untracked follow-up. Leaders can see whether the service is useful and sustainable.

**This document defines:** The consulting service boundary, local authority map, intake and response route, reusable question patterns, closing-readout handoff, staffed rotation, technical peer review, escalation and surge, service measures, and optional automation path.

## Document administration

| Field | Detail |
|---|---|
| **Document** | 50.3 |
| **Status** | Published framework component; local adoption is a separate decision. |
| **Type** | Adaptable procedure / operating guide; not an authorization or adopted local policy |
| **Maintainer** | Framework maintainers until a local program assigns an owner |
| **Local approval authority** | Defined by the adopting organization |
| **Review trigger** | Material change to testing authority, service routes, source policy, staffing, evidence expectations, disclosure, or automation behavior |

> [!CAUTION]
> This guide does not authorize a test, approve risk acceptance, create a service-level commitment, or permit release of a report. An adopter supplies its own authority, systems, people, hours, sources, and clocks before using it as an operating procedure.

## Where this fits

An adopter needs its own authorization boundary, testing and finding method, and enforceable engagement scope. In the full framework, read this guide alongside document control (§00.1), authority (§00.3), the umbrella test method (§20.1), scoping and rules of engagement (§10.1/10.2), evidence/reporting (§30.1/30.5), and the urgent-response and closing-readout companions (§50.2/50.4). Those components do different jobs; none makes the consulting desk an approval authority. This guide covers the continuing service around a reported test: explanation, evidence and retest guidance, technical quality review, partner routing, and accountable handoff. The issue-record system and the organization's vulnerability-management process remain authoritative for finding state and formal retest or closure. If AI affects finding substance or takes testing action, §90.1's capability boundary and a locally approved tool procedure also apply.

The consulting service supports those systems; it does not replace them. A new target, materially expanded scope, or full retest outside the existing authorized route returns to engagement intake and authorization.

## At a glance

`closing readout → shared consulting route → on-duty tester → researched answer / technical peer / formal workflow / partner / escalation → recorded next action`

Two audiences use the same staffed lane. Customers need to understand the finding and reach the right decision owner. Testers need a qualified second set of eyes and a team-owned route for follow-up. The service succeeds when both can move forward without losing technical truth, responsibility, or the record.

## 1. Purpose and service contract

The consulting desk shall provide a known point of contact for questions arising from penetration-testing work. It may explain a finding, clarify evidence requirements, research a technical question, help a requester find the formal retest or closure path, review another tester's work, and route a case to the function that owns the next decision. Responses should be specific enough to help the requester act and narrow enough not to promise a result the desk cannot deliver.

The desk shall not accept a new test by email, execute a test outside its authorized engagement route, approve a deferral or exception it does not own, change severity through negotiation, become an application's remediation team, or distribute controlled artifacts outside the applicable disclosure process. Helpful conversation is not a substitute for the formal record. A direct message may alert a tester; it does not by itself start a retest clock or create new scope.

The adopter shall publish the desk's hours, intake route, formal retest/closure route, office-hours route if offered, escalation chain, and how customers receive the result. A staffed business-hours rotation must not be described as 24/7 support. If extended coverage is needed, define and staff it as a separate commitment.

## 2. Local authority and service profile

Complete this profile before treating a response pattern as operational. Each entry points to the current source of record; a copied answer or old template is not authority.

| Decision or route | Local source / owner / version | Operational entry point | What the desk may decide |
|---|---|---|---|
| Authorized scope and new engagement | *Complete locally* | *Complete locally* | Explain and route; no scope grant |
| Finding and severity method | *Complete locally* | *Complete locally* | Interpret; technical review for challenge |
| Vulnerability record and retest | *Complete locally* | *Complete locally* | Check readiness and route; no email-only retest |
| Evidence and closure | *Complete locally* | *Complete locally* | Explain and review within local authority |
| Risk deferral or exception | *Complete locally* | *Complete locally* | Explain route; no substitute approval |
| Report and audit disclosure | *Complete locally* | *Complete locally* | Identify requester and hold where required |
| Credential and test access | *Complete locally* | *Complete locally* | Request authorized access; never collect secrets in an ad hoc thread |
| Urgent surge | *Complete locally* | *Complete locally* | Escalate into bounded, staffed support |

When a source is missing, contradictory, expired, or outside the tester's authority, the tester shall state the uncertainty, seek a qualified second view, and avoid a consequential commitment. Local policy may set a fixed severity, evidence threshold, or release tier for a class of issue; this guide does not invent one for every adopter.

## 3. Intake and disposition

For each request, identify the decision sought, the linked engagement or finding, the available evidence, the current owner, the deadline or consequence, and the channel in which the decision must be recorded. Classify by the question's substance, not merely a keyword. A single message may need more than one route; the most restrictive authority or disclosure boundary controls until the case is separated.

Choose one response disposition:

| Disposition | Use when | Tester action |
|---|---|---|
| **Send** | The current authority and case facts fit a known pattern. | Give a researched answer and next step; record it. |
| **Send and ask** | The answer is bounded but a material input is missing. | State what is known and request only the missing fact. |
| **Escalate first** | Technical validity, severity, scope, policy interpretation, or precedent is contested. | Acknowledge, gather the case, seek peer or leadership review before committing. |
| **Hold for approval** | A controlled disclosure, exception, or other reserved decision is requested. | Do not release or imply approval; route to the named authority. |

The minimum case record is the request, linked issue or engagement, source and evidence checked, disposition, next actor, next action, and any unresolved uncertainty. Use the existing record system where it can do the job. Do not create a parallel tracker merely to satisfy this guide.

### 3.1 Response shape

A substantive reply should acknowledge the question, name the relevant finding or decision, explain the tested fact and applicable rule in plain language, state any missing evidence or uncertainty, and close with *who does what next, through which route*. A template shall never be sent without checking the case and the source it relies on. An automatic acknowledgment may confirm receipt; it is not counted as a researched answer.

### 3.2 Fourteen common question patterns

These are reusable decision patterns, not universal verdicts or employer-specific email text. The adopter should turn each into a locally sourced response example, retain a technical-review route, and retire examples that no longer fit current policy.

| Pattern | Check before answering | Useful response and boundary |
|---|---|---|
| **1. Formal retest request** | Issue identity, authorized target, deployed change, environment, evidence, and test access. | Explain the issue-record request route and readiness criteria. Email alone does not initiate a retest. |
| **2. Evidence-only closure question** | Local severity/closure rule, evidence of the changed state, and issue record. | Explain whether the local process permits evidence review without a retest; identify what proof is missing. Do not close from assertion alone. |
| **3. Retest status or ETA** | Existing request identifier, queue state, readiness, and local clock start. | Use the identifier already supplied; state observed status and the applicable commitment without inventing an exact completion time. |
| **4. Deferral or deadline extension** | Risk owner, issue state, documented constraint, and local exception route. | Explain the governance path and offer technical clarification. The testing desk does not silently accept risk. |
| **5. Severity challenge** | Original evidence, scoring method, new technical facts, and the finding author. | Route a genuine methodology challenge to technical review. Do not negotiate a rating in email or dismiss new evidence. |
| **6. Exposure or asset-classification dispute** | Observed exposure, inventory/asset record, and the classification owner. | Separate an incorrect inventory record from a tested exposure; route each to its owner. |
| **7. Report request** | Requester identity, authorized recipient, purpose, classification, and prior distribution. | Provide only through the controlled report route; do not make a full report the default first attachment. |
| **8. Audit or external information request** | Requester's authority, exact objective, destination, classification, and approval path. | Hold controlled artifacts for the disclosure owner; choose the minimum necessary approved release and retain a disclosure record. |
| **9. Production retest concern** | Original test environment, deployment evidence, local retest method, and authorization. | Explain the permitted evidence and attestation route, if one exists. Do not imply non-production evidence universally proves production remediation. |
| **10. Wrong issue owner** | Proposed receiving group, their acceptance, and reassignment authority. | Route reassignment through the issue system; do not guess an owner or create an orphaned issue. |
| **11. Request to lower risk after partial remediation** | Changed condition, compensating control, current methodology, and risk owner. | Separate technical rescoring from governance acceptance; route to the authorized review. Do not volunteer a shortcut for ordinary schedule pressure. |
| **12. New test or scope expansion** | Requested target, method, objective, and existing authorization. | Send the requester to engagement intake and scoping; no side-channel testing commitment. |
| **13. Exposed secret or credential** | Secret validity, exposure path, policy, credential owner, and safe evidence handling. | Direct the owner to the local revoke/rotate/vault and issue process as applicable; do not paste the secret into the reply or assume a universal severity. |
| **14. Centrally managed configuration** | Exploitability evidence, affected component, central platform owner, and remediation constraints. | Keep technical validity separate from ownership. Engage the platform owner for a systemic fix or the risk owner for a documented exception; blocked remediation is not proof of a false positive. |

For a pattern that does not fit, stop using the template and write the case-specific question for peer review. New recurring patterns should be added only after the source, decision boundary, and next actor are understood.

### 3.3 Recognize the shape of pushback

Pushback can contain a new fact, a different decision request, or both. The desk's job is to separate them before replying. A new technical fact gets reviewed on its merits; repetition alone does not make it new, and a difficult schedule does not transfer approval authority to the tester.

| Shape of the request | What may have changed | Desk posture and next route |
|---|---|---|
| “It is only a test or internal system.” | The environment, exposure, identity or data classification may have been recorded incorrectly. | Verify the factual change against the tested condition and local method. If it is material, obtain technical review. Do not re-score merely to relieve schedule pressure. |
| “Another team owns the fix.” | The responsible component or effective remediation owner may be elsewhere. | Help name the partner and the joint next action. Keep issue ownership and technical validity separate; use the local reassignment or exception route where warranted. |
| “We need to ship before the fix.” | A genuine deadline or business constraint may exist. | State the technical condition and documented risk route. The desk neither grants an extension nor closes the finding in conversation. |
| “Can we have another call?” | There may be new evidence, a new decision-maker, or simply an unresolved path. | Ask for the new fact and desired decision before the call. Route technical change to review; use the meeting to clarify owners and next actions when the evidence has not changed. |
| “Can you also test this?” | A new target, operation or environment may be implicated. | Record the question and send it through engagement intake and authorization. Do not turn a consulting exchange into an unscoped test. |
| “I messaged the original tester.” | A direct conversation may contain relevant evidence but bypass the shared record. | Acknowledge the contact, preserve the useful context, and move the request and decision into the staffed route. |
| “This is a false positive.” | A control, fixture, target state or interpretation may have been missed. | Invite specific contrary evidence. Seek a qualified technical review against the original test; do not reject the challenge or accept it by label alone. |

These are question shapes, not customer motives. An adopter should replace the generic routes with its own current records, partners, authority, and response examples.

### 3.4 Decide whether a retest is ready

Before promising a retest or starting its local clock, verify the original issue and authorized target, the changed build or control, the environment in which that change is available, access for the approved actor, the expected result, evidence already supplied, the permitted test action, and the stop contact. A missing input is a readiness question to return to the requester; a materially different target or test action is a scope question for engagement authority. The issue system records the formal request, disposition, and result. Local policy—not this guide—sets the clock and whether an evidence-only closure review is permitted.

## 4. Set expectations at the closing readout

The closing readout shall give the application or service owner a route they can use after the tester moves on. Explain what was demonstrated, what remains untested, the possible footprint beyond the tested instance, who owns broader remediation, which evidence a fix should produce, how formal retest or closure is requested, and where later questions go. Name relevant architecture, secure-development, vulnerability-management, business, or third-party partners when they carry the next action.

The finding author should participate where their technical judgment is needed; they should not become the only durable entrance. Follow-up material should repeat the same routes and boundaries stated in the meeting. The consulting guide, closing readout, and actual intake system must agree.

## 5. Staff and hand off the rotation

A useful default is a planned, dedicated consulting turn: one qualified tester has protected time to monitor the shared route and formal queues, attend published office hours, answer customers, and provide peer review. Active engagement work should not silently consume that capacity. The adopter may choose a different coverage model, but shall name the actual staffed hours, competing work, replacement, and escalation; the service promise must match capacity.

The tester needs offensive-security depth, research habits, strong written and verbal communication, and the judgment to explain discovery and retest without claiming to own remediation. They should know when to ask the finding author, a specialist, a peer, or leadership for a second view. Onboarding should move from observation to supervised replies and reviews, then independent duty against demonstrated capability—not tenure alone.

Publish the schedule ahead of time. Swaps and leave coverage require a visible replacement and updated schedule. At the end of a turn, hand over open email and issue requests, age and next action, partner and escalation status, peer reviews in progress, and links to authorized evidence and access routes. Do not include credentials in the handoff. A named backup is useful when the duty tester is unavailable; its staffing and authority must be real, not decorative.

## 6. Provide technical peer review to the team

The consulting rotation is also a team-facing quality resource. A tester may bring a proposed finding, evidence package, scope question, severity rationale, or report for challenge. The reviewer should ask whether the claim is reproducible from the recorded conditions, whether impact and severity follow the evidence, whether the proposed wording exceeds scope, and whether a reader can understand the remediation. A specialty reviewer joins when the test class requires deeper expertise.

For a deliverable report, the adopter should define distinct author, technical-peer, and leadership acceptance roles, the minimum checklist, and the retained review record. Mechanical checks can catch missing fields and broken references; they cannot decide exploitability or defensibility. If the on-duty tester authored the material, assign another qualified reviewer. Unresolved disagreement follows the technical escalation path, not a quiet sign-off.

## 7. Escalation, partners, and urgent surge

Start ambiguous technical questions with an experienced peer or specialist. Bring unresolved technical, policy, scope, or precedent questions to named testing leadership with the original request, evidence, proposed answer, and precise point of disagreement. Use an exceptional senior route only when ordinary authority is unavailable or the consequence crosses the program. Engagement intake and capacity questions go to the scheduling owner, not through the technical escalation chain.

The desk should route solution and ownership work to the partner equipped to perform it: vulnerability management, security architecture, secure-development advocates, policy or secrets teams, business-line security partners, and the owner of a vendor relationship. A handoff is complete when the next owner and action are clear, not merely when a message was forwarded.

An urgent, high-touch request that exceeds rotation capacity needs a separate bounded surge decision: trigger, requester, scope, staffing, time or review point, record, and return to planned work. Multiple testers may be needed. If the request requires a full penetration-test method, it becomes a scoped engagement with its own authorization rather than an indefinitely expanded consulting case.

## 8. Service levels and effectiveness

Define distinct clocks for acknowledgment, researched guidance, retest after readiness, and closure review. Each local clock needs a start condition, required inputs, business-hour rule, pause or cancellation condition, owner, and customer-visible result. A fast acknowledgment is not substantive guidance; a missing fix, evidence, environment, or authorized access is not a ready retest.

Review effectiveness in aggregate. Useful signals include policy-aligned answers, time to actionable guidance, invalid retest requests redirected before a clock starts, peer-review rework, repeat inquiries, queue aging, missed intake, urgent interruptions, and whether customers could act on the first substantive answer. Pair counts with qualitative feedback and tester load. Avoid individual volume or closure-count targets that reward rushed responses or make the desk absorb work outside its authority. Target values and severity-specific timelines belong to the adopter's current policy and service agreement, not to this template.

## 9. Optional automation and AI support

Automate the stable seams first: link an incoming question to its issue and engagement, reconcile queues, detect missing retest-readiness inputs, and show the current source passage to the tester. A search or retrieval layer can help locate applicable guidance. A model may propose a classification or draft when the case is ambiguous, but its source, uncertainty, and proposed next actor must remain inspectable. A workflow can pause for technical peer review, risk-owner action, or disclosure approval and resume with the record intact.

No model may expand test scope, decide finding validity or severity, accept risk, release a controlled artifact, or send a consequential answer merely because it produced fluent text. An agentic step earns its place only when bounded investigation across permitted tools improves a real decision that rules and retrieval cannot. Test wrong-route cases, stale and poisoned guidance, missing-source abstention, privacy boundaries, human corrections, and recovery before granting more action. Any AI use that crosses into testing or finding substance requires separate approval and governance.

## 10. On-duty quick card

1. What decision is the requester actually asking for?
2. Which engagement, finding, evidence, and current source govern it?
3. Is this consulting, formal issue action, new engagement, partner work, peer review, or controlled disclosure?
4. Do the facts support **send**, **send and ask**, **escalate first**, or **hold for approval**?
5. Who acts next, through which route, and where will the outcome be recorded?
6. What remains open for the next tester or leadership to pick up?

## 11. Adoption profile

Before use, an adopter shall fill the local authority and service profile (§2), staff the route (§5), connect it to the actual closing readout and issue system (§4), assign technical and disclosure escalation owners (§6–7), and set local clocks (§8). Test the route with a retest request, disputed severity, report review, and external-information request. Exercise a rotation handoff and a changed-policy case; a guide that works only for its author is not yet a team service.

The organization may adopt the core pattern without adopting every response example or AI feature. Local choice can change channels, hours, tools, staffing, and thresholds; it cannot turn conversation into authorization, tool output into a finding, or a template into risk or disclosure approval.

## 12. Assurance evidence and maintenance

A credible local implementation can show a current source/route map, staffed schedule and handoff, source-linked response, issue-record action, technical review and leadership acceptance record, escalation record, controlled-disclosure record where applicable, and an improvement trace from recurring questions. The existence of this document proves none of those operations occurred.

Review the question patterns, route map, sources, and metrics when policy, system behavior, organizational responsibility, or demand changes. Record changes to the adopted guide through the local document-control process. Retire examples that are no longer correct; keep a correction path for an answer already sent under outdated guidance.
