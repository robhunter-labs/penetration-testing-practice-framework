# 10.5 · Engagement operational brief — template

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A cover sheet and index for an engagement package whose authorization depends on **more than one party's decision**. It gives every signatory a single coordinated record of what the engagement is for, which components it contains, who must decide what for each component, who can stop it, and where every referenced record lives. It points to the scope record and the Rules of Engagement; it does not restate them and it adds no authority of its own.

This is a draft template. It derives from a source that is itself a Draft, it has not been tried by an adopting practice, and nothing here indicates that it is deployed, proven, or formally approved anywhere. The adopting organization supplies its own authority model, signatories, legal and safety review, record system, and approval process.

| Component metadata | |
|---|---|
| Stable ID and title | §10.5 · Engagement operational brief — template |
| Availability and maturity | Published in this repository · **Draft template** (derived from a Draft source; not tried by an adopting practice) |
| Reader and task | The person assembling a multi-party engagement package, and each signatory reviewing it before testing begins |
| Applies when | Authorization for the engagement, or any component of it, needs a decision from more than one party (see *Do you need this brief?*) |
| Does not apply when | One authorizer with standing over every in-scope target and technique signs the scope record and RoE |
| Upstream | §00.3 (authority model) · §10.1 (scoping guide) · §10.2 (Rules of Engagement worksheet) · §10.4 (scoping requirements form) |
| Downstream and companions | §20.11 (physical testing method, for facility components) · §30.1 (archive set) · §30.3 (credential handling) · §40.5 (roles and responsibilities) |
| Review trigger | Change to §00.3, §10.1, or §10.2; a consumer probe that finds an undecidable field |
| Limitations | Not legal advice; not an authorization; not a conformance or certification instrument; not tested in a native form tool |
| Correction path | [Security and corrections](../../SECURITY.md): public GitHub issue for ordinary corrections; hello@robhunterworks.com for sensitive reports |

For a worked decision rather than a blank form, see the [fictional multi-party filled example](../../examples/multi-party-engagement/10-5-filled-example.md). It illustrates one component that is GO and another that remains NO-GO; it is not evidence of a real authorization or deployment.

---

## Do you need this brief?

List every component of the engagement (a system, an environment, a facility, a provider-hosted service, a technique that needs its own approval). For each, ask: **whose decision is required before this component may be tested?**

- **Every component needs the same single authorizer's decision, and that person has standing over all of it** → you do not need this brief. That makes only this brief unnecessary: the scope record, the RoE, and any other record the adopting organization requires still apply. Do not create this brief as ceremony; its absence is not a defect.
- **Any component needs a decision from someone else as well** — for example the controller of a facility, a building's landlord or managing agent, a third party that hosts or co-owns a system, or an internal owner the adopting organization requires to sign separately → use this brief so all those decisions are visible and tied to the right component.

A team may also choose to use the brief voluntarily as a cover sheet for a single-approver engagement. That choice adds no authority and creates no obligation for other engagements.

## What this brief is, and is not

| It is | It is not |
|---|---|
| A single coordinated record of objectives, components, parties, authorities, windows, stop paths, and the package index | A restatement of the scope record or the RoE |
| The place where each party's **specific** authority is tied to the components it covers | A grant of permission; the referenced decision records are the authority |
| A readiness check that marks each component GO or NO-GO | A way to let one party's signature stand in for another's |
| A change-control pointer | A change approval in itself |

If the brief and a referenced record disagree, **stop the affected component** until they are reconciled. The brief never widens what the scope record and RoE allow.

## The component rule

Authority is checked **per component, not per engagement**.

1. **Required authorities come from outside this brief.** The linked scope record, the RoE, and the adopting organization's authority model determine whose decision each component needs. Map every such party to a row in §6b. A required party with no row is a missing authority, not an absent requirement.
2. A component is **GO** only when every authority so required for it is mapped, recorded, current, and unconditional — or its conditions are met and recorded.
3. A **missing, unmapped, expired, conditional-but-unmet, withdrawn, or contested** decision makes that component **NO-GO**. Testing of it does not begin, or stops if under way.
4. **No substitution.** Another signatory's approval, however senior, does not cover a decision that belongs to a different party unless that signatory's recorded authority explicitly includes it.
5. Other components may proceed only if their own required authorities are complete, they do not depend on the NO-GO component (for example, a network test that would use access obtained during a blocked physical component), **and** the governing approval records permit partial execution. An all-or-nothing condition holds the whole package.
6. Record each NO-GO and its effect on the objectives. An objective that depended on it is reported as not answered, not as answered with no findings.
7. A GO component **pauses** whenever a stop or verification contact it requires (§7) cannot be reached, or its window or authority has ended, and resumes only on the decision of the party §7 names for resumption.

---

## The brief — one per qualifying engagement

Write **N/A and why** where a field does not apply. A blank means *not yet decided*, never *the tester may choose*.

### 1 · Brief control

| Field | Entry |
|---|---|
| Engagement name and ID | |
| Brief version and record state (draft / out for decision / readiness recorded / superseded) | |
| Authorization outcome: ALL COMPONENTS GO / PARTIAL — some NO-GO, see §6c / NO COMPONENT GO | |
| Prepared by (name, role) and brief maintainer | |
| Why this brief is used: which components need decisions beyond a single authorizer | |
| Linked scope record — reference and version | |
| Linked Rules of Engagement — reference and version | |
| Program authority reference (§00.3 or local equivalent) | |

"Readiness recorded" means the record is filled in, not that testing is authorized. GO in this brief means the required authorization decisions for that component are complete; activity still depends on the linked scope and RoE, the actual window, required contacts, and any package-level condition. Read the authorization outcome together with §6c.

### 2 · Purpose and objectives

**What this package covers (one or two sentences):** The testers named in §6 may perform the assessment described in the linked scope record, only on components marked GO in §6c, only within the windows in §5, and only under the linked RoE. ____________

| # | Objective or question to answer | Relying decision or user of the answer | Components it depends on | What cannot be concluded if a component is NO-GO |
|---|---|---|---|---|
| O1 | | | | |
| O2 | | | | |

### 3 · Scope and RoE references

This section points; it does not restate. The scope record and RoE remain authoritative.

| Component ID | One-line description | Surface (digital / provider-hosted / physical / other) | Scope record reference | RoE sections that bind it | Explicit exclusions (pointer) |
|---|---|---|---|---|---|
| C1 | | | | | |
| C2 | | | | | |

**Out of scope, one line (pointer to the scope record):** ____________

### 4 · Target and facility summary

| Component ID | Environment (production / nonproduction / site) | Who owns or controls it | Ownership state (owned / leased or shared / provider-hosted / co-owned / unknown) | Facility zones or site notes, if physical |
|---|---|---|---|---|
| C1 | | | | |
| C2 | | | | |

An **unknown** or **contested** owner makes the component CONDITIONAL in the scope record and NO-GO here until resolved.

### 5 · Test window

| Component ID | Authorized window (start–end) and time zone | Phases, if any (e.g. announced, then separately authorized covert) | Blackout periods and required notice | Contact coverage during the window, or the stated limitation |
|---|---|---|---|---|
| C1 | | | | |
| C2 | | | | |

Coverage is whatever the parties agree and record. Round-the-clock coverage is neither assumed nor required; if a stop or verification contact is reachable only during certain hours, limit that component's activity to those hours. Activity outside them needs a stop and verification contingency that the relevant authority has separately approved and recorded in §6b or §7; otherwise the component holds. A note explaining the gap is not a substitute for cover. At window end or authority expiry, the component stops.

**Retest or follow-on window, if any:** ____________

### 6 · Parties and authorities

#### 6a · Testing team

| Role in this engagement | Name | Contact | Components | May decide on their own |
|---|---|---|---|---|
| Responsible lead | | | | e.g. pause their own activity; invoke a stop |
| Additional tester(s), if any | | | | |

Use the role titles of the adopting organization. One tester or several is a local staffing choice.

#### 6b · Authority matrix

One row per party whose decision is required. State **exactly** what each party decides and which components it covers; "approves the engagement" is not specific enough when parties share a package.

| Ref | Party (local role) and organization | Name | Specific authority: what they decide, and limits | Components covered | May order a stop? (which components) | Decision record (signature or reference, date) | Expiry or conditions |
|---|---|---|---|---|---|---|---|
| A1 | | | | | | | |
| A2 | | | | | | | |
| A3 | | | | | | | |

Where a physical component needs a written authorization carried by testers, list it in §8 and reference it here; this matrix records who decided, and does not replace that document.

#### 6c · Component readiness

| Component ID | Authorities required (source: scope record, RoE, or authority model → 6b ref) | All mapped, recorded, and current? | State: GO / NO-GO | If NO-GO: what is missing, who must supply it, which objectives and dependent components are affected |
|---|---|---|---|---|
| C1 | | | | |
| C2 | | | | |

Apply the component rule above. A component cannot be marked GO because the engagement as a whole has a senior approval.

### 7 · Stop, deconfliction, and verification contacts

Confirm each contact is reachable before the window opens and record that check.

| Purpose | Name or function | Channel and backup | Hours reachable | Components | Checked reachable (by, when) |
|---|---|---|---|---|---|
| Can order a stop | | | | | |
| Security monitoring deconfliction | | | | | |
| Verifies tester authorization in real time (physical or third-party components) | | | | | |
| Operational or system-owner contact | | | | | |
| Authorizes resumption after a stop | | | | | |

**Escalation order if the first contact is unreachable:** ____________
**How a stop is communicated and recorded:** ____________ (the full stop conditions live in the RoE)

### 8 · Package index

Every record riding with this package, findable from this brief. Cite by reference and version in the adopting organization's own record system; do not copy content here.

| # | Record | Reference and location | Version | State: filed / N/A with reason / pending (→ which component it blocks) |
|---|---|---|---|---|
| 1 | Scope record (§10.1 practice; §10.4 intake form if used) | | | |
| 2 | Rules of Engagement (§10.2) | | | |
| 3 | Decision record for each authority in §6b | | | |
| 4 | Per-facility written authorization carried by testers (physical) | | | |
| 5 | Facility coordination record (physical) | | | |
| 6 | Third-party or provider permission (provider-hosted or co-owned) | | | |
| 7 | Credential handling record (§30.3), where used | | | |
| 8 | Method reference for each surface | | | |
| 9 | Other | | | |

A pending record that a component depends on keeps that component NO-GO.

### 9 · Change control

| Field | Entry |
|---|---|
| Where scope changes are decided and recorded (pointer) | |
| Where RoE changes are decided and recorded (pointer to the RoE change log) | |
| Who maintains this brief after a change | |

Rules: update the scope record or RoE **first**, then this brief; the brief is never the place a change is decided. A change that adds a component, a party, a facility, or a third-party boundary needs that party's authority recorded in §6b before the new part proceeds. A changed decision marks the brief's prior version superseded.

| Brief version | What changed | Triggering record and version | Changed by | Date |
|---|---|---|---|---|
| | | | | |

### 10 · Readiness before the window

| Check | Done (by, date) |
|---|---|
| Every §8 record is filed, N/A with reason, or pending with its blocked component named | |
| Every party the scope record, RoE, and authority model require is mapped in §6b; §6c shows a state for every component; each GO has complete, current authorities; §1 authorization outcome matches §6c | |
| §7 contacts confirmed reachable for the hours each component is active | |
| The responsible lead explained back which components are GO, which are NO-GO, how far each may go, who can stop it, and when to stop; the engagement authorizer and every required decision holder for a GO component accepted the readback or returned it for correction | |
| For each NO-GO component, the affected party was informed or the reason notice/acknowledgment is pending was recorded; the governing scope, RoE, and authority model say whether that pending state blocks independent GO components or the whole package | |

---

## Adoption and limits

Use this template to make multi-party authority visible and tied to components. It does not provide legal advice, authorize testing, certify conformance with any external standard, or show that any practice operates it. Local legal, safety, contractual, and organizational controls prevail. Its role terms are placeholders for the adopter's own. The physical-testing companion (§20.11) and the archive and credential companions (§30.1, §30.3) carry the detail this brief only points to.

### Component change note

2026-10-23, draft template revision 0.2: clarified multi-party applicability and publication-versus-maturity status; linked the live correction route and fictional filled example; separated GO-holder readback acceptance from NO-GO notice/pending-effect recording. This change does not certify an adopted process or retroactively authorize any engagement.
