# Change log

Corrections and changes are kept visible and dated here, newest first. The Git history has the full detail.

## 1.1.0 — 2026-11-10

- §30.1 and §30.5: a tester action log as a record class; the report carries a timeline drawn from it, with the log available on request (NIST SP 800-115 §7.4.1; PTES; CREST CDPT §10).
- §30.5: a statement of totality against the defined scope in the engagement overview and template (CREST CDPT §10).
- §00.3 §4: record whether legal reviewed the testing plan (NIST SP 800-115 §6.6).
- §90.1 §8.1: an automation-bias caution for validators (NIST AI 600-1 §2.7).
- §90.1 §8.6, new: where automated checks run out; an oracle that does not fire is recorded as `unknown`. §90.0 defines *oracle (check)*.
- §20.13: a training-data overlap caution for AI targets (NIST AI 600-1 MS-2.11-001).
- §10.2: where testing runs from, as an operating decision (NIST SP 800-115 §6.4.2); the scope and rules-of-engagement split now cites PTES.
- §40.6: an optional professional code of conduct (CREST CDPT §7.2).
- §90.5 Draft v0.2: new §7, noise classes behind the rates, with the measure each one moves.
- §90.1 §8.7, new: the validation package (six parts, a provenance label per part, four questions, a ruling tied to the package version), after *Proof Outside the Model*; §30.1 archives the package version ruled on; §90.0 defines *validation package*.
- §90.1 §9.4: a candidate escalated before validation finishes carries a "not yet validated" label and a named validator.
- §90.1 §10.5 and §30.1: integrity of agent-produced evidence: a run log the agent cannot alter, digests recorded at capture and re-checked, and what a digest does not show (OWASP APTS AR-010, AR-020, RP-005).
- §10.2 §6 and §90.1 §10.6, new: what a stop means before, during and after an action; stop requested, acknowledged and observed kept apart; what the next person needs at a handoff; resumption as a decision (OWASP APTS HO-006, HO-008, HO-009, HO-019, SC-009).
- §10.2 §6: prior compromise and possibly unlawful material as planned stop conditions: stop, leave in place, keep the tester's own record, escalate to the named contact and counsel (PTES, community mirror).
- §10.2 §3: proof without extraction as a selectable option for regulated or personal data, with its limit (PTES, community mirror).
- §10.1: the tester describes the relevant attack surface, direct and indirect, before the owner chooses breadth (CREST CDPT §9.1, §9.1.1).
- §10.3 §3 and §30.4: detection and response as a declared objective; notice may be limited to a named contact by the monitoring function owner's recorded decision (PTES, community mirror).
- §30.5 and §50.3 §4: tool severity, reported severity and program deadlines kept apart, with CVSS nomenclature for scores (FIRST CVSS v4.0 User Guide); the closing readout says who hears about a changed rating.
- §90.5 §1, §30.5 and §90.0: merge (same exposure) against group (distinct instances, shared cause or fix); the duplicate rate counts merges only; a finding covering several instances says which were proven and which are inferred (OWASP APTS RP-015).
- §90.5 §2: a "could not assess" result is `unknown` with a reason and stays out of rate numerators and denominators.
- §90.5 §8, new: comparing reviewer burden on matched cases; no result is reported.
- §90.3 §6.1 and §00.4: a control counts for a route once that route is shown to pass through it before the effect (CWE-693, CWE-638; *Declared, Not Wired*).
- §90.3 §10.1, new: retiring a testing capability: credentials, data, access, records (NIST AI 100-1 GOVERN 1.7, MANAGE 4.1; NIST AI 600-1 GV-1.7-002).
- §30.1: clear, purge and destroy as the vocabulary for recording disposal, with limits for cloud storage and copies outside the practice's control (NIST SP 800-88 Rev. 2; NIST SP 800-115 §7.4.4).
- §20.13: prompts for the facts a privacy or legal owner needs to map a disclosure finding; no legal determination (NIST AI 600-1 §2, §2.4).
- §00.3: when an outside supplier does the testing, what stays with the adopter (CREST, *A Guide to Penetration Testing*, 2022).
- §20.15: what the portfolio door starts from, with `unknown` where the adopter has no categorization or interval (NIST SP 800-115 §6.2).
- §40.9 §10: an effectiveness prompt for the measure-set review (CREST, *A Guide to Penetration Testing*, 2022, Part 5 step 4 and Part 6).
- §30.5: where the report names a testing guide, its edition and which categories were applied, partly applied or not applied (OWASP WSTG v4.2, Reporting).
- §20.13: responsible-AI evaluation is out of scope unless the engagement names it; insight access (logs, prompts, configuration, provider settings) as a scoping input; planted content recorded, then removed or handed to its owner at close-out with derived copies checked, and placed in a retraining path only under separate approval with a confirmed restore point (OWASP AI Testing Guide v1.0; MITRE ATLAS AML.M0035).
- §90.2 §4 and §90.1 §10.6: a ledger for resources the tool creates off the target, reconciled from records it cannot edit; credential revocation and resource removal checked separately (MITRE ATLAS AML.M0043).

## 1.0.0 — 2026-11-07

- Added governance, code of conduct, citation file, and this change log.

## 2026-11-04

- Clarified reader routes, draft status, and reader guidance in the README and register (#2).
- Refined README voice and scope (#1).

## 2026-11-01

- Section 90: added the glossary (§90.0) and the validation measurement annex draft (§90.5); applied validation-at-volume fixes across §90.1 to §90.4.
- §20.13: shared evidence states and OWASP 2025/2026 alignment.
- Register and README updated for 58 components.
- CI runner pinned to ubuntu-24.04.

## 2026-10-30

- Initial public release: components 00 through 90, diagrams, downloads, the synthetic API engagement walkthrough and multi-party example, issue templates, contributing guide, and the repository check.
- Review fixes applied to §10.5, §40.6, the issue templates, and the contributing guide.
- Workflow actions pinned to commit SHAs.
