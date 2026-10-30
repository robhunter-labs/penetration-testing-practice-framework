# 20.7 · Database Penetration-Testing Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## The database is where reach turns into consequence

A network method asks whether a service is reachable; a web or API method asks what an application exposes. This method asks a narrower question: given an authorized identity or position *at the data tier*, what can actually be read, changed, executed, or carried off—and where does the evidence stop and the inference begin? Databases can concentrate sensitive data and privileged paths to hosts, peer instances, identity systems, and cloud services. A confirmed primitive may therefore matter beyond one instance, but each downstream step still has to be proved and authorized.

The scope is the database layer of relational engines, NoSQL stores, cloud-managed databases, data warehouses, vector/RAG stores, and the authentication and authorization that sit in front of them. Application-layer SQL/NoSQL injection reached through a web or API front end, host-OS hardening of the database server, network segmentation around it, and storage-layer backup security each belong to a sibling method and are handoffs, not automatic grants.

Use §20.1 as the umbrella method and the engagement's scoping and rules documents (§10.1/10.2/10.4). Route web and API injection to §20.2/20.3; host-OS, directory, backup and virtualization depth to §20.6; network reach and positioning to §20.5; network admission to §20.10. A reachable port, a discovered link, or a graph edge is a question for the next scope conversation — not permission to cross into another system.

Anchor configuration expectations to the applicable primary sources for the *actual* engine, build, and deployment, and to the adopter's own chosen policy:

- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) — planning, execution and analysis reference.
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) — select the benchmark that matches the real engine and version; a benchmark deviation is an investigation prompt, not automatically a penetration-test finding.
- [MITRE ATT&CK Enterprise](https://attack.mitre.org/) — vocabulary for a demonstrated behavior; a technique ID is not evidence that the behavior occurred.
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) (Database Security, SQL Injection Prevention, NoSQL Injection Prevention) — control references.
- [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) — primary source for current PCI DSS text where cardholder data is in scope; PCI applicability is conditional, confirmed against a real scope, never a generic compliance claim.

Verify versions, CVEs, benchmark editions, and framework currency at engagement time against the primary vendor and standards-body sources. This method deliberately does not carry a fixed CVE, tool-version, or benchmark-edition list; those go stale and are checked per engagement.

## Establish the permission and evidence boundary first

Record these decisions before discovery or any authenticated action. Each is a decision the owner makes, not a default the test assumes.

| Decision | Required answer |
|---|---|
| Targets and positions | Named instances, engines, versions, deployment model (on-prem / cloud-managed / hybrid / warehouse), and approved source positions (direct, VPN, jump host, in-cloud identity). A reachable endpoint or a linked instance discovered mid-test is not in scope by default. |
| Starting identity | Issued test credentials and their privilege levels (read-only app user, standard app user, DBA for white-box review, host-OS access when in scope), how each was provisioned, its permitted uses, and how to rotate or revoke it. Distinguish supplied access from access the test discovers or captures. |
| Action ceiling | Whether OS-command execution via a database primitive, credential/hash capture and relay, offline backup restore, outbound-mail abuse, cross-instance link traversal, cloud cross-service pivots, and password guessing are permitted. "Database test" alone authorizes none of these. |
| Data handling | Classification of data present (the adopter's own policy; regulated types such as health, financial, or cardholder data), whether production or test data, permitted sampling depth, and prohibited extraction. Prefer schema-level proof over record-level capture; record-level capture is a separate, owner-approved decision. |
| Operational safety | Rate and load limits, test windows, coordination with the data owner and security-operations team, change/rollback authority, the stop condition, and a live escalation contact. Assume authentication and queries may be logged and monitored; confirm, do not assert, what that monitoring covers. |
| Custody and reporting | Protected originals, redacted derivatives, handling of high-sensitivity artifacts (captured credentials, hashes, packet captures, backup contents), retention, reviewer, cleanup, and owner-verified restoration. A public repository or a general AI service is not an evidence store, and secrets never enter a report body. |

Validate the starting position with a benign positive control: confirm the engine, version, and identity you actually hold (`version`/`@@version`/`v$version`/`db.version()` or the engine equivalent), and what that identity can list and do, before any chain-forward step. The rig's ability to run a tool is not authority to use it; keep test accounts separate from personal and operator accounts; scope credential, backup, and packet collection separately because their data reach can exceed the instance under test.

## Database and platform boundaries

| In this method | Routed elsewhere |
|---|---|
| Relational engines (SQL Server, MySQL/MariaDB, Oracle, PostgreSQL) at the data tier | Application/API injection reaching a database → §20.2/20.3 |
| NoSQL and in-memory stores (MongoDB, Cassandra, CouchDB/Couchbase, Redis, Elasticsearch as a data store) | Database-server OS hardening and host pivots → §20.6 |
| Cloud-managed databases and warehouses (managed relational, document, key-value, and warehouse services across major clouds) | Network segmentation and reach to the database port → §20.5 |
| Vector / RAG stores (dedicated vector databases and vector extensions to relational, document, and search engines) | Network admission control → §20.10 |
| Database-layer authentication, authorization, encryption, auditing, links/replication, stored logic, and backups *as reachable from the data tier* | Storage-layer backup-file security and LLM/agent application behavior → §20.6 / §20.13, by handoff |

Platform differences are real and must be tested on the platform actually in scope: a managed service often removes host-OS access while adding a cloud control-plane and identity surface; a warehouse or vector store has its own auth, sharing, and query-injection surface. Do not generalize a finding from one engine or one deployment model to another.

## Map the data tier so another tester could challenge it

Inventory the approved instances, engines and versions, editions and patch levels, deployment model, authentication mechanisms, privileged principals and roles, links/replication relationships, stored procedures/triggers/extensions, backup destinations, and cloud identities attached to managed instances. Label each relationship **owner-documented**, **tool-observed**, **configuration-verified**, **exercised**, or **not tested**. Those labels stop a diagram from laundering a reachable path into a confirmed one.

Record one row per security decision, not one row per tool output:

| Field | Record |
|---|---|
| Starting state | Issued identity, instance, engine/version, principal context (app user / service account / DBA), network position, time. |
| Expected rule | Who may hold a privilege, run a built-in, read a sensitive table, traverse a link, restore a backup, or reach a connected service — and the owner/policy source for that expectation. |
| Safe contrast | A known-permitted action and a bounded negative case with one meaningful variable changed. |
| Observation | The actual permission, response, resulting state, or configuration; provenance captured and alternative explanations checked. |
| Limit and handoff | The untested edge, the action ceiling reached, the reviewer decision, the specialist route, and the permission required for the next step. |

## A safe test sequence

Work the sequence below; at each confirmed primitive, stop and interpret it with the evidence ladder before continuing. Describe the *question* each family tests and the *evidence* that would answer it; the exact commands, payloads, and exploitation tooling belong in the adopter's scoped specialist playbooks and rules, not in a portable method.

**1 — Reach and identity (per instance).** Confirm network reach to the approved database endpoint from an approved position; establish the session with the issued identity; capture engine, version, edition, and the principal context. Determine what the identity can list and which later families are viable from this position. If reach or auth fails, escalate the scope conversation rather than widening the attack surface.

**2 — Discovery.** Confirm the engine and version from the service itself, not only from an inventory record. Note default-port exposure and any unauthenticated-access condition. For managed and warehouse services, enumerate exposure and attached identities through the provider's read APIs within the issued identity's permissions.

**3 — Authentication and access control.** Test for default, blank, weak, or shared credentials against the engine's known default administrative accounts, within the agreed window and rate limits. Inventory principals, roles, and grants; identify superuser-equivalent privilege on accounts that should not hold it, orphaned or stale accounts, and application accounts carrying far more privilege than their function needs. Treat "a privilege exists" as a question about whether it is *excessive for this application's real function* — a business-context judgment, not a category verdict.

**4 — Transport and at-rest protection.** Determine whether connections are encrypted in transit and whether cleartext is accepted; whether at-rest encryption is configured for data the adopter classifies as sensitive; and whether weak authentication handshakes transmit credentials observably. Record the posture; a cleartext-accepting listener is an exposure to test against a real network position, not a proven interception.

**5 — Privileged execution and reach primitives.** Establish, for the identity actually held, whether the engine exposes OS-command execution, file read/write, outbound-mail, hash-capture (attacker-controlled path), or external-data-source primitives, and whether the current principal can invoke them. Confirming that a primitive *exists and is callable* is one claim; demonstrating its effect is a separate, ceiling-gated action requiring explicit authorization. Modern engines add machine-learning, external-table, job-scheduler, and extension surfaces with equivalent reach — enumerate against the actual engine version.

**6 — Links, replication, and connected instances.** Enumerate links, database links, foreign-data wrappers, and replication relationships. Identify the credential context each uses (static, pass-through, or impersonation) and whether it would grant higher privilege on the far side. A link is a candidate pivot and a scope question; traversing it is a separate authorization.

**7 — Stored logic and injection at the data tier.** Review stored procedures, triggers, and functions for dynamic SQL, second-order injection, privilege-escalation paths, and backdoor logic — a code-review judgment, not an automated verdict. For NoSQL and search stores, test operator and server-side-JavaScript injection surfaces where the engine permits them, distinguishing an application-tier flaw (handoff to §20.2/20.3) from a data-tier one.

**8 — Backups, auditing, and data exposure.** Assess whether backups are encrypted, access-controlled, and retained per policy, and whether a reachable backup would permit offline extraction — stated as a reachability-and-permission question, with any restore gated by the action ceiling. Assess whether sensitive operations and failed authentications are logged and forwarded. Discover sensitive data by metadata and classification where authorized, preferring schema-level proof.

**9 — Cloud-managed, warehouse, vector/RAG, and supply-chain surfaces.** For managed services, test public-exposure and firewall posture, identity-based auth and token handling, and whether an attached instance identity carries cross-service permissions broader than the database needs. For warehouses, test enforced multi-factor and network-policy posture on accounts. For vector/RAG stores, classify embeddings and indexes in light of their source data, linkage, retrieval behavior, reversibility, and the adopter's obligations; a vector-only label does not itself remove sensitivity. Test unauthenticated exposure, retrieval/corpus poisoning, and injection via retrieved content as distinct classes. Consider the engine's driver, extension, and backup-tool supply chain. Each of these is engine- and provider-specific and must be tested on the real platform.

## Evidence and interpretation

Every result is placed on this ladder before it reaches a report. The ladder is what separates a defensible database finding from an attack narrative the evidence does not support.

| State | Example | Reportable claim |
|---|---|---|
| Observed | The issued identity lists a sensitive table, or a system view shows an OS-command primitive is enabled and callable by the current principal. | The exact engine/version, identity, object or configuration, and time. |
| Supported inference | That primitive or privilege *appears* to enable host command execution, a cross-instance pivot, or offline data extraction, subject to an untested condition. | A candidate chain, the supporting edges, and the missing proof — with no asserted compromise, data access, or blast radius. |
| Demonstrated under authority | Within the action ceiling, a bounded benign action produces the prohibited outcome (e.g., a benign command returns execution context, or an approved fixture confirms a link's privilege). | The bounded effect and the tested path — not every sibling table, instance, or connected system. |
| Not tested | The next edge would require OS execution, credential relay, a backup restore, a cross-service cloud action, or production data extraction beyond the agreed ceiling. | The limit and a request for a separately scoped decision. |

Two disciplines ride on the ladder. First, *reachable is not authorized and not proven*: a connected system becomes part of the narrative as a hypothesis to test under the rules, not an automatic scope expansion or a fleet-wide outcome. Severity is the adopter's contextual scoring of demonstrated effect, not a fixed value read from a pattern table. Second, *absence of a signal is a claim too*: "no detection," "no logging," and "no SIEM alert" are findings only when the test actually confirmed them, not assumptions carried in from a chain template.

## Failure and stop conditions

Stop, and route to the owner or reviewer, when any of these occur:

- Reach, authentication, or the positive control cannot be established — escalate the scope conversation rather than widening the surface.
- A step would cross the action ceiling (OS execution, credential relay, backup restore, cross-service cloud pivot, production data extraction) without explicit authorization for that class.
- A primitive points at a system, instance, tenant, or account not named in scope — halt and surface it for a scoping decision.
- Sensitive or regulated data would be captured at record level, or a captured credential would be reused beyond its issued scope — stop and get an owner decision on handling.
- An action risks production availability or integrity (destructive statements, service restart, load beyond the agreed limit) — do not proceed on a database the owner relies on without named targets, an explicit stop point, and an approved recovery route.
- The evidence does not support the claim being drafted — downgrade it on the ladder rather than asserting it.

High-reach surfaces earn an especially short leash: a primitive that reaches the host or directory, a link that reaches a higher-trust instance, a backup that holds the whole dataset, and a managed-instance identity that reaches the cloud control plane can each affect far more than the database in front of you. Keep proof at the least sensitive level that answers the question.

## Reporting and handoffs

A finding packet records expected versus observed behavior; the tested identity, instance, engine/version, and time; authentic evidence and a protected original; alternative explanations considered; permitted reproduction steps; the actual demonstrated impact and its limits; a remediation direction that both removes the primitive and breaks the chain where the primitive cannot be fully removed; the reviewer decision; and the retest condition. Cite a CIS or vendor control only when its exact edition and setting and its applicability are verified; add an ATT&CK label only for behavior established by evidence; include a CVE only when the specific version's exposure is confirmed. Apply the adopter's scoring and contextual-priority model rather than assigning severity from a category, a chain template, or a tool label. Phrase findings as the real defect — privilege misalignment, not "users exist"; a confirmed missing patch, not "the version is old"; weak key storage, not "keys are stored externally."

At handoff, route cleanly and preserve the authorized start and tested endpoint across methods: application/API injection to §20.2/20.3; host-OS, directory, virtualization and backup depth to §20.6; network positioning and transport interception to §20.5; network admission to §20.10; outbound-mail-trust and phishing chains to the general method with data-owner coordination; LLM/agent behavior reachable from a vector/RAG store to §20.13. A plausible cross-method chain is only as strong as its individually demonstrated links.

At closure, reconcile every account, token, captured secret, staged artifact, link or configuration change, and any restored backup. Record owner-confirmed rotation or restoration; "the window ended" is not cleanup evidence. Where sensitive material was deliberately captured, record its custody, retention, and rotation or notification route without embedding it in the report.

Automation may help with inventory, benchmark comparison, encryption-state and privilege enumeration, unauthenticated-exposure detection, and candidate-chain analysis. Orchestration proposals are not deployed capabilities; any automated action still inherits the target allowlist, the issued identity, the data ceiling, the stop path, logging, and human disposition of every finding. Privilege progression, credential capture and relay, backup restore, and cross-service cloud actions are not unattended defaults.

## Synthetic worked example

*Illustrative only; not drawn from any engagement.*

A grey-box engagement issues a standard application account on a relational instance. Step 1 confirms reach, the account context, and the engine version. In step 3 the account's grants show it holds a server-level role well beyond read/write on its one application database. Step 5 shows, from a system configuration view, that an OS-command primitive is enabled and that this role could invoke it.

On the ladder, this is **observed** (the role, the enabled primitive) and a **supported inference** (the account *could* reach host command execution, which *could* reach the directory if the service account is privileged and domain-joined). It is not host compromise, and it is not "adjacent systems in scope." Reporting it as "command shell available → host → directory → enterprise" would assert three transitions the test has not earned.

The action ceiling permits a single bounded, benign execution to confirm the primitive but prohibits host tooling, credential capture, and any directory action. The tester runs the one benign command on the approved target, captures the returned execution context as **demonstrated under authority**, and marks host enumeration, credential extraction, and lateral movement **not tested**, with a request for a separately scoped decision if the owner wants the chain proven further. The finding is written as a privilege-and-primitive misconfiguration with a demonstrated execution context and an explicitly bounded impact — the application account should not hold that role, and the primitive should not be callable from it — scored by the adopter's own model, with the untested downstream edges named rather than claimed.

## What this method is, and is not

The useful output is an inspectable account of how an authorized identity interacted with a defined data-tier boundary: what it proved, under what rules, and what remains a question for the next scoped step. This method is not an exploit command sheet, a compliance attestation, evidence that any live engagement used it, or a statement that a database "passed" every family above.
