# 20.6 · Infrastructure Penetration-Testing Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## Reaching a host is where this method begins—not where the story ends

The network method asks which path is reachable. This method asks what an authorized identity or position can do *on the systems reached*: Windows and Unix-like hosts, directory and certificate services, remote administration, configuration management, virtualization, backups, and the host/control-plane edges of containers and cloud infrastructure. A graph may draw a path to a privileged identity; the test still has to establish which edges are real, which actions are allowed, and where to stop.

Use §20.1 as the umbrella method and the engagement's scoping and rules documents (§10.1/10.2/10.4). §20.5 owns network protocol and reach testing; §20.10 owns network admission controls. Web/API/database, wireless and physical testing route to §20.2/20.3/20.7/20.9/20.11. A network observation or a discovered directory trust is a handoff question, not an automatic grant to test a host, domain, tenant or forest.

[NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) provides a planning, execution and analysis reference. Select the applicable [CIS Benchmark](https://www.cisecurity.org/cis-benchmarks) or [Microsoft security baseline](https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10) for the actual product/build and the adopter's chosen configuration policy; a benchmark deviation is an investigation prompt, not automatically a penetration-test finding. [MITRE ATT&CK Enterprise](https://attack.mitre.org/) may label a demonstrated behavior, but a technique ID does not demonstrate that the behavior happened.

## Establish the permission and evidence boundary

Record these decisions before enumeration or on-host tooling:

| Decision | Required answer |
|---|---|
| Systems and positions | Named hosts, images, domains, forests, tenants, management consoles, backup systems and container/cloud environments; approved source positions and environments. A domain name in a graph does not authorize every member system. |
| Starting identity | Issued test accounts and privilege levels, owner-approved fixtures, credentials' permitted uses, and how to revoke or rotate them. Distinguish supplied access from captured access. |
| Action ceiling | Whether local privilege escalation, remote execution, credential recovery, password guessing, directory-object modification, certificate enrollment, trust traversal, backup restore, snapshot access, C2 and Tier-0 progression are allowed. “Infrastructure test” alone authorizes none of these by default. |
| Operational safety | Rate/load, test windows, SOC coordination, sensitive systems, prohibited data extraction, change/rollback authority, stop condition and live escalation contact. Production management systems may act on many hosts from one interface. |
| Custody and reporting | Protected originals, redacted derivatives, high-sensitivity secret/packet/directory artifacts, retention, reviewer, cleanup and owner-verified restoration. A public repository or general AI service is not an evidence store. |

Validate the starting position with a benign positive control, current host/build and identity. Use the approved rig from §40.1/40.3/40.10 and keep test accounts separate from personal/operator accounts. The rig's ability to execute a tool is not authority for that tool's action. Treat credential, directory and backup collection as separately scoped because their data reach can exceed the host being tested.

## Make a system map another tester could challenge

Inventory the approved host and management roles, operating systems/builds, services, local identities, directory objects and trusts, certificate authorities/templates, privileged group membership, configuration-management relationships, virtualization boundaries, backup repositories, and relevant container/cloud identities. Label each relationship **owner-documented**, **tool-observed**, **configuration-verified**, **exercised**, or **not tested**. Those labels prevent a diagram from laundering a possible path into a confirmed one.

Use one row per security decision, not one row per tool output:

| Field | Record |
|---|---|
| Starting state | Issued identity, machine/tenant, build, network position, approved object/fixture and time. |
| Expected rule | Who may administer, read a secret, change a group/GPO, enroll a certificate, restore a backup or manage a guest—and the owner/policy source for that expectation. |
| Safe contrast | Known-permitted action and a bounded negative case with one meaningful variable changed. |
| Observation | Actual permission, response, resulting state or protected configuration; provenance and alternatives checked. |
| Limit and handoff | Untested edge, action ceiling, reviewer decision, specialist route and permission required for the next step. |

## Select the infrastructure test families

| Family | Question worth testing | Evidence and ceiling |
|---|---|---|
| Windows host | Can a supplied low-privilege identity cross a local service, registry, file, task, token or admin boundary contrary to policy? | Current build, effective permissions, benign contrast and observed elevated action. Local-admin membership or an enumeration flag alone does not establish exploitable escalation. |
| Linux/Unix host | Do sudo, setuid/capabilities, scheduled jobs, key material, service units or file permissions permit an unintended change? | Effective policy and one bounded proof on an approved host; do not run a kernel exploit or modify production state merely because a candidate appears in a tool report. |
| Directory graph and ACLs | Does an issued identity hold an actionable right over a specific directory object or privileged route? | Graph edge plus current ACL/group/trust state; prove each permitted transition separately. A shortest path to a privileged group is a hypothesis, not possession of that privilege. |
| Kerberos and delegation | Do service-account, pre-authentication or delegation settings create an exploitable identity boundary in this environment? | Exact account, configuration and permitted result. Ticket requestability, an SPN, or an offline-crackable artifact does not itself prove a recovered password or impersonation. |
| Certificate services | Can an authorized requester obtain and use a certificate beyond intended identity/role from a specific template/CA configuration? | Enrollment rights, mapping/configuration and observed safe outcome. “ESC” labels and a discovery-tool warning need context; do not request a privileged certificate without separate approval. |
| Remote host services | Is SSH, RDP, WinRM or another approved admin path accessible and protected as expected for these identities? | Successful controlled authentication or a verified policy gap. Do not equate a listening service with compromise or run credential attacks outside the rules. |
| Configuration management and software deployment | Can a lower-trust identity change code, package, job, agent or policy delivered to a broader fleet? | Effective authorization, delivery boundary and a safe non-propagating fixture. Never let a test job roll to production targets by default. |
| Virtualization and backup | Can an identity manage hosts/guests, snapshots, restore jobs or repositories beyond its role? | Rights and bounded metadata/fixture proof; guest access, historical data reach and fleet impact remain untested until separately demonstrated and authorized. |
| Hybrid, cloud and containers | Does an on-prem identity, workload token, control-plane grant or management agent cross a tenant/cluster/cloud boundary unexpectedly? | Precise trust and effective permission in the named environment. Route deep cloud, Kubernetes and SaaS work to a scoped specialist plan; do not generalize one token to an entire tenant. |

For configuration checks, pair a benchmark or vendor baseline with the adopter's approved exception and the *actual* exploit or exposure question. A setting can be nonconforming yet safely compensated; a conforming setting can still be part of an unsafe path. Record both the baseline result and the penetration-test result instead of collapsing them.

## Walk the path only as far as the evidence and rules allow

Navigation families include local privilege escalation, directory graph paths, ACL abuse, trust relationships, Kerberos, remote services, configuration management, hypervisors, backups and certificate services. Hybrid identity, modern coercion and certificate paths, deployment systems, cloud and containers may also be relevant. These are ways to choose a test, not conclusions prewritten for a report.

| State | Example | Reportable claim |
|---|---|---|
| Observed | A supplied test user can read a specific directory object's access-control list or a backup job's metadata. | The exact object, identity, build, right and time. |
| Supported inference | That right appears to lead to a privileged group or broader backup repository access, subject to an untested condition. | A candidate attack path, the supporting edges and the missing proof; no asserted privilege or data access. |
| Demonstrated under authority | A benign approved object is modified by the lower-trust identity and the change produces the prohibited outcome. | The bounded effect and tested path; not every sibling object, host or domain. |
| Not tested | The next edge would require a Tier-0 identity, live credential extraction, cross-forest action or backup restore outside the agreed ceiling. | The limit and a request for a separately scoped decision. |

**Synthetic directory example.** A supplied ordinary account appears in a graph path to an administrative group through write access on a test group. First confirm the effective ACL on that *specific group*, the group's current relationship to the privileged role, and the owner's expected policy. If the rules permit a reversible test-group membership change, make it on the approved fixture and verify the resulting role boundary. If the real privileged group cannot be touched, stop at the confirmed ACL and mark final privilege acquisition **not tested**. A diagram screenshot is not proof of Domain Admin access.

High-reach systems deserve an especially short leash: directory Tier 0, certificate authorities, configuration/deployment servers, hypervisors and backup repositories can affect many systems or expose historical data. Keep proof at the least sensitive level that answers the question; higher-impact actions require named targets, an explicit stop point and an owner-approved recovery route. An adjacent system is not in scope merely because it is reachable, and neither a default Critical label nor a fleet-wide outcome follows from a single tested path.

## Report the system boundary, then close the loop

A finding packet includes expected versus observed behavior, tested identity/object/build, authentic evidence and protected original, alternative explanations, permitted reproduction steps, actual impact and limits, remediation direction, reviewer decision and retest condition. Cite a CIS or vendor control only when its exact edition/setting and applicability are verified; add ATT&CK labeling only for behavior established by evidence. Apply the adopter's scoring and contextual-priority model rather than assigning severity from a category, graph edge or tool label.

At handoff, route network protocol posture to §20.5; network admission to §20.10; database-resident behavior to §20.7; web/API behavior to §20.2/20.3; and physical-entry questions to §20.11. Preserve the authorized starting point and tested endpoint across methods. A plausible cross-method chain is still only as strong as its individually demonstrated links.

At closure, reconcile accounts, tokens, secrets, host artifacts, jobs, agent configuration, snapshots and any approved directory changes. Record owner-confirmed revocation or restoration; “the window ended” is not cleanup evidence. Where sensitive material was deliberately captured, record its custody, retention and rotation/notification route without embedding secrets in the public report.

Automation may help inventory, baseline comparison, candidate path analysis and bounded correlation. Proposed orchestration is not a deployed capability until implemented and verified. Every automated action still inherits the target allowlist, issued identity, data ceiling, stop path, logging and human finding disposition. Privilege progression, credential extraction, certificate abuse, backup restore and production management changes are not unattended defaults.

This method's useful output is an inspectable account of how an authorized identity interacted with a defined system boundary, what it proved, and what remains a question. It is not an attestation that a host, domain or infrastructure practice passed every family above.
