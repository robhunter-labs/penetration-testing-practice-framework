# 90.4 — Leadership Decisions for AI-Assisted Testing

**§90.4 · Leadership decisions for AI-assisted testing · Penetration Testing Practice Framework**

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

**Component:** leadership decision aid and blank local dial register  
**Reader:** practice lead, tool owner, assurance partner, or adopter deciding how much autonomy and human work a testing capability may carry

## Why these decisions need their own page

An AI-assisted tool can compress work, but that does not make every trade-off a permanent rule. A practice may change how deeply it validates lower-consequence output, how often it checks for missed coverage, what the customer is told, or how it accounts for human and tool contribution. Those decisions should be visible, owned, and reversible **without silently changing the authority and evidence floor**.

This page is a schedule to *set* those choices locally. It does not choose values for an adopter, establish a deployed AI-testing program, approve a particular tool, or authorize a test. §90.1 is the operating-model parent; §90.2 records the resulting posture for one tool; §90.3 handles capability readiness.

## Fixed floor versus adjustable dial

A **fixed floor** is a condition a parameter cannot waive. A **dial** is an authorized local choice *within* that floor. This framework makes eight floors explicit; the public form preserves their functions without importing any enterprise-specific systems or data classification as universal rules:

1. A qualified human is accountable for and decides every finding delivered to a relying party. Human decision is not the same as full manual reproduction of every intermediate tool suggestion.
2. A finding needs evidence of the behavior and impact claimed; a weakness label, identifier, model statement, or score is not enough.
3. Critical or otherwise locally highest-consequence findings receive full human validation under the adopted method.
4. A new target class or materially new tool posture receives full validation until evidence justifies any narrower validation depth.
5. Use the least agency needed: bounded identities, permissions, data, tools, actions, network reach, time, cost, and a stop route. High-impact actions need their own specific authorization.
6. Tool operation and validation belong to qualified, locally authorized roles.
7. Data and provider restrictions are set by the adopter's actual authority. This schedule cannot waive restrictions on regulated data, secrets, retention, or egress.
8. A method that has not earned its claimed conformance or validation basis cannot use a reduced-validation setting on that basis.

These are proposed public-framework floors, not claims about an employer or an externally certified standard. An adopter must reconcile them with its own law, contracts, risk model, authority and local operating framework. If a conflict exists, do not resolve it by quietly turning the floor into a dial.

## The nine decisions

There are nine current levers (the numbering skips retired item 5). The public register retains every *decision job* but deliberately carries **no inherited numerical default**. Fill `local value`, `owner`, `evidence`, and `review trigger` before a setting is treated as active.

| Lever and reader question | Local value / decision owner | Options and trade-off to assess | Evidence and fallback |
|---|---|---|---|
| **1. Validation depth for eligible lower-consequence outputs.** How much direct revalidation is needed beyond a human finding decision? | `[LOCAL]` | Full validation versus calibrated sampling; less direct work trades away detection of false positives. | Prior full-validation comparison and error trend. Until calibrated and authorized, do not claim a reduced-depth route. |
| **2. Tester contribution or credit.** How are human skill, tool assistance and accountability represented fairly? | `[LOCAL]` | Weighted credit, effort model, team-level recognition, or no individual weighting; incentives can distort case selection and skill growth. | Actual work and behavior review; no invented productivity multiplier. |
| **3. Periodic full-validation check.** When is a tool's accepted-result quality challenged afresh? | `[LOCAL]` | Release-, class-, engagement-, or time-triggered reviews; more frequent checks cost human effort, less frequent checks detect drift later. | Defined specimen set, error trend, material-change trigger and reviewer. |
| **4. Coverage assurance.** How do we learn what the tool silently missed? | `[LOCAL]` | Parallel human testing, seeded cases, known-ground-truth benchmarks, or another fit-for-purpose method; stronger recall signal costs test effort and needs a credible denominator. | Missing/dead oracle is `unknown`, not zero missed cases. If no method is set, do not claim measured coverage. |
| **6. Additional control for high autonomy.** Who decides whether a more autonomous posture needs extra review? | `[LOCAL / EXTERNAL OWNER]` | Advisory challenge, additional authorization, or prohibition under local policy; oversight protects consequential actions but can slow adoption. | Current tier/posture and authority; absent external concurrence cannot be supplied by this document. |
| **7. Relying-party transparency.** What is said about material AI assistance? | `[LOCAL]` | Brief disclosure through fuller method explanation, within security and contractual limits; too little can weaken trust, too much may expose sensitive technique. | Engagement and contract need; approved language and correction route. |
| **8. Recognized methodology mappings.** Which technical sources may support a reduced-depth claim? | `[LOCAL]` | Maintained current source set or no recognized mapping; a broader list increases eligibility but can launder superficial conformance. | Exact version and behavior-level mapping review; absent mapping receives no reduced-depth credit. |
| **9. Model/system assurance cadence.** Which external AI-risk process governs the model or system? | `[EXTERNAL OWNER]` | Determined by the adopter's AI/model-risk authority; the testing practice aligns, it does not reset that authority. | Current owner decision and material-change route; local procedure references it. |
| **10. Recognition/equivalence scope.** For which uses may an external assurance decision be recognized? | `[EXTERNAL OWNER]` | Narrow or broad recognition under the relevant parties' agreement; broader reach saves duplicate work but increases reliance on another review's scope. | Exact parties, systems, conditions and limits; no recognition inferred from a similar product name. |

## How to set or change one dial

Use one decision record per changed setting. A leader should be able to tell both what effort the change saves and what assurance it may surrender.

```text
Dial / value / permitted band:
Exact tool posture, target classes and affected decisions:
Decision owner and any external concurrence:
Evidence used, denominator, date and uncertainty:
Alternative settings considered and why rejected:
Effect on human validation, coverage, safety and customer reliance:
Operational cost and incentives:
How §90.2 procedures and operators receive the change:
Effective condition, review trigger and rollback condition:
Record or signature location:
```

**Example of a question, not a selected policy:** A leader wants to sample direct reproduction of some lower-consequence candidate findings because a tool is generating more output than reviewers can fully re-run. First establish whether the tool's exact posture has a credible full-validation comparison, whether error rates and missed coverage are measured by living oracles, which cases remain full-validation, and whether a qualified human still decides *every delivered finding*. If those facts are missing, the reduction is an unproven hypothesis, not an earned efficiency. The decision may still be tested in a bounded evaluation; that is different from silently applying it to live delivery.

## Review what the setting actually did

At a material tool change, incident, surprising miss, correction, or scheduled local review, compare the dial's promised benefit with observed work and risk. Did it catch false findings? Did the team discover misses by a method with a real denominator? Did it duplicate another review? Did cost or delay cause operators to bypass it? Did credit weights reward volume over skill and accountability? Change or retire a dial when evidence says it no longer pays—without erasing the fixed floor.

For any missing, stale, or contradictory local value, record that state. Do not manufacture a default from a historical setting. The affected use returns to a locally authorized, more conservative posture or stops until its actual decision owner resolves it. The blank schedule itself is not a technical control.

## Public-release limitations

This is not a completed local dial schedule, proof of effective sampling, or a claim that AI tools are in production use. Historical settings are **not portable public defaults**.
