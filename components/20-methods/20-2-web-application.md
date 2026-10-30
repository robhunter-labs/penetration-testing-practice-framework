# 20.2 · Web Application Penetration-Testing Method

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

## The web application is a set of decisions, not a URL list

A browser can hide a field while the server returns it. A login can succeed while a later action ignores the resulting identity. A CDN and an origin can disagree about a response. Testing the pages alone will miss those decisions; testing every adjacent system without authority will exceed the engagement. This method helps a tester map the actual browser-to-service path, select bounded security questions, and report only what the evidence supports.

Use it with the umbrella §20.1 method and the engagement's written scope, rules of engagement, evidence custody, and reporting route. It covers server-rendered, single-page, and server-rendered/hydrated web applications, their browser-facing authentication/session flows, workflows, file processing, and integration boundaries. Deep API operations route to §20.3, database-engine assessment to §20.7, AI-specific behavior to §20.13, and mobile binary/runtime testing to §20.4. A web observation can raise a question about an adjacent system; it does not authorize testing that system.

[OWASP WSTG v4.2](https://wstg.owasp.org/stable/4-Web_Application_Security_Testing/) is a test-technique reference; [ASVS 5.0.0](https://asvs.owasp.org/) is a verification-requirement source; [OWASP Top 10:2025](https://top10.owasp.org/2025/0x00_2025-Introduction/) is a risk-awareness map. None is a substitute for a target-specific plan or a claim that every requirement was tested. Record the edition and selected control/profile used for an engagement. Check current category names and numbering rather than carrying labels from an older edition into the test plan.

## Fix the engagement boundary

Before sending traffic, the record should identify:

| Decision | Minimum useful answer |
|---|---|
| Authority | Named owner, environments, hosts/paths, test window, identities, prohibited actions, and stop/contact route. Does authorization cover a browser flow, the API it calls, and each third-party integration? |
| Application shape | Server-rendered pages, SPA, SSR/hydration, mixed, or an application with a mobile companion; frontend and backend versions where known. |
| Identity and policy | Issued roles, tenants, owned test objects, expected access/function rules, login/federation/MFA paths, and a way to reset or revoke test credentials. A missing role limits coverage; it does not prove access control. |
| Data and state | Sensitivity, permitted synthetic fixtures, allowed mutations, restore path, rate/concurrency/size ceilings, and production monitoring/deconfliction. |
| Evidence | Capture path for authentic requests, responses, browser state, timestamps, build/environment, redaction, protected originals, reviewer, retention, and escalation. |

Define the *target* before using discovery tools. A subdomain, archived route, source-map URL, exposed API description, credential, or redirect encountered during testing is a scope question until approved. For production or shared services, start with passive observation and safe contrasts; any load, race, parser differential, shared-cache mutation, credential attack, or destructive workflow needs its own explicit safety plan.

## Establish a reliable observation position

1. Use a permitted browser and interception/recording path. Show that a benign page load and authenticated action reach the intended build and appear in the evidence record. If a proxy certificate is used, keep trust changes in the test environment and remove them afterward.
2. Capture the login and session lifecycle without copying live tokens into public decoders, chat, screenshots, URLs, or committed collections. Label each capture with the account, role/tenant, browser profile, app version, and environment.
3. Identify where rendering and decisions occur. In a server-rendered app, compare the server response with the displayed page. In a SPA, distinguish client navigation and hidden UI controls from backend authorization. In an SSR/hydrated app, inspect the initial HTML/bootstrap data *and* later client fetches; neither view alone represents the whole flow.
4. Confirm a positive control for every negative test. A cached response, expired session, switched browser profile, stale fixture, WAF block, or gateway rewrite can explain an apparently interesting result.

The required capability is observation and safe replay, not a particular commercial proxy, scanner, OS image, or fixed port. §40.1/40.10 cover local tester and rig readiness; tool possession is not permission to use a capability on this target.

## Build a coverage map another tester can challenge

Inventory pages and browser actions, observed XHR/fetch and form calls, service endpoints, login/federation redirects, state-changing flows, file/import/export paths, third-party scripts, cache/CDN boundaries, and error paths. Compare supplied documentation with what the approved browser flow actually reaches. Mark **observed**, **documented but not reached**, **in-scope but not tested**, **excluded**, and **unknown ownership** separately.

Carry one row per selected security decision:

| Field | Record |
|---|---|
| Flow and target state | Page/action, HTTP operation, environment/build, account, object/fixture, expected side effect, and dependencies. |
| Expected rule | Who may see, submit, change, approve, or receive what; policy source or owner confirmation. |
| Safe contrast | Positive control and one negative/boundary case with the meaningful variable isolated. |
| Authority and ceiling | Exact in-scope action, rate/state/data limit, required notice, and stop condition. |
| Evidence and decision | Browser view plus server response/downstream state where relevant; time, alternative explanations, reviewer decision, and untested extent. |

An endpoint inventory is not a test plan until it says which caller, action, state, and expected rule will be compared.

## Test the security decisions

The categories below align to OWASP Top 10:2025 for navigation, but the test design follows the application. A risk category is not a finding or an automatic severity.

| Decision family | Representative bounded test | Evidence that changes the answer |
|---|---|---|
| **Access control (A01)** | Compare the same approved object or function under two issued roles/owners; inspect the server response and resulting state, not only which button appears. Test path and server-side routing assumptions only inside the approved target. | A policy the caller violates, a controlled contrast, protected content/action actually returned or performed, and cache/shared-object alternatives ruled out. Object, function, property, and workflow authorization are different questions. |
| **Configuration (A02)** | Observe reachable admin/debug surfaces, error detail, security headers, CORS, and proxy/framework trust behavior. Change one safe request property at a time. | A concrete exposure or boundary failure in this deployment. A missing header, server banner, exposed schema, or permissive-looking CORS line alone may be informational. |
| **Software supply chain (A03)** | Inventory third-party scripts, package sources and versions when supplied, integrity/trust controls, and which code executes in the browser or build. | A reachable, relevant vulnerable or untrusted dependency with a demonstrated impact path, or a defensible control gap under the product's own requirement. Missing SRI alone is not a universal finding. |
| **Cryptography (A04)** | Confirm sensitive transport and storage behavior along a defined flow; assess TLS and cookie/token handling against the actual client and data context. | Exact endpoint, protocol/configuration, sensitive data or trust consequence, and plausible exposure. A protocol version or checkbox does not establish a regulatory conclusion. |
| **Injection (A05)** | Trace a selected input to a specific interpreter, template, query, DOM sink, header, parser, or file-processing path; use a benign differential or agreed canary first. | Reproducible change showing data became control in that context. An error message or reflected string is a candidate, not proof of code execution or data compromise. |
| **Design and business logic (A06)** | Model a real workflow: permitted order, approval, limit, replay, ownership, and failure/rollback states. Use synthetic transactions and bounded attempts. | The owner's expected invariant and an observed contrary business outcome, not a hypothetical scale-up from one response. |
| **Authentication (A07)** | Compare login, reset, MFA, SSO, refresh, logout, session rotation and expiry with approved accounts; test the server outcome, not just UI gating. | A protected operation succeeds under an identity/session state the policy forbids. Credential stuffing or OTP brute force is not implied by this method. |
| **Software/data integrity (A08)** | Identify serialized or signed state, update/plugin paths, and trusted data imports; ask what verifies origin and integrity. | An unauthorized, controlled alteration is accepted and changes a security decision; encoded data or a library version alone is insufficient. |
| **Logging/alerting (A09)** | Agree on one safe, distinctive test event and ask the authorized owner to check the expected log/alert path. | A defined expected signal is absent or materially wrong in the observed system and window; lack of tester access to logs is a coverage limit. |
| **Exceptional conditions (A10)** | Exercise bounded invalid, interrupted, duplicate, or conflicting state transitions and check fail/restore behavior. | A broken security or business invariant under that condition; stress or large concurrency requires separate approval. |

### Follow the architecture-specific branches

The branches below are prompts for choosing relevant tests, not a mandate to run every payload family.

| Branch | Question worth asking | Boundary and claim ceiling |
|---|---|---|
| Front-end/origin request parsing | Do CDN, WAF, gateway, and origin agree on request boundaries and trusted headers? | Request smuggling and HTTP/2 downgrade probes can affect other users or shared caches. Use an isolated test path or separately approved plan; show a real parser disagreement and impact before claiming hijack/bypass. |
| Race windows | Can an approved state transition occur twice or out of order under a small, controlled concurrency test? | Use disposable fixtures and explicit concurrency ceiling; two success-looking responses do not prove duplicated final state. |
| GraphQL in a web flow | Does browser-visible field/function authorization hold at resolver level? Are batching and query complexity bounded? | Route deep protocol work to §20.3. Introspection is not automatically a defect; no high-cost query without approval. |
| Browser-held JWT | Does token storage/exposure matter in this browser threat model, and does the server validate signature, audience, expiry and intended use? | Decoding a JWT, seeing one in storage, or changing a header is not a finding until unauthorized acceptance/exposure is shown. Never submit live tokens to a public tool. |
| OAuth/OIDC | Are redirect, issuer, state/PKCE/nonce, token and account-linking decisions bound to the transaction and client type? | Use [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700/) and applicable profile. A grant name or an observed redirect alone is not a vulnerability. |
| Passkeys/WebAuthn | Does the server verify ceremony results, challenge, origin/RP ID, user presence/verification as required, and recovery/fallback? | A client-reported success must not be mistaken for server authentication; test only issued credentials and safe recovery paths. |
| Cache boundaries | Can an authenticated response become shared, or can unkeyed input affect content for another approved test identity? | CDN/global cache mutation can reach real users. Prefer isolated fixtures and an approved cache key/purge path; show actual cross-context delivery. |
| Prototype pollution | Does attacker-controlled JavaScript object data reach a sensitive gadget in client or server code? | A polluted property without a reachable security effect is an observation, not RCE or XSS. |
| Modern DOM/XSS | Is untrusted data reaching a browser execution sink despite CSP, Trusted Types, sanitization, message-origin checks, or DOM structure? | Demonstrate execution or a specific unsafe transformation in the actual browser context; a payload blocked by CSP does not prove broad safety. |
| User-interaction abuse | Can a crafted interaction cause a sensitive action without the user's intended consent? | UI-redress variants beyond iframe clickjacking are conditional on the actual flow; do not claim every frame defense is bypassed. |
| Client-side dependency trust | Which externally loaded scripts can access session or sensitive page data, and what constrains their source and changes? | An incident elsewhere or absent SRI is not proof this app is compromised; assess actual script, trust control and data access. |
| Framework internal-header trust | Can an external caller influence a header reserved for trusted middleware/proxy decisions? | Compare externally supplied and trusted-path behavior on a safe fixture. A framework CVE applies only to a verified affected build/configuration or reproduced behavior. |

### Cross-cutting checks that often belong in more than one row

- **Browser credentials, CORS, and CSRF:** identify whether the browser sends cookies or script-supplied bearer headers, whether the request can cause a state change, and whether a hostile origin can read a protected response. Header reflection, `OPTIONS 200`, or `SameSite` alone does not settle the test. Keep the browser and server perspectives together; §20.3 handles deeper API consequences.
- **TLS and headers:** check the endpoint, browser behavior, cache and content type against the actual policy. HSTS, CSP, `frame-ancestors`, `nosniff`, referrer and permissions policies answer different questions; a uniform missing-header finding is not a method.
- **Upload/import/export and XML:** trace accepted type/size, storage, processing and download/rendering context. Use benign fixtures first; parser amplification, external-entity fetches, shell execution and live-file access need distinct approval.
- **Framework and legacy features:** test a feature because the deployed stack exposes it, not because it appears in a generic list. A Java, .NET, PHP, SAML, cloud, or retired-plugin branch requires a version and reachable path. Legacy technology can be in scope, but an obsolete checklist row is not evidence.
- **Component advisory:** pair a verified package/version with a vendor advisory, reachable code path and configuration before asserting exploitability. A banner may be misleading; an advisory may cover a different build.

## One web-specific worked thread: hidden data in an SSR page

**Synthetic fixture:** a server-rendered project page hydrates a browser component from bootstrap JSON. The owner states ordinary project members may see a project title, while only billing-role members may see a billing contact. Two issued users are members of the same synthetic project; only one has the billing role. Read-only comparison is authorized.

1. Under the billing user, capture the initial HTML, embedded/bootstrap data, subsequent fetches, visible screen, role, project, build and time. Confirm the expected field appears.
2. Under the ordinary member, request the *same* project once in a clean browser profile. Capture the initial response and subsequent fetches even if the UI hides the field.
3. Check whether the ordinary member inherited billing access, whether a cache served the first user's response, whether the field is intentionally public, and whether the browser switched accounts.
4. If the raw initial response contains a protected billing contact contrary to a confirmed rule, record the exact server-side exposure and its affected page/role/build. If only a client component knows the field name, or the policy is unresolved, do not promote it to a finding.

The browser display, SSR response, hydration data and API fetch are different evidence surfaces. Deep API authorization goes to §20.3 if authorized; this one page does not establish a system-wide blast radius.

## Build an impact story without inventing the next step

Use these chain families—access control, cryptography, injection, deserialization, authentication and sessions, upload, configuration, SSRF/XXE, outdated components, and business logic—as *questions*, not prewritten conclusions. A named family is not a complete procedure or proof of a finding.

| Layer | Example | What may be reported |
|---|---|---|
| Observed | One ordinary test user received a protected field in initial HTML for one approved fixture. | The exact build, identities, response, field, policy and conditions. |
| Inferred, with basis | The SSR authorization or cache key likely failed to separate that role. | The basis and alternatives checked; no asserted root cause without adequate evidence. |
| Possible, not tested | Other pages, tenants, exports or production users could share the defect. | A bounded hypothesis for owner triage or a new authorization decision, not a confirmed population or severity multiplier. |

Follow-on database, host, cloud, third-party and other-user paths do not enter scope merely because a primitive makes them plausible. A real engagement may stop after a safe proof and ask the owner to assess blast radius. Record the absent test, not an imaginary chain step.

## Reporting and automation boundary

A finding packet should contain expected versus observed behavior, authorization and build context, reproducible steps within the approved limits, protected authentic evidence and a redacted recipient derivative, impact basis and limits, competing explanations, remediation direction, reviewer disposition, and a retest condition. Apply the adopter's scoring and contextual-priority model; do not map a category, data type or CVE automatically to Critical. A report can be valuable with a deliberately bounded claim.

Automation can assist inventory, header/TLS observation, candidate dependency matching, and low-impact differential checks. It must inherit the engagement's target allowlist, identities, request/state ceilings, credential custody, rate/stop path, output provenance, and human disposition. Active scanning, default-credential attempts, broad injection sweeps, desync, race, SSRF/XXE, and production shared-cache probes are not a default runbook. Any proposed automation needs its own bounded design and verification before use.

End with a coverage ledger: what was tested, what was not tested, which identities/builds were used, which assumptions were owner-confirmed, and which adjacent methods or new authority decisions remain. This method is not an attestation that any specific application or practice passed it.
