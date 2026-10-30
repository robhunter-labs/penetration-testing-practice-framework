# Practice Self-Assessment and Internal Review

**§60.2 · Practice self-assessment & internal review · Penetration Testing Practice Framework**

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

This is a reusable way for a penetration-testing practice to check whether its own controls operate as described. It is not an attestation, an external audit report, or evidence that an adopter has completed a review. Adopt it only after assigning local authorities, records, cadence, and escalation paths.

## Reader job

Use this document to plan a bounded review, inspect actual records, compare them with the practice's adopted rules, record exceptions, and verify follow-through. The question is not “Do we have a standard?” but “Can we show that the standard operated in the period we chose?”

The review covers controls the practice owns or is responsible for operating. It does not silently audit enterprise-wide systems, replace engagement quality assurance, or release records to an outside party. External information requests follow §50.5; engagement learning follows §60.1; program measures follow §40.9. Those functions may exchange evidence, but each asks a different question.

## 1. Choose a review domain

Five standing domains anchor the review. An adopter may split or add domains, but should keep each review's authority and evidence boundary explicit.

| Domain | Testable question | Example records | Companion |
|---|---|---|---|
| Access and operator lifecycle | Do current grants and qualified operators match active roles and approved tool access? | Access export, join/move/leave tickets, exception approvals, sample revocation evidence | §40.2; tool-specific procedures |
| Controlled documents | Do approved versions, owners, status, review dates, and actual use agree? | Register, approval record, distribution point, sampled work product | §00.1; §00.2 |
| Methodology currency | Do current methods and references still describe what testers actually do? | Method review record, test sample, deviation, source/currentness check | §20.1; tactical methods |
| Evidence and archive | Can a sampled engagement be reconstructed under the adopted retention and access rules? | Engagement index, authorization, evidence, report, review, archive access and retention records | §30.1; §30.2; §30.5 |
| Tooling and research-to-operation | Did a tool enter each environment only after the decision required for that state, and is its current posture still within that decision? | Inventory or custody record, bounded-readiness result, Delivery Authorization where required, tool procedure, change/stop evidence | §90.1; §90.2; §90.3 |

The tooling question must preserve the distinction between an isolated build/test state, a connected nonproduction evaluation, and findings-producing operation. Merely finding a draft or a lab script does not prove an operating tool; a lab safety decision does not grant engagement authority.

## 2. Set a cadence that can be operated

A useful starting pattern uses annual coverage of all five domains, a separately recurring access review, and event-driven checks. Those are a useful starting pattern, not a universal claim of compliance. An adopter shall record its actual coverage interval and why it fits access churn, tool change, engagement volume, regulation, and staffing.

A cycle may cover one domain or several. A trigger—such as a major role change, new tool posture, archive migration, incident, near miss, or material method revision—can open a focused review without restarting the entire calendar. A missed scheduled review is itself recorded and assigned; it should not disappear because a later review completed.

## 3. Run the cycle

1. **Plan the question.** Identify domain, period, control version, population, sample method, reviewer, accepting authority, and evidence location. State what this cycle will not test.
2. **Observe actual state.** Pull records from the systems that operate the control. A policy statement, a manager's recollection, or a clean-looking final report is not operation evidence by itself.
3. **Compare and classify.** Distinguish conforming evidence, control failure, missing evidence, a control that no longer fits the work, and an issue outside the practice's authority. Do not collapse “not checked” into “passed.”
4. **Assign a response.** Name an owner, due condition, containment if needed, and the evidence that would demonstrate correction. Route urgent security or privacy conditions immediately through the local response path rather than waiting for a review closeout.
5. **Verify and close.** A different person where practicable checks that the action operated, records residual risk or a locally authorized exception, and closes the exact issue. The accepting authority accepts the *review record*; acceptance does not erase open findings.

Sampling should be purposeful: record the population, selection rationale, dates, exclusions, and what a failed sample causes you to inspect next. A small clean sample supports only the sampled claim, not an assertion that every engagement or tool is compliant.

## 4. Separate doing, reviewing, and accepting

The practice owner commissions and receives the cycle. A reviewer gathers evidence and analyzes it. A named authority accepts the completed review and owns escalation of unresolved issues. The same individual should not be the sole producer, judge, and accepter of evidence they control.

Small teams may not have three separate people for every domain. Record the constraint and add a second perspective, independent sample, or later oversight where possible. Do not label a self-check “independent” unless the reviewer is actually sufficiently separate from the control and its records for the claim being made.

## 5. The self-assessment record

Copy this record for each cycle and bind it to a controlled, access-appropriate evidence location. References are preferable to duplicating sensitive evidence into a new repository.

| Field | Entry |
|---|---|
| Cycle ID and date |  |
| Domain, question, and period |  |
| Adopted control and version |  |
| Population and sample selection |  |
| Reviewer and accepting authority |  |
| Evidence references and access classification |  |
| Observed matches |  |
| Exceptions, missing evidence, and untested areas |  |
| Issue owner, containment, action, and due condition |  |
| Verification method and result |  |
| Acceptance, open risk, and next trigger |  |

Every exception needs a route to closure or an explicitly accepted residual state under the adopter's authority. Keep the original observation, action, verification, and correction history auditable. The record's existence is not proof that the underlying control worked.

## 6. A bounded example

**Fictional practice, access domain.** A five-person testing team selects its tool-access population as of a stated date and checks all current operators against role assignments and training records. One former contractor still appears on a tool's access list. The reviewer records the export and the local offboarding requirement, asks the access owner to revoke the grant, and tests that the removal is visible. The review also checks whether any use occurred after the contractor's departure and routes any concern through the local security response process. The accepting authority can close the review record while keeping a broader offboarding-process improvement open and owned.

This example shows the difference between correcting one grant and learning whether the access lifecycle itself needs a change. It does not assert that any real program has this failure or that revocation alone resolves an incident.

## 7. Hand the result to the right neighbor

- **§60.1:** Repeated or structural gaps become practice-improvement work, with an owner and a later check that the changed practice operated.
- **§40.9:** Measures can reveal drift and help select a review, but a dashboard is not a substitute for inspecting control evidence.
- **§50.5/50.6/50.8:** A self-assessment record may support an information request. Its external release still requires request scoping, authorization, redaction, and a disclosure log.
- **§00.1/00.2:** A document-control gap returns to the owner and register; the review does not silently rewrite an approved standard.

## 8. Adoption bindings and limits

Before calling this an active control, decide who owns the cycle, who may review and accept it, where sensitive evidence lives, which domains and cadence apply, which systems are authoritative, how urgent conditions escalate, and how corrections are verified. Record these in the adopting practice's control register or equivalent.

This guide does not claim certification, independent assurance, full sample coverage, or suitability for any particular regulator. Its value is a repeatable, inspectable question-and-evidence loop that can be challenged and improved.
