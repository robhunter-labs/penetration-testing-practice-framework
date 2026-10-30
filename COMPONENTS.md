# Open Practice Framework — Component register

This register lists every component of the Open Practice Framework: its section number, public title, type, where it lives, the reader job it does, and its publication status. It records **publication state, not operational adoption** — a guide can be a complete publication while no organization has adopted it, and an adopter can tailor a local copy without making the framework an external mandate. Those facts stay separate.

The register is the framework's front door: enter through a problem, find the component that bears on it, and see what it assumes before you open it.

## How to read a row

| Column | Meaning |
|---|---|
| **No.** | Section number: folder, then position (e.g. 30.5). Other documents cite a component by number and name, never by filename. |
| **Component** | Public title. |
| **Type** | Guide, Method, Template, Workbook (XLSX), Deck (PPTX + PDF), Diagram (SVG), Catalogue entry, or Register. |
| **Path** | Open the component directly. `downloads/` holds native files; `diagrams/` holds SVGs; everything else is Markdown under `components/` or the repository root. |
| **Reader job** | The one problem the component helps a reader solve. |
| **Status** | **Published** means the component is available in this repository. It does not mean an organization adopted or validated it. |

**Publication is not operational adoption.** A material correction to a component should carry a version note and a link to what changed. A retired number is never reused.

## Reader routes

| Route | First useful question | Walk |
|---|---|---|
| **Practice lead** | What must be in place to run and improve a testing service at my scale? | 00.1 → 00.3 → 20.1 → 10.1/10.2 → domain methods → 30.1/30.5 → 40.1–40.10 → 50.5–50.8 → 60.2 → 60.1 |
| **Working tester** | How do I turn a bounded engagement into defensible tests and evidence? | 10.1/10.2 → 10.3 → 20.1 → relevant 20.2–20.13 (+ 20.14 catalogue) → 30.3/30.4 → 30.1 → 30.5 → 50.4 |
| **Reviewer / assurance** | What was required, performed, reviewed, recorded, and left uncertain? | 00.2 → 00.3 → 30.5 → 60.2 → 50.5–50.8 → 50.1 |
| **Adopter / contributor** | What can I copy, tailor, and question without mistaking it for a mandate? | README → 00.2 → 00.1 → a component's sources → correction route |

---

## Components

### Start here & authority

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 00.1 | Document Hierarchy & Control | Guide | [components/00-start-here/00-1-document-control.md](components/00-start-here/00-1-document-control.md) | Keep one current, traceable version of each standing document, and decide what belongs under control. | Published |
| 00.2 | Framework Component Register | Register | [COMPONENTS.md](COMPONENTS.md) | This document: find any component, its job, type, and status. | Published |
| 00.3 | Authority to Operate | Guide | [components/00-start-here/00-3-authority-to-operate.md](components/00-start-here/00-3-authority-to-operate.md) | Define the authority a testing service needs, and what stays the adopter's to grant. | Published |
| 00.4 | Innovation & Capability Charter | Guide | [components/00-start-here/00-4-capability-charter.md](components/00-start-here/00-4-capability-charter.md) | Name the capabilities a practice commits to building and maintaining. | Published |

### Engagement setup

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 10.1 | Engagement Scoping Guide | Guide | [components/10-engagement/10-1-scoping-guide.md](components/10-engagement/10-1-scoping-guide.md) | Turn authority into a scoped, testable target without inventing reach. | Published |
| 10.2 | Rules of Engagement — Template | Template | [components/10-engagement/10-2-rules-of-engagement.md](components/10-engagement/10-2-rules-of-engagement.md) | Record the permitted actions, limits, identities, and stop conditions for an engagement. | Published |
| 10.3 | Methodology-to-Scoping Map | Guide | [components/10-engagement/10-3-scoping-map.md](components/10-engagement/10-3-scoping-map.md) | Choose which methods a given scope requires. | Published |
| 10.4 | Scoping Requirements — Form | Workbook (XLSX) | [downloads/10-4-scoping-requirements-form.xlsx](downloads/10-4-scoping-requirements-form.xlsx) (+ [downloads/10-4-scoping-requirements-example.xlsx](downloads/10-4-scoping-requirements-example.xlsx)) | Collect the scope facts an engagement needs, with a worked example to exercise first. | Published |
| 10.5 | Engagement Operational Brief — Template | Template | [components/10-engagement/10-5-operational-brief.md](components/10-engagement/10-5-operational-brief.md) | Coordinate component-level GO / NO-GO when an engagement needs decisions from more than one party. | Published (Draft template) |
| 10.6 | Engagement Process Flow | Diagram (SVG) | [diagrams/10-6-engagement-flow.svg](diagrams/10-6-engagement-flow.svg) (+ companion [components/10-engagement/10-6-engagement-flow.md](components/10-engagement/10-6-engagement-flow.md)) | See one engagement move through authority, design, testing, review, and delivery. | Published |

### Technical methods

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 20.1 | Methodology — Framework (umbrella) | Method | [components/20-methods/20-1-method-framework.md](components/20-methods/20-1-method-framework.md) | The common spine: how an observation becomes a reviewed, defensible finding. | Published |
| 20.2 | Method — Web Application | Method | [components/20-methods/20-2-web-application.md](components/20-methods/20-2-web-application.md) | Test a web application against a target-specific plan, not a checklist. | Published |
| 20.3 | Method — API | Method | [components/20-methods/20-3-api.md](components/20-methods/20-3-api.md) | Test whether each caller can do and see only what it should, across API styles. | Published |
| 20.4 | Method — Mobile | Method | [components/20-methods/20-4-mobile.md](components/20-methods/20-4-mobile.md) | Test a mobile app across platform, build, and backend boundaries. | Published |
| 20.5 | Method — Network | Method | [components/20-methods/20-5-network.md](components/20-methods/20-5-network.md) | Test a network's exposure, segmentation, and reachable services. | Published |
| 20.6 | Method — Infrastructure | Method | [components/20-methods/20-6-infrastructure.md](components/20-methods/20-6-infrastructure.md) | Test hosts, services, and the paths between them. | Published |
| 20.7 | Method — Database | Method | [components/20-methods/20-7-database.md](components/20-methods/20-7-database.md) | Test database access, privilege, links, and data exposure under authority. | Published |
| 20.8 | Method — Thick Client | Method | [components/20-methods/20-8-thick-client.md](components/20-methods/20-8-thick-client.md) | Test a thick-client application and its trust and isolation boundaries. | Published |
| 20.9 | Method — Wireless | Method | [components/20-methods/20-9-wireless.md](components/20-methods/20-9-wireless.md) | Test wireless networks and clients with ownership established first. | Published |
| 20.10 | Method — NAC | Method | [components/20-methods/20-10-nac.md](components/20-methods/20-10-nac.md) | Test network access control without over-claiming a bypass. | Published |
| 20.11 | Method — Physical | Method | [components/20-methods/20-11-physical.md](components/20-methods/20-11-physical.md) | Test physical controls safely, with per-technique authorization. | Published |
| 20.12 | Method — Secure Code Review | Method | [components/20-methods/20-12-secure-code-review.md](components/20-methods/20-12-secure-code-review.md) | Review source for reachable, demonstrable weaknesses, not pattern counts. | Published |
| 20.13 | Method — AI/LLM | Method | [components/20-methods/20-13-ai-llm.md](components/20-methods/20-13-ai-llm.md) | Test an AI/LLM system as a target (AI-as-target extension). | Published |
| 20.14 | Tactical Testing Checklists | Catalogue entry | [components/20-methods/20-14-tactical-checklists-catalogue.md](components/20-methods/20-14-tactical-checklists-catalogue.md) | **Catalogue-only — no workbook distributed.** Explains the role of a tactical coverage workbook and directs adopters to maintain their own. | Published |
| 20.15 | Threat-Informed Testing & CTI | Guide | [components/20-methods/20-15-threat-informed.md](components/20-methods/20-15-threat-informed.md) | Shape test design with threat intelligence without claiming a running CTI engine. | Published |
| 20.16 | Threat Modeling | Guide | [components/20-methods/20-16-threat-modeling.md](components/20-methods/20-16-threat-modeling.md) | Build a threat model that feeds the engagement method. | Published |

### Evidence & reporting

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 30.1 | Required Testing Archival Files | Guide | [components/30-evidence/30-1-archival-files.md](components/30-evidence/30-1-archival-files.md) | Decide what evidence an engagement must retain and why. | Published |
| 30.2 | Archive Storage Authority & Controls | Guide | [components/30-evidence/30-2-archive-storage.md](components/30-evidence/30-2-archive-storage.md) | Choose where evidence lives and what compensating controls apply. | Published |
| 30.3 | Credential Handling | Guide | [components/30-evidence/30-3-credential-handling.md](components/30-evidence/30-3-credential-handling.md) | Receive, store, rotate, and retire engagement credentials safely. | Published |
| 30.4 | Penetration Testing OpSec | Guide | [components/30-evidence/30-4-opsec.md](components/30-evidence/30-4-opsec.md) | Keep testing activity and data within the engagement's boundaries. | Published |
| 30.5 | Report Standard & Template | Template | [components/30-evidence/30-5-report-standard.md](components/30-evidence/30-5-report-standard.md) | Write a report whose every finding carries its evidence, with a blank template and one synthetic finding. | Published |

### Operations & people

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 40.1 | Tester Onboarding | Guide | [components/40-operations/40-1-onboarding.md](components/40-operations/40-1-onboarding.md) | Bring a tester to readiness before they touch an engagement. | Published |
| 40.2 | Tester Offboarding & Access Revocation | Guide | [components/40-operations/40-2-offboarding.md](components/40-operations/40-2-offboarding.md) | Revoke access and close out when a tester leaves the work. | Published |
| 40.3 | Testing Workstation | Guide | [components/40-operations/40-3-workstation.md](components/40-operations/40-3-workstation.md) | Build and keep a controlled testing workstation and evidence custody. | Published |
| 40.4 | Mobile Test Environment Guide | Guide | [components/40-operations/40-4-mobile-environment.md](components/40-operations/40-4-mobile-environment.md) | Stand up a mobile testing environment (fast-aging; check currency). | Published |
| 40.5 | RACI Matrix | Workbook (XLSX) | [downloads/40-5-raci-matrix.xlsx](downloads/40-5-raci-matrix.xlsx) | Assign decision rights across engagement activities; adopters set their own roles. | Published |
| 40.6 | Team Core Principles | Guide | [components/40-operations/40-6-team-principles.md](components/40-operations/40-6-team-principles.md) | The principles a testing team holds itself to. | Published |
| 40.7 | Team Working Agreement | Guide | [components/40-operations/40-7-working-agreement.md](components/40-operations/40-7-working-agreement.md) | How the team agrees to work together. | Published |
| 40.8 | Skills Matrix & Certification | Template | [components/40-operations/40-8-skills-matrix.md](components/40-operations/40-8-skills-matrix.md) | A blank, locally maintained map of skills and eligibility — no real roster. | Published |
| 40.9 | Program Metrics & KPIs | Guide | [components/40-operations/40-9-metrics.md](components/40-operations/40-9-metrics.md) | Measure a testing practice without mistaking activity for health. | Published |
| 40.10 | Managed Test Rig | Guide | [components/40-operations/40-10-test-rig.md](components/40-operations/40-10-test-rig.md) | Run a managed, repeatable test rig (fast-aging; check currency). | Published |
| 40.11 | Consulting Training — Deck | Deck (PPTX + PDF) | [downloads/40-11-consulting-training-deck.pptx](downloads/40-11-consulting-training-deck.pptx) (+ `.pdf`) | A training deck for the consulting rotation, with a PDF equivalent. | Published |

### Support & assurance

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 50.1 | Coordinated Vulnerability Disclosure | Guide | [components/50-support/50-1-coordinated-disclosure.md](components/50-support/50-1-coordinated-disclosure.md) | Run a disclosure process with clear boundaries. | Published |
| 50.2 | Quick Reaction Force — Urgent Response | Guide | [components/50-support/50-2-urgent-response.md](components/50-support/50-2-urgent-response.md) | Route an urgent retest or support surge without claiming a standing QRF. | Published |
| 50.3 | Penetration Testing Consulting Guidebook | Guide | [components/50-support/50-3-consulting-guidebook.md](components/50-support/50-3-consulting-guidebook.md) (repository root) | Give post-test technical questions, retest, closure, escalation, and rotation a reliable home. | Published |
| 50.4 | Closing Meeting — Deck | Deck (PPTX + PDF) | [downloads/50-4-closing-meeting-deck.pptx](downloads/50-4-closing-meeting-deck.pptx) (+ `.pdf`) | A closing-meeting template deck, with a PDF equivalent. | Published |
| 50.5 | Audit & External Request Handling | Guide | [components/50-support/50-5-audit-handling.md](components/50-support/50-5-audit-handling.md) | Handle an audit or external information request safely. | Published |
| 50.6 | Attestation & Audit Summary — Template | Template | [components/50-support/50-6-attestation-summary.md](components/50-support/50-6-attestation-summary.md) | Summarize what testing occurred for an assurance reader. | Published |
| 50.7 | Program-Practice Q&A | Guide | [components/50-support/50-7-qa-reference.md](components/50-support/50-7-qa-reference.md) | A repeatable answer discipline for recurring program questions. | Published |
| 50.8 | Audit Request & Disclosure Log — Template | Template | [components/50-support/50-8-disclosure-log.md](components/50-support/50-8-disclosure-log.md) | Record what was requested, released, and withheld, and why. | Published |

### Learning & stewardship

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 60.1 | Lessons-Learned & Continuous Improvement | Guide | [components/60-learning/60-1-learning-loop.md](components/60-learning/60-1-learning-loop.md) | Make sure a lesson from one engagement reaches the next. | Published |
| 60.2 | Program Self-Assessment & Internal Audit | Guide | [components/60-learning/60-2-self-assessment.md](components/60-learning/60-2-self-assessment.md) | Check the practice against itself and find the gaps. | Published |

### Versioned extensions (AI & R&D)

| No. | Component | Type | Path | Reader job | Status |
|---|---|---|---|---|---|
| 90.1 | Agentic AI Operating Framework | Guide | [components/90-extensions/90-1-ai-operating-framework.md](components/90-extensions/90-1-ai-operating-framework.md) | Where an AI agent may act in a human-led practice (AI-as-capability extension). | Published |
| 90.2 | AI Tool Operating Procedure — Template | Template | [components/90-extensions/90-2-ai-tool-procedure.md](components/90-extensions/90-2-ai-tool-procedure.md) | A blank procedure for operating a specific AI testing tool. | Published |
| 90.3 | R&D Build & Readiness | Guide | [components/90-extensions/90-3-rd-readiness.md](components/90-extensions/90-3-rd-readiness.md) | Decide when an R&D capability is ready to use. | Published |
| 90.4 | AI Leadership Levers & Dials | Guide | [components/90-extensions/90-4-ai-leadership-levers.md](components/90-extensions/90-4-ai-leadership-levers.md) | Leadership questions for adopting AI in testing, with measurement first. | Published |

---

## Count and denominator

56 active components — **4** start-here & authority · **6** engagement setup · **16** technical methods · **5** evidence & reporting · **11** operations & people · **8** support & assurance · **2** learning & stewardship · **4** versioned extensions. (4 + 6 + 16 + 5 + 11 + 8 + 2 + 4 = 56.) All 56 have a public component here; §20.14 is intentionally catalogue-only.

## Native downloads

| No. | File(s) | Note |
|---|---|---|
| 10.4 | [downloads/10-4-scoping-requirements-form.xlsx](downloads/10-4-scoping-requirements-form.xlsx), [downloads/10-4-scoping-requirements-example.xlsx](downloads/10-4-scoping-requirements-example.xlsx) | Blank fillable form + worked synthetic example. |
| 50.4 | [downloads/50-4-closing-meeting-deck.pptx](downloads/50-4-closing-meeting-deck.pptx), [downloads/50-4-closing-meeting-deck.pdf](downloads/50-4-closing-meeting-deck.pdf) | Deck + PDF equivalent for readers without PowerPoint. |
| 40.11 | [downloads/40-11-consulting-training-deck.pptx](downloads/40-11-consulting-training-deck.pptx), [downloads/40-11-consulting-training-deck.pdf](downloads/40-11-consulting-training-deck.pdf) | Deck + PDF equivalent. |
| 40.5 | [downloads/40-5-raci-matrix.xlsx](downloads/40-5-raci-matrix.xlsx) | Editable decision-rights matrix. |
| 10.6 | [diagrams/10-6-engagement-flow.svg](diagrams/10-6-engagement-flow.svg) | SVG diagram (text, accessible); must agree with §20.1. |
| 20.14 | *(none — catalogue-only)* | No workbook is distributed; adopters maintain their own checklists. |

## How to evaluate and adapt this framework

1. Enter through a reader route, then inspect the component's job, boundaries, local decisions, and sources before adopting it.
2. Use the method's test path or template as a starting point. Bind it to your own written authority, scope, roles, records, and obligations; a published page is not permission to test.
3. Check an external standard in its current edition and decide what applies to the target; this framework does not claim to replace it.
4. Try the native templates in the applications you actually use. The example workbook and [synthetic API walkthrough](examples/api-engagement/README.md) are illustrations, not proof that a practice operates.
5. Report broken links, unsafe implications, stale sources, or contradictions through the correction route below. A component may be improved or withdrawn without renumbering the rest.

## Corrections

Report a broken link, unsafe implication, stale external source, unusable example, or contradiction through the repository's [security and correction route](SECURITY.md) (GitHub private vulnerability reporting for a sensitive report). The register is updated on component release, supersession, or withdrawal — not on a fixed calendar.

---

Copyright © 2026 Rob Hunter. Original material is released under the MIT License.
