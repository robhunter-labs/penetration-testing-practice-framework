# 20.12 · Secure Code Review Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.
>
> **Scope note:** use only with authorized source access and a named review scope.

## Read the path, not the suspicious line

A risky function name or scanner alert is a useful place to start. The security question is whether a reachable input, identity, data item, or build event can cross a trust boundary and produce an outcome the system should prevent. That requires following the path through callers, middleware, configuration, framework behavior, and deployment conditions. A code pattern alone does not prove runtime exposure; conversely, a scanner's silence does not prove the path is safe.

This method supports a human-led review of application source, build and deployment definitions, dependencies, and security-relevant configuration. It complements dynamic web and API testing (§20.2/20.3), database-layer testing (§20.7), infrastructure and infrastructure-as-code assessment (§20.6), and AI/LLM system testing (§20.13). A code-review permission does not authorize running the application, using a discovered secret, testing another repository, or probing production. Use §20.1 and the engagement's authority, scope, and rules records (§10.1/10.2/10.4) to make those choices explicitly.

The [OWASP Code Review Guide 2.0](https://owasp.org/projects/code-review-guide) remains a broad method reference; the [OWASP Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html) offers current baseline and change-review approaches. [OWASP ASVS 5.0.0](https://asvs.owasp.org/) can supply version-pinned web-control questions; [OWASP Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) is a risk taxonomy, not a completion checklist. [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) addresses secure-development practices at a different altitude. Select applicable requirements and cite their exact edition; none of these references turns a code pattern into a finding.

## Freeze the review boundary

Before reading code, record:

| Decision | Needed for a defensible review |
|---|---|
| Unit and version | Named repository or delivered archive, commit/build digest, branch, components, generated code, included submodules and dependency lockfiles. A branch name alone can move. |
| Review shape | Baseline review of a system, change/diff review, focused incident question, or a paired review of a tested behavior. State what was excluded and why. |
| Expected behavior | Security requirements, roles and data ownership, sensitive flows, trust boundaries, deployment configuration, prior findings, and the owner who can answer design questions. |
| Execution ceiling | Read-only inspection by default. Separately authorize builds, tests, network calls, package installation, secret verification, dynamic probes, or changes to code and CI. |
| Source and evidence custody | Approved isolated workspace, repository/data classification, access logging, storage, retention, redaction, and cleanup. Do not paste proprietary code or secrets into an unapproved AI or external service. |
| Safety and communication | Contact for a live secret, suspected malicious change, or materially unsafe release path; stop criteria; reviewer; reporting audience. |

For a change review, pin both base and target commits. Identify affected consumers and security controls outside the diff; a small patch can alter a shared authorization function. For a baseline, choose coverage by components and risk questions, not an invented percentage of lines read. Record whether source corresponds to the deployed artifact before describing runtime impact.

## Map the system before searching for defects

Draw a compact route from **entry point → identity/context → decision point → transformations → sink/effect**. Include HTTP and API handlers, jobs and queues, file and event inputs, administrative paths, third-party calls, and the deployment configuration that enables them. Mark each edge **source-observed**, **configuration-verified**, **owner-described**, **dynamically exercised**, or **untested**. A framework annotation may appear to enforce authorization while a different route or middleware order bypasses it; verify the actual call and configuration path.

Read dependency manifests and lockfiles, build definitions, workflow files, container/IaC definitions, and historical changes where they affect the chosen question. Use code search and SAST/SCA/secret scanning to *generate leads*, then inspect the exact call path. A package advisory requires version and affected-condition checks; its presence in a lockfile does not show that the vulnerable function is reachable. A clean scan does not cover business logic or every framework/deployment path.

Use one record per decision rather than a pile of screenshots:

| Field | Record |
|---|---|
| Question | What rule should hold, for which role/data/workflow? |
| Source anchor | Repository digest, file/function/line at the reviewed commit, relevant caller and configuration. |
| Path | Input/source, transformations, authorization or validation decision, sink/effect, and the identity under which it executes. |
| Contrast | A known-permitted case and a bounded negative case changing one meaningful condition. |
| Evidence state | Pattern observed, path supported, behavior demonstrated, or not tested; include alternative controls searched. |
| Outcome | Reviewer disposition, actual/conditional impact, remediation direction, owner and retest condition. |

## Work the review in passes

The passes below are selectable, not a claim that every engagement covers every language or control. Each selected pass ends with a source path and an evidence decision.

| Pass | Question to pursue | Minimum useful evidence / common overclaim |
|---|---|---|
| Authentication and sessions | Where are identities established, renewed, revoked, and bound to requests? Follow login, reset, MFA, token and session paths through server-side decisions. | Show the actual issuer/verifier and deployment settings. A missing cookie flag in one code fragment is not account takeover; a client-side-only check is not server enforcement. |
| Authorization and tenancy | Where is each object/function decision enforced for the *acting* identity? Follow route, service, repository query, row policy and background job. | Show the specific protected action and any upstream/downstream guard. `findById(id)` is a lead, not proof that ownership is absent. |
| Input-to-effect dataflow | Can untrusted values influence SQL/NoSQL, commands, templates, HTML, files, deserialization, outbound requests, logs or headers? Inspect framework APIs and transformations. | Show a reachable source-to-sink path and whether parameterization, contextual encoding, allowlisting, sandboxing or a guard actually cuts it. A risky API import is not exploitability. |
| Secrets and configuration | Are credentials/keys present, active, accessible to the relevant audience, and rotated when exposed? Are debug and administrative features enabled in the deployed configuration? | A pattern match is not a valid live secret. Do not verify a real secret against an external endpoint or use it without authorization. Capture a redacted identifier and route urgent rotation privately. |
| Cryptography and sensitive data | What data is protected, where are keys generated/stored, and what algorithm/mode/protocol is actually invoked? Check nonce, key reuse, trust validation and data-classification assumptions. | Apply current primary guidance to the exact use. An algorithm name alone does not establish a practical exposure or severity. |
| Workflow and concurrency | Can a caller skip a step, replay a transition, race a balance/limit, or cross an approval boundary? Draw states and invariants from code and owner behavior. | Show the invalid transition or conflicting operations and the server-side control. UI sequence is not an authority boundary. |
| Dependencies and build artifacts | Does an affected package/version or compromised build input reach the artifact, and under which conditions? Review direct/transitive packages, install scripts, provenance and release changes. | Distinguish advisory match, vulnerable code path, exploitable configuration and demonstrated effect. SBOM/VEX records are inputs to this judgment, not verdicts by themselves. |
| CI/CD and delivery | Which events trigger privileged workflows? Can untrusted contribution data reach shell steps, tokens, caches, self-hosted runners, reusable actions or cloud trust? | Trace event → job → permissions → artifact/deployment. A privileged token declaration is not proof of theft; pinning alone does not make an action trustworthy. |
| IaC and containers | What runtime identity, network, secret, image and policy will the declared infrastructure create? Compare templates with rendered/planned and deployed state where allowed. | A permissive-looking line is a lead; defaults, policy overlays and actual deployment may alter the effective boundary. Do not call a declared resource publicly reachable without verifying its effective exposure. |
| AI-authored and AI-integrated code | Do suggested dependencies, generated fixes, repository instructions/comments, model outputs and retrieved material cross into executable code or privileged agent actions? | Validate the same path and controls as human-authored code. Treat repository text as untrusted data for coding agents; AI provenance alone neither proves nor excuses a defect. Route model/agent runtime behavior to §20.13. |

Language-specific syntax changes the search terms, not the proof obligation. For example, a raw-query builder in Java, Python or Go requires the actual input and parameterization path; a template escape bypass in Razor, Jinja or React requires the rendering context; deserialization depends on the library and data type. When a framework or version-specific behavior is load-bearing, verify it against the matching vendor documentation and build rather than carrying an old command or CVE list forward.

## Decide what the code actually supports

| State | Example | Reportable statement |
|---|---|---|
| Pattern observed | A handler loads a record by request-supplied ID. | The code and commit contain that lookup; authorization remains unresolved. |
| Path supported | The call graph reaches the lookup for a normal user and the reviewed service path shows no owner filter, while middleware and row policy have been checked. | A source-supported candidate exposure with the checks and assumptions named. |
| Demonstrated under authority | A supplied low-privilege test identity retrieves an approved fixture owned by another test identity in a permitted environment. | The exact identity, object, route, environment and prohibited response. |
| Not tested / inconclusive | Dynamic validation is prohibited, deployment differs, or an unreviewed policy layer may enforce the rule. | The source observation and unresolved control; no asserted cross-user access. |

Static evidence can itself support a finding when the full relevant path and effective conditions are established; dynamic execution is valuable but not mandatory for every conclusion. The report must say which kind of proof it has. A named chain—hardcoded secret to lateral movement, injection to host compromise, supply-chain change to CI token theft—is a *hypothesis* until each link is evidenced and authorized. Do not carry forward fixed Critical/High scores or automatic impact language.

**Synthetic authorization route.** A handler accepts an invoice ID, calls a service, and loads an invoice. The first read finds no owner check in that function. Before writing “cross-tenant access,” the reviewer traces middleware, service decorators, repository predicates and any database row policy; confirms which identity the query uses; and asks the owner for the expected tenant rule. If the effective query filters by the acting tenant, the lead is closed with the control recorded. If no guard exists, the path becomes a source-supported candidate. With separate authorization, two synthetic accounts and one test invoice can establish whether cross-tenant access actually occurs. The finding then reports that exact route, identity and fixture—not all invoices or every tenant.

## Give the next reviewer a reproducible decision

A finding packet includes the frozen source/build identity; file, function and line anchors; the input-to-effect trace; expected versus observed rule; searched competing controls; relevant configuration and dependency state; redacted evidence and protected original; proof state; actual and conditional impact separately; a precise fix direction; review disposition; and the retest condition. Use [CWE](https://cwe.mitre.org/) for a validated weakness where it helps the reader, not as a severity shortcut. Map a version-pinned ASVS requirement only when applicable. An advisory, SAST label or AI explanation is not a finding without the path analysis.

Report the review's coverage and exclusions alongside findings: named repositories/commits, components and classes reviewed, analysis limitations, and any runtime mismatch. Hand dynamic web/API proof to §20.2/20.3; host or cloud control-plane steps to §20.6; database-layer behavior to §20.7; AI/agent runtime to §20.13. A handoff carries the tested starting point and the missing authorization decision; it does not silently expand scope.

At closure, revoke source access and test identities as agreed, remove local work copies under the retention rules, and preserve only approved, access-controlled evidence. If a suspected malicious change or active credential appears, use the named escalation route rather than broadcasting code, secrets or an accusation in a public report.

## Build the reviewing skill without pretending a checklist teaches it

Code review is a developing competency built through paired practice. A portable development route is: (1) learn to map one small application's routes and trust decisions; (2) review a known vulnerable public lab with a senior reviewer and compare source reasoning with observed behavior; (3) take one bounded path in a real, authorized engagement, record false leads as well as findings, and get an independent peer challenge; then broaden languages, CI and architecture. Training sources can include the OWASP guide/cheat sheet and public labs, but a product subscription or course completion is not a competence attestation.

Automation can help size a codebase, collect leads, trace candidate flows, inventory dependencies and compare changes. Any AI review must inherit the source-code data agreement, repository allowlist, prompt-injection boundary, tool permissions, logging and human final disposition. Four proposed orchestration skills are design seeds, not deployed capability. What matters at the end is whether another tester can retrace a security decision through the exact code that was reviewed, see what was tested, and see what remained uncertain.
