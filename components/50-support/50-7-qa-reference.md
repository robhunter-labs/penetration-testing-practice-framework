# 50.7 — Program-practice answer reference

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

Assurance requests repeat a handful of program-practice questions — who tests, how independent they are, what is in scope, how often, what is monitored, what gets shared. This component gives each a safe, consistent **shape** so the first bounded answer (Pattern A under [audit and external information requests (§50.5)](50-5-audit-handling.md)) does not have to be re-derived under time pressure, and so no one improvises on a sensitive topic. It pairs with the [attestation summary (§50.6)](50-6-attestation-summary.md) and the first-reply step of [§50.5](50-5-audit-handling.md); anything past a bounded answer escalates there.

## What "pre-cleared" means here

Not "timeless permission." An answer is usable only when it has been reviewed against a **specific, dated source and a defined audience** — and it carries that provenance. An approval of the shape never preapproves a filled release; that decision returns to [§50.5](50-5-audit-handling.md).

## Answer record (per question)

`question · owning team (who can actually answer it) · bounded answer · evidence pointer (the record behind it) · last verified (date) · approved audience · approver · review trigger (date or event) · status (usable / confirm-first / withdrawn)`

An answer without a date, an owner, and an evidence pointer is not usable, however reasonable it sounds.

## Common questions and the evidence behind them

| Question | What to verify before answering | Boundary |
|---|---|---|
| Who performs the testing? | The adopter's actual sourcing (internal, external, or a mix) from an org/sourcing record | State the arrangement; do not name a specific vendor unless cleared |
| How is tester independence maintained? | The independence arrangement, especially for any regime that requires it | Describe the arrangement, not individuals |
| What can be tested, and how is scope selected? | The scope standard and the selection basis | Name surfaces at a safe level; adjacent controls are the partner teams' |
| How often does testing happen? | The cadence basis (risk-based, event-driven, or a required interval) | Give the basis; a supporting risk assessment is itself an artifact under [§50.5](50-5-audit-handling.md) |
| How are findings tracked and retested? | The finding system and retest practice | Status counts belong in the [§50.6](50-6-attestation-summary.md) summary, not prose detail |
| What methodology and review are used? | The named methodology and the review that is actually applied | Reference the method; do not paste tactical detail |
| Is public vulnerability intelligence monitored? | Which function actually monitors, and what testing references | Broad monitoring usually belongs to a partner team — route it (see below) |
| What can an auditor or customer receive? | The disclosure route | Point to [§50.5](50-5-audit-handling.md); do not promise artifacts here |
| **May a customer test the environment?** | The adopter's **contract terms and security owner** — never inferred | **Confirm with the contractual and security owner; no blanket answer.** Hold until cleared |
| **Are customers notified of shared-platform vulnerabilities?** | The adopter's **legal, customer, and incident owners** — potential contractual exposure | **Confirm with legal / customer / incident owners; no blanket answer.** Hold until cleared |

The last two questions carry real contractual exposure. They are listed so an adopter does not answer them off-hand — each is **held** until the responsible owner confirms the answer against the actual agreement, and only then folded into the usable set with a date.

## Routing, not ownership theater

Some questions are genuinely another team's: control/compliance evidence for a specific regime, deferral and risk-acceptance governance, vulnerability scanning and patch-aging reporting, and broad threat-intelligence monitoring. A penetration-test summary **supports** these but does not satisfy them — so confirm whether the requester actually needs a test artifact or a scanning/patch artifact, and route accordingly rather than answering outside your lane.

## Worked answer shape (fictional)

> *"Do you test every application every year?"*
> Unsafe: "Yes, everything is tested annually." (asserts a population and a cadence the records may not support)
> Safer: "Testing is {risk-based / on a defined interval for the applicable population}; for {that population} the current cadence is {X}, evidenced by {the engagement record and the selection basis}, as of {date}." (bounded, sourced, dated)

## Maintenance test

Could a reader tell, for any answer, who owns it, what record is behind it, when it was last verified, and whether it is cleared for this audience? If an answer cannot show that, it is a draft, not a usable answer — and a sensitive-topic answer with no confirmation is not usable at all.
