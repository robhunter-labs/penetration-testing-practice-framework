# 20.4 · Mobile Application Penetration-Testing Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## What this method covers

A mobile application is more than the app package. It runs on a device, stores and exchanges data, invokes platform capabilities, and calls backend services. An assessment must say which of those boundaries it actually examined. This method covers iOS and Android application binaries and runtime behavior, local data, authentication and sessions, network communication, platform interactions, code and resilience controls, and privacy. Backend API logic may be included when explicitly authorized; backend infrastructure, the operating system, and an AI model behind an in-app feature are separate targets.

Use the umbrella method (§20.1), the local scope and rules of engagement, and the API method (§20.3) where the app's authorized backend calls need deeper examination. §40.4 covers a safe mobile test environment; a rig being ready does not mean the application has been tested. [OWASP MASVS](https://mas.owasp.org/MASVS/) supplies control objectives, [MASTG](https://mas.owasp.org/MASTG/) supplies test techniques, [MASWE](https://mas.owasp.org/MASWE/) describes weaknesses, and [MAS Testing Profiles](https://mas.owasp.org/Profiles/) help select assurance depth. Record the specific versions and profile used for each engagement rather than treating a control map as proof of coverage.

## Set the boundaries before touching the app

| Decision | Record before testing |
|---|---|
| Platform and build | iOS, Android, or both; package identifier, signed build/version, distribution channel, environment, and whether debug/test and production behavior differ. Each platform is a distinct coverage claim. |
| Identities and data | Issued test accounts, roles, test objects, permitted personal/synthetic data, and credential custody. A second role or tenant is needed only if the authorized question requires it. |
| Device and tooling | Approved devices and OS versions, root/jailbreak/instrumentation permission, tool trust and network path, and restore or retirement plan. A bypass of a client protection is a test technique, not a finding by itself. |
| Backend boundary | Exactly which domains, APIs, and environments may be reached through the app. Do not follow an endpoint, credential, or discovered host into an unapproved target. |
| Safety and contact | Rate, concurrency, state-change, notification, stop, and incident-deconfliction rules; who can resolve a new exposure or shared-service dependency. |
| Evidence | Protected originals, redacted recipient copies, timestamps, app/device state, account context, access control, retention, and reviewer path. |

If a build, role, device, or backend prerequisite is absent, record the gap and defer that branch. A test environment guide may include organization-specific network exceptions, vendor rigs, and managed devices; adopters must substitute their own approved path rather than copying those details.

## Establish a repeatable test position

1. Confirm package identity and provenance, build hash/version, device/OS version, intended backend, issued account, and time. Keep package and device state tied to every evidence record.
2. Demonstrate one benign expected workflow. Check that the app reaches the intended environment and that any proxy or instrumentation captures what it claims to capture. Some traffic may evade a system proxy; absence from the proxy is not absence of traffic.
3. Establish a positive control for each identity or state you intend to compare. If client-side pinning, anti-tamper, or root detection prevents observation, record the limitation and obtain an approved test strategy. Do not weaken a production user's device or a live backend to make testing convenient.
4. Inventory package configuration, permissions/entitlements, exported or externally callable components, third-party SDKs, embedded endpoints and secrets, local data stores, and observed network operations. Separate static discovery from runtime observation and from a verified security failure.

## Choose tests by security decision

| Control area | Question and bounded comparison | Evidence and interpretation |
|---|---|---|
| Storage | After a permitted sensitive workflow, what remains in app storage, OS-protected storage, logs, caches, backup surfaces, clipboard, or snapshots? Compare before/after logout and device state with synthetic records. | Capture location, protection, data class, and who could access it under the stated attacker model. The mere presence of a token in a secure platform store is not automatically a flaw. |
| Cryptography | Is sensitive data protected with an appropriate platform primitive and key lifecycle, or is a hard-coded key or weak operation used for a security decision? | Show data and key location, operation, and consequence. A named algorithm alone does not establish exploitability. |
| Authentication/session | How do login, local unlock, biometric prompt, refresh, expiry, logout, and role changes affect server and device state? Compare approved identities and states. | Distinguish local UI gating from server authorization. Prove that a session or action remains usable when policy says it should not. |
| Network | Does the app validate its intended server and protect sensitive exchanges? Observe approved traffic under normal and controlled interception conditions. | Note client, OS, proxy, and certificate state. Pinning absence or bypassability alone is not equivalent to account takeover; demonstrate an actual trust failure and bounded impact. |
| Platform | Can another app or a crafted link invoke an exported component, deep link, URL scheme, WebView bridge, or pasteboard flow beyond the expected caller boundary? | Use an approved test app/link and synthetic object. Record caller, component, input, resulting action or data, and platform version. An exported component may be intentionally public. |
| Code/dependencies | Do debuggable settings, embedded credentials, parser behavior, or vulnerable SDKs create an exploitable path in this build? | Tie a package observation to reachability and a security decision. An SDK version or scanner label is a candidate, not a confirmed finding. |
| Resilience | If root/jailbreak, tamper, debugging, or hooking protection is required for the threat model, what happens when an authorized test device presents that condition? | Record the expected control and observed behavior. Bypassing a client control may only establish that the device owner can inspect their own app; assess consequences separately. |
| Privacy | Which data leave the app for first- and third-party endpoints, and is that aligned with the product's disclosed and approved behavior? | Capture data type, recipient, consent/state, and observed flow. Do not infer a regulatory violation from traffic alone. |

The eight groups are a coverage map, not a promise that one test per row suffices. Select relevant MASTG tests against the actual build and threat model; record tests attempted, not attempted, blocked, and inapplicable. A web-backed flow can require the web method; a backend authorization question can require §20.3. Neither is silently inherited from mobile coverage.

### One bounded mobile example: deep-link authorization

**Synthetic target:** an app opens a project detail screen from an external link. The engagement permits two test accounts, two synthetic projects, and a single approved test link on one test device.

1. Establish that Account A can open its own project through the normal app flow and record the app version, account, link, backend request, and response.
2. With Account B active, invoke the same link once for A's project. Keep device, build, and project fixed; observe both the screen and any backend call.
3. Ask whether the project is shared, whether the app switched accounts, whether the screen displayed stale cache, and whether the backend returned protected data or merely an error.
4. If policy forbids B's access and the app or backend exposes protected content, report the observed boundary and exact conditions. If only navigation occurs, or policy is unresolved, label the result accordingly. Do not enumerate project IDs or infer cross-tenant access.

This tests one link and identity relation; it does not establish general deep-link or API safety.

## Move from a primitive to an impact claim

| Observation to investigate | What must be established before a larger claim |
|---|---|
| Sensitive local data | Its sensitivity, persistence, access path, and attacker/device condition; a lost-device story is a hypothesis until those links are supported. |
| Interceptable traffic | An actual validation or confidentiality failure and exposure under an authorized network condition; do not equate pinning bypass with credential compromise. |
| Embedded secret | Whether it is sensitive, live, and grants an unauthorized capability; never use it outside scope. |
| Externally callable component | The permitted caller/action boundary and observed unauthorized effect. |
| Weak local gate or persistent token | Whether server-side authority survives or changes in a way the policy forbids. |

Mark each chain link **observed**, **inferred with basis**, or **possible but untested**. A backend or adjacent service relevant to impact does not become an authorized test target. Stop and seek a new scope decision where needed.

## Report and hand off

For each candidate: record build/device/OS, account and app state, target and backend environment, exact approved action, expected rule, observed behavior, time, evidence source, competing explanations, safety limits, impact ceiling, and retest condition. A screenshot can orient a reader; it does not replace reproducible conditions or a protected original. Map a confirmed result to MASVS/MASWE where useful, but do not derive severity from the category alone. Apply the adopter's current scoring and risk-context process; protect secrets and personal data in recipient copies.

Close the engagement with a coverage statement that separates iOS from Android and names omitted builds, identities, controls, backend paths, and device conditions. Record who accepted unresolved questions and where the evidence is retained. This method cannot attest that any real app or operational program has met it.

## Automation boundary

Package unpacking, manifest/entitlement inventory, endpoint discovery from observed traffic, and candidate secret/SDK/configuration checks can assist a tester. They do not establish identity policy, exploitability, privacy meaning, or report disposition. If automation is added, define its input, target boundary, data handling, stop conditions, output provenance, false-positive review, and human decision owner. Proposed orchestration remains future design, not a running registry or demonstrated capability.
