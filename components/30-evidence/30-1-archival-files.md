# 30.1 — Engagement archive: required record set

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

At the close of an engagement, the working mess becomes a record. This component says **what an archive must contain, in what form, redacted how**, so that a finding stays defensible, a reviewer can reconstruct it without re-running the test, and knowledge compounds instead of leaving with the tester. It is the per-engagement closeout record set — not the working folder, not the finding-tracking system, and not the customer-delivered report (which the archive's raw material deliberately exceeds). Where a file may live and who may read it is the [storage authority (§30.2)](30-2-archive-storage.md); how secrets inside it are held is the [credential handling guide (§30.3)](30-3-credential-handling.md); the delivered report itself follows the [report standard (§30.5)](30-5-report-standard.md).

## What archiving is for

Five jobs justify the work: a finding stays **defensible** (the test condition and evidence chain can be reproduced); knowledge **compounds** across engagements; **continuity** survives a tester's departure; the record is **auditable** against the adopter's own obligations; and a **retest** starts fast from a known state.

## The central rule

**A reviewer who was not there can rebuild the path from raw output to finding without re-running the test.** If the archive cannot support that, it is incomplete no matter how many files it holds.

## Minimum record set

Organize by engagement, then by record class. The adopter chooses the folder scheme; these are the classes, each required unless marked not-applicable with a reason recorded in the engagement README:

| Class | Holds |
|---|---|
| Scoping | Signed scope, scope-change requests (date + approver), intake reference, out-of-scope items with rationale |
| Architecture & onboarding | Target architecture, auth model, **test-account provisioning record** (names/roles/requestor/date — never credentials in cleartext; point to the secret store), environment spec |
| Test plan & methodology | Tailored plan (applied/skipped + why), methodology referenced, **coverage matrix** (section → tested? → evidence ref); for a control assessment: in-scope control, method subset applied + why, and efficacy outcome (held or bypassed, with evidence) |
| Tool configuration | Scope/session config notes, custom payloads/wordlists (or versioned reference), tool versions, authenticated-session capture method |
| Captured project files | The proxy/tooling project file(s) — see *Sensitive material and secrets* below |
| Tool output & logs | Scan output (machine + human readable), raw DAST, script logs with timestamps, packet captures (unintended third-party data redacted), all raw output that informs a finding |
| Evidence / screenshots | One set per finding, in report order, named for what each demonstrates; the **original uncropped capture kept alongside any annotated version** |
| Findings working notes | Reasoning, reproduction, candidate severity rationale, references; and **findings considered but not reported, with the reason** (false positive / out of scope / accepted / duplicate) |
| Final report | Delivered report + source, severity distribution, per-finding severity vectors, attack-chain evidence (in the report, or a separate rider when a multi-step chain cannot be shown inline), and the link from each finding to its tracking ID |
| Customer communications | Kickoff, status, real-time high/critical notices, delivery, acknowledgement, pushback/clarification, risk-acceptance correspondence |
| Retest | Request (date/requestor/findings), **result per finding** (Confirmed Fixed / Partially Fixed / Not Fixed / Not Retestable), evidence, memo, updated status |
| Closeout notes | Timeline, lessons learned, knowledge contributions (new issue-library entries, reusable patterns/scripts with location), and **sign-offs** (see below) |
| Agentic-tool records *(only when an autonomous/agentic tool was used)* | See *Conditional: agentic-tool records* below |
| README (engagement) | ID, target, type, dates, lead + supporting testers, one-paragraph summary, severity counts, not-applicable items with reason, deviations with reason + approver |

## Scope status vs coverage outcome (two different facts)

Record **scope status** — in-scope / out-of-scope / conditional — separately from **coverage outcome** — examined / partial / blocked / not-tested. A scoped item that was never reached is "in-scope, not-tested," not silently absent. The coverage matrix carries both so a reviewer sees what was promised and what was actually done.

## Evidence sufficiency

Evidence is sufficient when a qualified reviewer could accept or reject **that** claim for **that** method from what is archived — not when a universal artifact list is satisfied. Keep the original capture when redaction would destroy its evidentiary value (under the access controls of the storage authority). Where a finding rests on inference rather than demonstration, the working notes say so.

## Sensitive material and secrets

Some records hold exactly the sensitive content a finding is about — a response exposing data, a captured session token, a proxy project file that cannot be stripped without destroying its value. The archive's protection for these is **structural, not redaction**: a restricted location, a secret store holding real secrets by reference, access control, and audit logging, per [§30.2](30-2-archive-storage.md) and [§30.3](30-3-credential-handling.md).

**Sealed-artifact rule (consistent across §30.1 / §30.2 / §30.3):** prefer the least-revealing adequate form first. Retain an artifact **intact** only when a redacted or extracted form would destroy its evidentiary or retest value, **and** when any captured credentials it contains have been confirmed revoked or are test-only, **and** when it stays in the restricted location under the storage authority. Retaining an intact artifact is never justified by "pen-test evidence can't be sanitized" alone, and no storage location is promised safe in the abstract. To share evidence outward, export a bounded selection, never a whole project.

## Conditional: agentic-tool records

When an autonomous or agentic tool performed work, archive additionally: tool identity (name, version, capability tier, model-inventory reference); a **cleartext-secret scan** of logs and output before archival (per [§30.3](30-3-credential-handling.md)); session/run logs as the authoritative record behind any narration; the input configuration/prompts/scope as run; the raw pre-validation output; the **validation plan applied and its outcomes** (what was reproduced, by whom, what escalated); and the lead's sign-off on validation completeness with a reviewer co-sign.

## Sign-off and the authorization gap

Closeout records **two sign-offs**: the engagement lead (archive populated, redaction done, README complete) and an independent reviewer (completeness spot-checked, redaction confirmed). A one-person practice separates the *roles in the decision* and obtains an independent reviewer elsewhere when one is required and unavailable; it does not pretend a second reviewer exists. An action taken outside the rules of engagement is **paused, recorded, escalated, and classified under the adopter's own criteria** — closeout is blocked until that is resolved, and report or archive wording never cures an unauthorized action.

## Retention and disposal (adopter sets the clock)

Map each record class to the adopter's retention schedule and apply the longest applicable; a legal hold overrides and suspends disposal. **Disposal at end of retention is a reviewed decision, not an automatic deletion**, and is logged. Note the two clocks that the credential guide defines: a live secret is disposed at the retest-window close, while the archived artifact that references it follows the records schedule — disposing the secret does not delete the archive.

## Reader test before adoption

Can a reviewer who was not on the engagement open this archive and, from it alone, reconstruct what was tested, what was proven versus inferred, what was redacted and why, and who signed off — without calling the tester? If not, the closeout is not done because folders exist.
