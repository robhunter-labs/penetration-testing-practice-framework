# 10.2 · Rules of engagement worksheet

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

This worksheet records **how** an authorized penetration test may be performed. §10.1 records **what** is in scope; §00.3 describes the authority that must exist behind both. A completed worksheet is not permission to test. The adopting organization must supply its own authorized signatories, policies, legal and safety review, record system, and approval process before use.

**Reader and task:** A working tester and authorized risk/asset owner use one copy per engagement to settle execution conditions and preserve who decided them. A reviewer later uses the same record to test whether activity stayed within permission. Name a maintainer, connect the copy to the signed scope, and record decisions before execution. A blank field means *unsettled*, not “the tester may choose.” Where a section genuinely does not apply, write **N/A and why**; do not leave an ambiguous blank. If a condition changes, pause the affected activity, obtain the necessary decision, and version the record. The choices below are prompts, **not universal defaults**.

## 1 · Identity and decision basis

| Field | Engagement decision |
|---|---|
| Engagement ID, title, and version | |
| Objective or assurance question | |
| Engagement type: penetration test, targeted control assessment, code-assisted test, physical test, retest, or other | |
| Linked signed scope and its version (§10.1) | |
| Program authority and per-engagement permission reference (§00.3) | |
| Engagement owner / responsible tester and qualified backup | |
| Asset or risk owner, authorization signatory, and date | |
| Applicable local policies, contracts, and third-party permissions | |

**Decision check:** Can a tester point to both the authorized target and the conditions under which they may touch it? If ownership or permission is disputed, stop until it is resolved.

## 2 · Environment, identities, data, and time

| Question | Decision / exact reference |
|---|---|
| Which environments are allowed? Name production and nonproduction separately. | |
| Which accounts, roles, tenants, or identity contexts are supplied and who owns them? | |
| What data may be created, viewed, copied, or retained? What must be synthetic? | |
| What is the test window, time zone, blackout period, and required notice? | |
| Are production, externally exposed nonproduction, shared infrastructure, or third-party systems involved? What additional approvals are required? | |
| What rate limits, lockout thresholds, or resource-consumption limits apply? | |
| How are credentials issued, rotated/revoked, and protected after the test? | |

The scope should name the targets; this section binds the **operating conditions**. For example, “the API” is not enough to decide whether a second tenant, a downstream provider, or production data may be used. If the test depends on a policy exception or change window, cite the approval and expiry rather than assuming the exception exists.

## 3 · Techniques, proof depth, and exclusions

| Activity | Allowed, excluded, or separately approved? By whom? |
|---|---|
| Authentication and authorization tests across listed identities | |
| Automated scanning, concurrency, and exploit attempts | |
| Credential guessing or account lockout risk | |
| Use of discovered credentials, lateral movement, or access to adjacent systems | |
| Data extraction beyond the minimum proof | |
| Service disruption, load, destructive changes, persistence, or privileged actions | |
| Social engineering or contact with people | |
| Physical entry or access-control testing (complete §5 if permitted) | |
| Any other technique with unusual consequence | |

**Maximum permissible proof by activity:** Record the observation that is enough to support a conclusion, the stopping point, and who must decide if more is needed. Link each material §3 decision to its proof limit: ____________. An excluded technique does not become permitted because a tool can perform it. An unlisted target does not become in scope because it is reachable.

**Scope-change trigger:** A new asset, identity, technique, impact level, data class, or third-party boundary requires review against §00.3 and a revised scope/RoE decision before that part of testing proceeds. **Change approver and record path:** ____________. The tester cannot self-approve an expanded authority boundary.

## 4 · AI and agentic-tool declaration (conditional; mark N/A if neither applies)

Separate two questions that are often blurred:

| Question | Record |
|---|---|
| Is an AI/LLM/agent system **the target**? If yes, which model-facing application, prompt surface, tool integration, data store, and downstream action are authorized? | |
| Is AI or an agent used **by the testing team**? If yes, name the tool/version, role, data it can receive, autonomy/action boundary, human checkpoints, logging, and kill/stop mechanism. | |

The presence of either kind of AI does not authorize the other. If testing-team AI can invoke tools or affect a live system, the team must decide its permitted actions, credentials, network/data egress, human approval points, and response to unexpected behavior before use. Treat generated observations as candidates for human evaluation under §20.1, not as accepted findings. The applicable AI components of the framework are extensions; this worksheet does not assert an already deployed agentic testing program.

## 5 · Physical-testing overlay (conditional; mark N/A if not applicable)

Complete this block only when the engagement actually includes physical access. A digital-testing RoE cannot quietly absorb a physical test. Other high-consequence activities—including social engineering, disruptive testing, or production changes—need a separately approved local overlay or explicit additional decision recorded in §3 and 8; this physical block does not cover them.

| Physical decision | Record |
|---|---|
| Facility, address, in-scope zones, and explicit off-limits areas with reasons | |
| Announced assessment or covert exercise; objective of each phase | |
| Facility owner, tenant/shared-area boundaries, and permissions from every necessary party | |
| Written per-facility authorization carried or immediately verifiable by testers | |
| Safety contact, local response coordination, stop signals, and confronted-person procedure | |
| Security-staff posture and required briefing for a safe encounter | |
| Authorized classes of access-control components and techniques | |
| Follow-on or retest plan, if any | |

No technique is permitted merely because it appears in a checklist. The local authority, facility owner, legal/safety rules, and §20.11 method must align before entry. Exclude destructive entry unless the actual governing authorization and safety process expressly permits it; this public worksheet grants none.

## 6 · Coordination, stop, and escalation

| Field | Named person, channel, and expected action |
|---|---|
| Test-team communication channel and backup | |
| Asset owner / operational contact | |
| Security operations deconfliction and incident contact | |
| Data-loss, change-management, or platform coordination, where applicable | |
| 24-hour emergency contact or explicit coverage limitation | |
| Who can pause testing; how a pause is communicated and recorded | |
| Who may authorize resumption after an incident, outage, or scope dispute | |
| Handling for an out-of-scope observation | |
| Test-traffic source/identifier and security-operations deconfliction record | |

**Stop conditions to tailor:** unexpected harm or instability; contact with an unapproved system or person; discovery of live sensitive data outside the agreed proof; expired permission; a third-party boundary; or suspected real incident. The tester records the minimal observation, stops the affected action, and uses the named path. “Notify later” is not a substitute for a stop-and-decide path.

## 7 · Evidence, review, reporting, and close-out

| Field | Local decision / system of record |
|---|---|
| Evidence format and protected storage location | |
| Credential and sensitive-data handling, redaction, and transmission rules | |
| Cleanup or ownership transfer for test accounts, created data, deployed artifacts, and temporary access | |
| Technical peer-review contact and finding-decision route | |
| Severity scheme and local context/approval route | |
| Status, draft/final report, and closing-readout cadence | |
| Finding/issue system of record and retest/closure intake | |
| Archive owner, access controls, retention rule, and disposal | |
| Known limits or untested conditions that must appear in the report | |
| Production/high-impact recovery plan, backup/restore owner, and residual-risk acceptance, or N/A with reason | |

Keep enough of the decision trail for a qualified reviewer to distinguish what was authorized, done, observed, reviewed, and left uncertain. Use §30.1 for the local archive set, §30.3 for credential handling, §30.4 for testing operational security, and §20.1 for evidence and finding decisions. The organization chooses its systems; this template mandates none.

## 8 · Approval and change log

| Decision | Name / role | Date / record link |
|---|---|---|
| Scope and operating conditions approved | | |
| Additional production, high-consequence, physical, or AI-tooling decisions approved | | |
| Tester briefing completed | | |
| Changed condition reviewed and versioned | | |
| Tester explained the boundaries back; authorizer accepted or returned for correction | | |
| Stop/resume decision, if any | | |
| Close-out: signed scope, current RoE, method/evidence, review and final report filed | | |

Before the window opens, have the responsible tester explain this record back to the authorizer: **what can be tested, how far it can go, what is excluded, who to call, and when to stop**. Record the authorizer's acceptance in §8. If that explanation exposes ambiguity, the worksheet is not ready.

## Adoption and limits

This is an adaptable working template for a human-led practice. It does not provide legal advice, certify conformance with an external standard, prove that a practice is operating, or supply authorization to test. Local legal, safety, contractual, and organizational controls prevail. Its upstream decisions are §00.3 (authority) and §10.1 (scope); its downstream consumers are §20.1 (method), the selected domain method, §30.1 (archive), and the local reporting/retest path. Recheck it whenever a material operating boundary, linked component, or applicable technical guidance changes. A released version should point to a concrete correction route.
