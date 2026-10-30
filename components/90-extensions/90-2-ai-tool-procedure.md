# 90.2 — AI Tool Operating Procedure Template

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

**Component:** adaptable operating record  
**Reader:** testing-tool owner, qualified operator, engagement lead, validator, or reviewer

## What this template is for

Copy this record for **one actual AI-assisted or agentic testing capability in one materially consistent operating posture**. It turns a program-level decision into instructions an operator can follow: what the configured system is, where it runs, what it may touch, who may use it, what a human must verify, where results go, how it stops, and what change requires a fresh decision.

This blank form grants **no permission** to use a tool or test a target. A completed form does not replace local tool readiness, engagement authorization, scope and rules of engagement, or review of a reported finding. The adopting organization supplies those authorities and the systems of record. The human-led penetration-testing method remains the baseline; this is an optional capability extension.

Use §90.1 for the AI testing operating model and §90.3 for the capability-readiness decision. This procedure remains tool-specific: an adopter must name the exact tool, version, permissions, environments, operators, and stop conditions before using it.

**How to fill it:** Replace every `[LOCAL]` with an evidence-backed answer, or write `not applicable` with a reason. Do not paste secrets, live tokens, customer data, or internal targets into a public copy. The local filled record belongs in the adopter's controlled store, not in this public repository. A vendor claim is a source to assess, not proof that this deployment works as claimed.

## 1. Identity and operating posture

| Field | Local answer |
|---|---|
| Procedure ID, title, version, owner, review trigger | `[LOCAL]` |
| Capability and intended use | `[LOCAL]` |
| **Testing path** (can propose or perform tests/findings) or **support path** (no finding output) | `[LOCAL]` |
| Tool/model/orchestrator version and configured components | `[LOCAL]` |
| Autonomy classification and rationale under the local AI operating model | `[LOCAL]` |
| Approved target and engagement classes; exclusions | `[LOCAL]` |
| Local tool-readiness/authorization record and conditions | `[LOCAL]` |
| Technical custodian and stop/revoke authority | `[LOCAL]` |

Classify the *configured composite system*, not the product name. A model with tools, credentials, retrieval, memory, policies and network access can behave differently from the same model in a chat-only demonstration. Materially different posture needs a separate binding or revision.

## 2. Deployment, data and access

| Question | Local answer or evidence pointer |
|---|---|
| Where does it execute, and who operates that environment? | `[LOCAL]` |
| Which model/provider, endpoint, components, prompts/policies, plugins and adapters are in the run? | `[LOCAL]` |
| What network destinations, target environments and egress controls are permitted? | `[LOCAL]` |
| Which data classes may enter the system; where may logs, prompts, memory and artifacts persist? | `[LOCAL]` |
| What are the provider retention, training, telemetry, residency and third-party conditions? | `[LOCAL]` |
| Which identities and privileges are supplied, by what credential reference and revocation route? | `[LOCAL]` |
| What integrity evidence binds the deployed configuration? | `[LOCAL]` |

Use scoped, revocable credentials and the adopter's credential-handling method. Record references, not cleartext. Describe the actual enforcement boundary—network, account, tool policy and human control—rather than claiming that a prompt alone confines an agent. A sandbox or nonproduction environment is often a sensible initial posture, but this template does not silently convert that preference into universal authorization or ban.

## 3. Authority envelope and operator setup

| Boundary | Permitted by tool authorization | Prohibited or needs separate decision | Enforcement / negative-test evidence |
|---|---|---|---|
| Targets and network reach | `[LOCAL]` | `[LOCAL]` | `[LOCAL]` |
| Identities and credentials | `[LOCAL]` | `[LOCAL]` | `[LOCAL]` |
| Tools, actions, writes and persistence | `[LOCAL]` | `[LOCAL]` | `[LOCAL]` |
| Data, memory, logs and output | `[LOCAL]` | `[LOCAL]` | `[LOCAL]` |
| Rate, actions, cost and runtime | `[LOCAL]` | `[LOCAL]` | `[LOCAL]` |

**Qualified operator roles and supervision:** `[LOCAL]`  
**Setup sequence, configuration check, logging and stop test:** `[LOCAL]`  
**Human pre-authorization points and emergency stop path:** `[LOCAL]`

The tool's general operating approval is not the engagement's permission. For each run, the operator checks the current scope/RoE, exact target, identities, tool version, allowed actions, impact ceiling, evidence destination, validators and stop contacts. An out-of-scope, destructive, irreversible, production-impacting or otherwise reserved action waits for the *specific* local authority it requires; no completed form grants it by implication.

## 4. Per-engagement run card

```text
Engagement / target / environment:
Scope and rules-of-engagement reference:
Exact tool posture and configuration digest or version:
Authorized operator and validating human:
Allowed accounts, data, tools, actions and exclusions:
Time, request/action and cost limits:
Run-specific credentials (reference only) and expiry/revoke route:
Communication, deconfliction and stop contacts:
Pre-run scope, control, logging, egress and stop checks:
Operating sequence (no secrets):
Evidence, logs and output location:
Post-run reconciliation, cleanup, credentials and anomaly review:
Exceptions, interruptions and disposition:
```

The local procedure should link to a reproducible setup and run instruction, but public examples must not contain a working attack command against a real target or embedded credentials. A change of target or engagement resets the run card, even when the general tool procedure remains current.

## 5. Findings and human validation

If the capability produces candidate findings, record the path from tool output to the organization's report and vulnerability-management system:

| Stage | Local decision and record |
|---|---|
| Candidate | Tool output, exact target/state, actions, provenance, evidence, uncertainty and safety notes: `[LOCAL]` |
| Human validation | Qualified person, reproduction or other causal support, affected scope, false-positive challenge and rationale: `[LOCAL]` |
| Review | Independent/peer review conditions, disputed result, severity/impact decision and approval: `[LOCAL]` |
| Delivery | Required report fields, remediation guidance, system-of-record reference and trace to evidence: `[LOCAL]` |
| Correction | Withdrawal/correction trigger, prior recipients and accountable communication route: `[LOCAL]` |

Every delivered finding needs a human decision. Any sampling of *intermediate* tool output, if permitted locally, must be specified and justified without erasing the final finding bar. Do not copy a validation-depth claim from another tool or infer that an opaque agent's confidence score is ground truth. Critical or other high-consequence conditions need the stricter review required by the local program and evidence, not a universal number asserted by this blank form.

For a **support-path** tool, mark finding-pipeline fields not applicable and describe how its output is checked before a tester relies on it. A support classification is not a loophole if it actually proposes tests, makes target changes, or creates finding candidates.

## 6. Spend, integrity, response and records

| Operating question | Local binding |
|---|---|
| Budget, action/rate limits, anomaly signal and person who may change them | `[LOCAL]` |
| Prompt-injection, poisoned context, forged tool output or component drift detection | `[LOCAL]` |
| Egress, credential, scope, target and logging anomaly response | `[LOCAL]` |
| Stop, suspend, revoke, preserve evidence and incident route | `[LOCAL]` |
| Run logs, test evidence, memory/cache, credential references and retention | `[LOCAL]` |
| Customer-facing correction when a delivered claim proves wrong | `[LOCAL]` |

Treat target-origin content as untrusted data, not operator instructions. Pin or otherwise identify decision-bearing components; note material changes and rerun the relevant readiness checks. A failed stop, egress, scope or evidence control is a reason to suspend the affected operation and preserve what happened, not to silently rely on the output.

## 7. Readiness and local decision

Before findings-producing use, the adopter should be able to point to evidence that the configured posture was reviewed; allowed and prohibited behavior were tested; operators are qualified; data and provider terms are acceptable; scope and stop controls work; spend and incident response have owners; and the finding/evidence route was exercised. §90.3 holds the separate build-and-delivery readiness question. The local tool decision does not grant permission for a particular engagement.

| Decision field | Local answer |
|---|---|
| Approve / condition / refuse / suspend / retire | `[LOCAL]` |
| Exact configuration and use boundary | `[LOCAL]` |
| Evidence relied upon and open limitations | `[LOCAL]` |
| Accountable local authority and decision record | `[LOCAL]` |
| Review, change and expiry triggers | `[LOCAL]` |

**Change trigger:** Reassess when a model, orchestrator, prompt/policy, tool, adapter, retrieval source, memory behavior, credential, network path, target class, autonomy, validation method, provider term or cost behavior changes materially. Record what changed, which evidence remains valid, what must be rerun, and who made the new decision. A cosmetic edit should not force a full technical requalification; a material authority or behavior change cannot be called cosmetic.
