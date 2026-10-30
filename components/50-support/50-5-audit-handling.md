# 50.5 — Audit and external information requests

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

An assurance request can usually be satisfied without handing over the technical playbook an attacker would want. This component is the one route for **receiving, understanding, approving, delivering, and recording** such a request — aiming at a useful answer, proportionate disclosure, and an exact account of what left the practice, rather than a reflexive refusal or a reflexive report dump.

## The decision this supports

Auditors and other requesters usually need to verify that a control exists and operates — scope, in-period testing, finding tracking and remediation, retest — and rarely need exploitation detail. Matching the artifact to the requester's real objective is a security control, not obstruction.

## Roles and records to establish locally

| Role | Job | Boundary |
|---|---|---|
| Request coordinator | Owns intake, routing, answer assembly, and the request record | Cannot infer a requester's authority from a title alone |
| Authorized alternate | Keeps the route working when the coordinator is unavailable | Holds only the disclosure authority explicitly delegated |
| Artifact owner / qualified reviewer | Checks source records, accuracy, scope, and redactions | Does not approve disclosure beyond their authority |
| Disclosure approver | Resolves restricted or exceptional releases | Consults legal, privacy, customer, or other owners where the actual agreement requires |

Give the route a published intake channel and a named alternate, and record each request in [§50.8](50-8-disclosure-log.md) when it arrives. A one-person practice separates the *roles in the decision* without pretending to a second employee; if independent review is required and unavailable, it holds the release or obtains an authorized reviewer elsewhere.

## Request-to-disclosure route

1. **Receive and register.** Record who asked, on whose behalf, the claimed authority, the requested artifacts, the purpose, period, due date, destination, and handling terms. A due date is a request field, not a promise.
2. **Verify.** Confirm identity, entitlement, scope, and the permitted recipient/destination through authoritative records. A finding owner asking for **their own** report is a distinct controlled-delivery route — verify ownership and log the transfer; sending it anywhere else is a fresh disclosure decision.
3. **Define the answer.** Ask what the requester must actually establish: program design, an in-period sample, completion of a named engagement, a finding's status, or something else. Identify the system of record and the partner who owns any adjacent control — do not speak for scanning, remediation timelines, patching, contracts, or privacy merely because the request arrived at the testing team.
4. **Select the least-revealing adequate artifact.** A verified summary or attestation often answers the question. If not, select a bounded extract. Full reports, raw evidence, exploit paths, credentials, sensitive data, bulk archives, and out-of-scope material go through the restricted route.
5. **Check and approve.** Verify factual claims against current records; check classification and contract terms. For a redacted extract, the producer and an independent qualified reviewer inspect the **actual export**; for a restricted release, obtain the designated approval and any required partner review. A template being approved does not preapprove its filled contents.
6. **Deliver and witness.** Use an approved, recipient-bound channel. Check the recipient, payload, restrictions, and the delivery result. Do not grant general access to the testing workspace in place of a bounded package.
7. **Close the record.** In [§50.8](50-8-disclosure-log.md), link the released artifact and version, the decision and approver, the withheld items and reasons, the redaction record, the delivery proof, and any follow-up commitment. Retain the original and the exact released copy under the adopter's schedule. Feed recurring requests and review friction into [practice improvement (§60.1)](../60-learning/60-1-learning-loop.md).

## Three disclosure patterns (per artifact, not per requester)

| Pattern | Candidate content | Required decision |
|---|---|---|
| **A — Bounded program answer** | Verified program description, period/scope summary, aggregate measure, blank template, or a filled [attestation summary (§50.6)](50-6-attestation-summary.md) | Confirm the answer is accurate, in scope, and safe for this recipient |
| **B — Redacted case extract** | A specific engagement summary or selected report fields | Confirm need; inspect the redaction on the exported copy with a qualified second reviewer; preserve original and released versions |
| **C — Restricted detail** | Full report, raw evidence, an exploitable path, sensitive personal data, a bulk corpus, or another party's information | Hold until the named disclosure authority and applicable partners approve the exact scope, recipient, terms, and channel |

The patterns apply **per artifact**. An auditor's title does not automatically authorize a full report; an internal request can still be too broad; and a legitimate regulatory or contractual obligation may require more than a summary. The adopter's actual authority and law govern — these are not universal confidentiality classes.

## First reply

The first reply **acknowledges and scopes without an attachment**; after the requester, authority, and destination are verified, the first *substantive* disclosure is normally a filled, verified [attestation summary (§50.6)](50-6-attestation-summary.md). Do not send even a summary to an unverified destination.

> Thank you. We can help identify the evidence that addresses your request. Please confirm the control or question, the period and scope, the specific level of detail needed, your authority to receive it, the destination and handling terms, and the requested date. We will verify the applicable records and respond through the approved channel.

## Redaction and release check

Before exporting, look for credentials and tokens, personal or regulated information, internal addresses or topology, payloads and reproduction steps, unremediated exploit paths, third-party data, comments and hidden fields, embedded files, and metadata. Remove or mask in a way appropriate to the format, and **verify the rendered/exported bytes, not the editing view**. Keep a reference to the original, the exact released version, and a redaction-decision record. Do not promise that a category can *never* be released — route an exceptional legal or contractual requirement through the responsible authority.

## A compact example (fictional)

An internal assurance team asks whether a defined application population was tested during an audit period and requests two sample reports. The coordinator verifies the team's authority and the exact population and period, provides a filled [§50.6](50-6-attestation-summary.md) summary drawn from the engagement and finding records, then decides whether a redacted sample is genuinely necessary. A second qualified reviewer checks any extract; full reports and raw evidence are not bundled by default. The [disclosure log (§50.8)](50-8-disclosure-log.md) records both what was delivered and what was withheld. *This illustrates the route, not an actual assessment or a universal requirement.*

## Reader test before adoption

Can a person unfamiliar with the request find the recipient's authority, the period and population, the source record for every claim, the exact delivered artifact, and who reviewed the release? If not, the answer is not ready merely because a form was completed.
