# 10.3 · Methodology-to-Scoping Map

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## Reader headlines

**Primary audience:** Engagement leads, scopers, testers, technical reviewers, and adopters who need to translate an authorized testing objective into enforceable scope and rules-of-engagement inputs.

**Objective:** Prevent scoping from becoming a shallow asset count by showing which target objects, identities, trust boundaries, invariants, prerequisites, constraints, and evidence expectations each testing surface brings into the engagement.

**Intended outcome:** A scoper can select the relevant target surfaces, pull the right questions from the umbrella and domain methods, incorporate threat-model outputs, and produce scope that supports safe execution and honest coverage without importing a local tool, rig, depth label, or effort formula.

**This document defines:** The scoping route, common pull-points, surface map, overlays and scoped-subset pattern, effort drivers, quality checks, adoption profile, and assurance evidence.

## Document administration

| Field | Detail |
|---|---|
| **Document** | 10.3 |
| **Type** | Reference map |
| **Maintainer** | Framework maintainers; an adopter names its own maintainer |
| **Local approval authority** | Defined by the adopting organization |
| **Review trigger** | At least annually and on material methodology, target-class, scoping, rules-of-engagement, evidence, safety, or effort-model change |

> [!CAUTION]
> This map does not authorize testing and does not replace a scope statement or rules of engagement. It exposes decisions that local authority must bind. A row is a prompt for target-specific judgment, not a promise of coverage or a universal effort estimate.

## Where this fits

§20.1 defines the common engagement method. §20.16, when adopted, produces boundaries, invariants, high-risk paths, hypotheses, test prerequisites, and expected evidence. This map translates those outputs and the applicable domain method into §10.1 scope and §10.2 rules-of-engagement inputs. §10.4 carries the corresponding intake questions. These ID links must be resolved against the released public register at integration; a named component is not automatically available or approved.

An adopter's scoping guide, intake form, scope statement, and rules-of-engagement record remain separate controlled objects. This map tells them what to pull; it does not prescribe their system or format.

## At a glance

Use the map in six moves:

1. Name the engagement objective and relying decision.
2. Select every target surface and overlay that materially changes authorization, technique, safety, or evidence.
3. Decompose each surface into enforceable scope objects and identity contexts.
4. Pull current trust boundaries, security invariants, high-risk paths, and uncertainty from §20.16 **if adopted and available**; otherwise capture these questions with a named qualified reviewer and record the method gap.
5. Bind prerequisites, permitted/prohibited actions, impact limits, stop conditions, and expected evidence into the rules of engagement.
6. Estimate effort using the factors in §7—not counts alone.

## 1. Purpose and scope

The methodology library is source material for scoping as well as execution. A well-written scope gives the method an authorized target, identities, boundaries, constraints, and evidence objective. A weak scope forces testers to invent those decisions during execution.

This map applies to penetration-testing engagements and bounded control assessments across the target surfaces below. It is intentionally generic: adopters may add or remove rows. Its table groups related prompts for scanning, but the actual scope and RoE should keep target object, identity, boundary, prerequisite, constraint, evidence, and effort as distinct decisions.

## 2. Working terms

This map is a decision aid, not an external mandate. Its prompts need local authority, scope, and rules of engagement before they govern a test.

| Term | Meaning |
|---|---|
| **Effort driver** | A condition that materially changes preparation, execution, evidence, review, or coordination effort. |
| **Overlay** | A condition such as production, regulated data, physical access, safety, third-party effect, or AI/agentic action that changes constraints across one or more target surfaces. |
| **Prerequisite** | Access, information, build, device, facility, account, data, environment, coordination, or capability required to perform the intended test. |
| **Scope object** | The smallest target unit that must be named or bounded because it changes authorization, technique, evidence, or coverage. |
| **Scoped-subset assessment** | An engagement that tests one control or property and only the surrounding target paths needed to evaluate it. |

**Decision states for each material object or path:** `IN` (authorized for the named conditions), `OUT` (explicitly excluded), `CONDITIONAL` (work waits on a named approval or prerequisite), or `UNTESTED` (in scope but not examined; report the reason and coverage limit). None of these states supplies authorization on its own. A scoping record should name the object, state, identity, environment, applicable condition, decision owner, and version/change reference. The adopter chooses the form and system of record.

## 3. Common pull-points

Every scoped surface should resolve these questions:

| Pull-point | Scope / RoE decision |
|---|---|
| Objective | What security decision will rely on the engagement? |
| Target identity | Which system, environment, version, location, build, account, endpoint, interface, workflow, or facility is included? |
| Perspective | Which attacker/tester starting position and supplied knowledge apply: outside with no account, supplied credentials/context, transparent design/code access, requirement-focused verification, or a declared combination? How does that change the objects and identities to list? |
| Identity contexts | Which user, role, service, workload, device, model, agent, or physical credential contexts are in scope? |
| Trust boundaries and invariants | Where does trust or authority change, and what security property should hold? |
| High-risk paths | Which attacker hypotheses or design concerns deserve explicit testing? |
| Dependencies | Which upstream, downstream, shared, provider, third-party, physical, or human systems affect the test? |
| Prerequisites | What access, data, documentation, accounts, builds, equipment, test environments, or coordination must exist? |
| Methods and constraints | Which techniques are permitted, prohibited, impact-limited, time-bound, monitored, or pre-authorized? |
| Evidence | What will be captured, protected, reviewed, retained, and used for finding or closure decisions? |
| Coverage and uncertainty | What cannot be tested, what assumptions remain, and how will the limitation be communicated? |
| Change triggers | What target, scope, authorization, or safety change requires re-scoping? |

## 4. Surface map

For each selected surface, consult the **released public register** for a current domain method and its status. A row here is a scoping prompt, not evidence that a corresponding guide is released or complete. If no usable domain guide exists, use the authorized umbrella method and a qualified subject-matter reviewer to derive the needed questions, mark the method gap and limits, and do not claim domain-method coverage. The examples below are prompts, not exhaustive taxonomies. The mobile row in particular is not a claim of a complete mobile method.

| Surface | Distinct scope objects | Important identities, boundaries, and invariants | Typical prerequisites and constraints | Material effort and evidence drivers |
|---|---|---|---|---|
| **Web application** | Application, host or route, environment, workflow, function, object, tenant | Anonymous/user/admin roles; browser/service/backend boundaries; object and function authorization; state and transaction integrity | URLs, accounts, workflows, test data, rate and production limits | Workflow and role interactions, tenant variation, client/server state, business logic, evidence of authorization contrast |
| **API and service** | API, version, endpoint, method, resource, event or message, calling context | Client/service/workload identities; gateway/service/data-store boundaries; object/function authorization; replay and sequencing | Interface description where available, auth flows, clients, accounts, sample data, rate/impact limits | Endpoint behavior diversity, identity contexts, asynchronous flows, downstream effects, request/response and state evidence |
| **Mobile application — method maturity must be checked** | Platform, app build, device state, local component, backend API, update path | User/device/app/platform/backend identities; local storage, IPC, signing, update and server trust | Installable build, devices or emulator authority, accounts, backend access, safe test data | Platform and build variants, device protections, reverse engineering, backend overlap, capture constraints |
| **Client / thick application** | Binary, build, process, plugin, local store, IPC, updater, backend | User/process/service identities; local privilege, IPC, update, signing and backend boundaries | Build, compatible host, symbols or code if provided, accounts, updater path | Packaging variants, native analysis depth, local privilege paths, update chain, runtime instrumentation |
| **Network and protocol** | Range, segment, host, interface, service, protocol, management plane | External/internal/admin/service identities; segmentation, routing, management and trust-zone boundaries | Authoritative ranges, exclusions, windows, monitoring, rate and disruption limits | Host/service diversity, reachability, segmentation paths, protocol state, production sensitivity, packet and service evidence |
| **Infrastructure, cloud, container, and identity** | Host, cluster, account, subscription, project, tenant, directory, role, workload, image, control plane | Human/workload/provider identities; tenant, account, management/data plane, secret, role and federation boundaries | Inventories, architecture, test roles, provider coordination, console/API access, production limits | Role graph, inherited permissions, cross-account paths, ephemeral assets, shared responsibility, configuration and action evidence |
| **Database and data platform** | Instance, engine, database, schema, role, interface, replication or analytics path | User/service/admin identities; application/database, tenant, replication and backup boundaries; row/object authorization | Engine/version, connection paths, test accounts/data, backup and safety constraints | Engine diversity, privilege models, data sensitivity, linked services, destructive-query limits, query and state evidence |
| **Wireless, radio, and device network** | Site, network identifier, protocol, controller, access point, device, pairing or onboarding path | User/device/network/admin identities; air/edge/core, pairing and physical proximity boundaries | Location access, equipment, spectrum/safety rules, coordination, permitted impersonation or interference | Physical location, protocol variants, environmental noise, equipment setup, disruption risk, over-air and backend evidence |
| **Network access control (NAC)** | Enforcement point, authentication/posture path, admitted segment, exception or fallback state | Device/user identity; 802.1X or other admission path; policy decision versus actual network access | Named test segment, supplied device identities, coordination with network operations, safe bypass/lockout limits | Policy branches, device states, segmentation contrasts, change risk, and evidence of the resulting access |
| **Physical security** | Facility, perimeter, entry path, area, barrier, credential, guard or process; announced audit versus covert test as distinct phases | Person/credential/escort identities; public/restricted/high-security areas; time, tailgating and process invariants | Written per-facility authority, dates, locations, safety, contacts, tenant/owner permission, prohibited entry methods, response coordination | Sites and paths, the chosen phase(s), observation periods, safety and legal constraints, physical and witness evidence |
| **Source code review** | Repository, branch, component, language, dependency, review boundary | Developer/reviewer/service identities; source/dependency trust; secret and integrity boundaries | Repository access, build instructions where relevant, dependency data, permitted execution | Codebase diversity and size, generated code, dependency graph, trace from a code condition to an authorized consequence |
| **AI, ML, retrieval, and agentic system** | Model or endpoint, prompt/policy, application boundary, dataset, retrieval store, memory, agent, tool, connector, downstream action | User/model/agent/tool/workload/provider identities; prompt, retrieval, memory, data, tool, human and action boundaries; authority and output-trust invariants | Exact capability posture, test identities/data, provider terms, cost/rate limits, tool sandbox, egress, human stop and validation | Composition and autonomy, nondeterminism, tool/action consequence, data/provider boundaries, repeatability, trajectory and contrast evidence |
| **Control assessment** | Named control, enforcement point, protected path, bypass path, telemetry and response | Subject/control/target/operator identities; placement, alternate path and fail-open boundaries | Control owner, expected policy, authorized bypass techniques, monitoring, reset/rollback | Number and diversity of protected paths and bypass hypotheses, control state, observability, negative contrast |

**Scoped-subset pattern:** If the objective is one control rather than an entire application or network, name the control and its expected property, then identify only the enforcement point, representative protected path, plausible alternate path, identities, control state, and evidence needed to test that property. Make the broader host surface and untested paths explicit exclusions or limits. For example, a gateway-bypass assessment may need an authorized client, gateway policy, protected destination, one alternate route, and telemetry; it does not silently authorize a full internal network test. §10.2 must bind any bypass technique and stop condition.

## 5. Overlays

Overlays attach to selected surfaces and should be explicit in scope and rules of engagement.

| Overlay | Additional decisions |
|---|---|
| **Production or shared service** | Test window, monitoring, traffic and impact limits, deconfliction, stop, rollback, shared-tenant and third-party conditions |
| **Regulated or sensitive data** | Data minimization, approved test data, evidence handling, access, transfer, retention, masking and disclosure |
| **Safety or physical consequence** | Permitted actions, observers, emergency stop, excluded systems/areas, legal and safety authority |
| **Third-party or provider** | Ownership, contractual authority, shared-responsibility boundary, notification, prohibited actions, external communication |
| **AI used by tester** | Approved capability posture, autonomy, identities/tools, data/egress, evidence provenance, validation and stop under §90.1 |
| **Compliance or requirement-driven** | Exact requirement interpretation, evidence format, reliance boundary, assessor or customer expectations without overclaiming conformance |
| **Coordinated response** | Shortened decision window, live communications, incident or urgent-response boundary, evidence and disclosure path |

## 6. Threat-model pull-through

§20.16 outputs should enter scoping at the lowest effective object:

| Threat-model output | Scope / RoE pull-through |
|---|---|
| New target component or dependency | Add, exclude, or explicitly bound the affected scope object |
| Trust boundary | Name identities, paths, environments, providers, or physical locations on both sides |
| Security invariant | State the property the engagement is allowed and expected to test |
| High-risk attack path | Allocate method, prerequisite, identity, and evidence needed to examine it |
| Test exceeds current authority | Add a requested permission or record the path as untested; do not proceed implicitly |
| Destructive or consequential hypothesis | Define surrogate proof, pre-authorization, impact ceiling, stop, and cleanup |
| Evidence or contrast requirement | Ensure logging, accounts, test data, control state, and archival support the finding decision |
| Uncertainty or missing architecture | Add discovery time, stakeholder input, a conditional scope item, or an explicit limitation |

The full invariant-first method remains in §20.16. This map records only the decisions needed for the engagement boundary.

### Worked pull-through: one synthetic API question

A team wants to test whether two authorized test accounts can read only their own synthetic customer records. The API row turns “test the API” into a versioned endpoint and resource, two identity contexts, a named nonproduction environment, and an object-ownership invariant. §10.1 records those targets and exclusions. §10.2 adds the allowed request rate, supplied accounts, test-data handling, maximum proof depth, stop contact, and whether any downstream service is excluded. The selected API method then designs the contrasts and evidence. If the team cannot obtain the second account or establish record ownership, it narrows or conditions the test; the scope does not quietly promise an authorization conclusion it cannot support.

A source-code review does not automatically include build-pipeline testing; add those targets and authority explicitly if an adopter extends the work.

## 7. Effort model

Effort is estimated from the work needed to reach the intended evidence and review bar. Counts inform effort but do not determine it alone. Counts are inputs, not a formula.

Consider:

- number and diversity of scope objects;
- number and interaction of identity contexts and privilege levels;
- workflows, states, trust boundaries, and high-risk hypotheses;
- target and environment variability;
- setup, access, device, build, facility, provider, or data dependencies;
- production, safety, privacy, physical, disclosure, and third-party constraints;
- manual reasoning, reverse engineering, code review, or specialist knowledge;
- evidence capture, reproducibility, negative contrasts, and peer review;
- retest and cleanup expectations;
- uncertainty, architecture gaps, and coordination overhead; and
- AI/agent autonomy, nondeterminism, trajectory length, cost, and downstream action.

An adopter may use ranges, historical data, or calibrated models. Endpoint, host, line-of-code, role, model, or facility counts alone do not justify a deterministic effort or coverage claim.

Where prerequisites are missing, the estimate should distinguish discovery/setup from testing and narrow the coverage claim accordingly.

## 8. Scope quality checks

Before authorization, a reviewer should be able to answer:

- Can every target and exclusion be resolved by the tester and action point?
- Are environment, version/build, location, interfaces, workflows, identities, data, and third parties clear where they matter?
- Do selected domain methods and overlays match the target and objective?
- Are trust boundaries, invariants, and high-risk paths represented?
- Are required accounts, access, devices, builds, data, equipment, documentation, monitoring, and contacts available or conditionally stated?
- Are permitted and prohibited actions, impact limits, window, stop, cleanup, and change triggers explicit?
- Can the evidence plan support finding, coverage, and retest decisions?
- Are uncertainty and untested paths visible?
- Is effort justified by complexity and consequence rather than a convenient count?
- Does the scope remain inside local program authority?

A missing answer should be resolved, made conditional, or recorded as a limitation before relying on the intended coverage.

## 9. Adoption profile

An adopter needs to bind:

| Local binding | Adopter decision |
|---|---|
| Scoping roles and authority | Requester, engagement owner, tester, target owner, approver, safety and escalation roles |
| Scope and RoE records | System of record, required fields, signatures/approvals, change handling, and precedence |
| Local target taxonomy | Added, merged, or excluded surfaces and current domain-method resolvers |
| Required overlays | Conditions that automatically add production, data, safety, physical, provider, AI, or compliance treatment |
| Prerequisite and readiness checks | Minimum access, accounts, data, builds, equipment, monitoring, and evidence capability |
| Effort model | Historical inputs, estimating method, uncertainty treatment, and review cadence |
| Evidence and coverage | Required artifacts, limitation language, review, retention, and retest expectations |
| Re-scoping triggers | Material target, authority, data, environment, dependency, method, or safety changes |

## 10. Assurance evidence

Evidence that this map is operating may include:

- scopes that resolve to target objects and identity contexts;
- threat-model outputs that changed scope, prerequisites, or test design;
- rules of engagement that bind overlays and consequential techniques;
- estimates with recorded complexity, uncertainty, and actual effort;
- blocked or conditional work made visible before testing;
- coverage statements that match authorized and completed work;
- re-scoping records following material change; and
- lessons that improve a specific row or pull-point without adding unnecessary program-wide ceremony.

The presence of a completed scoping form is not sufficient evidence that the scope was technically usable.

## Adoption, review, and correction boundary

This map does not grant permission to test, certify coverage, or prescribe a universal depth or effort formula. Connect it to the public versions of §00.3 (authority), §20.1 (method), §10.1 (scope), §10.2 (rules of engagement), §10.4 (intake), the selected domain guide, and §20.16 (threat model) where adopted. If AI is used by the tester, also resolve §90.1's actual release status and local approval boundary. Recheck this map when a domain method, target class, safety constraint, or evidence expectation changes. The release package must provide a concrete correction/contribution route and the current ID resolver.
