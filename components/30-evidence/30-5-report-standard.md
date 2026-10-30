# 30.5 — Penetration test report: standard and template

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A penetration-test report is a deliverable an author produces and a reviewer defends. This component gives the **author** a fixed required-content skeleton and a fill-in template, and gives the **reviewer** a claim-by-claim check that every rating and assertion is earned before anything is delivered. It is a reporting standard, not a testing methodology and not a disclosure authority — a vulnerability that needs to leave the adopting organization follows [coordinated disclosure (§50.1)](../50-support/50-1-coordinated-disclosure.md); an external or auditor request for a report follows [audit and external information requests (§50.5)](../50-support/50-5-audit-handling.md).

## The central rule

**No claim ahead of its evidence.** A finding does not ship on a published-advisory or CVE mapping alone; a severity that departs from the base score shows both the base score and the reason; an impact stated in business terms is traceable to a technical observation. Elegant writing never converts an untested possibility into a stated fact.

## Part 1 — Required report content

Every report carries these sections, in this order. Depth varies with the engagement; the skeleton does not.

1. **Executive summary** — for leadership and risk owners. Business risk in plain language: what was tested, the headline outcome, the most material exposures, and overall posture. No raw technical detail.
2. **Engagement overview** — scope (assets / URLs / endpoints and the declared depth of testing), objective, dates and window, the methodology referenced, the authorization relied on (the adopter's authority-to-operate plus the engagement scope and rules of engagement), and the limitations and caveats that bound the result.
3. **Findings** — one per issue. Each finding records: title · severity (a named scoring model's base result plus a contextual rating) · affected component · impact (business and technical) · **evidence** · reproduction steps · remediation · references (e.g. CWE / OWASP / CVE). See the evidence and severity rules below.
4. **Attack chains** — where individually low or medium issues combine into a higher-impact path, the path is shown explicitly. A single finding record cannot stand in for a chain.
5. **Positive observations** — controls that held. Balanced reporting is part of the standard.
6. **Appendices** — references to full tool output and evidence held in the engagement archive (not pasted inline), scope detail, the identity contexts tested, and any compliance overlays.

### Evidence (typed, with residual uncertainty)

State **how** each finding is known, and what remains unproven:

- **Demonstrated** — exploited safely within the rules of engagement (proof attached by reference).
- **Observed behavior** — the system behaved in a way that reveals the flaw, short of full exploitation.
- **Configuration / Code / Design** — the weakness is established from inspected configuration, source, or design where live exploitation was unsafe, out of scope, or disallowed.

Each finding names its evidence type, the validation performed, and the **residual uncertainty** that a reader needs to weigh. Configuration, code, and design evidence can support a finding where exploitation would be irresponsible — but the report says so rather than implying a demonstration that did not happen.

### Severity

Compute a named model's base severity first; a contextual layer may raise or lower the **reported** severity for real exposure (reachability, compensating controls, data sensitivity, strength of evidence). Any departure from the base is justified in the finding, with both the base result and the rationale shown. Severity is justified, never asserted. Context from an environment that was **not** tested never moves a rating.

### Classification, distribution, and redaction

- Mark every report with the adopter's own confidentiality level, on the title page and in the footer, and raise it where regulated data is involved.
- Deliver only to the engagement requester / risk owner and the named remediation stakeholders, through the agreed controlled channel. Do not grant the recipient general access to the testing workspace in place of a bounded package. Onward-handling terms travel with the report.
- **Redaction is a reviewed process, not a one-time pass.** Before export, remove or mask real personal or regulated data, authentic production credentials, out-of-scope third-party data, and internal specifics more useful to an attacker than to a remediator. Strip hidden metadata and comments. Share the minimum adequate subset of evidence (selected items, not a whole project export). Verify the rendered/exported bytes, not only the editing view; a reviewer confirms the redaction on the actual export.

## Part 2 — The template (fill-in skeleton)

```
[Title] Penetration Test Report — <Engagement ID> — <Date>
<Confidentiality marking>

1. Executive Summary
   Business risk, what was tested, headline outcome, posture. No raw detail.

2. Engagement Overview
   Scope & depth · Objective · Dates/window · Methodology referenced ·
   Authorization (authority-to-operate + scope/RoE) · Limitations & caveats

3. Findings  (repeat per issue)
   - Title
   - Severity: <model> base <score> → reported <level>  (rationale if adjusted)
   - Affected component
   - Impact: business / technical
   - Evidence: <Demonstrated | Observed | Configuration | Code | Design> + validation + residual uncertainty
   - Reproduction steps
   - Remediation
   - References: CWE / OWASP / CVE / other
   - Tracking reference: <adopter's finding-register ID>

4. Attack Chains
   Explicit path(s) where lower-severity issues combine.

5. Positive Observations
   Controls that held.

6. Appendices
   Evidence references (archive), scope detail, identity contexts, compliance overlays.

Footer: <Confidentiality marking> · <report ID> · <version> · page <n>
```

A retest addendum references the original report rather than silently editing it. An erratum is a dated correction that preserves the version originally delivered.

## Part 3 — Review before delivery

Two human reviews gate every report; the review correspondence is retained as the audit record.

- **Stage 1 — peer review.** A second tester runs the mundane completeness checks (formatting, required fields present, cross-reference and link integrity — automatable) and reads the report against the acceptance checklist below.
- **Stage 2 — defensibility review.** A designated senior reviewer reads for defensibility, severity calibration, executive-summary fit, and onward-handling.
- Route the draft to the review group and the senior reviewer together, adding a specialty reviewer when the engagement type calls for one. When a report is authored by an outside contributor, a designated reviewer for that contributor's work is always included.

**Acceptance checklist (every item passes, or the report does not ship):**

- Every finding has: severity (base + contextual + rationale), impact, typed evidence with residual uncertainty, reproduction, remediation, references, and a tracking reference.
- No finding rests on an advisory/CVE mapping alone.
- Attack chains are shown where they exist.
- Executive summary present and calibrated to the technical body.
- Redaction confirmed on the actual export; classification and distribution marked; delivery channel confirmed.
- Scope, authorization (authority-to-operate + rules of engagement), and limitations stated.
- Severity treatment consistent; no rating asserted without justification.

**One disposition left for the adopter:** independent review is the norm. Where a single reviewer is genuinely unavailable, a release needs a separate approver's agreement. A lower-consequence report delivered without independent review is a documented exception, conspicuously marked **NOT INDEPENDENTLY REVIEWED** and sent only with the requester's written agreement — it is never recorded as a passed review. An unauthorized action is never cured by report wording; a technique outside the rules of engagement is paused, recorded, escalated, and classified under the adopter's own criteria.

## Part 4 — Lifecycle

Draft → Stage 1 peer review → Stage 2 defensibility review → redaction and a cold-reader check → delivery via the engagement channel → presentation at the closing meeting → file the **final** as the locked engagement record in the archive ([§30.1](30-1-archival-files.md)). The final is the record of the engagement; working drafts are not retained as the record.

## Part 5 — A worked finding (fictional)

> **F-01 — Cross-tenant access to order records (staging).** Severity: base High → reported High. Affected component: orders API, staging. Impact: a tenant could read another tenant's order history (business: confidentiality breach across customers; technical: missing tenant check on the records endpoint). Evidence: **Demonstrated** in staging with two test tenants; residual uncertainty — production enforcement was not tested and is reported only as an unverified statement from the asset owner, which would need separately authorized validation. Reproduction: [steps, archived]. Remediation: enforce tenant scoping server-side; add a regression test. References: CWE-639; OWASP API1.

This illustrates the record shape only; it is not evidence of an actual assessment.

## Reader test before adoption

Can an author fill this without inventing authority, and can a reviewer fail a report that does not earn its claims? Can a cold reader, from the report alone, see what was tested, what was proven versus inferred, what is still uncertain, and who may receive it? If not, the report is not ready because a template was completed.
