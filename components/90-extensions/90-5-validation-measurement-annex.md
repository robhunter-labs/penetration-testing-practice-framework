# 90.5 — Validation Measurement Annex (Draft v0.1)

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.
>
> **Status: Draft v0.1.** Offered for comment. Definitions may change before a published release; a cited version should name this draft.

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

## 2. Measures

| Measure | Numerator | Denominator | Collect at | Note |
|---|---|---|---|---|
| **Yield** | Accepted findings | Candidates | After delivery decision | Low yield is expected for broad discovery; trend it per posture. |
| **Precision** (per triage band) | Candidates validated as real, in the band | Candidates validated, in the band | After validation | Band by triage band: the higher of the tool's severity and the human triage severity, fixed before validation. Banding by validated severity would make precision 100% by construction. Report chains separately from single findings. |
| **False discovery rate** | Candidates validated as not real | Candidates validated | After validation | Equals 1 − precision. Used instead of a false-positive rate, which needs a set of true negatives that testing rarely has. |
| **Severity inflation** | Candidates whose tool severity is higher than validated severity | Candidates validated as real | After validation | Also report the reverse (understatement). A high rate shrinks the real high-consequence queue and can mislead sampling eligibility. |
| **Duplicate rate** | Candidates merged into another | Candidates | At grouping | Grouping must keep chain steps. |
| **Validator minutes per accepted finding** | Validator time | Accepted findings | Per engagement | The core burden measure. Also report per triage band. |
| **Time to validate** (per triage band) | Elapsed time from candidate emitted to validation decision | — (report median and maximum per band) | Per candidate | Pairs with queue age; long times at the top band are the first sign capacity is short. |
| **Queue age** (per triage band) | Age of each unvalidated candidate | — | Continuously | Report the maximum and median against the declared maximum age (§90.1 §9.4). |
| **Capacity ratio** | Candidates awaiting validation | Validator hours remaining in the window | During the run | When the backlog exceeds the declared backlog threshold, backpressure applies. |
| **Chain confirmation rate** | Chains with every step at *Reproduced* or *Demonstrated impact* | Chains proposed | After validation | Report partly proven chains separately. |
| **Correction rate** | Delivered findings later corrected or withdrawn | Delivered findings | Rolling, per posture | Include time to unwind downstream tickets. |
| **Run-to-run stability** | Unique issues found in at least *k* of *n* identical runs | Unique issues found in any run | Evaluation (§90.3) | Report as "k of n", never as best of n alone. |
| **Recall / missed-coverage estimate** | Seeded or known issues found | Seeded or known issues present | Evaluation or coverage check | Needs a living answer key; otherwise `unknown`. |

A measure without its denominator, unit and collection point is not reported.

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

One engagement, one posture. The tool emits 240 candidates. Grouping merges them into 96 unique issues (duplicate rate 144/240 = 60%). The tool rated 70 of the 96 high or critical. People validate all 96, counting per unique issue: 38 are real (precision 38/96 ≈ 40%; yield 38 accepted findings from 240 candidates ≈ 16%). The tool had rated 30 of those 38 high or critical; validators kept 15 there, so at least 15 of 38 real issues (≥ 39%) were rated higher by the tool than by people. That severity inflation matters most for sampling eligibility. Validators spend 1,900 minutes in total: 50 minutes per accepted finding. The practice cannot yet sample anything: it has 96 validated unique issues spread across several strata, and no stratum has enough to bound its error usefully.

These numbers are invented to show the arithmetic. They are not a benchmark.

## 6. Reporting a measure

For each reported measure, state: the posture and its configuration digest; the stratum; the unit and denominator; the period; the answer-key status (`living`, `stale` or `unknown`); and the number of runs. A rate without these is an anecdote.

## Version notes

- **2026-11 — Draft v0.1, new.** First draft, written after independent review found that §90.1, §90.3 and §90.4 named the right measures but did not define them.
