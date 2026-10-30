# Tester Onboarding and Technical Readiness

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

Components in this framework are cited by section number and name. The adopting practice names a maintainer for this guide and reviews it when its testing image, tool baseline, access route, policy, or method changes; it also sets a periodic review interval.

A new tester can have an account, a laptop, and a tool list without being ready to conduct an authorized test. This guide connects those pieces: establish the operator's policy and access boundary, prepare a controlled testing environment, prove its tools and evidence paths work, then record what the tester can actually do. It covers technical readiness, not HR onboarding, every tactical method, or permission to test a particular target.

## Purpose and boundary

Use this guide when a tester joins a penetration-testing practice, changes operating environment, or takes over a testing surface. An onboarding lead and tester work through the record together; access and environment owners verify the parts they control. Adapt the paths, products, and evidence to the adopting organization.

**Roles to bind locally:** the onboarding lead coordinates the record and accepts rig-readiness evidence; access, endpoint, tool, records, and security-operations owners confirm their own systems; the engagement authority approves a particular test under its separate scope. One person may hold several roles, but the record must show which decision they made.

Three decisions must remain separate:

1. **Identity and policy:** the person may access the practice's approved systems and understands the applicable acceptable-use, data-handling, and escalation rules.
2. **Technical readiness:** the assigned environment, licensed tools, evidence storage, and network posture have passed a bounded check.
3. **Engagement authority:** a specific test still needs its own scope, rules of engagement, target access, and authorization. Passing onboarding never grants that authority.

Record the rig's readiness separately from specialist equipment and method training. A working web proxy does not demonstrate wireless-kit or database-method competence. This guide does not itself impose a hands-on qualification gate for every method; the relevant method and local role standard decide whether additional training or practice is required. A designated backup for specialist equipment does need an observed exercise (§6).

**Working terms:** a *fixture* is a tester-owned or isolated lab target explicitly designated for onboarding, never a production or third-party target; a *clean reference* is a restorable, checked rig state; a *method class* is a testing domain such as web, wireless, or database. *Engagement authority* is the separate permission to test named targets under agreed rules. In-band or *bridged* networking places the rig on a target-connected segment; network address translation (NAT) routes its traffic through another device and does not conceal it.

## 1. Bind the prerequisites before setup

| Needed before setup | Local owner to name | Evidence of readiness or reason to pause |
|---|---|---|
| Individual identity and approved access path | Identity/access owner | The tester can authenticate with their own account; no borrowed credentials. |
| Assigned host or remote workspace | Endpoint/virtualization owner | Asset or workspace assigned, baseline and support path identified. |
| Software and license route | Tool/IT owner | Approved source, entitlement, install authority, and exception route known. |
| Policies and data classification | Policy/security owner | Current rules accessible; required acknowledgment recorded. |
| Methods and secure evidence location | Practice/records owner | Current method set and controlled work/archival path accessible. |
| Escalation and monitoring contacts | Practice and security-operations owners | Scope, policy, tool, and incident questions have distinct routes. |

Keep engagement-specific credentials out of onboarding. They are issued only for an authorized engagement and returned, rotated, or revoked under its own closeout rules. Confirm required current policy acknowledgments **before** the tester begins rig setup. If any other prerequisite is missing, the onboarding lead decides whether a safe, unrelated setup step may proceed; record the gap and do not mark the dependent check as passed. No real engagement starts with an unresolved core prerequisite.

## 2. Choose an environment profile

Two common paths are a managed workstation running the testing environment and remote access to a separate managed host that runs it. Determine where execution actually occurs and which owner supports it; do not assume the access desktop provides the test environment.

| Decision | Managed local host | Remote or third-party path |
|---|---|---|
| Where does the testing environment execute? | On the assigned managed host if approved and capable. | On the approved remote execution host; the access desktop may be only a bridge. Verify actual virtualization support. |
| Who owns host software and updates? | Local endpoint/IT owner. | Name both the organization's and provider's owners; do not assume one controls the other. |
| Where can test data and snapshots reside? | Approved local or managed storage named in the evidence rule. | Approved remote storage; determine whether any data can reach provider endpoints or sync services. |
| What is the access teardown? | Individual accounts, host, tools, secrets, and assets. | Also remove jump/remote path, temporary tenancy, and vendor-specific accounts. |

Document the selected profile, asset/workspace ID, support owner, data boundary, and network path. A remote access channel is not itself the test rig. On a shared execution host, identify each tester's VM/reference state and storage, prevent cross-tester access to engagement evidence, and prove that one person's restore or cleanup cannot overwrite another person's work.

### Entry-to-exit register

Make the eventual teardown discoverable when access is granted, not only when someone leaves. Keep identifiers and evidence references in an access-controlled register; do not copy passwords, tokens, or sensitive personnel data into this template.

| Grant, asset, or duty | Assigned identity / custodian | Grant or issue owner | Evidence reference | Exit action and owner |
|---|---|---|---|---|
| Individual tool or repository account |  |  |  | Disable and verify removal. |
| Shared credential or token the tester could know |  |  |  | Rotate/revoke or record an owned exception. |
| Host, VM, remote path, or hardware key |  |  |  | Remove logical access; recover/transfer asset. |
| Engagement, review, consulting, or backup duty |  |  |  | Reassign and transfer necessary context. |

## 3. Build and verify the controlled rig

Use the current approved workstation standard and vendor documentation for installation details. This guide records the decisions and checks that survive product/version changes.

1. **Host baseline.** Confirm the assigned host is patched to the adopter's standard and its security controls are active. Install host software only through the authorized channel. If a needed tool is absent, route an exception; do not quietly install it from a personal download or another tester's media.
2. **Guest image and provenance.** Obtain the approved testing image from a trusted source, verify its integrity against that source, record its version and owner, apply required updates, and test login. Size CPU, memory, disk, and USB/peripheral access for the intended methods; fixed values in an old setup guide are not portable acceptance criteria. Freeze the tested baseline version after updates and re-run affected checks whenever it changes.
3. **Network posture.** Start from a locally approved low-exposure setting. Record whether the guest uses translation, a bridged network, or an isolated segment, and what traffic can leave it. A bridged or in-band setting is a deliberate, engagement-bound change with the right monitoring and authorization; reset it when the need ends. “NAT” does not mean traffic is private or unmonitored.
4. **Tool and license baseline.** Install only a versioned, approved baseline through the channel appropriate to the host or guest. Activate individual licenses under the assigned tester's identity and verify the feature actually needed; do not share license files. Add domain-specific tools only when the method and work require them. A failed license or missing tool is a recorded coverage limitation, not an invisible fallback.
5. **Evidence path.** Create an engagement-separated working location and prove that evidence can be saved, access-controlled, exported, and archived under the adopter's rules. Do not use personal cloud storage or copy sensitive evidence into this onboarding record.
6. **Clean reference state.** After the baseline checks pass, create a recoverable clean image or equivalent configuration reference. Record its identity, software state, storage owner, and restore test. Before each engagement, record material changes and capture the pre-test state if the local procedure calls for it. At closeout, capture any required final state, export and verify the actual evidence archive, then restore a clean state before the next unrelated engagement to prevent cross-engagement contamination. Refresh the baseline on the adopter's review cadence and after material tool/image changes; do not let an old snapshot silently become the standard. A snapshot is not an archive, and restoration is not proof that data was handled correctly.

**Equipment custody:** for shared or portable kit, record check-out against the engagement, who holds it, expected return condition, approved locked storage, and return inspection. For transport, use a custody record suited to the asset and data it contains. A remote or backup-tester handoff must transfer the asset record as well as the assignment.

### Tool baseline record

Keep one row per required tool or tool class. This is more durable than copying a one-time install command that silently pulls newer packages.

| Tool / purpose | Approved source and version or pin | Host or guest | License / owner | Verification that matters | Limitation or exception |
|---|---|---|---|---|---|
| Web interception proxy | Example only: adopter-approved vendor release `x.y`, digest recorded in local inventory | Guest | Individually assigned license; tool owner named locally | Launch, confirm the required feature, and save/reopen a synthetic project in the approved path. | If the feature or path fails, do not claim proxy readiness. |
| Network discovery utility |  |  |  | Confirm executable/version and run only a harmless local or approved fixture check. |  |
| Evidence/reporting client |  |  |  | Save and retrieve a synthetic artifact under the right access controls. |  |
| Method-specific tool |  |  |  | Verify the actual method-relevant feature against an authorized fixture. |  |

Do not use a tool's presence in a package list as proof that the tester can use it safely or that its method is in scope. Capture version, source, and the observed check. An update changes the baseline: review and re-run affected checks before treating it as the new reference.

## 4. Rehearse policy and monitoring boundaries

Have the tester explain the rules back in the context of real work, rather than treating a policy acknowledgment as comprehension. At minimum, walk through:

- An engagement credential is offered for another target: do not use it outside the signed scope; ask the engagement authority.
- A tool can collect more data than needed to demonstrate a weakness: stop at the authorized minimum and follow the evidence-handling method.
- A captured secret remains in the VM after closeout: report the exposure through the engagement finding/credential route, protect and rotate it under the local procedure, and remove unauthorized copies. Never copy the secret value into onboarding notes or this record.
- A new host tool is needed but is not approved: use the local request/exception path, not an unreviewed install.
- Personal browsing, email, or chat from a managed testing rig: follow the adopter's actual policy, not the assumption that a guest VM is a private device.
- An engagement detail is about to be shared outside authorized participants: apply need-to-know and the local data-handling rule.
- Testing traffic may appear to the security-operations team: name the engagement owner who coordinates the target range, testing window, source identity, pause/verify contact, and urgent escalation where the local process requires notification. After the test, offer a bounded detection-learning handoff without exposing unnecessary evidence. An isolated guest or encrypted connection does not make traffic invisible.
- A possible policy violation by oneself or another tester, or loss of sensitive evidence, occurs: stop the affected activity and report immediately through the local security/incident path. A product owner or scheduler is not automatically that path.

When permission is unclear, **ask before acting**. The practice should name who answers a technical-method question, who resolves a scope or authorization question, who owns policy interpretation, and who receives a security concern. The same person may fill more than one role in a small team, but the routes must remain distinct in the record. If AI-assisted tooling is part of the rig, its own tool/posture, data, autonomy, and human-review rules must be bound separately; ordinary rig readiness does not approve an AI tool for an engagement.

## 5. Run a day-one readiness check

Use an observed acceptance test, not an inventory of tools that merely ought to work. Adapt this record to the local environment and add method-specific checks where needed. A tester and onboarding lead sign only the state actually observed.

| Check | What to observe | Result | Evidence reference and verifier |
|---|---|---|---|
| Identity and approved host/remote route | Individual login works; host/workspace matches assignment. |  |  |
| Policy and support routes | Current required acknowledgments and distinct escalation routes are recorded before setup. |  |  |
| Guest integrity and updates | Approved image provenance/version, boot/login, patch state. |  |  |
| Network and monitoring | Starting mode, source identity, and owner-approved benign egress endpoint. Use a simple connection check, never discovery/scanning, for this item. |  |  |
| Tool baseline and licenses | Required capabilities launch and pass checks on the designated onboarding fixture. |  |  |
| Method documents and training | Current methods open; record separately any specialist training or practice the role requires. |  |  |
| Evidence and archive path | Synthetic file save, retrieve, access check, and handoff path work. |  |  |
| Clean reference and recovery | Reference captured and restore path checked without losing needed evidence. |  |  |
| Equipment custody | Issued assets and specialist kit recorded with storage/return owners. |  |  |
| Engagement authorization | **Not granted by this onboarding record.** A specific test needs its own approved scope and rules. | NOT GRANTED |  |

Mark each applicable core check **PASS**, **LIMITED** (name the restriction), **NOT RUN**, or **FAIL**. Full technical readiness for engagement work requires **PASS on every required core check**; LIMITED is a diagnostic state, not a relaxation of the gate. A narrower training or repair activity may proceed only under its own safe local authority, not as a real target test. Retest changed or failed rows after repair. The completion record states who observed each result, when, the version/profile tested, and the rig capabilities demonstrated. A separate engagement authorization still governs every real target.

## 6. Prove a backup can take over

For a specialist surface with only one regular operator, reading the method is not enough. Name a backup, give them supervised equipment time on a designated onboarding fixture, have them perform the setup and a bounded task, and record the result and gaps. Keep operations notes and kit custody current. Refresh the exercise after meaningful changes or before relying on the backup; the adopter sets cadence. If the regular operator is unavailable during a required test, the backup takes over only after their own readiness and the engagement's authority are checked, with equipment custody transferred in the record. A departure also triggers the separate offboarding route for the former operator's access.

## Example: access is working, readiness is not

**Fictional practice.** A tester can launch a managed testing environment. The proxy opens, but its licensed feature is unavailable and evidence export points to a personal sync folder. The onboarding record marks identity and guest boot **PASS**, tool capability and evidence path **FAIL**, and full technical readiness **NOT ACHIEVED**. The lead assigns an owner to correct the license and evidence path, then repeats both checks with a synthetic project on the designated onboarding fixture. No real target testing begins solely because the login and VM worked.

This example tests the distinction between access, capability, records, and engagement permission. It does not describe an actual contractor or an organization's deployed environment.

## Lifecycle handoff and adoption limits

Keep the entry inventory usable at exit: each identity grant, tool account, secret exposure, equipment item, and assigned duty needs a named removal or transfer action. §40.2 is the paired offboarding guide. The workstation standard (§40.3), method framework (§20.1), domain methods, evidence/archive guidance, and engagement authorization remain distinct consumers; this onboarding guide does not replace them.

An adopter must bind this template to actual policies, hardware, approved software channels, remote-access contracts, tool licenses, data-handling rules, monitoring agreements, role qualifications, and records. It does not certify a tester, attest compliance with an external standard, authorize live testing, or prove this template is in operational use.
