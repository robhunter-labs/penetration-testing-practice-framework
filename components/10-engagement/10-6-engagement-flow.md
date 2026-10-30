# 10.6 — Engagement process flow

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

The [engagement flow diagram](../../diagrams/10-6-engagement-flow.svg) shows one penetration-testing engagement moving from selection and written authorization through testing, review, delivery, issue handoff, retest, and learning. It separates three sets of decisions that may involve different people: the target owner and authority, the testing practice, and vulnerability management or local risk authority.

The diagram is a design aid. It does not prescribe an organization chart, a ticketing platform, a staffing model, a deadline, or permission to test. One person may hold several local roles, but the decisions and records still need named owners.

## Find the decision

| Reader question | Place on the map | Record to find or establish locally |
|---|---|---|
| Who authorized this test? | Target-owner lane, **Authorize testing** beside step 4 (Q1) | Written permission and the approved scope and rules of engagement. |
| How did a result become a finding? | Testing lane, **Review and finding decision** at step 7 (Q2) | Evidence, reviewer disposition, uncertainty, and report version. |
| Who owns the issue after delivery? | Step 9, **Hand off accepted findings** (Q3) | The local issue record and its receiving owner. |
| Where does a retest return? | Step 10, **Retest the original condition** (Q4) | Retest request, tested change and environment, evidence, and outcome. |

An inconclusive result stays inconclusive. A finding in one tested instance does not set enterprise-wide remediation policy. Broader patterns and urgent conditions route to the appropriate local stakeholders; vulnerability management and risk authority retain their own priority, deadline, deferral, and closure decisions.

## Walk an engagement

1. **Select and assign.** Record why the work was selected, its requester, and its accountable engagement owner.
2. **Scope and authorize.** The testing practice proposes target boundaries and conditions. An accountable target or risk owner grants written permission before testing starts.
3. **Prepare.** Confirm target state, identities, access, contacts, notification, stop conditions, and evidence custody.
4. **Test and record.** Work inside the authorized limits. A meaningful scope or impact change returns to scoping and authorization rather than becoming tester discretion.
5. **Review and deliver.** A qualified reviewer challenges the evidence and conclusion. The report separates accepted findings, rejected candidates, unresolved questions, and untested coverage.
6. **Hand off and retest.** Accepted findings enter the adopter's issue-management route. The testing practice can retest the original condition after an authorized request and a changed target state. The local issue owner closes or defers the record under its policy.
7. **Learn.** Preserve the engagement record and feed useful corrections into the next selection, method, or handoff.

The flow is deliberately connected to [§00.3](../00-start-here/00-3-authority-to-operate.md), [§20.1](../20-methods/20-1-method-framework.md), [§10.1](10-1-scoping-guide.md), [§10.2](10-2-rules-of-engagement.md), [§30.5](../30-evidence/30-5-report-standard.md), and [§50.3](../50-support/50-3-consulting-guidebook.md). Those components answer different parts of the same engagement; none silently transfers authority to the testing team.

## Use and limits

- A practice lead can walk a recent or synthetic engagement across every lane crossing and ask who decided, where the decision was recorded, and what happens when that person is unavailable.
- A tester can use steps 4–10 to find the permissions, review, and handoff records needed before claiming completion.
- A reviewer can start at step 7 and trace one conclusion backward to evidence and authorization, then forward to issue handoff and retest.

The SVG contains a text title and description, uses labeled decisions and loops, and does not rely on color alone. On a narrow screen, open or download the SVG at full size. This companion provides the linear reading path and question map. The diagram and this explanation have not been validated with independent real readers; adopters should test them against their own work and correct local bindings before use.
