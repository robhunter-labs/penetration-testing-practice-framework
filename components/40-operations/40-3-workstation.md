# Penetration-Testing Workstation and Field Kit

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A testing workstation is not just a laptop with tools installed. It is a controlled path from an authorized test to a defensible record: who owns the host, what it can reach, where credentials and evidence live, how a clean state is recovered, and what happens to the equipment and data when the work ends. This guide helps a practice specify and verify that path. It is an adaptable design and operating record, not a claim that one hardware stack is required or that any named organization has deployed it.

In the checks below, a *fixture* is a deliberately designated lab target or synthetic artifact, never a production or third-party target. A *clean reference* is a tested restorable build state, not a copy of an engagement's evidence.

## 1. Choose the operating posture deliberately

Name one accountable workstation owner and one support route. “Managed” means the adopting organization can apply and observe its normal device controls. “Outside the normal managed fleet” describes a **device-management exception**, not an exemption from inventory, security, or review. A remote execution host adds a second custody and administration boundary. Select a posture only after the owner records how the missing or changed controls will be handled; never call a device safe merely because it is isolated from the corporate network.

| Decision | Questions the adopter must settle | Evidence to retain |
|---|---|---|
| Ownership and custody | Who owns the host and peripherals? Who may use, administer, transport, recover, and retire them? | Asset/assignment record, custodian, loss route. |
| Management model | Which endpoint controls are present? Which normal controls do **not** apply, and what compensates for each material gap? | Current baseline, exception/risk decision, verifier. |
| Workload separation | Will testing, tool evaluation, and reporting share a host, guest, or data store? What must be physically or logically separate? | Boundary diagram or table and approved exception. |
| Connectivity | Which host and guest paths reach the internet, target, management plane, and evidence destination? When may a guest be bridged or directly attached? | Tested network profile, owner, change/reversal rule. |
| Data and recovery | Where are credentials, raw captures, curated evidence, backups, snapshots, and keys? Who can restore each? | Storage and retention map, recovery test, archive handoff. |
| Tooling and field kit | Which capability does each tool or peripheral supply, and what method, training, license, firmware, and authority does it need? | Versioned inventory and readiness check. |

The source design used a personally assigned, organization-owned host outside the ordinary device-management stack, with a testing guest and a separate R&D posture. That is one *design case*, not the default this framework prescribes. A different practice may choose a managed host, a dedicated remote rig, or another separation model. The obligation is to make the trade-off and its evidence visible.

For a host outside normal management, use one row per missing control. A compensating measure has to supply an observable property; “the tester is careful” is not a measure. An unresolved material gap remains an exception with an owner, not a silent PASS.

| Normal control or property absent | Compensating design | How it is checked | Residual limit and decision owner |
|---|---|---|---|
|  |  |  |  |

## 2. Draw the trust boundaries before selecting products

Use this compact map to document the local build. Replace every bracketed field; a blank boundary is a readiness gap.

| Boundary | Local choice to record | Minimum question to test |
|---|---|---|
| Operator → host | Named individual account; privileged maintenance route; authentication and recovery owner: `[ ]` | Can an ordinary test session change host controls or install software without the approved route? |
| Host → testing guest | Image source and digest, hypervisor, guest storage, update owner, snapshot/restore mechanism: `[ ]` | Is the image authentic, current enough for the work, and recoverable without losing evidence? |
| Guest/host → network | Starting route, DNS, egress identity, VPN/proxy where used, bridge/direct-connect exception: `[ ]` | What source does the target and monitoring team actually see? What path bypasses the intended control? |
| Work area → evidence archive | Local encryption, access, classification, curated package, destination, receiver verification: `[ ]` | Can the receiver confirm the intended bytes arrived and remain under the right access controls? |
| Host/guest → secrets | Separate system, operator-tool, and engagement credentials; key and break-glass custody: `[ ]` | Could a guest restore, personal sync, or next engagement expose an earlier secret? |
| Workstation → field | Kit custodian, transport, local law/site rules, captured-item return: `[ ]` | Can each item and any data on it be accounted for before and after travel? |

Network address translation (NAT) is a routing choice, **not** an anonymity, containment, or monitoring guarantee. Bridging or direct attachment can change both target visibility and attack surface; it requires an engagement-specific network decision under the actual rules of engagement. A VPN or split tunnel is also a route to test, not proof that all traffic follows the intended path. Use a benign, owner-approved endpoint for route checks—never a real target scan merely to verify setup.

## 3. Specify the host and guest baseline

Record outcomes and versions rather than pasting a setup command that will age. The local baseline should identify the supported host/guest versions and the authority for each change. It should cover:

- **Host:** disk encryption and recovery-key custody; boot and operating-system integrity controls; standard versus privileged accounts; patch and security-update handling; screen lock; local firewall and endpoint protection or compensating detection; application-source controls; audit/log review; physical loss response. Confirm what is actually active, especially on a host outside central management.
- **Guest:** approved image source and integrity check; hypervisor and architecture compatibility; required CPU, memory, storage, USB/pass-through and network modes for the selected methods; tool and license provenance; patch state; guest-to-host data flow. A package list is not proof that its method-relevant feature works.
- **Reference state:** a tested clean build or reproducible configuration; the location and custodian of the reference; a safe restore exercise; pre-engagement change record; and post-engagement cleanup. A snapshot can restore execution state, but it is **not** the evidence archive. Export and verify required evidence *before* any restore or deletion.
- **Untrusted tool evaluation:** if the practice evaluates new security or AI tooling, use a separately governed evaluation posture. First-run containment, permitted egress, synthetic data, authority to promote, and human review belong in §90.3 and the tool-specific procedure (§90.2). A clean engagement guest is not automatically a detonation environment.

Do not turn any one model, processor, memory size, operating system, hypervisor, browser extension, tool bundle, update delay, or audit cadence into a universal requirement. The adopting practice selects and tests them against its methods, management capability, support model, and current vendor guidance. Record a date or trigger for reevaluating a baseline when the host OS, hypervisor, image architecture, tool entitlement, or method changes.

### Baseline record — copy per build profile

| Field | Local entry |
|---|---|
| Profile ID, version, maintainer, approval and review trigger |  |
| Host/remote asset and management posture; explicit exceptions |  |
| Host OS/security baseline; encryption and recovery-key owner |  |
| Standard/privileged identities; maintenance route |  |
| Guest image source, version, digest, hypervisor and architecture |  |
| Guest storage, network mode, allowed egress, DNS, monitoring contact |  |
| Tools/versions/licenses required by method; observed feature checks |  |
| Clean reference, backup/restore test, and separate evidence archive |  |
| Lost device, compromise, rebuild, and retirement routes |  |
| Limitations, exceptions, reviewer, and evidence references |  |

**Fictional profile example.** A managed laptop accesses a dedicated remote test host. The organization owns the laptop baseline; a named platform team owns host patching and guest snapshots. The tester can authenticate, but the remote guest still points its evidence export at an unapproved personal sync folder. The host/guest identity checks may PASS; the evidence boundary and full profile readiness FAIL. The platform owner changes the path, the tester and receiver verify a synthetic handoff, and the affected acceptance rows are rerun. This example is a decision pattern, not a real deployment or a shortcut to testing authority.

## 4. Separate secrets, work product, and the archive

System credentials, the tester's own tool accounts, and secrets obtained during an engagement have different owners and lifecycles. Keep them logically separate and under the adopting practice's approved storage and recovery rules. Use individual identities; avoid placing engagement secrets in a system keychain, general tooling vault, personal account, or another engagement's workspace by convenience. Hardware-backed authentication or a separate engagement vault may improve the design, but the exact product and recovery plan are local choices. No public template should contain real credentials or key material.

Evidence egress needs a **sender and receiver contract**. Decide what is collected, minimized, redacted, packaged, inspected, transferred, received, archived, retained, and eventually disposed. Where a digest or signature is used, record *which files* it covers, who controls the signing key, how the receiver obtains trusted verification material, how a failed verification is handled, and the receiver's actual result. A checksum written beside the same untrusted upload does not independently authenticate its origin; “upload succeeded” is not “archive verified.” Antivirus scanning is useful but cannot certify that a package contains no sensitive material or malware. High-sensitivity evidence takes the local escalation route before transfer. Keep raw captures, scripts, and vaults only where the record's purpose and authority justify them; do not assume they must never be retained or always be exported.

| Evidence handoff | Local record |
|---|---|
| Engagement and approved package/classification |  |
| Sender, receiver, destination, transport, and access control |  |
| Inventory or manifest, digest/signature method, trusted key route |  |
| Screening, minimization and redaction decisions |  |
| Upload/transfer receipt **and** receiver integrity/access result |  |
| Raw-data disposition, archive reference, retention rule, exception owner |  |

## 5. Close an engagement without destroying the record

Use the method, engagement rules, evidence/archive guide (§30.1/30.2), and local records policy to order the closeout. The safe dependency is: **identify required evidence → curate and transfer → verify receipt and integrity → confirm retention/custody → remove only the working copies and states authorized for removal → rebuild or restore and test the clean state.** If any archive verification fails, pause destructive cleanup and resolve it. Secure deletion on solid-state media is not established by an overwrite command; choose supported encrypted-volume/key-lifecycle and device-erase mechanisms with the platform owner, and verify the result appropriate to the device. A lost or suspected-compromised rig additionally takes the incident route; a rebuild is not a substitute for triage.

Record the closeout result, not only a checked box. Include the guest/reference state, browser or remote profiles, engagement vaults, locally held captures, removable media, hardware keys, peripheral storage, and any still-active tokens or sessions. Keep the archive separate from the clean-reference snapshot. The offboarding guide (§40.2) is the operator-exit counterpart; device retirement and tester departure can overlap but are not the same event.

## 6. Manage the traveling kit as a capability, not a shopping list

Build an inventory by **method role**: wireless assessment; network-access-control testing; badge/credential assessment; physical-access work; support items such as power, adapters, containment and transport. Each item needs a custodian, identifier, approved firmware/software, method owner, support and calibration state if relevant, training prerequisite, issue/return record, and a rule for any captured data. Record the *capability gap* if a device is absent or incompatible; buying a tool does not make a tester qualified or expand an engagement's authority.

| Field-kit item/class | Purpose and linked method | Custodian/ID | Readiness and legal/site check | Data or captured-item custody | Return/exception |
|---|---|---|---|---|---|
| Wireless adapter or assessment appliance | 20.9 |  |  |  |  |
| Network-access-control test device | 20.10 |  |  |  |  |
| Credential or physical-access equipment | 20.11 |  |  |  |  |
| Power, cables, protective case, isolation/storage | Applicable method |  |  |  |  |

Before transport or hand-off, verify the itinerary and destination rules, the target/site's written authorization, the actual kit contents, and whether any locally held data must first be removed or protected. Use a receiving-party acknowledgment and item-condition check for shipment or shared-kit transfer. Travel and physical-access law vary by jurisdiction; this framework does **not** issue legal advice or permission to carry or operate any device. Captured items follow the approved engagement evidence and return/disposal agreement. A specialized physical kit also requires demonstrated operator competence; §20.11 owns the method detail, not this inventory.

## 7. Verify the build before relying on it

Use one acceptance record per build or material revision. §40.1 owns *tester onboarding readiness*; this is the underlying workstation/kit profile it consumes. A rig can pass its baseline and still be unusable for a specific method, and neither result grants permission to test a real target.

| Check | Observed result and evidence reference | Owner/verifier |
|---|---|---|
| Asset, custodian, management posture and explicit exceptions match the profile |  |  |
| Encryption/recovery, host protections and standard/admin separation work as designed |  |  |
| Guest image provenance, integrity, boot, patch and restore are observed |  |  |
| Benign network-route test matches the recorded source, egress and monitoring path |  |  |
| Required tool entitlement and method-relevant feature work on an approved fixture |  |  |
| Synthetic evidence can be saved, transferred, received, verified and retrieved under the right access |  |  |
| Engagement data is absent from the clean reference and an unrelated tester's space |  |  |
| Field kit inventory, custody, training and any method-specific functionality are checked |  |  |
| Loss/compromise response, backup and rebuild route can be invoked |  |  |
| Engagement authorization | **Not granted by this workstation record.** A specific target needs its own scope and rules. |  |

Mark each applicable row **PASS**, **LIMITED**, **NOT RUN**, or **FAIL**, with the version and person who observed it. A required LIMITED/NOT RUN/FAIL is not full readiness; state the narrower capability and the owner of repair. Re-run affected rows after a significant change. Do not claim “compliant with PCI/HIPAA/SOC 2/HITRUST” from a tool list or a crosswalk: an actual requirement, scoped system, implemented control, and evidence need an independent assessment. A mapping can assist discussion; it is not an attestation.

## 8. Use the links at the right boundary

- **§40.1** uses this profile and its observed checks to onboard a tester; **§40.2** closes the tester's grants, equipment, and duties at exit.
- **§10.1/10.2/10.3** bind a real engagement's scope and rules. This workstation guide cannot authorize testing, traffic routes, field access, or evidence collection outside them.
- **§20.9/20.10/20.11** own wireless, network-access-control, and physical testing methods and specialized competency.
- **§30.1/30.2/30.3/30.4/30.5** govern archive, evidence storage, credentials, testing operational security, and reporting in their respective jobs. Resolve their public titles and links at integration rather than assuming a candidate is released.
- **§90.3** governs research/evaluation posture; **§90.2** is the tool-specific operating record. Neither is silently satisfied by a workstation baseline.

This guide retains a distinctive job: a host/guest/network/evidence control model plus portable equipment custody and an inspectable acceptance record. It deliberately does not prescribe a specific hardware architecture, a dated product purchase list, an exact regulatory crosswalk, legal assertions, or product-version claims as universal instructions. An adopter must fill the records against a real or synthetic profile and check the adjacent documents, technical and currentness claims, rights and attribution, and accessibility before relying on it. No adoption, certification, or production use is claimed.
