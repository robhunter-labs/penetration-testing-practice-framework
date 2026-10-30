# Managed-Device Test Rig: Choose and Operate the Right Layer

**§40.10 · Managed-device test rig · Penetration Testing Practice Framework**

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

The machine a tester signs into may not be the machine that runs the test. That distinction matters: host policy, guest tooling, network identity, evidence custody, and support ownership can sit on different systems. This guide helps a practice choose and operate a test rig on managed devices without confusing a remote access desktop, a virtual guest, and a workstation standard. §40.3 is the separate workstation/field-kit design guide for other management postures and portable equipment; §40.10 focuses on managed-device execution profiles and layer selection.

## 1. Map where the work actually executes

Two common profiles are shown below. They are *patterns*, not employment-status rules. Choose by actual host capability, data boundary, contract, and authority.

| Profile | Entry path | Execution location | What must be verified |
|---|---|---|---|
| Managed local rig | Organization-managed workstation → approved hypervisor or local execution layer → testing guest | The managed workstation and its approved guest. | Host software channel, guest provenance, network route, tool support, evidence location and restore capability. |
| Remote execution rig | Individually assigned access device → approved remote access/desktop → separate managed execution host → testing guest | The named managed execution host; the access desktop may only be a bridge. | Who owns each hop, whether the remote host supports the chosen layer, what data can land on the access device or provider side, guest isolation, logs and teardown. |

Do not assume that every virtual desktop forbids nested virtualization, or that every remote host permits it. Test the actual provider/host configuration. An entry laptop or desktop is not the testing rig simply because the tester uses it to connect. Where an external provider is involved, the practice and provider must bind support, data, access, logging and exit responsibilities. A shared execution host must keep testers' workspaces, snapshots, secrets and evidence separated, and one person's restore must not affect another's engagement.

**Profile record — complete before assigning a tester:**

| Field | Local entry |
|---|---|
| Profile name/version; maintainer; review trigger |  |
| Entry device and its owner; remote hops and their owners |  |
| Actual execution host; management baseline; support route |  |
| Guest or local layer; source/version; compatibility check |  |
| Host, guest, target and evidence network paths/source identities |  |
| Storage and archive locations; provider/endpoint data boundary |  |
| Individual access, licenses, secrets and exit actions |  |
| Shared-host isolation and restore test, if applicable |  |
| Method capability gaps, exceptions, verifier and evidence references |  |

## 2. Select a layer by capability, not fashion

One documented setup used a full hypervisor guest as the general testing rig and a lighter Linux-on-Windows layer for selected web/API/code/scripting work. The portable decision is what the engagement needs: direct or in-band networking, peripheral access, snapshots, tool compatibility, containment and evidence handling. A lighter layer can be useful; it is not equivalent when a method depends on those properties.

| Requirement | Full virtual guest or dedicated test host | Lighter host-integrated Linux layer |
|---|---|---|
| Engagement-separated snapshot and tested restore | Verify guest-level or equivalent reference. | May lack the same snapshot semantics; provide a different tested recovery path or select the full rig. |
| In-band/bridged network presence | Possible only if hardware, hypervisor, network owner and rules permit it; observe actual route. | Do not infer support from ordinary internet access. Use only after a method-specific proof and permission. |
| Wireless or other USB/peripheral-dependent method | Verify physical/peripheral pass-through, drivers and method capability on an authorized fixture. | Often unsuitable; do not assume parity without observed support. |
| Web/API/code review and scripting | Suitable if tools, scope and evidence paths work. | May be suitable with approved host integration, versions, storage and network path. |
| Data separation and cleanup | Guest and host sharing must be explicitly controlled. | Host integration can blur that boundary; specify data paths and cleanup. |

An *authorized fixture* here is an isolated or tester-owned lab target explicitly designated for a setup check, never a production or third-party target. A “works on my VM” check is not permission to touch a real target. §10.1/10.2/10.3 remain the engagement's scope and rules.

## 3. Keep host and guest rules distinct

The adopter must write down what is allowed **on each layer**. One local rule banned host downloads outside a certified software channel while permitting specific guest tool installation. That is a local policy split, not a public grant to install anything in a guest.

| Layer | Local owner and question | Required record |
|---|---|---|
| Entry device/remote desktop | May any engagement data, credential, tool or artifact reside here? | Approved access role, storage/clipboard/download limits, logging and exit route. |
| Managed host | Which channel installs or updates host software and enables virtualization features? | Approved packages/features, admin route, endpoint controls and exception owner. |
| Testing guest | Which tools, sources and licenses are allowed, and how are updates reviewed? | Approved guest image/baseline, version pins or update rule, tool/feature checks and change log. |
| Network and monitoring | What does the security-operations team see from each layer? Who coordinates an engagement? | Source identity, target range, test window, pause/verify and incident contact as applicable. |
| Evidence destination | Can host sharing, clipboard, sync or remote-provider storage copy evidence outside the chosen archive? | Data-flow check, approved handoff/receiver and cleanup action. |

Policy applies to traffic and data from the guest too. A test VM does not make personal browsing, chat, unapproved downloads, or extra-scope activity permissible. Avoid treating monitoring as either total visibility or zero visibility: establish the actual logging and response route. When a host install, network change, or data transfer is unclear, ask the named local owner *before* acting. A guest-to-host clipboard or shared folder should be disabled or tightly bounded unless its purpose, content and cleanup are approved and verified.

## 4. Build, check, and recover the guest

1. Obtain the approved guest image from its trusted source; verify integrity, architecture and compatibility with the selected layer. Record the tested version and owner. Install host-level software only through the host's authorized route.
2. Apply approved guest updates and tool changes, then freeze the versioned baseline that was actually checked. A rolling distribution does **not** mean “update immediately before every engagement” is safe: updates can change tool behavior or break evidence repeatability. Review change impact and rerun affected feature checks before a test.
3. Start from a locally selected low-exposure network profile; record host and guest egress identities. A NAT guest can still generate monitored traffic. Bridged or in-band mode is an engagement-bound change, not a standing default; verify and reverse it under the rules of engagement.
4. Prove the licensed feature and method-relevant tool behavior on a designated fixture. An installed application or fallback edition may not provide the same capability. Individual licenses and secrets belong to their assigned operator and local vault/entitlement process.
5. Create a clean reference or equivalent reproducible build. Before closeout restore, export and verify required evidence with the receiver. Restore only the named guest/workspace; check that other testers and archived records are unaffected. Refresh the reference after material changes and on the adopter's review trigger.

§40.1 owns the tester's observed onboarding check. §40.3 owns the broader host/guest/evidence/kit design decisions; this guide makes the managed-device execution profile and virtualization choice specific. §30.1/30.2/30.3/30.4 own archive, storage, credentials and operational-security decisions, respectively. These are separate reader jobs; no one document supersedes the others by implication.

## 5. Record readiness without claiming authorization

| Check | PASS / LIMITED / NOT RUN / FAIL | Evidence and verifier |
|---|---|---|
| Execution host and each remote hop match the profile; ownership and access are individual |  |  |
| Host/guest security controls and permitted software routes are observed |  |  |
| Guest source, version, patch state, tool entitlement and needed feature are observed |  |  |
| Benign egress test confirms source identity and monitoring/escalation route |  |  |
| Method-specific network, snapshot or peripheral capability works on a fixture |  |  |
| Synthetic evidence transfers to and is verified by the approved receiver |  |  |
| Restore and cleanup do not affect another tester or the archive |  |  |
| Engagement authorization | **NOT GRANTED by this rig record** | Separate approved scope and rules required. |

Every applicable required row must PASS for full rig readiness. A LIMITED/NOT RUN/FAIL means a named capability is unavailable or unproved, not that the tester can improvise on a live target. Record the profile version, tester, observer and repair owner. Changing the execution host, layer, guest baseline, network path, tool entitlement or data route reopens the affected checks.

**Fictional counterexample.** A tester can enter a remote desktop and launch a Linux shell, but the actual execution host has no usable guest snapshot and the security team cannot identify its egress address. Identity/access PASS; the intended network and recovery capabilities FAIL. A web-code-review task might be designed with a separate approved layer and archive, but the full managed rig is not ready for a network engagement. The lead cannot cure that failure by calling the access desktop “the rig.” No real test is authorized by this example.

It does not certify a device, attest a policy or compliance control, prescribe one vendor, or authorize target testing. An adopting practice must bind its actual endpoint, virtualization, monitoring, identity, evidence, privacy, contract and incident rules.
