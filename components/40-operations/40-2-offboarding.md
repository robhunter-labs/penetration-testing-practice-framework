# Tester Offboarding and Access Revocation

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

An operator's departure does not end when their account is disabled. A tester may also hold tool-specific accounts, active sessions, shared secrets, engagement data, hardware, and work that someone else must take over. This guide gives a penetration-testing practice a repeatable way to close those paths and show what was checked. It is a template to adapt, not a claim that an adopter operates these controls.

## Purpose

For a departure, contract end, or role transfer, identify what the person could reach, remove or transfer that access under local authority, verify the result, and leave a record that another person can inspect. Pair this with the practice's onboarding inventory: every grant, asset, and operator responsibility created at entry needs a corresponding exit action. A new grant without an exit route is a design gap, not merely a checklist omission.

## 1. Choose the route and clock

| Trigger | First decision | Closure condition |
|---|---|---|
| Planned departure or contract end | Set the effective last-access time and coordinate the work handoff. | Applicable access is verified removed by its deadline; assets, secrets, and assignments are verified separately. |
| Role transfer | For a move out of the practice, use the exit route. For a move within it, identify which grants the new role still needs; do not carry old access forward by default. | Unneeded grants are verified removed; retained grants have a new owner and reason. |
| Urgent separation or suspected misuse | An authorized leader directs immediate access removal without waiting for exit paperwork. | The access owner confirms actual revocation, and any security concern follows the incident path. Other exit work has its own deadline and owner. |

Set **two clocks** for each route: the deadline to remove access and the deadline to complete asset, data, secret, handoff, and record work. An adopter must define those clocks, trigger authority, employment/contract constraints, and escalation for either missed deadline. Immediate removal for an urgent separation and removal by the last working day for a planned exit are possible local defaults, not universal SLAs. A submitted access ticket is not evidence that access stopped. For a contractor exit, decide who may initiate the process on both the practice and vendor sides.

## 2. Build the exit inventory from actual grants

Start with the onboarding record, current identity and tool inventories, engagement assignments, and asset register. Ask the departing operator and system owners about less-visible paths. Record the account or asset identifier, owner of the removal, action, deadline, evidence location, and verification result. At minimum, check:

- **Identity and tools:** SSO, groups, repositories, testing platforms, reporting and collaboration systems, vendor tenants, per-engagement accounts, and temporary environments.
- **Secrets and sessions:** personal vault access, shared or engagement credentials, API keys, tokens, active sessions, device certificates, hardware authenticators, and any recovery paths. Disable individual access and rotate or revoke shared material the person could have known. If rotation is deferred or technically impossible, record the exposure, owner, compensating action, deadline, and authorized exception; “they probably will not use it” is not a control.
- **Assets and data:** workstations, mobile or wireless rigs, licensed devices and keys, local working copies, synchronized storage, and custody of engagement evidence. Recover or account for them without copying sensitive evidence into the offboarding record. Check whether credentials or engagement data persist on personal devices or cloud-sync, using an authorized method. A lost hardware authenticator requires logical removal even while physical recovery remains open.
- **Work and knowledge:** reassign active engagements, review and consulting duties, queue items, incident/on-call roles, distribution lists, and recurring meetings. Check that engagement records and archives are complete; transfer runbook and tooling knowledge into the approved knowledge base or an authorized owner. An urgent access stop must not wait for a knowledge-transfer meeting.

For a third-party tester, include the vendor-managed access path and temporary tenancy, confirm who may attest to vendor-side data handling, notify the vendor contact through the approved channel, and retain the acknowledgment. Do not claim that data has been removed from a vendor endpoint unless an authorized check supports that claim.

## 3. Verify before declaring closure

The person who requests removal should obtain a result from the system or access owner, not just a ticket number. Compare the post-action access state with the exit inventory. For a critical path, use a direct revocation check appropriate to the system: group membership, account state, token/session invalidation, key rotation result, or an explicitly authorized access attempt. Record who checked, when, what was observed, and the evidence reference. Periodic roster-to-access reconciliation is a backstop; it does not replace the exit check.

If an account is disabled but a previously issued API token still works, offboarding is **not complete**. The access owner blocks or revokes the token promptly; if that action would destroy needed logs, preserve them through an authorized response path without leaving the token live unnecessarily. Investigate scope and use, then retest that the token is rejected. For a shared token, coordinate rotation and dependent users. Add that token type to the entry/exit inventory so the next departure does not repeat the gap. An unverified system, missing asset, unknown shared secret, or unacknowledged vendor path remains open with an owner and escalation—not silently marked “not applicable.”

## 4. Use one inspectable record

Copy this table for each exit. Keep personnel details and sensitive access evidence in approved, access-controlled systems; the record needs only references.

| Field | Entry |
|---|---|
| Case ID; departure or role-change type; effective time |  |
| Triggering authority, including vendor counterpart if applicable; coordinator |  |
| Access-removal deadline; remaining-work deadline; missed-deadline escalation |  |
| Onboarding inventory and current-grant references |  |
| Identity, tool, vendor, and temporary access actions |  |
| Secrets, sessions, recovery paths, and rotation actions |  |
| Assets/data custody and work handoff |  |
| Each action's owner, completion time, verifier, and evidence reference |  |
| Independent or second-person verification where practical |  |
| Exceptions, residual access, containment, escalation, and due condition |  |
| Final sign-off authority, date, and reason closure is justified |  |

“Not applicable” needs a reason. “Requested” and “verified removed” are separate states. If urgent revocation is complete but asset return or knowledge transfer is not, record the access result and keep the overall case open. Sign-off means the named authority accepts the recorded state; it does not erase unresolved exposure.

## 5. A bounded example

**Fictional contractor exit.** A tester's contract ends Friday. The coordinator inventories their SSO and tool accounts, a temporary jump environment, repository access, a hardware key, an API token, and two active engagements. The access owners remove the grants; an engagement owner takes the work; the vendor contact acknowledges the exit. The coordinator sees the SSO account disabled but an authorized check shows the API token still works. The case stays open. The API's access owner revokes it, checks for use after the effective time under the local security process, and confirms in a retest that the token is rejected. The hardware key is still in transit, so its logical grant is removed while the record names its physical custodian and follow-up date. The token type is added to the onboarding/offboarding inventory.

This example illustrates separate access, asset, and work states. It does not describe an actual departure or prove that one successful token check found every hidden access path.

## 6. Keep the lifecycle symmetrical

When onboarding adds a new system, credential type, device, or duty, add its exit action at the same time. Periodically compare active operator rosters with group and tool membership, sample completed exits, and feed missed paths back into the onboarding inventory and offboarding procedure. The useful outcome is not a signed checklist alone; it is a demonstrable transition from authorized operator to no longer authorized operator, with remaining work owned.

## Adoption and claim boundary

Before use, bind this template to the adopter's employment and contractor process, identity systems, secret stores, incident authority, asset custody, record retention, privacy rules, verification methods, and feasible review cadence. This document does not grant termination authority, set a universal revocation SLA, certify access removal, or replace an incident investigation. It is one public, adaptable part of a larger practice framework, not an account of a fully deployed external program.
