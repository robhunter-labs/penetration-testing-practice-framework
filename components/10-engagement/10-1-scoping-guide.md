# 10.1 · Engagement Scoping Guide

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

What does “test the application” actually authorize a tester to examine? Usually, not enough is known to answer. An application name may conceal several environments, identities, workflows, providers, and data boundaries. This guide helps a practice lead, target owner, and tester turn that request into an exact, reviewable scope before execution.

This is an adaptable guide, not an approval to test or a universal minimum. The adopting organization supplies its own authority, signatories, legal and safety review, record system, and approvals. A reachable target is not an authorized target. An unanswered scope question is a decision still to make, not discretion transferred to the tester.

## The three decisions that must not blur

| Decision | Home | Reader should be able to answer |
|---|---|---|
| **What and why** | This scoping guide and the engagement's scope record | Which exact targets, workflows, identities, environments, and dependencies are included, excluded, or conditional? What question is the test meant to answer? |
| **How far and under what conditions** | §10.2, Rules of Engagement | Which techniques, data, windows, proof limits, contacts, stop conditions, and changes are authorized? |
| **How to test and judge** | §20.1 and the chosen domain method | Which hypotheses, test cases, evidence, review, and finding decisions answer the scoped question within the RoE? |

§00.3 sits behind all three as the program's authority model. §10.3 helps translate the scoped surface into method choice. None of these documents can enlarge the permission supplied by the actual authorized engagement record.

## Start with the decision, not an asset list

Begin the scoping conversation with the requester or risk owner, someone who knows the target's architecture and operations, and the testing representative. Add other owners when a boundary crosses teams or providers. Record:

1. **Purpose and relying decision.** What is the security question, why now, and who will use the answer? A release gate, exploratory assessment, retest, or focused control question may call for different coverage.
2. **Tester perspective.** Is the test outside-in, supplied-credential, code-assisted, transparent, physical, or a declared combination? What information and access will the tester actually receive?
3. **Coverage and effort.** What breadth and depth are intended, which scenarios matter, what specialist effort and time are needed, and what cannot be concluded if a prerequisite is missing?

Do not turn “we want everything” into an unbounded promise. Decompose it into decisions about surfaces and coverage, then show the owner the time, access, and consequence tradeoffs.

## Name the boundary at the resolution the question requires

The right unit of scope is the smallest unit whose change would alter authorization, test design, or the meaning of the result. A host or domain may be enough for one question and far too broad for another. Move from a named property to its components, then to the workflow and user context, then to relevant trust and dependency boundaries. These are *levels of resolution*, not a universal five-level maturity score or a required minimum for every engagement.

| Dimension | Scoping question | Example of a useful statement |
|---|---|---|
| Target and version | Which app, API, host, repository, device, facility, interface, build, or endpoint? | “Orders API v2, staging build 2.4, `GET /orders/{id}`” |
| Environment and location | Production or nonproduction? Which tenant, account, network, facility, or region? | “The staging tenant only; production excluded” |
| Workflow and state | Which user journey, transaction, control, or system state is at issue? | “Read an order belonging to a second synthetic customer” |
| Identity and privilege | Which roles, users, service accounts, devices, or agents are involved? | “Two separately issued customer test accounts” |
| Dependency and control | Which identity provider, data store, provider, gateway, tool, or downstream action may be reached? Who owns it? | “Shared identity provider is a dependency; payment provider is excluded” |
| Evidence question | What observation would answer the question? | “Whether a Tenant A account can obtain one Tenant B synthetic record” |

The final row defines the question and intended evidence, **not** permission to collect it. §10.2 binds the maximum permissible proof, permitted actions, data handling, and stop point.

### Show what is in, out, conditional, and untested

For each material scope object, record a status and its reason. `IN` means the object is covered by the authorized scope under the linked conditions; `OUT` means excluded; `CONDITIONAL` means it waits on a named prerequisite or approval. `UNTESTED` is a coverage outcome for an authorized object that was not examined, not an authorization category. Record it with a reason and report the limitation. Do not quietly treat unknown or reachable objects as `IN`.

Name likely misunderstandings explicitly: adjacent tenants, older versions, production, shared infrastructure, third-party systems, connected mobile or API surfaces, and discovered assets. A broad system label does not silently include all of its parts.

## Validate ownership and prerequisites

Before relying on a scope, establish who controls each target and dependency and who can grant or obtain any needed permission. Co-owned, outsourced, hosted, and shared services may require a separate party's decision. If ownership is unknown or contested, hold that object as conditional; the requester's enthusiasm does not settle the boundary.

List what the test needs to start: named target and version, stable environment, working identities and privilege levels, synthetic or approved data, interface or architecture information, safe test equipment, access path, monitoring/operational contacts, and any specialist or physical arrangements. Assign who provides each prerequisite and what changes if it does not arrive. A missing second tenant account, for example, may make a tenant-isolation objective unanswerable even if the API is reachable.

The scope may identify safety facts the target owner knows—fragile services, live data, shared tenants, operational dependencies, people who may be encountered. Transfer those into §10.2's binding conditions and stop/resume procedure. Do not leave a safety observation in a scope note and assume it became a RoE rule.

## Apply the boundary to different surfaces

- **Digital application or API:** Name version, environment, endpoints or workflows, user roles, data classes, connected components, and the business action being tested. A generic application name rarely carries the authorization or evidence boundary.
- **Cloud, infrastructure, or provider-owned service:** Distinguish owned resources from connected provider functions, account/tenant boundaries, and shared-control surfaces. Authorization from one party does not establish authorization from every party.
- **AI feature as a target:** Name the model-facing application, prompt and data surfaces, tools, retrieval sources, identity, and possible downstream actions. Testing an AI feature is not the same as authorizing the test team to use agentic tooling; the latter is a separate §10.2 decision.
- **Physical site:** Name each facility and authorized zone, the objective and phase (for example announced assessment or separately authorized covert exercise), people and safety boundaries, and components permitted for examination. A physical site is not simply another endpoint on a digital inventory. The RoE and physical method must carry facility-specific authority and stop mechanics.
- **Focused control or retest:** Name the original claim or finding, current build/configuration, exact control, identities, representative path, and what remains outside the narrower question. A retest of one instance does not become a new full-system assessment by implication.

These are prompts, not one-size-fits-all packages. The right scope depends on the question and the actual target.

## Handle change without improvising permission

When the tester finds an adjacent system, new identity, unexpected data class, changed build, or third-party path, record the minimum observation and stop the affected activity. The authorized owner can choose to revise the scope and RoE through the local approval path, with effects on time and effort made explicit, or keep the boundary and report the resulting limitation or follow-on question. Until that decision is recorded, the newly discovered object stays out of scope. Unaffected work may continue only if its existing authority and RoE still hold.

A change of **target or objective** is a scope question. A change of **technique, proof depth, data use, timing, or consequence** is a RoE question. Some discoveries affect both. The tester should not self-approve a wider boundary.

## What a usable scope record should leave behind

The adopting organization may use its own form or system, but a reviewer should be able to reconstruct:

- the objective, relying decision, tester perspective, and engagement/version identifiers;
- exact included, excluded, and conditional targets; environments, workflows, identities, dependencies, owners, and exclusions;
- assumptions, supplied access, prerequisites, timing/effort estimate, and unresolved decisions;
- the authorized decision record and linked current RoE, without confusing the scope with permission to test;
- requested coverage and intended outputs, including how untested objects and limits will be reported; and
- who decided a material change, when, and against which version.

The final report should say what was actually examined and what was not. “No findings” is not a statement about an untested path. Preserve the scope and change trail in the adopting organization's access-controlled, auditable record system under its own retention rule.

### A small example

“Test the orders API” is not yet a scope. A useful starting statement is: “In staging build 2.4, test whether a customer with a supplied Tenant A account can read one synthetic order owned by Tenant B through the v2 order retrieval workflow. Include the named v2 endpoint and both supplied identities. Exclude production, v1, the payment provider, and other tenant data. The product owner must confirm the target and identities; a separate RoE must authorize the technique, proof limit, test window, data handling, and stop path.”

If the second account never arrives, the tester can report that the central isolation question was not answered. The scope should make that limitation visible before someone treats a completed test as a complete answer.

## Adoption and limits

Use this guide to make boundary decisions explicit, not to claim conformance with a framework or evidence of an operating program. Its examples are synthetic and its terms are adaptable. Review the scope with the owner and tester before the window, and revisit it when the target, architecture, identity, ownership, or intended question changes. §10.2 is the operating-condition companion; §10.3 maps the decided scope to testing approaches. A local intake worksheet can collect these decisions, but the worksheet is not the decision itself.
