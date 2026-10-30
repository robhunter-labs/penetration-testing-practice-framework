# 50.2 — Urgent response (quick-reaction) procedure

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

An offensive team sometimes faces an urgent, out-of-cycle need — a critical issue on a deployed product, a time-boxed escalation, a leadership ask — that should not wait for the normal pipeline and should not quietly consume it either. This component is the bounded lane for that: a short, recorded, ring-fenced rapid response that is explicitly **not** a full engagement and **not** a disclosure, and that escalates the moment it outgrows rapid response. A confirmed third-party-product flaw hands off to [coordinated disclosure (§50.1)](50-1-coordinated-disclosure.md); a mission that needs full methodology becomes a scoped engagement whose deliverable follows the [report standard (§30.5)](../30-evidence/30-5-report-standard.md); every action is recorded per [§30.1](../30-evidence/30-1-archival-files.md).

## What the lane buys — and what it must not swallow

It buys a fast, qualified read when timing matters. It must not become an unstaffed promise, an open-ended embed, or a full assessment wearing a "support" label. The boundary is the **work performed and the authority required**, not a universal clock.

## Four mission lanes

| Lane | Entrance (a possible signal, not a required trigger) | Useful bounded output | Hand off / escalate if it grows |
|---|---|---|---|
| **M1 — Rapid triage of a threat signal** | A threat-intelligence or asset-owner flag that something critical is active and out-of-cycle. An automated prioritization flag is **one possible signal, not the required trigger.** | Is it present, reachable, and exploitable in our context? A minimal non-destructive proof-of-exposure plus an estate-wide presence sweep. | Broad asset testing, unrelated findings, or full methodology → scoped engagement. |
| **M2 — Critical-issue offensive review** | A critical issue surfaces out-of-cycle (new critical advisory on a deployed product, a critical finding or scan result) needing a fast offensive read. | Real-world exploitability and reachability (not score alone), exposure-based prioritization, and hands-on support to the remediating team (reproduction, fix validation). | Full product assessment, ownership of remediation (that is the issue owner's), or sustained testing → scoped engagement. |
| **M3 — Concierge escalation support** | An urgent escalation needing dedicated support faster than normal staffing (retest campaign, closure review, board/audit/customer escalation, a live situation). | Dedicated rapid support — which may surge multiple testers over several days — until the escalation clears. | A full test dressed as support, open-ended embedding, or routine pipeline work → scoped engagement. |
| **M4 — Urgent leadership request** | Leadership refers an urgent out-of-cycle task that does not fit M1–M3. | The smallest bounded task that answers the ask. | Anything that cannot be bounded → say so; it is a scoped engagement, not this lane. |

One intake, one rule: the on-duty tester acknowledges, classifies the mission, and applies that lane's scope and response limit. A mission spanning lanes takes the **tighter scope and the faster limit**. Needing more than the limit, or more than bounded scope, is itself the signal to escalate — **except M3**, where a multi-tester, multi-day surge is within the lane and escalates only when it needs full methodology (a real engagement), not merely because it is large.

## Stand up the service before calling it live

This lane is only real when an adopter has actually put it in place. Before claiming an operating service, establish and be able to show: a known on-duty assignment with a named backup and a handoff that passes open items; a ring-fenced capacity reserve so an urgent call does not blow up planned deliverables (and a leadership decision point when demand exceeds the reserve, rather than silent absorption); the authority each mission runs under; and the response and review limits the adopter chooses. **An automated trigger and a standing rotation are a target architecture, not a prerequisite** — and not something to assert as operating when it is not.

## Authorization and a lightweight triage posture

Testing missions (M1, M2) run under the adopter's standing authority using a **pre-authorized lightweight triage posture** — a thin variant of the [rules of engagement (§10.2)](../10-engagement/10-2-rules-of-engagement.md), default read-mostly / least-agency: presence checks, version/exposure validation, and a minimal non-destructive proof are in; destructive actions, exfiltration beyond proof, and production-impacting tests are out by default (escalate for explicit approval if production validation is unavoidable). Support missions (M3, M4) are advisory under standing authority **without** a testing posture unless they turn into active testing, at which point the triage posture applies or, if unbounded, the mission escalates. A program-level authority is **not** a substitute for permission to touch a specific target or take a specific action. Notify the monitoring/incident function for any active-traffic triage. An optional agentic assist runs at its own authorized, least-agency posture, with every result human-validated and a human making each finding decision.

## On-trigger procedure

1. **Receive and classify** — acknowledge, pick the mission lane, apply its scope and limit.
2. **Check authority and safety** — separate advisory from active testing; pause any hazardous action until the specific authority exists.
3. **Bound the assignment** — write down the smallest task that answers the need.
4. **Do the narrow work** — configuration and version evidence first; a tool or agent only under its own authorized posture; a human makes the finding decision.
5. **Route the outcome** — `confirmed` / `not observed` / `inconclusive`; a confirmed exposure goes to the issue owner and, if it warrants full methodology, to a scoped engagement; a third-party-product flaw takes the separate [disclosure path (§50.1)](50-1-coordinated-disclosure.md); a consulting-scale need routes to normal engagement planning.
6. **Archive and learn** — a short record (mission, trigger, scope, actions, result, disposition) per [§30.1](../30-evidence/30-1-archival-files.md); a recurring need is a signal to *plan* the work, not to keep absorbing it here.

## One-page mission record

`mission ID · lane · trigger/source · authority relied on · scope as bounded · actions · result (confirmed / not observed / inconclusive) · disposition and hand-off · time spent · follow-on`

## A cold-reader test

Can someone who was not there see which lane this was, what authority it ran under, what was and was not done, and where it went next? And before calling the lane operational: can the adopter show the staffing, backup, authority, and capacity reserve — rather than describing a rotation that is not yet staffed? If not, the lane is a plan, not a service.
