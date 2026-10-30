# 00.3 · Authority to test

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

Credentials, network access, a vulnerability report, or a request from an application team may make a test *possible*. None of them, on its own, makes the test *authorized*. This component gives a penetration-testing practice a way to show where its authority comes from, where it stops, and how someone outside the team can verify it.

**This is an adoption pattern, not permission.** The public framework cannot authorize any organization, tester, target, technique, tool, or physical entry. The adopting organization must record its actual policy/contractual authority and approve local program and engagement decisions through the roles that hold them.

## The decision in one view

An action is permitted only when it is inside **all** applicable boundaries:

> Actual program mandate ∩ authorized asset/engagement scope ∩ technique and consequence constraints ∩ current execution conditions.

The first boundary says the practice may exist and names the classes of work it may perform. The second says which assets and objectives are authorized *this time*. The third covers techniques and consequences that need distinct decisions—such as physical access, significant production impact, third-party systems, sensitive data, or autonomous tool action. The last covers the window, people, stop rules, and conditions still being true at execution.

No broad program statement makes an unlisted target in scope. No signed scope can grant a capability the program does not have. A team can have all the right tools and still be outside its authority.

## 1. Record the basis before writing the permission

A local authority record should point to the real source of each permission. Do not replace a missing source with a confident sentence in a template.

| Authority question | Local evidence to resolve | If unresolved |
|---|---|---|
| Who mandates and governs the practice? | Executive/policy delegation and accountable program role. | Leave the capability unapproved. |
| Who may authorize testing of this asset? | Ownership, contract, delegated control, and provider conditions. | Exclude the asset until confirmed. |
| Which testing actions are allowed at program level? | Approved capability classes, sanctioned tools/environments, policy exceptions or variations. | Do not infer permission from technical access. |
| Who decides special consequences? | Legal, privacy, safety, facilities, third-party, incident, data, and model/AI governance owners as applicable. | Hold that action, not necessarily every unrelated test. |
| How is authority kept current? | Effective date, review triggers, exception owner, revocation/stop process. | Treat stale or revoked authority as a stop condition. |

The practice may document an interface to another function's authority. It does not become the owner of that function's policy or decision by restating it.

## 2. Define the program envelope

A local program authorization should identify:

- the mission and accountable approving role;
- asset and engagement classes within the organization's actual authority;
- capability classes the practice may exercise, and classes explicitly excluded;
- qualified operators and sanctioned testing environments;
- conditions for credentials, data, evidence, disclosure, deconfliction, and retention;
- consequence triggers requiring additional decisions;
- an immediate stop and resumption path; and
- which local documents define *how* approved work is performed.

The envelope can cover web, API, mobile, infrastructure, network, database, cloud, wireless, source review, AI/LLM, or physical testing only to the extent each capability is actually approved and supported. This is a menu of possible domains, **not a claim that every practice provides them**. The method library does not itself enlarge the program envelope.

AI used *as a testing tool* and AI/LLM systems used *as targets* are different scope questions. An AI tool may introduce data egress, autonomy, model-risk, or action-boundary decisions even when the target is an ordinary web application. An AI target may require specialized tests even when the tester uses no AI tool. Each belongs in the applicable local authority and engagement rules; neither is automatically permitted because the framework has a component about it.

## 3. Authorize the engagement, not a vague intention

Before execution, the engagement record should let a tester and an independent verifier answer:

| Required decision | Minimum usable answer |
|---|---|
| Why test? | Objective and assessment type. |
| What exactly? | Target identifiers, ownership basis, identities/roles, environments, interfaces, and explicit exclusions. |
| What actions? | Permitted techniques and depth; prohibited or conditional actions. |
| When and by whom? | Authorized operators, window or start/stop conditions, trusted contacts. |
| With what? | Accounts, credentials, source access, testing infrastructure, tooling and data constraints. |
| How safely? | Availability, privacy, physical, third-party and production limits; deconfliction and emergency stop. |
| What happens to results? | Evidence handling, escalation, reporting, disclosure, retention, and closeout. |
| Who approved? | Actual authorized decision and date, including additional approvals where triggered. |

§10.1 (scoping) and §10.2 (rules of engagement) are separate working tools for this record. A completed form cannot be substituted for an approver's real authority. Scope change is a new decision, not a note added after the fact.

## 4. Attach extra decisions to the consequence

Some activities need a distinct owner or narrower conditions. Examples include disruptive or destructive techniques, sensitive/regulated data, shared or third-party environments, provider-specific terms, physical entry or confrontation, public disclosure, high-impact automated actions, or systems whose failure affects people or critical operations.

The additional decision belongs to the role with authority over that consequence. This does **not** mean every minor update to a testing method needs that role's approval. Record the trigger, decision, evidence, constraints, and expiration in the engagement package. If a planned action crosses the boundary during testing, pause that action until the record catches up.

Physical testing is a clear example: a general application-testing mandate is not permission to enter a facility. A per-site authorization and safety/confrontation plan are necessary for that mode. The physical method (§20.11) describes how to carry out work *after* those conditions are met.

## 5. Due care during execution

Approved work remains bounded after kickoff. A practical floor is:

1. Use the least-impact action that answers the test question.
2. Stop at the agreed proof depth; do not turn an incidental out-of-scope discovery into an exploit.
3. Minimize real data access and keep evidence in approved storage.
4. Use protected, attributable credentials and sanctioned testing environments.
5. Make defensive deconfliction possible without disabling legitimate incident response.
6. Escalate unexpected safety, availability, privacy, legal, or uncontrolled-impact conditions immediately.
7. Let the named stop authority pause work; resumption requires an explicit decision.
8. Use test access only for the approved objective, never personal benefit or unauthorized disclosure.

The local rules may be stricter. No sentence in this component overrides law, contract, provider terms, policy, or the engagement's signed constraints.

## 6. Make sanctioned activity verifiable

People outside the testing team need a safe verification route. A local authorization should identify a durable program contact or incident/deconfliction path, the engagement identifier, trusted coordination contacts, and what may be disclosed to a verifier. The answer should distinguish a confirmed sanctioned test from an unverified observation. If it cannot be confirmed promptly, responders should follow their own incident procedures; the tester should not demand that an observer ignore suspicious activity.

Keep the program authority, engagement authorization, scope changes, additional decisions, stop/resume record, and completed evidence traceable under the adopter's access and retention rules. “Auditable” means the records can support a review; it is not a promise that a document alone proves compliant operation.

## Two quick cases

**In scope, but not yet permitted:** The agreed API target exposes an adjacent production tenant. The tester can reach it using the same account. The tenant is absent from the signed target list. The tester records the discovery and seeks a scope decision; access does not extend authority.

**Program-approved capability, extra decision still needed:** The practice is authorized to perform physical security assessments. A covert entry at a particular facility has no per-site authorization or confrontation/safety plan. The team can continue unrelated authorized testing, but cannot start that physical action.

## Adoption and interfaces

To use this component, fill the authority-basis table with local evidence, write the program envelope, bind an engagement authorization and RoE, name consequence owners and stop authority, and test the verification route before a live exercise. Then check that the actual method (§20.1 and applicable domain guide), scoping documents (§10.1–10.4), credential and OpSec guides (§30.3–30.4), records guide (§30.1), and disclosure process (§50.1) neither assume more permission nor omit a necessary restriction.

The useful result is not a longer authorization letter. It is a short chain of decisions that a tester can follow and another person can challenge.
