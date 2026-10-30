# 40.8 · Skills and Engagement-Eligibility Matrix

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.
> This is a blank, locally maintainable template. It contains no real roster, individual credential, clearance, or personnel record.

## Purpose

The question is not simply “Who has a certification?” It is “Who can safely and credibly take this particular assessment now, with the required authority, equipment, supervision, and availability?” A skills matrix helps route work, identify single-person dependencies, pair a developing tester, and plan training. It does not replace engagement authorization, human assessment of competence, employment decisions, or a controlled personnel system.

Maintain the named matrix in a restricted team location. Share only aggregated or de-identified capability coverage outside the authorized audience. Do not publish filled rows, citizenship/clearance details, individual performance notes, or copies of credentials in a public repository.

## Separate four different states

| State | Meaning | Evidence / refresh |
|---|---|---|
| Demonstrated capability | A tester has performed or reviewed the domain to the local standard, with a date and appropriate evidence. | Peer-reviewed work, supervised exercise, or other accepted proof; recheck when technology or method changes. |
| Development path | A tester is learning or can assist under named supervision, but is not yet an independent assignment choice. | Training or pairing plan; do not turn interest into proficiency. |
| Eligibility | The person may work this target and data class under current legal, contractual, organizational, and engagement constraints. | Approved access/authorization reference and expiry or event trigger; keep sensitive reasons in a separate controlled system. |
| Readiness | The necessary device, tool license, network path, safe environment, time, and reviewer/backup are actually available for this assignment. | Current rig/access check and staffing confirmation; a past capability mark is insufficient. |

`Go-to` means a locally acknowledged specialist or reviewer; it does not make one person the only permitted owner. `Not primary` means a pairing or spin-up route may be available, not that the person lacks all skill. Organizations should define proficiency bands with examples rather than letting a check mark carry an unexplained judgment.

## Blank restricted roster structure

Store the following in the authorized roster, not in a public artifact. One row per person and capability, or link a separate person table and capability table if the team is large.

| Field | Local entry |
|---|---|
| Tester identifier and employment/contract status | [Restricted local record] |
| Capability domain and level | [Web, API, mobile, network, infrastructure, database, thick client, wireless, physical, AI/LLM, code review, or a locally defined domain; demonstrated / supervised / developing / not assessed] |
| Evidence and assessor | [Record pointer, date, reviewer; no customer data in this sheet] |
| Specialist/backup | [Named primary reviewer and at least one alternative or explicit gap] |
| Scope/eligibility constraints | [Opaque authorization pointer, permitted target class, next check; sensitive reason elsewhere] |
| Equipment and environment | [Rig/kit/license/access readiness and date verified] |
| Availability and assignment | [Current capacity/rotation pointer, not a permanent capability claim] |
| Credential record | [Credential name, issuer, ID if needed in restricted system, earned date, applicable renewal or continuing-education rule, verified date] |
| Next development/review action | [Pairing, lab, review, renewal if actually required, or method update] |

Do not invent an expiration date for a credential. Track a renewal date only when the issuer or applicable rule actually provides one; otherwise record the correct standing and a reasonable verification trigger. A credential may be useful evidence but does not prove current ability in every test domain. Conversely, a capable tester may be temporarily ineligible because a device, contract boundary, or authorization is missing.

## Assignment decision card

For a proposed engagement, record:

1. Target domain, technology, data class, authorized scope, and required methods.
2. Candidate tester's demonstrated level and date/evidence, with supervised route if relevant.
3. Current eligibility and equipment/access readiness, checked for this engagement.
4. Review/backup coverage and whether the team can withstand absence or urgent reassignment.
5. Any gap, mitigation, and decision authority. A gap may lead to pairing, a different tester, adjusted scope, or a deferred start; it does not disappear because the roster is green.

**Synthetic example:** a tester has strong mobile experience but the only authorized device cannot run the supplied build. Another tester has the device but is still supervised in mobile testing. A defensible plan could pair them with a qualified reviewer if the engagement permits it, or delay until a supported rig is available. Neither person's credential list answers the assignment question alone.

## Maintenance and output

Each tester can propose corrections to their own capability and credential record; a designated steward verifies eligibility and restricted evidence. Refresh on joining/leaving, authorization or equipment change, credential-rule change, method change, and a locally chosen periodic review. A de-identified capability view may show domains with zero, one, or multiple independently ready testers, reviewer coverage, and training gaps. Do not expose small-cell details that re-identify people. Use the result for staffing and development decisions, not as an automated performance rating.
