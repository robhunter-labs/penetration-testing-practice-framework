# 90.5 — Validation Measurement Annex (Draft v0.2)

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.
>
> **Status: Draft v0.2.** Offered for comment. Definitions may change before a published release; a cited version should name this draft.

**Component:** measurement definitions for §90.1, §90.3 and §90.4  
**Reader:** practice lead, capability evaluator, assurance partner  
**Vocabulary:** [Section 90 glossary](90-0-glossary.md)

## Why this annex exists

Agentic testing tools can produce many more candidates than a manual test, often rated high or critical by the tool and often including proposed attack chains. The work then moves from finding to validating. §90.1 and §90.4 already say *that* a practice measures quality, coverage, burden and capacity. This annex says *how*: what each measure counts, over which denominator, and how much evidence a sampling decision needs.

It does not set targets or defaults. Numbers below are illustrations of the arithmetic, not recommended values.

## 1. Units of analysis

Name the unit before any rate. Most disputes about "the tool halved the work" are disputes about the denominator.

| Unit | Meaning |
|---|---|
| **Candidate** | One item a capability proposed, as emitted, before grouping. |
| **Unique issue** | Candidates grouped into one underlying weakness, after merging duplicates. |
| **Affected instance** | One location where a unique issue applies (an endpoint, host, account or object). |
| **Accepted finding** | A unique issue a qualified person validated and accepted for delivery. |
| **Chain** | A recorded attack chain, counted once, with its steps counted separately where a measure needs it. |
| **Validator time** | Qualified-person time spent on validation and review, in minutes, recorded per candidate or per batch. |

State whether a chain counts as one accepted finding or as its steps; do not switch mid-comparison.

**Merge or group.** Two decisions sit under "deduplication", and they count differently. The distinction follows [*Proof Outside the Model*, §05](https://robhunterworks.com/writing/proof-outside-the-model/).

A *merge* says two candidates are the same exposure: the same weakness at the same affected instance, so one piece of evidence proves both. Several names for one instance, such as hostnames that redirect to one site, still merge, unless the issue sits on the redirect itself. A merge needs the shared instance shown (same route, parameter, method, identity), not assumed from a matching title or response.

A *group* keeps distinct affected instances under one unique issue because they share a root cause or a fix. Each instance keeps its own evidence, or is marked inferred, and its own place in the affected-instance count; the group is one unique issue and says how many instances were proven and how many are inferred. A shared fix is not enough to merge: one change can close a flaw on several routes, and each route is still its own instance. The duplicate rate (§2) counts merges only.

The two errors are not equal. A false merge hides a real issue behind another's label, where no one reviews it; a false split costs a second review and can leave two copies with different outcomes. Three safeguards follow:

- Keep every original candidate with its link.
- Make each merge and each grouping reversible.
- Reopen a random sample of merges with the §4 method: a step tuned only to shrink the queue lowers the count whether its merges are right or wrong.

State 3 (§90.1 §8.4) is for merges; a grouped candidate keeps its own state and a link to the unique issue. OWASP APTS (v0.1.0) asks for a similar balance where findings are delivered downstream: deduplication policies documented to prevent duplicate ticket storms "while preserving distinct finding instances" ([APTS-RP-015](https://github.com/OWASP/APTS/blob/0c2b7d05371bcbb006aa5d3799c820f6944d65df/standard/8_Reporting/README.md#apts-rp-015-downstream-finding-pipeline-integrity), SHOULD).

## 2. Measures

| Measure | Numerator | Denominator | Collect at | Note |
|---|---|---|---|---|
| **Yield** | Accepted findings | Candidates | After delivery decision | Low yield is expected for broad discovery; trend it per posture. |
| **Precision** (per triage band) | Candidates validated as real, in the band | Candidates validated, in the band | After validation | Band by triage band: the higher of the tool's severity and the human triage severity, fixed before validation. Banding by validated severity would make precision 100% by construction. Report chains separately from single findings. |
| **False discovery rate** | Candidates validated as not real | Candidates validated | After validation | Equals 1 − precision. Used instead of a false-positive rate, which needs a set of true negatives that testing rarely has. |
| **Severity inflation** | Candidates whose tool severity is higher than validated severity | Candidates validated as real | After validation | Also report the reverse (understatement). A high rate shrinks the real high-consequence queue and can mislead sampling eligibility. |
| **Duplicate rate** | Candidates merged into another | Candidates | At deduplication | Counts merges only (§1). A merge must not remove a step a chain depends on (§90.1 §8.5). |
| **Validator minutes per accepted finding** | Validator time | Accepted findings | Per engagement | The core burden measure. Also report per triage band. |
| **Time to validate** (per triage band) | Elapsed time from candidate emitted to validation decision | — (report median and maximum per band) | Per candidate | Pairs with queue age; long times at the top band are the first sign capacity is short. |
| **Queue age** (per triage band) | Age of each unvalidated candidate | — | Continuously | Report the maximum and median against the declared maximum age (§90.1 §9.4). |
| **Capacity ratio** | Candidates awaiting validation | Validator hours remaining in the window | During the run | When the backlog exceeds the declared backlog threshold, backpressure applies. |
| **Chain confirmation rate** | Chains with every step at *Reproduced* or *Demonstrated impact* | Chains proposed | After validation | Report partly proven chains separately. |
| **Correction rate** | Delivered findings later corrected or withdrawn | Delivered findings | Rolling, per posture | Include time to unwind downstream tickets. |
| **Run-to-run stability** | Unique issues found in at least *k* of *n* identical runs | Unique issues found in any run | Evaluation (§90.3) | Report as "k of n", never as best of n alone. |
| **Recall / missed-coverage estimate** | Seeded or known issues found | Seeded or known issues present | Evaluation or coverage check | Needs a living answer key; otherwise `unknown`. |

A measure without its denominator, unit and collection point is not reported.

**"Could not assess"** is a statement about the check, not about the candidate. Where nothing could reach a result (no oracle fired and no person could reproduce it, a replay that was blocked or could not run, or a ruling of *not enough evidence* or *deferred to a named owner* under §90.1 §8.7), record the candidate as `unknown` with the reason.

- It stays in the candidate count, so yield is unchanged.
- It is kept out of both the numerator and the denominator of precision, false discovery rate and severity inflation, which count only what was assessed.
- Where the answer key is dead, the measure itself is `unknown`.
- Report the number of unknowns beside each of those rates: if the unassessed cases are the hard ones, leaving them out flatters the rate, and a large unknown share is itself a result about the checker.

In a calibration sample (§4), an unknown is not a pass. Where the reduced-depth decision called the candidate real or not real and full validation could not, it is a failure; where both were unknown, it does not count toward *n*.

This rule is about a check that could not reach a result. A tool that gives no answer on a seeded issue has missed it.

## 3. Estimating what was missed

- **Seeded issues:** plant known, real issues where authorized, and count how many come out the other end. This is the most direct recall measure.
- **Capture–recapture:** when two independent methods (for example a tool and a person, or two people) cover the same scope, let *n₁* and *n₂* be the unique issues each found and *m* the issues both found. An estimate of the total is *N ≈ n₁·n₂ / m* (Lincoln–Petersen); when *m* is small, use Chapman's form, *N ≈ (n₁+1)(n₂+1)/(m+1) − 1*. Both assume the methods are independent and every issue is equally findable. In testing, easy issues tend to be found by both methods, which makes the estimate run low. Treat the result as a lower-bound indication and say so.
- **Training-data contamination:** public vulnerable applications are likely known to models. Prefer held-out or newly built fixtures for any recall claim (§90.3 §7.1).

## 4. Sampling: how much evidence a reduced-validation decision needs

Sampling means directly reproducing only part of the eligible candidates. It is allowed only under §90.1 §8.2 and §90.4 lever 1, and never samples the human decision on a delivered finding.

**Stratify.** Calibrate separately for each stratum: posture × target class × vulnerability class × triage band (the higher of the tool's severity and the human triage severity). The triage band is fixed before validation, so a stratum cannot be redrawn after the results are known. A rate earned on one stratum does not transfer to another.

**Define failure and select at random.** A failure is any sampled candidate where the reduced-depth decision on whether it is real, or on its severity band, would differ from full validation. The calibrating body, and every later sample, is selected at random within the stratum; a hand-picked or convenience sample does not support a bound.

**Bound the error.** With *n* randomly sampled candidates from one stratum and no failures, the one-sided 95% upper bound on the stratum's failure rate is about 3/*n* (the rule of three). With failures in the sample, use the one-sided exact (Clopper–Pearson) bound, as in the table.

| Sample size *n* | One-sided 95% exact (Clopper–Pearson) upper bound, 0 failures | 1 failure | 2 failures |
|---|---|---|---|
| 30 | 9.5% | 14.9% | 19.5% |
| 60 | 4.9% | 7.7% | 10.1% |
| 150 | 2.0% | 3.1% | 4.1% |
| 300 | 1.0% | 1.6% | 2.1% |

Read a row as: "after 150 candidates in this stratum were fully validated and none failed, we can say with 95% confidence the failure rate is below about 2%." The adopter decides which bound is acceptable for which stratum; this table does not.

**Ongoing sampling** can follow an established acceptance-sampling scheme (for example ISO 2859-1 or ANSI/ASQ Z1.4) or a sequential test, with a rollback trigger that returns the stratum to full validation on failure. Record the scheme, the acceptable bound, the minimum *n* before any reduction, and the owner, in the §90.4 lever record.

**Eligibility uses the triage band.** A candidate's stratum uses the higher of the tool's severity and the human triage severity (§90.1 §8.2), so neither an inflated nor an understated rating moves a candidate into a sampled band. A candidate that is a step in a chain takes the chain's consequence.

## 5. A worked illustration (fictional numbers)

One engagement, one posture. The tool emits 240 candidates. Merging duplicates leaves 96 unique issues, each at one affected instance in this illustration (duplicate rate 144/240 = 60%). The tool rated 70 of the 96 high or critical. People validate all 96, counting per unique issue: 38 are real (precision 38/96 ≈ 40%; yield 38 accepted findings from 240 candidates ≈ 16%). The tool had rated 30 of those 38 high or critical; validators kept 15 there, so at least 15 of 38 real issues (≥ 39%) were rated higher by the tool than by people. That severity inflation matters most for sampling eligibility. Validators spend 1,900 minutes in total: 50 minutes per accepted finding. The practice cannot yet sample anything: it has 96 validated unique issues spread across several strata, and no stratum has enough to bound its error usefully.

These numbers are invented to show the arithmetic. They are not a benchmark.

## 6. Reporting a measure

For each reported measure, state: the posture and its configuration digest; the stratum; the unit and denominator; the period; the answer-key status (`living`, `stale` or `unknown`); and the number of runs. A rate without these is an anecdote.

## 7. Noise classes behind the rates

Many candidates were never new, never the target's doing, or never anyone's to fix. They move yield, duplicate rate and validator minutes, and each class has a trap: a way a filter can hide a real finding. Record the class on the candidate's suppressed or merged record (§90.1 §8.4, states 2 and 3), so discards can be audited by class with the §4 method and the measures in §2 read against them. The seven classes below are a working selection, ordered from well understood to open as of this draft. In the last column, a measure is moved if the noise goes unfiltered; *(trap)* marks one moved if the filter is wrong.

| Class | What a reviewer sees | What answers it | The trap | Measure it moves |
|---|---|---|---|---|
| **Soft 404s** (well understood) | Sensitive paths all return success, and each is the application's index page | Probe random paths in the same directory first, and compare response shape ([Bar-Yossef et al., *Sic Transit Gloria Telae*, §3](https://www.ee.technion.ac.il/people/zivby/papers/decay/decay.pdf)); templated or dynamic success pages can defeat this | A real file that happens to match the error page is dropped | Precision; recall *(trap)* |
| **One candidate, many addresses** (well understood) | The same issue on several hostnames that redirect to one site, or the same bug reported again in new words | Follow redirects; compare route, parameter, method and identity; merge candidates for the same instance, keep each original candidate linked, and group distinct affected instances under the unique issue (§1) ([DefectDojo, *About Deduplication*](https://docs.defectdojo.com/triage_findings/finding_deduplication/about_deduplication/)) | A bug that returns after a fix is a regression, not a duplicate | Duplicate rate; yield |
| **The edge answered** (partly addressed) | A block page on a JSON API, or a 403 read as "the admin panel exists" | Edge markers, such as the header [Cloudflare sets on challenge pages](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/challenge-pages/detect-response), plus the same probe to the origin where the origin is in scope (§10.1) and the rules of engagement allow | Shielded is not fixed: record "blocked at the edge, origin unknown" | Precision; recall *(trap)* |
| **Works one time in N** (partly addressed) | It reproduces, then doesn't, and is closed as flaky | Rule out caching; where nodes can be pinned, test each ([AWS, *Sticky sessions with load balancer generated cookies*](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-balancer-stickiness/alb-cookies-stickiness.html)); otherwise report a success rate across repeated tries. Some real flaws, such as race conditions, are intermittent by nature | "Not reproducible" can be the one node that missed the patch | Recall *(trap)*; confounds run-to-run stability (§90.3) |
| **The target moved** (open) | It no longer reproduces, or the address now belongs to someone else | Bind the candidate to what was tested (certificate, build, account or response). Re-check only after re-confirming ownership and scope; a reassigned address stops testing and is escalated under §00.3 §5 | "Fixed since" is treated as a false positive, and a reassigned cloud address is someone else's host ([Pauley et al., IEEE S&P 2022, §II-C](https://arxiv.org/abs/2204.05122)) | False discovery rate; correction rate |
| **The test's own footprints** (open) | A stored script that is last quarter's test payload, or a lockout the test caused read as a control | A shared record of everything testing changed, across runs and testers, built on the tester action log (§30.1) | True but not new, and still a cleanup miss worth reporting | Yield; duplicate rate |
| **The tool grades its own work** (open) | A confident report citing functions that don't exist | Capture evidence in the harness; let the model cite it, never write it; corroborate narrated steps against captured actions (§90.1 §7.1) and replay independently (§90.1 §8.4) | A provenance check can pass while impact is still unshown; outside the marks in §90.1 §8.6, impact remains a person's call | False discovery rate; severity inflation |

A filter may lower a candidate's rank or route it; it does not close it. A qualified person closes it, on evidence the tool could not have written where such evidence exists (§90.1 §8.6). A label such as "blocked", "unreachable" or "duplicate" describes the test, not the target. A fuller catalog of 103 classes in 16 families, most keyed to published sources and the rest marked as reasoning, is published with the [validation package catalog](https://github.com/robhunter-labs/ai-security-field-lab/tree/main/validation-package/catalog).

## 8. Comparing reviewer burden on matched cases

Validator minutes per accepted finding (§2) describes a burden. It does not show that a change reduced it. A claim that a validation package (§90.1 §8.7), a filter, or a grouping step saves reviewer time needs a comparison on matched work: candidates of the same kind, from the same stratum (§4), reviewed with the change and without it. To run the comparison:

- Fix the cases, the measure, and the stopping rule before the run (§90.3 §7.1).
- Use cases whose answer is already known (seeded, or fully validated by someone else).
- Give each reviewer both conditions on different matched sets, and alternate which condition comes first, so a faster second pass is not read as a saving.
- Time the whole route from candidate to recorded ruling, including rework and the time the new step itself takes, and report validator minutes per candidate for each condition, since the number of accepted findings can differ between them.
- Record decisions as well as minutes: a condition that is faster but misses more real issues, or produces more rulings that full validation would reverse, has moved the burden, not reduced it.
- State the number of reviewers and cases, and treat a difference seen with a few reviewers as an indication, not a rate.

The comparison measures the change, not the people, and is not a measure of individual performance (§40.9 §7.7). Report pooled figures. The comparison does not lower validation depth on live work (§90.1 §8.2).

This annex reports no result from such a comparison; the measure is defined here so that a claimed saving can be checked.

## Version notes

- **2026-11-10, Draft v0.2 additions.** §1: merge against group, and which one the duplicate rate counts. §2: a "could not assess" result is `unknown`, with a reason, and stays out of rate numerators and denominators. §5: wording of the worked illustration aligned with §1 (numbers unchanged). New §8: comparing reviewer burden on matched cases.
- **2026-11-08, Draft v0.2.** Added §7, noise classes behind the rates, with the measure each one moves.
- **2026-11 — Draft v0.1, new.** First draft, written after independent review found that §90.1, §90.3 and §90.4 named the right measures but did not define them.
