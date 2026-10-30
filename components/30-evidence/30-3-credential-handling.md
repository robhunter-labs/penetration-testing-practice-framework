# 30.3 — Credential handling guide

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A penetration test accumulates secrets — customer-provided test accounts and keys, credentials and tokens captured during authorized testing, and the tool's own keys. This component is the **one controlled lifecycle** for all of them: intake, transit, storage, use, rotation, and disposal, plus a short list of things that are never allowed. The baseline here is human-led testing; an agentic-tool extension is at the end. How a secret is *held* is this document; the machine, network, and operator around it are [testing OpSec (§30.4)](30-4-opsec.md); where an archived artifact that contains a secret may live is the [storage authority (§30.2)](30-2-archive-storage.md).

## The central rule

**Each secret has one authoritative custody record; every other copy is a named, time-bounded exception.** Secrets live in a controlled secret store and flow elsewhere by reference, not in cleartext. Retention is bounded to the engagement window plus an explicit retest reserve.

A note the guide keeps straight: the **custody record** (the live secret, in the store) is not the same as **protected evidence** (an archived artifact that happens to contain a captured secret). They have different lifecycles — see *Two clocks* below — and acknowledging that an artifact holds a copy is honest, not a contradiction of the one-authoritative-record rule.

## What counts as a secret

Customer-provided (test accounts and multi-role logins, API keys, OAuth client secrets, service accounts, VPN/database/cloud/repository credentials); team-encountered (session cookies, JWTs, bearer/SAML tokens, credentials found in code/config/responses, credentials obtained through authorized exploitation, cracked hashes, incidental real credentials); and team-generated (tooling keys, including model-provider keys for agentic tools; secrets embedded in scripts; tool configs). Personal single-sign-on/MFA credentials and non-engagement infrastructure credentials are out of scope.

## Lifecycle

1. **Intake — ranked channels.** Prefer direct delivery into the secret store; otherwise an encrypted-in-transit-and-at-rest secure-mail channel; otherwise a leadership-approved exception channel (sanctioned secure transfer, in-person-then-store, an ephemeral dispenser). **Never** plain email, chat, SMS/personal messaging, an unencrypted ticket body or attachment, or personal cloud storage. If a customer cannot use an approved channel, pause rather than accept a secret through the wrong one.
2. **Register at receipt.** Record source/channel, date, purpose/role/scope, expiry/rotation, and the reset path.
3. **Transcribe and verify before deleting the only copy.** Move the secret into the store, verify a clean read-back, and only then remove the intake copy — and defer even that to the adopter's records, legal-hold, incident, and e-discovery rules and any sender-side control. Deleting the sole copy first is the error the ordering prevents.
4. **Store by engagement scope**, with separate areas for customer-provided, captured, and team-tooling secrets, and per-entry metadata (purpose, source, received-at, engagement, contact, expiry, reset path, retention note).
5. **Use by retrieval, not bulk export.** Retrieve at the moment of use; scripts read from the store at runtime and never commit a secret to a repository or an archived artifact.
6. **Keep secrets out of cleartext everywhere else** — not in notes, working files, customer-facing screenshots, chat/email outside the approved channels, or a ticket/report body. References are fine.
7. **Communicate findings without the value.** A real-time high/critical notice describes impact; a captured credential value travels only by the secure channel or a store pointer.
8. **Hand off by granting store access**, never by sending a value.
9. **Rotation and retest.** At closeout the **customer rotates** provided credentials — and a secret the team *captured and reported* is revoked too, because rotating the provided account is not enough: surviving sessions and derived artifacts matter, so revocation scope is explicit and "rotated" is not assumed to make old copies harmless. At retest, verify credential state and prefer fresh credentials after a long gap.
10. **Disposal.** The live secret is disposed at the retest-window close (the lead requests deletion; the store owner executes; the audit log is preserved; a hold extends the window).

## Two clocks

A **stored-secret entry** (the live secret) is short-lived — disposed at the retest-window close. The **archived artifact** that references or contains it (a proxy project file, evidence) follows the records schedule's longest applicable retention, with legal hold overriding. Disposing the secret does **not** delete the archived artifact, and retaining the artifact does not keep the secret live. Keep those two lifecycles distinct.

## Per-type quick reference

| Secret | Intake | Lifecycle note |
|---|---|---|
| Test account / API key / OAuth secret | Store-direct or secure channel | Customer rotates/revokes at closeout |
| VPN / database / cloud credential | Store-direct or secure channel | Scoped to engagement window |
| Captured session token / bearer | Created during testing → store by reference | **Revoked** at closeout; surviving sessions matter |
| Discovered credential / cracked hash | Store by reference | Reported by impact, value never in the body |
| Proxy project file (contains secrets) | Restricted store, intact per the sealed-artifact rule | Retained on the artifact clock, not the secret clock |
| Team-tooling / model-provider key | Store under team-tooling | Rotated on cadence and on operator change |

## Never allowed

Plain email, chat, or SMS for a secret; unredacted screenshots; cleartext in working files, repositories, or ticket/report bodies; personal endpoints or personal cloud; retention past the retest window without a hold justification; bulk export; sharing outside the engagement team. Capturing a secret during authorized testing is allowed — mishandling it afterward is the violation.

## Conditional: agentic-tool credentials

When an agentic tool is used: engagement credentials are read from the store at runtime and never baked into config, prompt, memory, or session; run logs and output are scanned for cleartext before archival (feeding [§30.1](30-1-archival-files.md)'s agentic records). The tool's own standing keys (model-provider and service credentials) are controlled team assets in the store, **rotated on a set cadence and on operator departure or role change**, with a named owner. Guard against runaway spend ("denial of wallet") with a usage-anomaly alert and a baseline threshold owned by a named person — an alert is treated as a possible compromise and routed to the incident path. Outbound egress from the tool's enclave is default-deny, with only the approved endpoint allowed (the network control itself is [§30.4](30-4-opsec.md)).

## Reader test before adoption

For every secret in an engagement, can someone say where it lives, which copies exist and why, whether it is dead yet, and — for anything captured — whether it was revoked, not just rotated? If not, the lifecycle is not controlled.
