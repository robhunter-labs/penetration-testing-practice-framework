# 50.6 — Attestation and audit-summary template

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

This is the fillable form behind the first substantive answer to an assurance request: a bounded summary that a penetration test happened — in scope, in a stated period, by qualified testers, with findings tracked and remediation underway — **without** exploit detail. It is the default Pattern A disclosure under [audit and external information requests (§50.5)](50-5-audit-handling.md); anything beyond it escalates there and is recorded in the [disclosure log (§50.8)](50-8-disclosure-log.md).

## When to use it

As the first substantive reply after a requester, authority, and destination are verified. It carries summary facts only — no reproduction steps, exploit detail, raw evidence or tooling output, affected-system specifics, or unremediated-finding detail. A field that would require any of those is a Pattern B/C decision under [§50.5](50-5-audit-handling.md), not a line in this form.

## Verification before wording

Every value is filled from a named source with a cut-off, and qualified where the record is incomplete. Do not label open work "remediated," and state an unknown honestly. Before issuing, check the wording for unsupported absolutes — "all," "independent," "compliant," "closed," "no vulnerabilities" — each of which can turn a summary into a false attestation; remove any the records do not support.

## The form (fill the `{...}`; delete guidance in braces)

```
PENETRATION TESTING — ATTESTATION & AUDIT SUMMARY
Confidentiality: {adopter's marking}          Prepared on: {YYYY-MM-DD}
Recipient & handling terms: {named recipient · destination · NDA / handling ref}
Summary ID / version: {id · v}                Source records referenced: {engagement + finding records, with cut-off date}

1. UNIT OF ASSERTION
   This summary attests to: {a single named engagement} OR {a defined population over a period}
   — state which; do not let a single engagement imply a whole program, or vice versa.

2. WHAT WAS ASSESSED
   Scope (safe level of detail): {category — web app / API / internal / external / mobile / control assessment / red team / retest, and the unit}
   Test window / period: {start – end}
   Authorization of record: {the adopter's authority to operate / rules of engagement / engagement ID}
   Methodology used: {named methodology + any external references the adopter actually follows}
   Testers & review: {qualified internal testers / approved external testers; the review that was applied}

3. WHAT THE RECORDS SHOW  (summary facts only — no technical detail)
   | Measure | Verified value | Source & cut-off | Qualification |
   |---|---|---|---|
   | Engagements (or assets) due vs tested in period | {n of m} | {record · date} | {completeness note} |
   | Findings by severity | {Critical/High/Medium/Low/Info counts} | {finding record · date} | {as-of note} |
   | Remediation status | {n remediated · n open within target · n accepted/deferred} | {finding record · date} | {targets owned by {owner}} |
   | Retest status | {performed? outcome} | {retest record · date} | {scope of retest} |
   Overall posture: {1–2 plain-language sentences, calibrated to the counts}

4. HOW THE CONTROL OPERATES
   Methodology is versioned and controlled; severity uses {named model}; reports pass {the adopter's review};
   findings are tracked in {the adopter's finding system} with remediation targets owned by {owner};
   records are retained per {the adopter's schedule}.

5. WHAT IS AND IS NOT INCLUDED
   Included: this attestation, scope/period, severity counts, remediation/retest status, how the control operates.
   Not included: reproduction steps, exploit detail, raw evidence or tooling output, affected-system specifics,
   unremediated-finding detail — available only through a separate decision under §50.5.

Prepared by: {coordinator / alternate}      Approved (if beyond Pattern A): {approver}
Disclosure logged: {§50.8 ref}           Handling terms: {ref}
```

## Issuance checklist

- The unit of assertion is stated (single engagement vs population) and not overstated.
- Every value has a source and cut-off; incomplete records are qualified, not rounded up.
- No unsupported absolute ("all / independent / compliant / closed / no vulnerabilities").
- Counts and status are pulled from the finding and engagement records as of a stated date, and any remediation target is attributed to its owner rather than asserted as met.
- The filled content — not just the format — is checked before issue; an approved format does not preapprove this instance.
- Issuance is recorded in [§50.8](50-8-disclosure-log.md); anything beyond a bounded summary escalates under [§50.5](50-5-audit-handling.md) rather than being bundled in.

## Reader test before adoption

Could a reviewer take this summary and the cited source records and confirm each value independently, and see plainly what is attested, as of when, and what is deliberately excluded? If a value cannot be traced to a record, it does not belong on the form.
