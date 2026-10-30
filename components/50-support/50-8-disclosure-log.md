# 50.8 — Audit request and disclosure log template

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

This is the operating log that records each audit or external-information request from intake through delivery, evidencing **both** cooperation and minimum-necessary disclosure. It is the record half of [audit and external information requests (§50.5)](50-5-audit-handling.md) and captures the issuance of each [attestation summary (§50.6)](50-6-attestation-summary.md). A single request often produces several release decisions over time — corrections, additional payloads — so the log keeps **one stable request record** plus **append-only release events**, rather than a single flat row that could hide a later correction.

## The log itself is sensitive

A disclosure log exposes engagement metadata — who asked, what was shown, what was withheld. Restrict access to it, retain it under the adopter's schedule, and **disclose even the log only through [§50.5](50-5-audit-handling.md)** — do not treat it as freely releasable program evidence by default.

## Request record (one per request, opened at intake)

| Field | Definition |
|---|---|
| Request ID + received date | A stable identifier and the date it arrived |
| Intake route + coordinator/alternate | Which door it came through and who owns it |
| Requester + represented org | Role and organization — not bare initials |
| Claimed and verified authority | The basis asserted, and how it was verified before any release |
| Purpose / control / question / population / period | What the requester must actually establish |
| Artifacts / detail requested | What was asked for, and at what level of detail |
| Classification + other data constraints | The adopter's marking and any privacy/contract constraint |
| Destination / recipient / handling | Where it will go, to whom, under what handling terms (NDA, retention, discoverability) |
| Requested date + response commitments | The due date (a field, not a promise) and any commitment made |
| Current state | open / awaiting-verification / awaiting-approval / partially-delivered / closed / withdrawn |

## Release / decision event (append one per decision; never overwrite)

| Field | Definition |
|---|---|
| Event ID + request ID + timestamp | Links the event to its request, in order |
| Item + disposition | released / withheld / corrected / superseded / redirected |
| Disclosure pattern + reason | The [§50.5](50-5-audit-handling.md) A/B/C pattern and why |
| Exact artifact + version/hash | Precisely what left, by version and digest |
| Redaction record + independent check | Reference to original/released/manifest, and who checked the export |
| Decision authority + partner reviews | Who approved; any legal/privacy/customer review |
| Recipient + delivery witness | Who received it and confirmation of receipt (a send success is not a witness) |
| Withheld scope + reason | What was deliberately not provided, and why |
| Follow-up / correction / retention | Commitments, corrections, and the retention applied |

## Worked example (fictional)

> **Request EXAMPLE-001** — received {date}; intake via the assurance desk; requester: a control-assurance analyst at an internal assessment function; claimed authority: an internal control assessment, verified against the known internal team; purpose: evidence that the testing control operates (methodology, tracking, a sample); classification: restricted program evidence; destination: an internal assessment workspace, no external transfer; state: delivered.
> - **Event -A** — released the [attestation summary (§50.6)](50-6-attestation-summary.md) and a methodology reference and policy crosswalk (Pattern A); recipient confirmed; nothing withheld at this step.
> - **Event -B** — released one engagement report reduced to executive summary and findings list (Pattern B); redaction checked on the export by a second reviewer; original and released versions preserved.
> - **Event -C** — withheld raw evidence, full reports, and unremediated-finding detail (Pattern C not requested); reason recorded.

*This illustrates the structure, not an actual request.*

## How to use it

- Open **one request record at intake** and update its state through delivery; add a **release event per decision** — never a new request row per release.
- Verify identity and authority **before** any release.
- Record what was **withheld**, not only what was provided.
- **Reference, don't embed** — point to the redaction manifest and the exact artifact/version; do not paste sensitive content into the log.
- Retain under the adopter's schedule; surface the log only through [§50.5](50-5-audit-handling.md), under access control.

## Reader test before adoption

From a request record and its events, can a reviewer see who asked, under what verified authority, exactly what was released and withheld across every decision, who approved each, and who received it — without the log itself leaking the engagement detail it is meant to govern? If not, the log is not doing its job.
