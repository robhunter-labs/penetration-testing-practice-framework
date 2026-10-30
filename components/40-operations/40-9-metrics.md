# Program Measurement Guide

**§40.9 · Program measurement guide · Penetration Testing Practice Framework**

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## Reader headlines

**Primary audience:** The practice lead who chooses and defines a penetration-testing program's measures, and the reviewer or assurance partner who must be able to recalculate and challenge them. Testers are a secondary audience: they are the people most often affected by a badly defined measure.

**Objective:** Help a practice lead choose a small set of measures, define each one precisely enough that someone else can recompute it, name its source and owner, interpret its movement honestly, and correct it when it turns out to be unfair or wrong.

**Intended outcome:** Every reported number has a written definition, a denominator, a clock that the measured party actually controls, a single source of record, a data-quality check, either a locally set target or an explicit trend-only designation, and a stated interpretation. A trend prompts a question and a learning action before it prompts a celebration. A tester who believes a measure misrepresents their work has a route to dispute it.

**This document defines:** The purpose and limits of program measures; the line between test-practice process measures and vulnerability-management outcome measures; seven optional measure families; the decisions an adopter must make before reporting any measure that runs on a response window; a blank metric-definition register; one fully worked synthetic measure (delivery against a frozen plan) with a small event fixture that a reader can recompute; a catalogue of perverse incentives and their design counters; data-quality, finalization, and recalculation rules; worked decision examples; and three reader walkthroughs.

**This document does not define:** Which measures an adopter must run, any numeric target, a ready-made formula for any windowed service measure (retests, request responses, review queues, urgent triage), a dashboard design, a reporting tool, or who in an adopting organization is accountable for remediation.

## Document administration

| Field | Detail |
|---|---|
| **Document** | 40.9 |
| **Status** | Published framework component; local adoption is a separate decision. |
| **Type** | Practice operating guide with template |
| **Maintainer** | Framework maintainers until a local program assigns an owner |
| **Local approval authority** | Defined by the adopting organization |
| **Review trigger** | Material change to services offered, systems of record, clock definitions, partner responsibilities, staffing model, or any measure being used for a new kind of decision |

> [!CAUTION]
> This guide does not claim that any measure in it is deployed anywhere, endorsed by any organization, or proven to improve outcomes. It supplies no target values. Examples are synthetic, and any numbers in them are illustrative only. An adopter supplies its own services, systems, clocks, owners, and targets before using any measure to report on or judge a practice.

## Where this fits

Measurement sits on top of the rest of a practice: authorization and scoping decide what work is legitimate; the testing methods decide what an engagement contains; the consulting-service guide in this framework describes the post-test desk and its own service clocks; and the framework's lessons-learned and improvement process receives the questions that measures raise. This guide does not restate the consulting desk's clock rules; where a measure depends on them, it points to that guide by role.

The issue-record system and the organization's vulnerability-management process remain authoritative for finding state, remediation, and closure. A testing practice's measures can *read from* those systems; they do not replace them, and a dashboard that aggregates them is never a second source of record.

## 1. What a program measure is for

A program measure exists to support a named decision: whether to change staffing, scheduling, method, intake rules, partner agreements, or the service promise itself. A number that supports no decision is reporting cost without value. Before adding a measure, write the sentence: *"If this moves, we will ask ___ and may decide ___."* If the sentence cannot be completed, do not add the measure.

Six rules apply to every measure in this guide:

1. **No definition, no number.** A measure is reported only once its register entry (§5) is complete and versioned.
2. **No count without its denominator.** "40 engagements" says nothing until it is read against planned, eligible, or available capacity. Where a count is genuinely useful on its own (for example, urgent requests received), label it a *demand signal*, not a performance measure.
3. **Missing is not zero, and not-yet-due is not late.** Incomplete or unreconciled data is reported as *insufficient data* for that period, with the reason. A false zero misleads more than a visible gap. An empty denominator is *not applicable*, never 0% or 100%. An item that could not yet have missed its window at the reporting cutoff is not a failure (§4.1).
4. **Actual, target, and trend travel together.** A bare number without its target (or its trend-only designation) and its recent history invites the reader to supply their own.
5. **A dashboard aggregates; it does not decide.** Every displayed value must trace back to a named source-of-record extract that a reviewer can obtain.
6. **A trend is a question.** Improvement in one measure is a prompt to check its paired measure (§7) before it is presented as success.

## 2. Process measures and outcome measures

Two different kinds of measure are often reported side by side, and confusing them is the most common way a testing practice ends up judged on work it does not control.

| | Test-practice process measures | Vulnerability-management outcome measures |
|---|---|---|
| **Answers** | Is the testing service planned, delivered, responsive, and sustainable? | Is identified risk being reduced, accepted, or deferred appropriately? |
| **Typical examples** | Engagements delivered against plan; retests started within a local window after readiness; coverage by surface; time to actionable guidance; capacity in use | Remediation within the organization's remediation timelines; overdue findings; exceptions and deferrals; recurrence after closure |
| **Who usually controls the clock** | The testing practice, once its start condition is met | Remediation owners, risk owners, and the vulnerability-management function |
| **Testing practice's relationship** | Produces and owns | Feeds (findings, evidence, retest results) and may *report alongside* as context |

This guide does not tell an adopter who is accountable for which outcome; organizations divide that responsibility in different ways, and some deliberately share it. It does require one design check for every measure:

> **Control test.** Does the party being measured control both the clock start and the clock stop? If not, the measure is reported as *context* for that party, not as *performance* of that party, until the adopter has explicitly agreed otherwise and recorded why.

Under this test, a tester or testing team is not scored against a remediation timeline it cannot move, and a remediation owner is not scored on how quickly a test was scheduled. Outcome measures can and often should appear in the same review — a practice that tests well and sees nothing fixed has a real problem — but they appear with their actual owner named.

## 3. Choosing measures

Start small. Three to five well-defined measures that are read and acted on are worth more than a dozen that are merely displayed. For each candidate:

1. **Name the decision and the audience.** Who reads this, and what could they decide differently?
2. **Pick the family** (§4) and draft the definition in the register (§5).
3. **Run the control test** (§2).
4. **Name the behavior risk.** How could someone make this number look better without the service getting better? Choose a paired measure that would reveal it (§7).
5. **Cost the collection.** If the number requires manual re-keying from several systems, decide whether the decision is worth that effort, or whether the system of record can be improved first.
6. **Baseline before target.** Collect at least a few periods under the final definition before setting a target. A target set before the baseline exists is a guess wearing authority. A measure may also stay *trend only* with no target at all.
7. **Set a retirement trigger.** State when the measure will be reviewed for removal — for example, when the decision it supported no longer arises, or when it has been stable and unread for a full review cycle.

A practice starting from nothing may find delivery against a frozen plan (§6) the easiest first measure: every input is a recorded state at a fixed moment, and no response window has to be defined. Windowed measures are often more valuable and always harder; begin them only after §4.1 is complete.

## 4. Optional measure families

These families are a menu, not a mandate. An adopter may run none of a family, one measure from it, or a locally invented measure the table does not list. Each entry gives the question the family answers, the definition shape it usually takes, and its characteristic trap. Families marked **windowed** run on a response clock; this guide gives their shape only, not a formula, and none may be reported until the adopter has completed §4.1 for it.

| Family | Question it answers | Usual definition shape | Characteristic trap |
|---|---|---|---|
| **Delivery against plan** | Is planned testing being delivered? | Engagements in a plan frozen at the start of the period that reach recorded closeout within the period ÷ engagements in that frozen plan; each engagement counted once, regardless of how many techniques, surfaces, or testers it involved. Fully worked in §6 | Rewards under-planning, splitting, narrowing, or shallow engagements; says nothing about depth or value (§7.1) |
| **Retest service** (windowed) | When a fix is ready, does the practice retest within the locally agreed window? | Shape only: retests whose first test activity falls within a local window after a recorded readiness event ÷ an eligible population the adopter defines. The clock starts on a recorded, verifiable readiness state, not when a request is first mentioned. **No ready-made formula is offered: complete §4.1 first** | Clock started before readiness; readiness used as a place to hide delay (§7.5); items scored before they could be late; withdrawals or pauses used to move the score (§7.9) |
| **Service responsiveness** (windowed) | Do requesters get timely, usable guidance after a test, and are queued reviews (such as evidence or closure reviews the practice performs) worked within their local window? | Shape only: for each service clock defined in the consulting-service guide, requests answered within that clock ÷ eligible requests; for a review queue, items reviewed within window ÷ items that entered the queue. **Complete §4.1 first** | A fast acknowledgment counted as an answer; volume targets that reward rushed replies |
| **Coverage by surface** | Is testing reaching the kinds of systems the organization actually runs? | Engagements completed ÷ planned, broken down by surface category the adopter defines (for example web, API, mobile, network, cloud, AI-enabled systems), and optionally by a locally defined depth or assurance tier. Can reuse the frozen-plan rule of §6 | Counting "touched" as "covered"; a plan that silently drops hard surfaces makes coverage look complete |
| **Finding and retest profile** | What is testing finding, and what happens on retest? | Findings by severity per engagement (reported as a distribution, not a target); retest results by outcome (resolved, partially resolved, not resolved, could not test) ÷ retests performed | Pass-rate gaming in either direction (§7.2); treating fewer findings as better testing |
| **Capacity** | Is the practice sustainably staffed for its commitments? | Hours on planned engagements, unplanned or interrupt work, service duty, and development ÷ available hours; plus a count of skills or authorizations held by only one person | Utilization targets that punish learning and review time; hiding interrupt work inside engagement hours |
| **Urgent-response demand** (windowed for its rate; not for its count) | How much unplanned, time-critical work is arriving, and is it handled within the local triage window? | Urgent requests received per period, as a demand signal (no window needed). Shape only for the rate: urgent requests triaged within the local window ÷ eligible urgent requests. **Complete §4.1 before reporting the rate** | Count without denominator; urgent work crowding out planned work invisibly |

AI-enabled systems appear above as one possible *surface* to test. Whether AI is used *as a testing aid* is a separate, optional matter addressed in §11.

### 4.1 Before reporting any windowed measure

A windowed measure scores each item by whether something happened within a response window after a start event. It looks simple and is not: the same extract can give different numbers depending on decisions that are easy to leave implicit. This guide therefore supplies no universal retest formula. An adopter who wants a windowed measure writes down, in its register entry, an answer to each of the following — and does not report the measure until every answer is written and the test states below have been worked through on paper.

1. **Start event.** What recorded event starts the clock, what conditions must be true, and who records it. Prefer a system-generated timestamp over a user-entered date.
2. **Window, calendar, and boundary.** The window length; calendar or business time and which calendar; the time zone; and whether the deadline instant is inclusive. Write how a start at 16:00 on the last working day before a weekend is counted.
3. **Stop event.** What counts as the response (for a retest, *first recorded test activity against the finding*, not a ticket touch). Whether a stop recorded after the item was cancelled can count.
4. **Pauses.** Who may authorize a pause — not solely the party being measured; whether a pause may begin after the deadline has already passed (if it may, a missed deadline can be undone); how overlapping pauses combine (union of paused time, or sum); what evidence ends a pause, and who records it; and whether a pause record must be created at the time, as shown by the system's own record-creation time.
5. **Cancellations and withdrawals.** Which reasons qualify (the target or fix genuinely went away) and which never do (the requester gave up waiting); whether "took effect" means the effective time or the recorded time — a backdated cancellation can otherwise turn a recorded failure into an exclusion; who reviews each one independently of the measured party; and what happens if a review stays open past a stated age.
6. **Maturity.** When an item can be scored; how an item that cannot yet be scored is shown (with its count, age, and reason); and whether one unresolved item blocks the whole period's rate or is reported beside it.
7. **Finalization.** When a period's value is final. If items can stay open indefinitely, say so, and say how the open count is shown. Any rule that closes a period by forcing open items into a disposition, or by "carrying them forward," must be written as an explicit, versioned rule that discloses the count it affected — it is never a default.
8. **Corrections and snapshots.** Keep an extract at every reporting cutoff, not only at finalization, so that an earlier report can be recomputed using only what was known then. Say what happens when a start event is corrected: does the item move period, or stay?

**Test states.** Before first use, write down what your definition produces for each of these, and have someone who did not write it check the answers: an item ready on the last moment of a period; a response before the window has elapsed; a response exactly at the deadline; a late response; a long, legitimate pause still open at the next cutoff; a pause recorded after the deadline had passed; two overlapping pauses; a cancellation filed before the deadline whose review is still open; a cancellation recorded after the deadline but dated before it; a withdrawal after the requester waited; a period whose denominator is zero; and a correction found after a period was final. If any of these gives two defensible answers, the definition is not ready.

A windowed measure whose answers differ from another measure's — for example, a retest window and a review-queue window with different pause rules — is defined separately. Do not transplant one clock's rules onto another unexamined.

## 5. Metric-definition register

Keep one register entry per measure. Version the entry: any change to eligibility, clocks, population or cutoff rules, source, or target creates a new version, and reports state which version they used. History calculated under an older version is not silently recalculated under the new one; where restatement is needed, report both and say why.

### 5.1 Field guide

| Field | What to write | Common error |
|---|---|---|
| **ID and version** | A local identifier and version for this measure | Changing the definition without changing the version |
| **Name** | Plain-language name a non-specialist will read correctly | A name that implies more than the formula measures |
| **Family** | One of §4, or "local" | — |
| **Decision supported** | The completed sentence from §1 | "Visibility" with no decision |
| **Audience** | Who reads it and how often | — |
| **Unit** | What one counted thing is, and the rule that stops one piece of work being counted as several | Leaving "engagement" or "request" undefined |
| **Numerator** | Exactly what is counted on top, including the condition for counting | Vague verbs ("handled", "done") |
| **Denominator** | Exactly what the numerator is divided by | Missing; or a denominator that excludes the hard cases |
| **Population, period, and cutoffs** | When the population is fixed (for example a plan freeze), the period boundaries and whether each is inclusive, and the reporting cutoff at which the extract is taken | Moving the population or the cutoff after seeing results |
| **Changes after the population is fixed** | What happens to additions, removals, and deferrals after the population is fixed, and where they are logged | Removals that quietly shrink the denominator |
| **Eligibility and exclusions** | Which records are in scope; which are excluded, on what recorded disposition, and where that is logged | Undocumented manual exclusions; exclusions that remove service failures |
| **Clock start and stop** | The recorded events that start and stop any clock, and the conditions that must be true | Starting on a message rather than on a verified state; stopping on a status that can be set without the work being done |
| **Windowed-clock rules** | For windowed measures only: the written answers to every item in §4.1, and the worked test states. "Not applicable" for a non-windowed measure | Leaving any §4.1 item implicit |
| **Time basis** | Calendar or business time; which calendar; time zone | Mixing bases between periods |
| **Zero denominator** | How a period with an empty denominator is shown | Showing 0% or 100% |
| **Control test result** | Who controls start and stop; whether this is a *performance* or *context* measure for each party | Skipping it |
| **Source of record** | The system and the specific record type each input comes from | Naming a dashboard or spreadsheet |
| **Owner** | The role that maintains the definition, reconciles data, and answers challenges | An individual's name with no role; or no one |
| **Refresh** | How often it is recalculated, and the data cut-off for each period | Recalculating mid-period without noting it |
| **Data-quality checks** | Checks run before reporting (see §8), the population each check applies to, and what result makes the period *insufficient data* | None; checks that never fail; checks applied to records they should not cover |
| **Local target** | The target, who set it, the baseline it was set against, and when it is next reviewed — or "no target; trend only" | A target copied from another organization or set before a baseline exists |
| **Paired measure** | The measure that would reveal gaming or side effects of this one (§7) | None |
| **Interpretation** | What a rise, a fall, and a flat line would each prompt you to ask | "Higher is better" |
| **Known limitations** | What this measure cannot tell you | Left blank |
| **Dispute route** | Where a person affected by this measure raises a challenge (§12.3) | None |
| **Retirement trigger** | When this measure is reviewed for removal | None |
| **Change history** | Version, change, reason, and whether past periods were restated | — |

### 5.2 Blank register entry

Copy this block for each measure.

```text
ID / version:
Name:
Family:
Decision supported:      If this moves, we will ask ___ and may decide ___.
Audience / cadence read:
Unit (and counting-once rule):
Numerator:
Denominator:
Population fixed at:
Period boundaries (inclusive/exclusive) and time zone:
Reporting cutoff:
Changes after population is fixed (and where logged):
Eligibility:
Exclusions (disposition required, and where logged):
Clock start (event + required conditions):
Clock stop (event):
Windowed-clock rules:    Answers to §4.1 items 1-8 and the worked test states,
                         or "not applicable"
Time basis:
Zero denominator shown as:
Control test:            Start controlled by ___ ; stop controlled by ___ ;
                         performance measure for ___ ; context for ___
Source of record (per input):
Owner (role):
Refresh / data cut-off:
Data-quality checks (population each covers; insufficient-data rule):
Local target (value, set by, baseline, next review)  — or "trend only":
Paired measure:
Interpretation:          Rise suggests asking ___ ; fall ___ ; flat ___
Known limitations:
Dispute route:
Retirement trigger:
Change history:
```

## 6. Synthetic worked measure: delivery against a frozen plan

The following is invented for illustration. The practice, systems, dates, and data-quality threshold are fictional and are not recommendations; no target is given. It was chosen because every input is a recorded state at a fixed moment, so a reviewer can recompute it exactly from the fixture below.

### 6.1 Register entry

```text
ID / version:            DP-01 v1
Name:                    Planned engagements delivered in the period
Family:                  Delivery against plan
Decision supported:      If this falls, we will ask whether the misses were
                         in progress, deferred by the practice, or removed by
                         requesters, and may decide to change how much is
                         planned, how work is sequenced, or how requesters
                         commit to test dates.
Audience / cadence read: Practice lead and testing team monthly; leadership
                         quarterly with the paired reads.
Unit (counting-once):    One engagement = one authorized engagement record with
                         one scope statement. It is counted once, whatever its
                         number of techniques, surfaces, or testers. If the
                         frozen scope is split into child records later, the
                         frozen parent ID remains one unit. Delivery requires
                         final deliverables for the entire frozen authorized
                         scope; a child closeout alone does not close the unit.
Numerator:               Engagements in the frozen plan whose FIRST closeout
                         timestamp is at or after the period start and strictly
                         before the period end.
Denominator:             Every engagement in the frozen plan. Nothing is removed
                         after the freeze, for any reason.
Population fixed at:     Plan freeze = the period start. The frozen plan is the
                         list of engagement IDs scheduled to close in the
                         period, captured as an extract at that instant.
Period boundaries:       Half-open: [period start, period end). A closeout at
                         exactly the period end belongs to the next period.
                         All times UTC.
Reporting cutoff:        A named extract time after the period end. Because the
                         closeout timestamp is system-generated, records created
                         after the period end cannot change the numerator except
                         through a visible correction.
Changes after freeze:    Additions, removals, and deferrals after the freeze are
                         logged (engagement ID, change type, reason category,
                         who, system timestamp). They never change this
                         period's numerator or denominator. A removed or
                         deferred plan entry is a miss for this period; its
                         reason is shown in the miss breakdown. An engagement
                         added after the freeze that closes in the period is
                         reported as "unplanned delivered," outside the rate.
                         A deferred engagement may appear in a later period's
                         frozen plan; that period scores it independently.
Eligibility:             Engagements open (not closed) at the freeze instant.
Exclusions:              None.
Clock start:             Not applicable (not a windowed measure).
Clock stop:              Closeout = the system's state transition to closed,
                         which requires a final-deliverable record. Only the
                         first closeout counts: reopening a delivered
                         engagement later for an amendment does not undo the
                         delivery. If a closeout is found to be wrong (the
                         deliverable was not delivered), that is a record
                         correction (§8), not a reopen.
Windowed-clock rules:    Not applicable.
Time basis:              Calendar time, UTC.
Zero denominator:        Empty frozen plan -> "not applicable" (N/A), with the
                         unplanned-delivered count shown. Never 0% or 100%.
Control test:            The practice controls the plan it commits to (with
                         requesters' agreement) and the closeout. Requester
                         withdrawals and target unavailability are outside the
                         practice's control. The rate is therefore a
                         performance measure for the practice's planning-and-
                         delivery commitment only when read beside the miss
                         breakdown; it is never a measure of individual testers
                         (§7.7), and misses outside the practice's control are
                         shown, not removed.
Source of record:        Engagement record system (plan list at freeze,
                         closeout transitions, final-deliverable records);
                         plan-change log in the same system.
Owner (role):            Engagement scheduling lead.
Refresh / data cut-off:  Monthly; extract at the reporting cutoff.
Data-quality checks:     Applied to the frozen-plan population only.
                         (1) the frozen-plan extract exists, is dated at the
                         freeze instant, and lists engagement IDs;
                         (2) no frozen-plan entry was already closed at the
                         freeze instant;
                         (3) every frozen-plan entry counted as delivered has a
                         final-deliverable record dated at or before its first
                         closeout;
                         (4) closeout timestamps come from the system's state-
                         transition history, not an editable date field;
                         (5) every frozen-plan entry not delivered has a miss
                         reason category;
                         (6) delivered + missed = frozen-plan count.
                         Illustrative threshold: any failed record in the
                         frozen-plan population makes the period insufficient
                         data, with the reason. Checks are evaluated before the
                         zero-denominator rule: a failed check on an empty or
                         near-empty plan is insufficient data, not N/A.
Local target:            None. Trend only until a baseline exists.
Paired measure:          (a) Miss breakdown by reason category: in progress at
                         period end; deferred by practice; withdrawn by
                         requester; target unavailable; other.
                         (b) Frozen-plan size against the previous periods and
                         recorded scheduling demand: distinct scope requests
                         entering engagement intake during the period,
                         including requests deferred or declined. This is a
                         separate demand signal, not the rate denominator.
                         (c) Unplanned delivered count.
                         (d) A periodic sample of delivered engagements
                         reviewed for scope depth against their authorized
                         scope.
Interpretation:          Rise: check (b) — did the plan shrink? — and (d)
                         before crediting it. Fall: read (a) first; a fall
                         driven by requester withdrawals is a partner
                         conversation, not a delivery finding. Flat: check
                         whether the plan still reflects demand.
Known limitations:       Says nothing about depth, quality, or value. Early
                         delivery of a later period's engagement shows only as
                         unplanned delivered. Small monthly counts make
                         percentages volatile; read counts beside the rate.
Dispute route:           Comment on the monthly report or raise with the owner,
                         citing engagement IDs; the owner reviews against this
                         definition within the next cycle.
Retirement trigger:      Review if unread for a full annual cycle, or if the
                         plan is no longer set in advance.
Change history:          v1: first version.
```

### 6.2 Event fixture

One synthetic month. Period start `2001-03-01T00:00Z`, period end `2001-04-01T00:00Z` (exclusive). Plan freeze at the period start. Reporting cutoff `2001-04-03T12:00Z`.

| ID | In frozen plan? | Recorded events (UTC) | Result |
|---|---|---|---|
| E0 | No | Closed `2001-02-27T15:00` | Outside the frozen-plan population; its prior closeout does not enter the rate |
| E1 | Yes | First closeout `2001-03-12T10:00`; reopened `2001-04-10` for an amendment and re-closed `2001-04-11` | Delivered: first closeout counts |
| E2 | Yes | First closeout `2001-03-31T23:59` | Delivered: inside the half-open period |
| E3 | Yes | First closeout `2001-04-01T00:00` | Missed — in progress at period end (exactly at the boundary belongs to the next period) |
| E4 | Yes | Plan-change log: withdrawn by requester `2001-03-09T09:00` | Missed — withdrawn by requester; stays in the denominator |
| E5 | Yes | Plan-change log: deferred by practice to next period `2001-03-20T14:00` | Missed — deferred by practice |
| E6 | No | Plan-change log: added `2001-03-05T11:00`; first closeout `2001-03-25T16:00` | Unplanned delivered; outside the rate |

For this synthetic extract, the five frozen IDs were captured at the freeze. Every listed closeout is a system-generated state transition. Final-deliverable records exist for E1 at `2001-03-12T09:00Z` and E2 at `2001-03-31T22:00Z`; E3–E5 each has the miss reason shown above. The plan-change log retains the E4, E5, and E6 events. Those companion records are part of the example, not a claim about a real system.

**Report at the cutoff:** delivered 2 (E1, E2) of 5 planned (E1–E5) = **40%**, trend only. Miss breakdown: 1 in progress at period end, 1 deferred by practice, 1 withdrawn by requester. Unplanned delivered: 1. Plan changes logged: 3. All six checks pass on the stated synthetic records. Status: **final** at the cutoff — every frozen-plan entry is either delivered or missed by the period end, so nothing is left open.

**Three variants a reviewer should also recompute:**

- **Zero denominator.** A second synthetic month has an empty frozen plan and one unplanned engagement delivered. Report: **N/A**, unplanned delivered 1. Not 0%, not 100%.
- **Failed check.** In the original month, suppose E2's final-deliverable record is missing. Check 3 fails for a frozen-plan record, so the month is **insufficient data** with that reason — not 1/5 and not 2/5.
- **Correction after finalization.** After the month is final, an audit finds E2's final-deliverable record was attached to the wrong engagement and E2's actual delivery happened on `2001-04-02`. A correction note shows: final value 2/5 = 40%; corrected value 1/5 = 20%; record affected E2; cause; whether any decision relied on 40%. Both values stay visible (§8).

A reader who recomputes any of these and gets a different result from the rules in §6.1 has found a defect in this guide; please report it (§14).

## 7. Perverse incentives and design counters

Every measure changes behavior. The questions are which behavior, and whether anyone would notice. Each trap below names how it shows up and a design counter. None of the counters is free; choose the ones that fit the risks you actually see.

### 7.1 Delivery counts alone

**How it shows:** Delivery against plan rises because the plan got smaller; engagements become narrower, shorter, or less deep; hard targets slide to later periods; one piece of work is split into several engagements.

**Counter:** Freeze the plan before the period and never remove entries from it (§6). Count each engagement once, under a written rule for what one engagement is. Read the rate beside plan size against demand, and periodically review a sample of engagements for scope depth against plan. Never present delivery without the planned denominator.

### 7.2 Pass-rate gaming

Retest results can be gamed in both directions. A practice judged on *high* pass rates may delay retests until success is certain, narrow what a retest checks, or accept weaker evidence. A practice judged on *low* pass rates (as proof of rigor) may test beyond the original finding or refuse reasonable evidence.

**Counter:** Report retest outcomes as a distribution with no target, never as a single pass-rate goal for the testing practice. Pair with the readiness rejection rate and a periodic peer sample of retest records. Treat a large shift in either direction as a question about fix quality, readiness, or method — not as a verdict on testers or on remediation owners.

### 7.3 Counts without denominators

**How it shows:** "We found 300 findings" or "we handled 80 urgent requests" presented as achievement, with no reference to engagements, surface area, demand, or capacity.

**Counter:** Every count either gets a denominator or is explicitly labeled a demand signal. Finding counts are read per engagement and by severity, and are never targeted: more findings can mean better testing, worse systems, or broader scope.

### 7.4 Missing data reported as zero

**How it shows:** A system outage, an unfilled field, or an unreconciled extract produces a zero or a perfect score; a surface with no planned tests shows "0 of 0" as 100% covered.

**Counter:** The register's data-quality checks (§8) decide whether a period is reportable. When they fail, the period is shown as *insufficient data* with its reason. Zero-denominator cells are shown as *not applicable*, not as success. Run the checks before the zero-denominator rule, so bad data cannot hide behind "not applicable."

### 7.5 Clocks started before readiness — and readiness used to hide delay

**How it shows:** A retest clock starts on the first email, before the fix is deployed or access works, so the practice is charged with time it could not use. In the opposite failure, the readiness gate becomes a place to park requests: the practice meets its window by rejecting or delaying readiness.

**Counter:** Start the clock only on a recorded, verifiable readiness state (§4.1 item 1). Take the readiness conditions from the practice's existing retest route and consulting-service guide rather than writing a second, competing definition for the measure. Then measure the time *before* readiness, and the rejection rate, as paired measures — so the gate stays honest in both directions. Readiness criteria are published to requesters before they apply.

### 7.6 Testers measured against a remediation-owner timeline

**How it shows:** A testing team's report card includes the organization's remediation timeline compliance, or an individual tester is questioned because "their" findings are overdue.

**Counter:** Apply the control test (§2). Outcome measures appear with their actual owner named. If an adopter deliberately chooses shared accountability, record that decision and its reasoning in the register so it is a visible choice rather than a drift.

### 7.7 Program measures used to rank individuals

**How it shows:** Delivery or response figures, designed to describe a service, appear in individual performance conversations without adjustment for assignment difficulty, interrupt load, or review duty.

**Counter:** This guide's measures describe the practice. Whether and how any measure informs individual performance is a separate people-practice decision for the adopter, which needs its own fairness review, its own definitions, and the affected person's ability to see and dispute the data. Do not let a program measure become an individual one by default.

### 7.8 Utilization as a target

**How it shows:** High utilization is rewarded, so method development, peer review, training, and slack for urgent work disappear — and quality and resilience fall later.

**Counter:** Report capacity as a breakdown of where time went, not a single utilization figure to maximize. Name a sustainable ceiling locally, and treat single points of skill or authorization as a capacity risk in their own right.

### 7.9 Exclusions, pauses, and open items that move the score

**How it shows:** An item that was due but not done is "withdrawn," "paused," or "cancelled" and drops out of the denominator, so a failure improves the rate. A pause recorded after a deadline already passed turns a miss back into an open item. A cancellation filed and left unreviewed keeps a period from ever being reported. Or the reverse: items that became due on the last day of a period are scored late before they could have been late.

**Counter:** Prefer designs with no exclusions at all, as in §6, and show reasons beside the rate instead of removing items. Where a windowed measure genuinely needs pauses or cancellations, write every rule in §4.1 items 4–7 before reporting, have someone other than the measured party review each exclusion, and report exclusions, pauses, and open items as counts beside the rate, so a rise in any of them is itself visible.

## 8. Data quality, finalization, and recalculation

A measure is only as defensible as the ability of someone else to recompute it. For each reporting period, the owner keeps:

- **The extracts.** A dated snapshot or reproducible query of the source-of-record data used, taken at every reporting cutoff (and, for a frozen-plan measure, at the freeze), retained for the period the adopter's records rules require. An earlier report must be recomputable from what was known at its own cutoff.
- **The register version** in force for that period.
- **The population list**: the frozen plan, or for a windowed measure, the list of items scored and the items still open at each cutoff, with how and when each open item was later resolved.
- **The change and exclusions logs**, with each changed or excluded record, its reason, and (where the register requires one) its reviewer.
- **The check results** for every data-quality check in the register, including any that failed, and the population each check covered.
- **The reconciliation note** for any measure that spans more than one source: which records did not match, and how each was resolved.

Minimum checks for most measures: every record in the population a check covers has the fields the formula needs; no clock stop precedes its start; changes, pauses, and exclusions carry reasons; the record count agrees with the source system's own count; timestamps used for scoring come from the system's own history rather than editable fields; and the period boundaries and cutoff were applied consistently. Scope each check to the records it should cover — a field that is legitimately empty at an earlier stage of a workflow is not a data error. The register states the failure threshold above which the period is reported as *insufficient data*; the adopter chooses that threshold and writes it down before the first report.

**Order of evaluation.** Data-quality checks first: failure means *insufficient data*. Then the zero-denominator rule: an empty denominator means *not applicable*. Only then the rate.

**Finalization.** A period's value is final when its reporting cutoff has passed, its checks have passed, and nothing in its population can still change state under the register's rules. For a frozen-plan measure that is the reporting cutoff itself (§6). For a windowed measure, the register's answer to §4.1 item 7 decides; this guide supplies no default, and "carried forward" is not a finalization rule. A report issued before its value is final is labeled *provisional* and shows the count of items still open. The final value, extracts, and lists are frozen.

**Corrections.** If an error is found after finalization, issue a correction note that states the final value, the corrected value, the records affected, the cause, and whether any decision relied on the original. Keep both values visible; the corrected value is the one used from then on, and the note says so. Do not silently backfill or overwrite the final figure.

## 9. Reading trends: decision examples

In each case below, the first move is a question and a bounded learning action — not a claim. The examples are synthetic.

**Example A — delivery up, findings per engagement down.** Planned engagements delivered rose noticeably over two quarters, while findings per engagement fell and repeat retests on the same systems rose. *Question:* did the plan shrink, did scope narrow, did testing get shallower, or did the systems genuinely improve? *Learning action:* compare plan size with demand; peer-review a sample of recent engagement plans against their delivered scope and the previous year's equivalents; report what was found before reporting the rise.

**Example B — a locally defined retest window met almost always, while rejections triple.** In a practice that has completed §4.1 for its retest measure, the within-window rate climbed toward its target while readiness rejections rose sharply. *Question:* is the readiness gate catching genuinely unready fixes, or deflecting work? *Learning action:* review a sample of rejected requests with the remediation-partner lead; measure time from first request to readiness; clarify the published readiness criteria if requesters were surprised by them.

**Example C — one surface below plan for consecutive periods.** Coverage of one surface category stayed below plan while others met plan. *Question:* is the cause demand (fewer such systems ready to test), skill (only one person able to test it), or scheduling? *Learning action:* check the capacity family's single-point-of-skill count for that surface; if skill is the constraint, the answer is a development or staffing decision, not simply scheduling more of it.

**Example D — urgent demand rising, planned delivery falling.** Urgent requests per period rose while planned delivery fell, and capacity showed interrupt hours growing. The miss breakdown shows "in progress at period end" growing. *Question:* is urgent work being counted anywhere as delivered work, and is the planned commitment still realistic? *Learning action:* make interrupt time visible as its own capacity category; bring the trade-off to whoever sets the planned commitment, with the data, rather than absorbing it silently.

**Example E — retest resolution rate falling.** The share of retests resolved on first attempt fell for two periods. *Question:* did fix quality change, did readiness checks weaken, or did the testing method for retests change? *Learning action:* a joint sample review with the remediation partner; this is context for both parties, not a performance finding against either until the cause is understood.

Each example ends by sending the question and its result into the practice's lessons-learned and improvement process, so the learning outlives the meeting.

## 10. Reporting and review cadence

The adopter chooses its cadence. A pattern that works for many practices: operational measures read by the team at a short cadence to catch problems early; the full set with targets, trends, and open questions reviewed by practice leadership at a longer cadence; and the measure set *itself* — which measures still support a decision, which should be retired, which definitions caused disputes — reviewed at least annually, or whenever services, systems, or partner responsibilities change. Do not report against a target that has not been confirmed for the current cycle; report the trend and say the target is under review. Do not trend a provisional value against final ones.

## 11. Optional AI support

An adopter may use automation or AI to help gather records, reconcile sources, draft a narrative from already-computed numbers, or flag records that fail data-quality checks. Each of these remains subject to the same register: the source, the computation, and the human who accepted the result must be inspectable. A model's summary of a trend is not an interpretation of record.

This guide makes no claim that AI assistance improves testing productivity, and it does not offer an "AI productivity" measure. If an adopter wants to evaluate AI-assisted testing, treat it as a bounded experiment with its own written definition, a baseline under the same definition, a comparison that controls for engagement type and scope, explicit quality checks, and a published limitation — and keep the result separate from the program's ordinary measures until it has survived review.

## 12. Walkthroughs

### 12.1 A practice lead sets a measure

A practice lead wants to know whether planned testing is being delivered. They complete the §1 sentence: *"If this falls, we will ask whether the misses were in progress, deferred, or withdrawn, and may decide to change how much we plan."* They choose the delivery-against-plan family and start from §6. They write the unit rule first, because "engagement" means different things to different people. They fix the plan at the period start and decide that nothing leaves the frozen plan; reasons are shown instead. They run the control test and record that requester withdrawals are outside the practice's control, which is why the miss breakdown always travels with the rate. They name the behavior risk — a shrinking plan — and pair it with plan size against demand and a scope-depth sample. They mark the measure *trend only*, collect a baseline, then either set a local target with its baseline recorded or keep it trend-only. They add a dispute route and a retirement trigger. Later, when they want a retest-window measure as well, they begin with §4.1 and do not report it until every item there is answered and the test states are worked. **Pass condition:** a colleague who did not write the entry can compute the measure from it alone.

### 12.2 An auditor recalculates a final value

An auditor selects one final value of a frozen-plan measure and asks for the register version, the freeze extract, the cutoff extract, the plan-change log, and the check results for that period. They confirm the freeze extract is dated at the period start and contains no engagement already closed. They take each frozen-plan entry, read its first closeout timestamp from the system's state-transition history, and apply the half-open period. They confirm that nothing was removed from the denominator, that every miss has a reason category, and that delivered plus missed equals the frozen-plan count. They then sample a few records from the source system itself — not from the extract — to confirm the extract represents the source, and check whether a correction note exists. **Pass condition:** the recomputed value matches the final value, or every difference is explained by a logged reconciliation or a visible correction note. **Fail conditions:** the value exists only in a dashboard; the plan was fixed after the period began or changed after the freeze; an entry left the denominator; closeout times came from an editable field; the definition or cutoff changed mid-period without a version; the final value was overwritten rather than corrected; or failed data-quality checks were reported as a number instead of *insufficient data*.

For a windowed measure, the auditor follows the same steps against the adopter's own §4.1 answers, and additionally recomputes at least one earlier provisional report from that report's own cutoff extract.

### 12.3 A tester disputes an unfair measure

A tester sees the practice's delivery figure discussed in a team meeting alongside a list of "missed" engagements, two of which were assigned to them. They check the records and find two problems: one engagement was withdrawn by its requester in the first week and is shown as missed with no reason; and the list itself is being read as a record of individual performance. They raise a dispute through the route named in the register, with the engagement IDs. The owner reviews the cases against the register definition. The withdrawn engagement correctly stays in the denominator, but the missing reason category is a data-quality failure; the owner corrects the record and, if the period is final, issues a correction note. The owner also confirms that the register says this measure is never used for individual performance (§7.7), and removes the per-person miss list from the report. The outcome and reasoning go back to the tester and into the change history. **Pass condition:** the dispute is resolved by reference to the written definition and the records, not by seniority, and the correction is visible. The dispute itself is never treated as a mark against the tester.

## 13. Adoption profile

Before reporting any measure, an adopter should: name a measurement owner role; choose an initial small set of measures; complete a register entry for each, including the unit, the population and cutoff rule, the control test, and a paired measure; for any windowed measure, answer every item in §4.1 and work the test states; connect each input to a named source of record; run a baseline before setting targets, or designate the measure trend-only; publish the dispute route; and test the set with the three walkthroughs in §12. An adopter may take the register and the incentive checks without adopting any of the §4 families.

Local choice can change which measures exist, their windows, cutoffs, cadence, tools, thresholds, and targets. It cannot make a count meaningful without its denominator, turn missing data into a zero, score an item before it could be late, quietly remove items from a fixed population, or make a dashboard into a source of record.

## 14. Assurance evidence, limitations, and correction

A credible local implementation can show: a versioned register; per-period freeze and cutoff extracts, population lists, change and exclusions logs, and check results; at least one recalculated final value; a record of at least one trend that was investigated rather than simply reported; a dispute and its resolution, or the route ready to receive one; and the annual review of the measure set. The existence of this document proves none of those operations occurred.

**Limitations.** This guide offers no benchmark data and no target values, and its examples and thresholds are invented. It deliberately offers no ready-made formula for windowed service measures; §4.1 lists what an adopter must decide instead, and those decisions are where most of the difficulty lies. The measure families reflect common testing-practice services; a practice offering different services will need different measures. Small practices may find monthly percentages too volatile to read and should prefer longer periods or raw counts read against their denominators.

**References.** The NIST Cybersecurity Framework 2.0 is relevant, in particular its Govern function's oversight outcomes and its Identify function's improvement outcomes; consult the current version directly for exact category wording. Other program-measurement guidance from established testing and assurance bodies may apply to an adopter's context.

**Correction path.** Report an error, an unfair example, or a missing trap through the framework's published contribution and correction route. Corrections to this guide are recorded and dated.
