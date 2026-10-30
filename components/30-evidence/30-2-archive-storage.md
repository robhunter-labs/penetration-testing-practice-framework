# 30.2 — Archive storage authority and compensating controls

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

Penetration-test evidence is unusually sensitive: a finding often *is* the sensitive content it reports, and a captured session token or proxy project file loses its value the moment it is stripped. So a general "no secrets in storage" rule collides with "keep the evidence that makes a finding defensible." This component is the decision aid for that collision — **where evidence may live, who may read it, and when a standard control may be excepted for a specific file** — and the standing authority record that makes the answer legible to a later reviewer. It governs the restricted store; it does not own secrets (that is the [credential handling guide (§30.3)](30-3-credential-handling.md)) or define the record set (that is [§30.1](30-1-archival-files.md)).

## The central rule

**A blocked file is a question before it is a request.** When a data-loss control flags or quarantines a required file, ask first whether sensitive content was left in it *by accident* — if so, remediate it; there is nothing to except. Only a file whose value would be destroyed by sanitization, and which must be retained anyway, is a candidate for a scoped exception.

## Five commitments an adopter makes

1. Data-loss prevention stays **on by default**; a location is never broadly disabled to make pen-test storage convenient.
2. Standard security controls (encryption, access control, audit logging, retention, external-sharing restriction, strong authentication) are **never excepted** — only the narrow content-scanning block on one justified file is.
3. Compensating controls operate **alongside** the standard controls, not instead of them.
4. Every exception, and the authority behind the whole arrangement, is **recorded** so it reads the same regardless of how any single case arose.
5. The posture is **reviewed and renewable**, not asserted once.

## Three layers

| Layer | What it is | Who decides |
|---|---|---|
| Base controls | Encryption, access control, audit logging, retention, external-sharing restriction, strong auth — the platform's standing security | Set by the adopter's enterprise; not the testing team's to weaken |
| Compensating controls | Restricted location + named access group, the [record standard (§30.1)](30-1-archival-files.md), the [credential guide (§30.3)](30-3-credential-handling.md), audit logging with periodic sampling, periodic and annual review | The testing team operates; leadership owns |
| Exception | A scoped content-scanning exception for **one specific required file** that meets the bar below | Requested by the tester, endorsed by the team lead, actioned by the data-security owner |

## The exception bar

A file qualifies only when **both** are true: a redacted or extracted form would **destroy** its evidentiary or reproduction value (so a lesser form was genuinely tried first), **and** it must be retained under the record standard and retention schedule. The routine case is a proxy project file; occasional cases are raw tool-output logs and finding-evidence screenshots. "Pen-test evidence can't be sanitized" is never, by itself, an acceptable reason — the lesser form comes first, and the intact form is a last resort, not a default.

A granted exception is a **content-scanning exception for that file**, not a security-control exemption. It is logged in the engagement record.

## What monitoring can and cannot do

Audit logging answers *who did what* (access, modification, sharing, permission change); content scanning answers *what a file contains*. They are different questions, and neither substitutes for the other. Logs are useful for anomaly detection (bulk download, unexpected accounts, off-path permission changes → escalate) — but their immutability and admin-proofing are properties to **verify on the actual platform**, not to assume. Monitoring catches some misuse, not all; state that limit rather than promising detection.

## Roles (assigned locally)

Request originator (documents the file, context, and need) · team lead (endorses the request, owns the governance path, confirms compensating controls are in force) · data-security / platform owner (reviews and actions the scoped exception) · leadership (escalation for material exceptions, annual review) · access-audit owner (designs and runs the periodic access review). Separate the roles in the decision even in a one-person practice; where independent review is required and unavailable, **hold the change** or obtain an authorized reviewer elsewhere — never self-approve a material exception.

## Decision path

1. A required file is blocked or needs to live in the restricted store.
2. Was sensitive content left by accident? → remediate; no exception.
3. Does the file genuinely need to remain, in a form a lesser version would ruin? → if no, use the lesser form.
4. Confirm it is retained under the schedule and classified correctly.
5. Document file + context + need; confirm compensating controls are in force.
6. Team lead endorses; a material exception (broadens scope, spans teams, sets precedent, touches a high-importance control) is escalated — when in doubt, escalate.
7. Data-security owner reviews and actions a scoped content-scanning exception.
8. Record the decision, approver, and compensating controls in the engagement record.
9. Review on the normal cycle; re-decide on change.

## Retention, hold, and disposal

Retain under the adopter's schedule, applying the longest applicable; a legal hold suspends disposal. Disposal at an end condition is a **reviewed decision**, not a calendar auto-delete, and is logged. Credential disposal and artifact retention run on different clocks (see [§30.3](30-3-credential-handling.md)); disposing a live secret does not delete the archived artifact that referenced it.

## Review and renewal

Sample periodically (structure, classification, credential-handling compliance, anomalous content) and review formally on a set cycle, with off-cycle triggers (a change to the classification, cloud, or data-loss policy; a change to the record or credential standard; an incident; a change to the team's scope, membership, or mission).

## Reader test before adoption

Can a reviewer trace the authority chain — sanctioned activity → artifacts → location → access → governance → retention → disposal — and see, for any excepted file, why the exception was necessary, who approved it, and what still protects the file? If the arrangement cannot be explained without "because we needed to," it is not ready.
