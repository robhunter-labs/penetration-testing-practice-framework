# 10.5 · Synthetic multi-party engagement brief — filled example

> **Fictional teaching example only.** Every organization, person, address, record ID, decision, date, and contact below is invented. No authorization, system, test, approval, or supporting file exists. The reference IDs illustrate how an adopter might index *its own* records; they are not links or evidence. This example must never be used as an engagement authorization.

This example fills the §10.5 engagement operational brief template. It demonstrates a deliberately split outcome: **C1 is GO** for a separately authorized staging API; **C2 is NO-GO** for a provider-controlled component whose provider decision is pending. In this invented case, the scope record and Rules of Engagement (RoE) *expressly permit C1 to proceed independently*; neither C1 access nor C1 results depend on C2. The brief coordinates decisions and does not itself grant permission.

## 1 · Brief control

| Field | Fictional entry |
|---|---|
| Engagement name and ID | Example Organization staging API review · `EX-ENG-041` |
| Brief version and record state | `EX-BR-041 v1.0` · readiness recorded; C2 remains NO-GO |
| Authorization outcome | **PARTIAL — C1 GO, C2 NO-GO; see §6c.** No package-level all-or-nothing condition in the fictional scope/RoE. |
| Prepared by and brief maintainer | Morgan Vale, fictional assessment coordinator; maintains this index, not the underlying approvals |
| Why this brief is used | C1 needs decisions by the internal engagement authorizer and C1 owner. C2 also crosses a separately controlled provider boundary; the provider must decide for C2. |
| Linked scope record | `EX-SCOPE-041 v1.0`, fictional internal case-file reference; §2 objective/component map, §3 component bounds, §7 independent partial execution |
| Linked Rules of Engagement | `EX-ROE-041 v1.0`, fictional internal case-file reference; §2–5 windows, techniques, contacts, stop rules; §6 partial execution |
| Program authority reference | `EX-AUTH-MODEL v1.0`, fictional internal authority model; §4 requires engagement authorizer plus component controller, including a provider decision for C2 |

“Readiness recorded” means this fictional cover sheet is complete enough to expose the split, not that this document authorizes activity. In any real engagement, the actual decision records, scope, RoE, current window, contacts, and local controls govern.

## 2 · Purpose and objectives

**Package purpose.** The named fictional testers would assess the specified staging API only within the scope and RoE, and would separately assess the provider-controlled edge only if its missing provider decision, contact coverage, and window were later recorded. The C1 test is self-contained: distinct test credentials and endpoint; no provider-hosted feature, route, identity, data, or access path is used.

| # | Objective or question | Relying decision or user | Components needed | If a component is NO-GO |
|---|---|---|---|---|
| O1 | How does the internal staging API enforce authorization between fictional test tenants? | Fictional C1 application owner deciding whether to advance its release candidate | C1 only | Still answerable from C1 within its approved bounds; no claim about C2 |
| O2 | What controls are visible at the provider-managed API edge for the planned integration? | Fictional integration owner deciding whether to request a later provider-authorized assessment | C2 only | **Not answered**; no inference of safety, weakness, or “zero findings” |
| O3 | Does the end-to-end path behave consistently across the internal API and provider edge? | Fictional architecture review | C1 **and** C2 | **Not answered** until C2 is separately authorized and tested; C1-only observations are not end-to-end results |

## 3 · Scope and RoE references

This is an index, not a replacement for the fictional scope and RoE. The case-file references here are illustrative labels, not existing files.

| Component | One-line description | Surface | Scope pointer | Binding RoE pointer | Exclusions pointer |
|---|---|---|---|---|---|
| C1 | Internal staging API with two synthetic test tenants | Digital, internal nonproduction | `EX-SCOPE-041 v1.0 §3.1` | `EX-ROE-041 v1.0 §2.1, 3.1, 4–6` | `EX-SCOPE-041 v1.0 §3.1`: production, real user data, provider route, and lateral access excluded |
| C2 | Provider-controlled API edge proposed for a later phase | Provider-hosted | `EX-SCOPE-041 v1.0 §3.2`, expressly conditional | `EX-ROE-041 v1.0 §2.2, 3.2, 4–6`, conditional and inactive | `EX-SCOPE-041 v1.0 §3.2`: all C2 activity excluded until provider decision and revised window are filed |

**Out of scope.** Production, real personal data, denial-of-service, social engineering, physical access, other provider assets, and any route from C1 into C2 (`EX-SCOPE-041 v1.0 §3.3`, fictional reference). The invented scope §7 and RoE §6 explicitly allow independent C1-only execution while C2 is held; they forbid treating C1 access as a path into C2.

## 4 · Target and facility summary

| Component | Environment | Controller | Ownership state | Facility notes |
|---|---|---|---|---|
| C1 | Nonproduction staging, synthetic data only | Fictional Example Organization application owner | Internally controlled | N/A: no physical component |
| C2 | Proposed provider-managed test edge, not yet available for testing | Fictional Example Provider service controller | Provider-controlled | N/A: no physical component |

The controller of C2 is known in this invented scenario; the missing item is its **decision**, not an unknown owner. If real ownership were contested, C2 would remain NO-GO until resolved.

## 5 · Test window

| Component | Window and time zone | Phase | Blackout/notice | Contact coverage |
|---|---|---|---|---|
| C1 | Fictional scope/RoE window: 12 November 2026, 10:00–16:00 America/New_York; activity ends at 16:00 or earlier stop/expiry | Announced staging assessment only | 15-minute pre-start notice to monitoring; no activity during 12:00–12:30 staging deployment blackout (`EX-ROE-041 v1.0 §3.1`) | Stop, owner, deconfliction, and resumption contacts in §7 confirmed for 10:00–16:00 except blackout; pause if any required contact is unavailable |
| C2 | **No authorized window.** A later date is merely proposed and cannot be treated as permission. | No active phase | Notice and blackout terms pending provider decision and RoE/scope update | Provider stop/verification coverage not confirmed; **NO-GO** |

**Retest or follow-on window:** None authorized. Any follow-on requires the local change process and new decision records. The fictional November date is not a real appointment or permission.

## 6 · Parties and authorities

### 6a · Testing team

| Role | Fictional person / function | Fictional contact route | Components | May decide independently |
|---|---|---|---|---|
| Responsible lead | Alex Rowan, assessment lead | Case-file contact code `EX-CONTACT-LEAD` (not a real address) | C1 only while C2 is NO-GO | Pause their own activity, invoke stop, record observations; cannot authorize scope, restart after external stop, or activate C2 |
| Additional tester | Priya Chen, assessment tester | Case-file contact code `EX-CONTACT-TESTER` (not a real address) | C1 only while C2 is NO-GO | Pause own activity and alert lead; no independent approval or C2 access |

### 6b · Authority matrix

The fictional scope/RoE/authority model, not this table, determine which decisions are required. Decision references are invented case-file labels and **not actual signatures**.

| Ref | Fictional party and organization | Fictional name | Specific authority and limit | Components | Stop power | Decision record and date | Expiry / conditions |
|---|---|---|---|---|---|---|---|
| A1 | Engagement authorizer, Example Organization | Dana Ellis | Permits Example Organization's assessment participation and the explicitly independent C1-only phase; cannot grant provider permission | C1 and organizational portion of C2 | May stop entire fictional engagement | `EX-DEC-A1 v1.0`, fictional signed-decision example dated 9 Nov 2026 | Valid only through the C1 window; C2 remains conditional on A3 and a later approved window |
| A2 | C1 application controller, Example Organization | Sam Idris | Permits the named C1 staging endpoint, synthetic tenants, and test accounts; cannot approve C2 or broaden techniques | C1 only | May stop C1 | `EX-DEC-A2 v1.0`, fictional signed-decision example dated 9 Nov 2026 | Valid through 12 Nov 2026 16:00 America/New_York, subject to staging blackout and RoE |
| A3 | Provider service controller, Example Provider | Name pending provider assignment | Must independently decide whether C2 may be tested, exact provider surface, conditions, contacts, and window; no other party substitutes | C2 only | If approval later granted, may stop C2 under the recorded terms | **Pending; no decision record or signature** | No permission, window, or contact coverage exists; C2 is NO-GO |

No physical-testing written authorization applies, because neither component is a physical test. A1's seniority and approval of the package do not stand in for A3.

### 6c · Component readiness

| Component | Required authorities and source | Mapped, recorded, current? | State | Missing item and consequence |
|---|---|---|---|---|
| C1 | A1 + A2 (`EX-AUTH-MODEL v1.0 §4`; `EX-SCOPE-041 v1.0 §3.1`; `EX-ROE-041 v1.0 §2.1`) | **Yes in this synthetic example**, for the stated C1 window and conditions | **GO**, subject to window, contact, blackout, and stop checks | N/A. O1 can be pursued independently. O3 cannot be answered while C2 remains NO-GO. |
| C2 | A1 + A3 (`EX-AUTH-MODEL v1.0 §4`; `EX-SCOPE-041 v1.0 §3.2`; `EX-ROE-041 v1.0 §2.2`) | **No**: A3 has no decision; C2 window and required provider contacts are unconfirmed | **NO-GO** | Provider controller must issue its own recorded decision, after which scope/RoE and this brief need an approved update. O2 and O3 remain unanswered. C1 is not dependent on C2 and may proceed only because scope §7 and RoE §6 expressly permit partial execution. |

## 7 · Stop, deconfliction, and verification contacts

All contact codes are fictional case-file labels, not reachable phone numbers or email addresses. The “checked” cells show what a completed *fictional* readiness record would look like; they do not attest to a real call.

| Purpose | Fictional name/function | Fictional primary / backup channel | Reachable hours | Components | Fictional reachability check |
|---|---|---|---|---|---|
| Can order a stop | Dana Ellis (A1); Sam Idris (A2) for C1; provider A3 for C2 if later approved | C1: `EX-STOP-PRIMARY` / `EX-STOP-BACKUP`; C2: pending | C1 10:00–16:00; C2 none confirmed | A1: all; A2: C1; A3: C2 | C1 primary and backup example-check by Morgan Vale, 11 Nov 2026 15:00; C2 **not checked / NO-GO** |
| Security monitoring deconfliction | Example Organization monitoring desk | `EX-DECON-PRIMARY` / `EX-DECON-BACKUP` | C1 10:00–16:00, excluding blackout; C2 pending | C1; C2 only after separate agreement | C1 example-check by Morgan Vale, 11 Nov 2026 15:05; C2 **pending** |
| Verify tester authorization in real time | C1: Sam Idris plus decision register; C2: provider verification function pending | C1: `EX-VERIFY-PRIMARY` / `EX-VERIFY-BACKUP`; C2: pending | C1 10:00–16:00; C2 none confirmed | C1; C2 pending | C1 example-check by Morgan Vale, 11 Nov 2026 15:10; C2 **not checked / NO-GO** |
| Operational/system owner | Sam Idris, C1 owner; provider operations owner pending | C1: `EX-OWNER-PRIMARY` / `EX-OWNER-BACKUP`; C2: pending | C1 10:00–16:00; C2 none confirmed | C1; C2 pending | C1 example-check by Morgan Vale, 11 Nov 2026 15:15; C2 **pending** |
| Authorizes resumption after a stop | C1: A1 **and** A2 after a stop they ordered or an operational stop, with renewed contact/window checks; C2: provider A3 plus A1 if ever approved | C1: `EX-RESUME-PRIMARY` / `EX-RESUME-BACKUP`; C2: pending | C1 only within live window; C2 none | C1; C2 pending | C1 example-check by Morgan Vale, 11 Nov 2026 15:20; C2 **pending** |

**Escalation if first contact is unreachable:** pause affected activity immediately; try the listed backup once, then responsible lead informs A1 through the fictional decision-register route. No response is not consent. If a required C1 contact remains unreachable, C1 pauses until the relevant authority confirms contact coverage and resumption within the current window. C2 cannot start regardless of contact attempts.

**Stop communication and record:** lead halts affected traffic, notifies the stop/owner/monitoring contacts, records time, reason, affected component, and caller under fictional `EX-STOP-LOG`; resumption requires the named §7 authority decision and rechecked conditions. Full triggers belong to `EX-ROE-041 v1.0 §5`; this brief adds none.

## 8 · Package index

These are illustrative **fictional case-file references, not actual files or links**. The table demonstrates what would be filed or held in a real adopter's controlled record system.

| # | Record | Fictional reference / location label | Version | State and component consequence |
|---|---|---|---|---|
| 1 | Scope record (§10.1 practice; §10.4 intake, if used) | `EX-SCOPE-041` / invented case register `EX-ENG-041` | v1.0 | Fictionally filed for C1; C2 described as conditional, not authorized. Separate §10.4 form N/A: same fields captured in fictional scope intake. |
| 2 | Rules of Engagement (§10.2) | `EX-ROE-041` / invented case register | v1.0 | Fictionally filed for C1; C2 inactive; partial C1-only execution explicit in §6 |
| 3 | Decision record for each §6b authority | `EX-DEC-A1`, `EX-DEC-A2`, `EX-DEC-A3` / invented decision register | A1/A2 v1.0; A3 none | A1 and A2 fictionally filed for C1. **A3 pending → C2 NO-GO.** |
| 4 | Per-facility written authorization carried by testers | N/A | N/A | No physical component or facility testing |
| 5 | Facility coordination record | N/A | N/A | No physical component or facility testing |
| 6 | Third-party/provider permission | `EX-DEC-A3` / invented decision register | None | **Pending; C2 NO-GO.** A1/A2 do not substitute. |
| 7 | Credential handling record (§30.3) | `EX-CRED-041` / invented controlled credential register | v1.0 | Fictionally filed for C1 synthetic tenants and named testers; C2 credentials are **not provisioned** |
| 8 | Method reference for each surface | `EX-METHOD-C1` and `EX-METHOD-C2` / invented method register | C1 v1.0; C2 draft only | C1 fictional method filed; C2 method is **draft, not approved**, and cannot be used until provider decision and scope/RoE update |
| 9 | Stop/contact check record | `EX-CONTACT-CHECK-041` / invented case register | v1.0 | Fictional C1 checks recorded; C2 contacts **pending → C2 NO-GO** |
| 10 | Stop event log, if a stop occurs | `EX-STOP-LOG` / invented case register | Not opened | N/A before any activity or stop; if a stop occurs, file the event before resumption |
| 11 | Lead readback and component notice record | `EX-READBACK-041` / invented case register | v1.0 | Fictional A1/A2 C1-only readback filed; A3 cannot yet be notified as a named party, so C2 notice is pending and C2 stays NO-GO |
| 12 | Local authority model that assigns component decision rights | `EX-AUTH-MODEL` / invented policy register | v1.0 | Fictionally filed; §4 requires A1 plus each component controller's decision, including A3 for C2 |

## 9 · Change control

| Field | Fictional entry |
|---|---|
| Scope changes decided and recorded | Fictional scope decision workflow under `EX-AUTH-MODEL v1.0 §5`, recorded first in a new `EX-SCOPE-041` version and the relevant party's decision record |
| RoE changes decided and recorded | Fictional RoE change log `EX-ROE-041 §8`, with approval by the parties whose component/condition changes |
| Brief maintainer | Morgan Vale updates this cover sheet **after** the source decision records, scope, and RoE change; prior brief version becomes superseded |

| Brief version | Change | Triggering record/version | Changed by | Fictional date |
|---|---|---|---|---|
| v1.0 | Initial readiness record: C1 GO, C2 NO-GO | `EX-SCOPE-041 v1.0`; `EX-ROE-041 v1.0`; fictional A1/A2 decisions; A3 pending | Morgan Vale | 11 Nov 2026 |

If A3 later decides, C2 does **not** automatically become GO. First file that decision, reconcile the exact C2 scope, RoE, window, stop/verification contacts, and method; then issue a new brief version with a new §6c assessment. If A1 or A2 withdraws, or a C1 condition changes, C1 stops pending the relevant updated decisions. An attempted C1-to-C2 pivot is a new component/boundary request, never covered by C1 GO.

## 10 · Readiness before the window

| Check | Fictional disposition |
|---|---|
| Every §8 record filed, N/A with reason, or pending with blocked component | Morgan Vale, 11 Nov 2026: **yes in this synthetic record**; A3/provider permission, C2 method/contact/window all pending and explicitly block C2 |
| Required parties mapped; each component has state; C1 authorities current; §1 outcome matches | Morgan Vale, 11 Nov 2026: **yes in this synthetic record**; A1 + A2 cover C1; A1 + pending A3 required for C2; outcome PARTIAL. The fictional scope/RoE explicitly permit independent C1-only execution. |
| Contacts confirmed for active hours | Morgan Vale, 11 Nov 2026: C1 primary/backup example-checks recorded for its 10:00–16:00 window; C1 must pause if coverage fails; C2 provider contacts unconfirmed and it remains NO-GO |
| Lead explains limits and GO decision holders accept or return for correction | Alex Rowan example-readback to A1 and A2, 11 Nov 2026: “C1 only, 10:00–16:00 excluding blackout; C2 and any pivot are prohibited; O2/O3 remain unanswered. A1 can stop the whole engagement; A2 can stop C1. We also stop on lost contact, window end, changed decision, or an RoE trigger.” Fictional A1/A2 acceptance is recorded as `EX-READBACK-041`; they are the required decision holders for C1. |
| NO-GO party notice and package effect recorded | C2 provider decision holder A3 is not yet assigned or reachable; notice and acknowledgment remain pending in `EX-READBACK-041`. C2 stays NO-GO. Fictional `EX-SCOPE-041 v1.0 §7` and `EX-ROE-041 v1.0 §6` explicitly permit independent C1-only execution despite that pending C2 notice; if those source records instead required package-wide acceptance, **neither component would be GO**. |

**Final boundary:** this is a model of *recording a split decision*, not evidence that either component was tested. C1's fictional GO cannot be carried into a real environment; C2's fictional NO-GO illustrates the default when a required provider decision is missing.
