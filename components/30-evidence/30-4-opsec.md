# 30.4 — Testing operational security

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

An offensive testing capability is itself an asset worth attacking: the tooling, the access it holds, the data it touches, and the people who run it. This component is the single place the operational-security requirement lives — **the tooling stays a controlled asset, only qualified operators run it, the environment contains it, its secrets are protected, and misuse is an incident** — across human-led and agentic tooling. It states requirements as risk outcomes and points outward for mechanics: secrets to the [credential guide (§30.3)](30-3-credential-handling.md), the record set to [§30.1](30-1-archival-files.md), third-party-product disclosure to [coordinated disclosure (§50.1)](../50-support/50-1-coordinated-disclosure.md), and outward audit requests to [§50.5](../50-support/50-5-audit-handling.md).

## Six outcomes to protect

1. Offensive tooling is not copied, shared, or leaked out of the team.
2. Only a qualified operator runs a given tool, and setup is held to a higher bar than use.
3. The environment contains the capability — isolated, segmented, egress-controlled, observable, stoppable.
4. Secrets the capability uses or captures are protected (by reference to [§30.3](30-3-credential-handling.md)).
5. Testing traffic is deconflicted so defenders are not chasing a ghost, and attribution is possible.
6. A tool or credential compromise, or an egress anomaly, is treated as an incident, not absorbed.

## Tooling is a controlled asset

Offensive tooling — commercial, open-source, in-house, or agentic — is set up and run only inside a team-controlled environment, by authorized operators, on controlled systems, never on personal or general corporate devices. Who holds a tool and on what system is recorded. Taking a tool out of the team, copying, or leaking it is a reportable incident.

**A control another function owns is not the team's to disable.** When a standing control (a network control, a data-loss policy, a platform setting) obstructs a legitimate test, request a scoped change through that owner's process, keep the safeguard in force meanwhile, keep leadership informed, and never represent a control as removed on your own authority.

## Operators and tool admission

An operator is qualified for a tool per that tool's operating procedure and the onboarding standard, with a lead's sign-off before unsupervised use. A new tester does not stand up or configure tooling alone — **setup is a higher bar than running**. Maintain an authorized-operator list per tool. Admit a tool through states — not-admitted → lab-only → admitted — and re-admit on a material version change; a registered tool is evidence of *intent to control*, not proof of integrity, so admission is a judgment, not a list entry.

## Environment and egress

Default to non-production, isolated, segmented environments. **Egress is default-deny with an allowlist at the enclave boundary, with telemetry**; egress points are named per tool in its procedure. A stop mechanism (kill switch) is available and verified for agentic tooling. Member-facing or production systems are out of scope for the capability itself and follow the enterprise's own lifecycle. A pre-production promotion of a sandboxed tool carries its own deconfliction notice.

## Deconfliction

Maintain a pre-registered inventory of the team's testing systems and source address ranges, shared with the monitoring/incident function and refreshed. Before an alert on that inventory becomes an incident, defenders self-verify against the inventory and the standing authorization. Engagement-level deconfliction is unchanged: notify the customer, stakeholders, and the monitoring/incident function before an engagement and whenever detection is likely. **A register is evidence of intent, not integrity, and attribution support is not an exemption from containment** — a tool still has to be contained, not merely identifiable.

## Credentials and secrets

Held in the controlled secret store, referenced not cleartext — the [credential handling guide (§30.3)](30-3-credential-handling.md) is authoritative for storage, transit, rotation, and disposal, including the two-clock model. Tooling credentials are scoped, time-bound, and revocable; agentic credentials carry a rotation cadence and a named owner; captured customer/session tokens are revoked at closeout.

## Agentic-tool operational security

Where an agentic tool is used, these must be enforceable, not aspirational: a spend/usage-anomaly guard against runaway cost with a named owner and threshold, cross-linked to the incident path; egress control and telemetry at the enclave boundary; a per-engagement memory reset; **target content treated as data, never as instructions**; integrity verification of the tool's extensions / connected servers; a cleartext-secret scrub of agentic logs and output before archival; and a fresh baseline and re-review when the agent stack materially changes. An attempted prompt injection that the controls catch is a handled event; it becomes an incident only when a control actually fails — do not conflate the two. There is **no blanket ban on agentic tools against production** — production use is a scoped, authorized decision, not a reflex prohibition. An adopter may keep these controls here or in a separately versioned AI operating component, but the engagement must point to the controls that actually govern its tool.

## Restricted engagement classes

Some engagement classes carry additional operator-eligibility and tooling constraints, set in the rules of engagement or the per-tool procedure and not relaxed for convenience. Keep eligibility stated generically (need-to-know discipline), without reproducing the specifics of any restricted program.

## Data handling and incidents

Engagement data is classified and handled per the adopter's data governance and [§30.1](30-1-archival-files.md), with chain of custody; no findings or credentials over chat or personal email. Report to leadership and enter the incident path on out-of-team tool use, a tool or credential compromise, an egress anomaly, or a runaway-spend alert. A compromise in a third-party product routes to [coordinated disclosure (§50.1)](../50-support/50-1-coordinated-disclosure.md).

## Pre-run readiness check

Before a run, confirm each outcome is met or has a documented local equivalent: tool admitted for this version · operator authorized · environment isolated · egress default-deny with telemetry · stop mechanism verified (agentic) · secrets by reference only · deconfliction inventory current · incident path known. Answer each Yes / Not-applicable / Equivalent / No; a "No" is the signal to stop, not a note to carry.

## Reader test before adoption

Can a tester, a lead, and a defender each confirm — before a run — that this tool may run, in this environment, by this operator, with a way to stop it and a plan if it is compromised? If any of the four cannot, the capability is not ready to operate.
