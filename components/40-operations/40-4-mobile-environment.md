# Mobile Application Test Environment — Guide

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A mobile test environment is not a pile of jailbreak tweaks and a proxy. It is a controlled, provenance-checked, reversible path from an authorized test to a defensible record: which device and operating system the work runs on, where the build came from, what the device is allowed to reach, how traffic is observed, which identities and data are in play, and how the rig is restored and accounted for when the work ends. This guide helps a practice specify, build, and verify that path for iOS and Android. It is an adaptable design and operating record, not a claim that one device model, operating-system version, jailbreak or root tool, instrumentation version, commercial platform, or network route is required, nor that any named organization has deployed it.

Two definitions used throughout. A *fixture* is a deliberately designated test target — an app build you are authorized to test, a synthetic account, a lab endpoint — never a production service or a third party's app or data. A *clean reference* is a tested, restorable device/tool state, not a copy of an engagement's evidence.

**Authorization comes first, and this guide cannot grant it.** Rooting or jailbreaking a device, trusting an interception certificate, bypassing a client-side control, and reaching a backend are test techniques that belong only to a device you own or are assigned and to a target inside a written scope and rules of engagement (§10.1/10.2/10.3). A ready rig is not permission to test anything, and — per the mobile method (§20.4) — a ready rig is not evidence that any application has been tested.

**Where this sits.** §20.4 is the mobile *method* (what to test and how to judge it); this document is the *environment* it runs on. §40.3 (workstation and field kit) and §40.10 (managed test rig) own the host and rig baseline; this guide covers the mobile-device-specific layer that sits on top of them. Resolve the exact public titles and links of adjacent documents at integration rather than assuming any candidate is released.

---

## 1. Choose the device posture deliberately

Name, per platform, who owns each test device, what it may reach, and how it returns to a clean state. Mobile rigs tend to accumulate: a device rooted for one engagement, a certificate trusted for another, an instrumentation server left running. Decide the posture before provisioning, and record it.

| Decision | Questions the adopter must settle | Evidence to retain |
|---|---|---|
| Device ownership and custody | Who owns each device? Who may provision, root/jailbreak, carry, wipe, and retire it? Is it segregated from any personal device? | Asset/assignment record, custodian, loss route. |
| Dedicated vs shared | Is a device dedicated to testing, or shared with other use? Is a device dedicated to a managed commercial platform vs. general instrumentation? | Device role record; separation rationale. |
| Managed vs. exception | Does the organization apply its normal mobile-device controls to the device, or is this a device-management exception? What compensates for each absent control? | Baseline, exception/risk decision, verifier. |
| Instrumentation model | Hands-on instrumentation (your own tooling) and/or a commercial managed mobile analysis platform? Each is a distinct provenance and trust decision. | Tooling inventory; platform instance owner. |
| Network path | How does the device reach the internet, the proxy/observation point, and any authorized test backend? | Tested network profile; egress identity; change/reversal rule. |
| Identities and data | Which issued test accounts, synthetic data, and credentials are permitted on the device? | Identity/data record; credential custodian. |
| Restore and retirement | How is the device returned to a clean reference, and retired at end of life? | Restore test; retirement/wipe route. |

A practice may use dedicated devices, a managed mobile analysis platform, hands-on tooling, cloud device labs, or a combination. None is the default required by this framework. The obligation is to make the choice and its evidence visible, and to keep every technique inside the device owner's authority and the engagement's scope.

For a device outside normal management, use one row per absent control. A compensating measure must supply an observable property; "the tester is careful" is not a measure. An unresolved material gap stays an exception with an owner, not a silent PASS.

| Normal control or property absent | Compensating design | How it is checked | Residual limit and decision owner |
|---|---|---|---|
|  |  |  |  |

## 2. The environment matrix — fill one row per device/platform build

This is the editable core of the rig. Record *outcomes and versions*, and pin each tool and operating-system choice to its official current source at adoption time (see §10), rather than relying on an old setup note. A blank field is a readiness gap, not a default.

| Field | iOS device A | Android device A | Device B `[ ]` |
|---|---|---|---|
| Device model and identifier | `[ ]` | `[ ]` | `[ ]` |
| OS version; signing/rollback constraint recorded (see §3) | `[ ]` | `[ ]` | `[ ]` |
| Device role (hands-on / managed platform / shared) | `[ ]` | `[ ]` | `[ ]` |
| Root/jailbreak state and tool + version (if authorized) | `[ ]` | `[ ]` | `[ ]` |
| Instrumentation server + version; host-side tool + version (matched) | `[ ]` | `[ ]` | `[ ]` |
| Interception CA: name, scope (device-only), install location | `[ ]` | `[ ]` | `[ ]` |
| Static-analysis tooling available (capability, see §5) | `[ ]` | `[ ]` | `[ ]` |
| Network path to internet / proxy / authorized backend (see §7) | `[ ]` | `[ ]` | `[ ]` |
| Test identities and data permitted on this device (see §8) | `[ ]` | `[ ]` | `[ ]` |
| Clean-reference snapshot/restore mechanism and owner (see §9) | `[ ]` | `[ ]` | `[ ]` |
| Date/trigger to re-evaluate this row | `[ ]` | `[ ]` | `[ ]` |

Host-side instrumentation tooling and the on-device instrumentation server generally must be version-compatible; a mismatch is a common and silent cause of a rig that "connects but does nothing." Record both versions and the observed compatibility check, not just that the tool is installed.

## 3. Device, operating-system, and build provenance

Before any trust decision, establish what the device and app actually are. Provenance is the difference between a defensible observation and an artifact of an unknown build on an unknown device.

- **Device identity.** Record the model, unique identifier, and whether the device is a dedicated fixture. Do not place engagement data on a device whose provenance or custody you cannot state.
- **Operating-system constraints.** iOS and Android each impose constraints on which OS versions can be installed or restored. A usable research position for a given version may exist only for a limited window; Android devices can also impose anti-rollback behavior. Record the device's actual constraint and current OS version, then check the official vendor source and research-tool support notes before changing either. Where a technique depends on a version that cannot be reacquired, consider a separately maintained device or another authorized test strategy.
- **Build provenance.** For each app under test, record the package identifier, signed build/version, distribution channel (store, enterprise/managed distribution, QA/test distribution), environment (production vs. test backend), and a build hash where available. Note whether a test/QA build behaves differently from production. Prefer a build whose exact identity you can confirm over "the latest" from a distribution portal.
- **Attestation / integrity posture.** Record whether the platform's device-integrity or app-attestation signal is in scope and how the authorized build responds to a research device. Treat platform integrity APIs as a moving target: name the control and observed behavior, and resolve the current API and its status from the official platform source rather than a dated checker or recipe.

## 4. Instrumentation, root, and jailbreak as a recorded, authorized capability

Dynamic instrumentation and (where authorized and necessary) root or jailbreak let a tester observe and manipulate an app's runtime on a device they control. Treat these as capabilities to record, not as commands to paste.

- **Keep this inside authority.** Root/jailbreak and client-control bypass are performed only on a device you own or are assigned, for an app and target inside the written scope. Never weaken a production user's device or a live service to make testing convenient.
- **Pin procedures to the current official source.** Jailbreak and root tooling, the on-device instrumentation server, and the host-side tools all version frequently and depend on device model, chip generation, and OS version. **This guide deliberately does not reproduce step-by-step root/jailbreak commands or version-specific recipes, which age badly and can brick a device.** Obtain the current procedure from the official project/vendor documentation for the specific tool and device at adoption time, and record the tool, version, and outcome in the §2 matrix.
- **Instrumentation server/tool compatibility.** Record the on-device server version and the host-side tool version and confirm they are compatible before relying on the rig (§2).
- **A bypass is a technique, not a finding.** Bypassing certificate pinning, root/jailbreak detection, or anti-tamper on your own authorized test device establishes a test *position*; it does not by itself establish a vulnerability. If the threat model requires the app's resilience controls to hold, record the expected control and the observed behavior, and assess consequences separately (this is §20.4's judgment, not the environment's).
- **Resilience / detection-evasion tooling.** Where an authorized engagement requires operating a research device against an app that checks for root/jailbreak or device integrity, the technique and its current tooling are domain-standard but fast-moving and platform-gated. Name the capability and the authorization; resolve the exact current tooling from official/community-maintained current sources at adoption time rather than a dated module or attestation-fix recipe. Do not present any one evasion tool or version as required or as universally effective.

## 5. Static and dynamic analysis tooling — capability, not a product list

Build the analysis toolset by *capability role*, and select products against the platform, the method, and current tool support — not by copying a named bundle.

| Capability role | What it supplies | Selection notes |
|---|---|---|
| Package unpacking / decompile (Android) | Manifest, resources, smali/bytecode, embedded strings and configuration | Multiple interoperable tools exist; pick current, maintained ones. `grep` over decompiled output is often faster than an in-tool search. |
| Decompiler/viewer (Android) | Side-by-side decompiled Java/bytecode views | Capability, not a specific version; confirm it loads your build. |
| iOS binary reverse engineering | Disassembly/decompilation of the app binary and resources | Production store binaries carry encryption/obfuscation; a QA/test build is usually the practical target. Commercial and trial tools exist; record which. |
| Dynamic instrumentation | Runtime hooking, method tracing, client-control bypass on an authorized device | Version-match on-device and host-side components (§2, §4). |
| Managed mobile analysis platform (optional) | A commercial, workflow-oriented static/dynamic platform with its own provisioning model | One option, not a requirement; it carries its own device-provisioning and trust constraints — record them. |
| Emulator / virtual device | Convenience for some static and reversing work | Decide whether a physical device is needed for the question; emulators may lack features (e.g., biometrics) or differ from device behavior. Note when a result depends on emulation. |
| Framework-specific extraction | Extracting assemblies/resources from cross-platform app frameworks for further static analysis | Framework packaging changes over time; use current extraction tooling and cite it in the record. |

Record the exact tools and versions used for an engagement in the §2 matrix. A tool being installed is not proof that its method-relevant feature works on your build; confirm against a fixture.

## 6. Proxy trust and interception — and its constraints

Observing an app's network traffic usually means routing it through an intercepting proxy and establishing certificate trust on the authorized test device. Record the setup and, just as importantly, its constraints.

- **Certificate trust is device-scoped and reversible.** Install the proxy's CA only on the authorized test device, record where it is installed, and remove it at teardown (§9). On modern Android and iOS, a user-installed CA and a system-trusted CA are treated differently; achieving system-level trust generally requires a rooted/jailbroken device and an explicit, recorded step. Treat added trust as a deliberate, logged change to a device you control — never to a personal or production device.
- **Not all traffic honors the system proxy.** Apps built on certain cross-platform frameworks, and apps using non-HTTP transports, may ignore the system proxy entirely. Transparent/invisible proxying and traffic-redirection techniques exist for these cases and are documented by OWASP MASTG; use them only against an authorized app on a device you control, and record the technique used. **Absence of an app's traffic from the proxy is not absence of traffic** — it may indicate a non-proxy-aware transport, pinning, or a bypassed route.
- **Pinning and anti-interception.** If certificate pinning or transport validation blocks observation, record the limitation and obtain an approved test strategy (a client-control bypass on your authorized device, or a scoped exception) rather than forcing it. Pinning present, or pinning bypassable, is a property to record — not, by itself, an impact claim.
- **Reduce noise deliberately.** Mobile devices generate substantial background traffic. Scope the capture to the app under test (e.g., pass-through/exclusion rules for unrelated domains) so the evidence record stays legible. This is an observation-quality choice, not a security control.

Editable proxy/interception record:

| Field | Local entry |
|---|---|
| Proxy product/version; listener interface and port |  |
| CA name, device(s) it is installed on, user vs. system store |  |
| Non-proxy-aware handling used (technique + reference), if any |  |
| Pinning/anti-interception observed; approved handling |  |
| Capture scope / exclusions applied |  |
| Teardown owner: CA removed, routes reverted (date) |  |

## 7. Reaching an authorized test backend — a network decision, not a recipe

A mobile app usually calls backend services, and an authorized test backend often sits behind network controls that a tester must legitimately traverse. **How a device or workstation is permitted to reach a scoped test environment is an organization-specific network decision under the rules of engagement, obtained through your organization's current, approved network-access process — not a reusable recipe.**

This guide does **not** specify a tunnel configuration, static egress address, allow-listing request, change-ticket procedure, or administrative access to a network endpoint. Those details depend on the adopter's topology and access controls and must not be used to circumvent a control outside the engagement's authority. Record only the facts your engagement needs:

| Field | Local record |
|---|---|
| Authorized test backend/environment (from scope) |  |
| Permitted network path to reach it (owner-approved) |  |
| Egress identity the target/monitoring team will see |  |
| Who provisions and revokes the path; change/reversal rule |  |
| Whether the device, the workstation, or both use the path |  |
| Route-validation check against a benign, owner-approved endpoint |  |

Validate the path against a benign, owner-approved endpoint — never a real target scan merely to confirm setup — and record the egress identity, because a tunnel or proxy is a route to *test*, not proof that all traffic follows the intended path.

## 8. Test identities and data

- Prefer **issued test accounts** and **synthetic data**. Record the accounts, roles, and permitted data, and keep credentials under the adopting practice's approved custody. If a test requires a production identity or non-synthetic data, that is a separate, explicit authority and handling decision—not a default implied by this environment guide.
- A second role, account, or tenant is provisioned only when the authorized question requires a comparison.
- **No real credentials, keys, or personal data belong in the environment record or on a shared/clean-reference image.** No public or shared template should contain secret values.
- Do not follow a credential, token, or endpoint discovered in the app into an unapproved account or target.

## 9. Evidence, hygiene, and teardown

- **Capture.** Screen mirroring and capture make evidence collection practical (platform-dependent: some platforms allow interactive control from the host, others only mirroring). Record device/build/account/time with each artifact. A screenshot orients a reader; it does not replace reproducible conditions or a protected original.
- **Archive before you wipe.** Borrowing the workstation lifecycle (§40.3): export and verify required evidence *before* any restore, re-flash, or deletion. If archive verification fails, pause destructive teardown and resolve it. A device snapshot/clean reference restores a working state; it is **not** the evidence archive.
- **Reverse the trust and instrumentation changes.** At teardown, remove test CAs, stop and remove instrumentation servers, revert proxy/network settings, and return the device to its clean reference. A device left trusting a test CA or running an instrumentation server is a standing exposure.
- **Update and connectivity hygiene.** Keep a version-pinned research device from being silently moved off its tested state (uncontrolled OS updates, background sync). The *goal* is "the device stays on its tested, authorized state"; the specific mechanism (airplane mode when idle, controlled update settings, per-device network policy) is a local choice — do not transplant a specific domain block or router recipe from a dated source, and never apply a network-wide block that would affect devices or people outside the test scope.
- **Retirement.** Retire a device through a supported, verified erase and the practice's asset/retirement route; a factory reset is a convenience step, not an attested sanitization.

## 10. Version-pinned official instructions — the discipline

Mobile setup depends on products, operating-system releases, and research tools that change. The portable discipline is to verify the current procedure and preserve its provenance, not to freeze a command list here:

- Record the **outcome and the version**, and pin each step to its **official current source** at adoption time.
- Prefer the official vendor/project documentation and release notes over a transcribed command.
- Re-evaluate a row when the host OS, device OS, instrumentation version, tool entitlement, or method changes (the §2 "re-evaluate" field).

| Capability | Official source class to pin at adoption |
|---|---|
| Device OS versions, signing/rollback behavior, integrity/attestation APIs | Platform vendor's official developer and support documentation |
| Jailbreak / root tooling and procedure | The specific tool's official project/vendor documentation for the exact device and OS |
| Dynamic instrumentation (server + host tools) | The instrumentation project's official docs and release notes; version-match guidance |
| Static-analysis / reversing tools and framework extractors | Each tool's current official project page |
| Mobile testing techniques (interception, non-proxy-aware handling, storage/platform tests) | OWASP MASVS / MASTG / MASWE / MAS Testing Profiles (official project pages) |
| Managed commercial platform provisioning | The platform vendor's current support portal |
| Network access to a test backend | Your organization's current, approved network-access process (§7) |

Citing a control map or tool page does not make this guide an OWASP publication, a vendor-endorsed procedure, or a completed test library.

## 11. Unverified or incomplete setup steps

Do not count a setup step as available because a draft procedure, tool name, or heading exists. Record its status as **verified on the named build**, **limited**, **not run**, or **failed**. If a capability is needed but its procedure is incomplete or known not to work, keep it as an open item and obtain a current procedure from the official project or vendor source before trying it on an authorized fixture. A missing capability narrows the rig's readiness claim; it does not silently become a pass.

## 12. Verify the environment before relying on it

Use one acceptance record per device build or material revision. A rig can pass its baseline and still be unusable for a specific method, and neither result grants permission to test a real target.

| Check | Observed result and evidence reference | Owner/verifier |
|---|---|---|
| Device identity, custody, role and management posture match the matrix |  |  |
| OS version and signing/rollback constraint recorded; reacquisition plan exists |  |  |
| App build provenance (package id, version, channel, environment, hash) confirmed |  |  |
| Root/jailbreak state (if authorized) matches the matrix and is reversible |  |  |
| Instrumentation server and host tool are version-matched and demonstrably attach on a fixture |  |  |
| Proxy CA is installed only on authorized device(s); interception works on a fixture |  |  |
| Non-proxy-aware handling (if needed) observed on a fixture |  |  |
| Benign network-route test matches the recorded path and egress identity |  |  |
| Test identities/data present and correct; no real secrets on the device or image |  |  |
| Evidence can be captured, exported, verified, and retrieved before any teardown |  |  |
| Teardown reverses CA trust, instrumentation, and routes to a clean reference |  |  |
| Engagement authorization | **Not granted by this environment record.** A specific target needs its own scope and rules (§10.1/10.2/10.3). |  |

Mark each applicable row **PASS**, **LIMITED**, **NOT RUN**, or **FAIL**, with the version and the person who observed it. A required LIMITED/NOT RUN/FAIL is not full readiness; state the narrower capability and the owner of repair. Re-run affected rows after a significant change.

## 13. Troubleshooting (vendor-neutral checklist)

Record the *class* of problem and the first checks, not a one-environment fix:

- **Instrumentation attaches but sees nothing / refuses to run.** Confirm on-device server and host-tool versions are compatible; confirm the device is trusted by the host and reachable over the chosen transport (USB vs. network); confirm the target app is actually running.
- **No traffic in the proxy.** Confirm interception is not paused; confirm the CA is trusted in the right store; confirm the app is not pinning or using a non-proxy-aware transport (see §6); for non-proxy-aware apps apply the recorded redirection technique.
- **Device/host not on the same network / isolated.** Guest or segmented wireless networks can silently isolate clients even on the same subnet; confirm the device and host can actually reach each other.
- **Lost version/clean state.** If a device has drifted off its tested OS or configuration, restore the clean reference; if the OS version is no longer reacquirable, fall back to another device provisioned for that version (§3).
- **Network path to backend down.** Revalidate the path against a benign owner-approved endpoint and confirm the egress identity; path provisioning and revocation are owner-controlled (§7), not something to reconstruct ad hoc.

## 14. Use the links at the right boundary

- **§20.4** owns the mobile *method* — what to test and how to judge it. A ready environment is not a tested application.
- **§40.3 / §40.10** own the workstation/field-kit and managed-rig baselines this mobile layer sits on.
- **§20.1** is the umbrella method; **§20.3** owns backend/API testing where the app's authorized backend calls need deeper examination.
- **§10.1/10.2/10.3** bind a real engagement's scope and rules. This guide cannot authorize device modification, interception, backend access, or evidence collection outside them.
- **§90.2 / §90.3** govern tool-specific operating records and research/evaluation posture; a commercial platform or a new tool is not silently satisfied by this environment baseline.

Resolve the public titles and links of these documents at integration rather than assuming a candidate is released.

---

This guide defines a provenance-checked, authorization-bound, reversible mobile-device rig: provisioning, instrumentation, static/dynamic analysis, proxy trust and its constraints, test identities, evidence and teardown, and version-pinned official instructions. Its records are designed for an adopter to fill and inspect. A completed record shows what was verified on a named build, not that a mobile application was tested or that a particular vendor, platform, or version is universally required. An adopter must fill the records against a synthetic or authorized environment and check the adjacent documents, technical currency, rights, and accessibility before relying on it. No adoption, certification, operational deployment, or production use is claimed.
