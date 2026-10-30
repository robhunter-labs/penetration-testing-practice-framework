# 20.5 · Network Penetration-Testing Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## What is the network test actually testing?

A reachable service is not necessarily a broken boundary, and an open route is not necessarily an authorized one. Network testing asks how a defined position can reach, identify, authenticate to, influence, or cross a particular network control—and what the evidence proves about that control. The aim is a defensible account of the *tested path*, not a port list with an enterprise-wide story attached.

Use this method with §20.1 (umbrella method), §10.1/10.2/10.4 (scope, rules and requirements), the adopter's evidence and reporting rules, and the appropriate safety controls for production. It covers external/perimeter and internal positions, network-device management and data planes, VPN, network protocols, transport protection, and bounded segmentation tests. Its neighbors are intentionally distinct: §20.10 tests network admission/control, §20.6 tests host and directory infrastructure, §20.9 wireless, §20.2 web applications, §20.3 APIs, and §20.7 databases. Discovering one of those surfaces does not add it to the authorization.

[NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) informs the planning, execution and analysis structure. [MITRE ATT&CK Enterprise](https://attack.mitre.org/) is a vocabulary for possible adversary behaviors, not proof that a chain occurred. If a PCI claim is needed, verify the current [PCI SSC standard and applicability](https://www.pcisecuritystandards.org/document_library/) for that engagement; this document does not itself attest to a PCI test or decide the applicable requirement.

## Fix the path and the stopping point first

The engagement record needs an explicit answer to each question before active traffic:

| Decision | Record that makes the test bounded |
|---|---|
| Authority and position | Owner, approved source and target addresses (IPv4 **and** IPv6 where present), environments, test window, identities, permitted test classes, and contacts. Distinguish external, internal, VPN and device-specific positions. |
| Expected boundary | Architecture and inventory current enough to identify perimeter, routing, segmentation, management, CDE or other regulated boundaries, and who can confirm expected reach. “Filtered” is a hypothesis until the expected rule is known. |
| Safety | Rate/concurrency limits, production monitoring and deconfliction, high-impact prohibited actions, stop and escalation route, and recovery plan. Name authorization separately for credential attacks, poisoning/relay, traffic interception, exploitation, routing changes and segmentation validation. |
| Data and evidence | Use of synthetic or approved accounts, sensitive-output handling, packet-capture scope, protected originals, redacted reporting copy, retention and cleanup. Never upload captured credentials, configuration or packet data to an unapproved service. |
| Coverage limit | What is unavailable: missing subnet or source position, unknown policy, unissued credential, unobserved IPv6, device ownership, or a service excluded by the rules. A limited vantage point limits the conclusion. |

The tester first verifies the actual source position and a benign positive control. Capture source IP, route/egress context, time, target identity and expected result; coordinate monitoring as required. Start with the least disruptive discovery adequate to confirm reach. Scanner coverage, packet capture and protocol probes are selected and throttled against the real environment; they do not start simply because a tool is installed. A bridged rig or on-segment capture is a separate access and safety decision. Rig readiness is addressed by §40.1/40.3/40.10; it is not engagement authority.

## Build a network coverage map, not just a scanner output

For each in-scope position, inventory observed hosts, TCP/UDP services, device roles, management interfaces, VPN endpoints, name services, routing/segmentation boundaries, and transport choices. Compare with supplied diagrams and expected access rules. Mark **observed**, **documented but untested**, **in scope but unreachable**, **excluded**, and **ownership unknown** separately. Record when a banner or version is inferred rather than verified.

Use a compact row per boundary decision:

| Field | Minimum useful record |
|---|---|
| Path | Source position and identity → destination and service; IPv4/IPv6, time and environment. |
| Expected control | Who supplied the intended reach/authentication/configuration rule and how current it is. |
| Contrast | Allowed path or known-good response, then one bounded negative or boundary case. |
| Observation | Packet/protocol response, authenticated result or configuration evidence—not a tool label alone. |
| Decision | Confirmed effect, alternative explanation, untested extent, reviewer and any new authorization needed. |

## Select the test families that fit that map

| Family | Bounded question | Evidence that changes the answer |
|---|---|---|
| Perimeter and management planes | Is a management or exposed network service reachable and protected as expected from this source? Does a verified device build match a relevant advisory? | Reachability plus intended policy, authentication behavior or corroborated vulnerable configuration. An exposed login or banner alone does not prove device control. |
| Service and protocol posture | Are SMB/NTLM, LDAP, DNS, SNMP, NTP, routing and other in-scope services configured against the intended trust boundary? | Specific protocol response/configuration and its consequence for an authorized path. A protocol being enabled is not automatically a finding. |
| VPN and remote access | Which client/identity/device posture controls the approved remote position? Is the negotiated transport and session behavior as designed? | A safe, issued-identity contrast or corroborated configuration. A historical CVE or a weak-looking option needs an affected build and applicable context. |
| Name resolution and directory relay conditions | Do fallback resolution, signing and channel-binding controls create a plausible relay/capture path? | Distinguish posture, safely observed authentication, a demonstrated relay, and directory impact. These are different evidence states. Active poisoning/coercion/relay needs express rules and a stop path. |
| Firewall, ACL and segmentation | Can the authorized source cross a boundary the owner expected to deny? | Expected rule, both source and destination, observed service behavior and a control path. “Open port” without the policy is not a segmentation failure; a CDE conclusion needs the approved CDE boundary. |
| Device configuration and management | Do approved white-box configurations or bounded probes reveal unsafe management access, SNMP write, route or ACL behavior? | Configuration plus permission and effect. Do not change a production route, ACL or device configuration to demonstrate a potential outcome without separate authorization. |
| Transport and encryption | Do SSH, TLS, IPsec or other relevant protocols protect this data and client path as required? | Actual negotiation/configuration, exposure and policy. A cipher list alone is not a universal risk score. |
| Scanner candidate validation | Is the component/weakness present, reachable and exploitable within the approved ceiling? | Verified version/configuration, vendor advisory or safe reproduction, and an alternative-explanation check. Scanner severity is a triage cue, not the final finding. |

Modern environments add branches the older network checklist will not settle by itself: IPv6 control-plane behavior; AD CS and other directory enrollment/relay surfaces; software deployment systems; HTTP/2, HTTP/3 and QUIC at the edge; cloud and container networking; zero-trust access brokers; out-of-band management; and time/routing control planes. Select a branch only when the approved architecture exposes it, then route to the specialist method or an explicit scope extension. Operational technology or safety-sensitive systems require their own authorization and safety design; proximity on a network diagram is not permission.

## From primitive to demonstrated impact

The chain families include perimeter devices, relay, name-resolution poisoning, VPN, SNMP, DNS, ACLs, component vulnerabilities and protocol injection. IPv6, AD-CS and other relevant branches may also matter. A family is a hypothesis to test, not a prewritten finding. Use three evidence states:

1. **Observed:** an approved source reached a specified service, a control posture was read, or a safe test action produced an actual response. Preserve exact configuration, vantage point, time and limits.
2. **Supported inference:** the observed posture makes a follow-on path plausible under stated preconditions. Name the missing step and alternatives. For example, signing posture alone does not establish a successful relay, and a zone transfer does not establish interception.
3. **Not tested:** the path would require credential use, a new host, another method, disruption, data access or config change not authorized in this engagement. Route it to the owner rather than writing the imagined final step as fact.

**Synthetic boundary example.** From an approved non-CDE test segment, the tester reaches one service address documented as denied by a current segmentation rule. A second allowed path and a packet/response trace rule out a mistaken source position. The report can say the tested source reached that service under those conditions. It cannot say “the CDE is compromised,” that all non-CDE networks can reach it, or that a reachable service contains sensitive records. If the expected rule was never confirmed, this is a policy question or coverage note before it is a finding.

Some source chain text calls all adjacent systems “brought into scope” and assigns Critical/High from a primitive. That is not the rule here. Technical reach can suggest impact or a next question; only written authority changes assessment scope. Severity follows demonstrated effect, exploit preconditions, exposure, business context and the adopter's scoring model. An ATT&CK mapping describes behavior, not a proof or rating.

## Handoff, report and close

A useful finding packet contains the expected boundary, exact source/destination and build, authorized procedure and positive control, authentic protected evidence, redacted recipient copy, observed effect, uncertainty, consequence with a bounded claim, remediation direction, reviewer disposition and retest condition. Where the work touches PCI or another obligation, map only the applicable requirement after the scope and evidence are checked. Distinguish an owner-confirmed policy exception from a control failure.

Refer host/AD exploitation to §20.6, admission and VLAN controls to §20.10, web/API behavior to §20.2/20.3, and database behavior to §20.7. Those are method handoffs, not automatic scope grants. Capture what was not tested and why. At close, reconcile temporary accounts, captured secrets, tool artifacts and any approved changes; verify restoration or owner acceptance rather than assuming cleanup because the test window ended.

Automation can help with bounded discovery, service inventory, version/advisory correlation and candidate sorting. It must carry the same source/target allowlist, traffic ceiling, credential custody, stop route, provenance and human finding disposition. Proposed orchestration and broader attack-class coverage require separate implementation and validation; this method does not establish either. Human authority remains especially important for poisoning, relay, exploitation, segmentation and production change.

The output of this method is a reviewable account of what one authorized network position could and could not establish. It is neither a certification nor a claim that a specific network passed every test family above.
