# 20.15 — Threat-informed testing: from signal to scoped decision

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.
>
> **Proposed capability blueprint.** This component describes a target *design* — CTI ingestion, a threat-model engine, automated priority flagging, a dedicated channel, a QRF rotation — that an adopter can build and test. It is not evidence that any of those controls are deployed or operating.

## The problem and the useful separation

Cyber threat intelligence (CTI) describes adversary activity, exploited weaknesses, affected technologies and techniques across a broad environment. A penetration-testing practice plans specific engagements against authorized targets. Threat information should improve *which hypotheses and targets get attention* without silently expanding scope or turning every alert into an emergency test.

Keep four assertions separate: **a source reported a signal; a target may match it; a qualified person decided it matters; an authorized test observed an outcome.** A lookup hit proves none of the later assertions by itself.

## Target architecture (design, not installed system)

```text
CTI source + provenance       Asset/technology data       Engagement scope & RoE
             \                       |                       /
              \                      |                      /
               → candidate match + uncertainty register ←
                              ↓ human validation
                    per-target threat hypothesis
                              ↓ decision + authority
              scoping emphasis | planned priority | urgent triage
                              ↓
                   test record + outcome feedback
```

A small practice can begin with a controlled table and a human analyst; a store/engine is an optional later implementation. Automation may propose matches and draft threat models, but it does not grant test authority, assert exposure, assign findings, or override the Rules of Engagement (RoE). Every hop should preserve source date, classification, confidence, asset-match basis, reviewer and disposition. A high-confidence match still needs a scoped action decision.

## The three workflow doors

| Door | Trigger | Allowed effect | What does **not** follow |
|---|---|---|---|
| Engagement scoping | A relevant signal intersects an in-scope target | Add a test hypothesis or emphasis to the approved plan/RoE | New target, new technique authority, or finding by inference |
| Portfolio planning | Several candidate tests compete for planned capacity | Reorder or deepen the backlog with recorded rationale | An unplanned production action or a claim that all flagged assets were tested |
| Urgent response | A credible time-sensitive threat could affect an owned asset | Route a bounded question into [§50.2](../50-support/50-2-urgent-response.md) | Automatic exploitation, estate-wide scanning, or a standing QRF claim |

The urgent door must work on a human CTI report or issue-owner escalation even when no engine exists. Otherwise the blueprint would require its own unbuilt prerequisite to handle the very event it is meant to address.

## Priority decision, without false precision

P0–P3 style labels are common. An adopter may keep such labels, but the thresholds are local decisions and the label is **a work-routing cue, not a vulnerability severity or test result**. A useful record includes: reported behavior/technology; source and age; match to version/configuration; internet or business exposure; exploitation evidence; asset owner; uncertainty; proposed action; human decision; scope/authority reference; and reconsideration trigger. A missing inventory match can mean *unknown*, not “not exposed.”

| Illustrative decision | Meaning | Next action |
|---|---|---|
| Urgent validation | Credible active threat plus plausible affected deployment | Verify the match and route bounded triage; notify response owners |
| Planned priority | Relevant technology or behavior likely in the portfolio | Bring the target forward in planning or deepen its next scoped test |
| Engagement emphasis | Relevant technique or condition within a scheduled test | Add a hypothesis to the approved test plan |
| No actionable match yet | Weak, stale, or unresolved signal | Keep a watch/recheck condition; do not assert a negative finding |

## Example (fictional)

A CTI report describes exploitation of component version X. Inventory lists two applications with that product family but not their deployed versions. The analyst records a **candidate**, asks the owners for version/configuration evidence, and does not mark either application vulnerable. One version match is confirmed. The owner and testing lead decide whether the least invasive exposure check belongs in the existing engagement or an urgent §50.2 mission. Only a bounded authorized test can support a testing outcome; a separate issue owner handles remediation. If the CTI source is withdrawn or corrected, the affected decisions are revisited.

## Build and proof sequence

1. **Human route first:** agree CTI-to-practice contact, source handling, target inventory owner, decision record and manual three-door workflow. Exercise a false match and a genuine urgent match.
2. **Reusable store, if earned:** ingest with provenance, freshness, classification and correction/withdrawal handling. Prove an asset join on version/configuration rather than name resemblance.
3. **Proposal engine, if earned:** generate per-target hypotheses and optional priority suggestions; evaluate against manually reviewed cases, including stale data and absent inventory. A suggestion remains pending until a qualified reviewer acts.
4. **Consumers:** wire only the accepted decision into RoE, planning or urgent response; test the actual downstream reader and revocation path. Measure whether this improves decisions without flooding the planned pipeline.

The [MITRE ATT&CK Enterprise catalog](https://attack.mitre.org/tactics/enterprise/) can provide technique vocabulary; record the version used rather than hard-coding one in a standing method. Check [MITRE's version history](https://attack.mitre.org/resources/versions/) when adopting or updating a mapping. ATT&CK language does not establish that an actor targets a specific adopter or that a technique is present in an application.
