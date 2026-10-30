# 50.1 — Coordinated vulnerability disclosure

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

A vulnerability found during authorized testing or research sometimes reaches beyond the adopting organization — to a vendor who can fix a product, to other deployers, or to the public. This component is the route that protects the adopter's own exposure first, notifies affected external parties responsibly, and lets **nothing about the vulnerability leave the organization without the required approvals**. A vulnerability reported inside a normal engagement stays in its lane — its report follows the [report standard (§30.5)](../30-evidence/30-5-report-standard.md); this component links that work to the external-disclosure decision. An external request *for* an artifact follows [audit and external information requests (§50.5)](50-5-audit-handling.md), not the vendor-contact route.

## Two decisions, kept separate

**Handling the exposure** and **disclosing information about it** are related but different. A third-party flaw can affect the adopter's own systems, other deployers, and a vendor able to fix the cause — so internal protection and external coordination can run in parallel under the right authority when delay would harm others; internal handling need not *finish* before vendor coordination begins. A public advisory is a further, separate decision, never the automatic result of notifying a vendor.

| Track | Immediate question | Record |
|---|---|---|
| Internal exposure | Which authorized systems or users may be affected, and who owns mitigation? | Confirmed scope, issue route, remediation owner, retest status |
| External coordination | Who can fix or coordinate the product issue, and what minimum detail may they receive? | Recipient, disclosure authority, exact report, channel, acknowledgements, timeline |
| Public communication | What should users know, when, through whose voice, with what residual risk? | A separate publication decision, affected-party consultation, exact released text |

## Case route

1. **Capture carefully.** Record the affected product/component and version if known, the conditions, observed impact, bounded reproduction evidence, and what remains unverified. Do not broaden exploitation to make a stronger story. Preserve the evidence under the [archival](../30-evidence/30-1-archival-files.md) and [storage-authority](../30-evidence/30-2-archive-storage.md) components.
2. **Validate and classify.** Have a qualified reviewer distinguish a real flaw from a hypothesis, duplicate, configuration issue, or dependency. Record the affected parties, the exposure, the severity rationale, whether a public exploit or active exploitation exists, and whether an identifier already exists. "Zero-day" is not a synonym for "new to us."
3. **Protect affected operations.** Route the adopter's own exposure to its issue, remediation, and incident owners as applicable. A vulnerability case alone does not declare an incident; if one is suspected, use the incident process. Keep a link between finding, mitigation, fix, and retest.
4. **Decide external notification.** Identify the vendor/maintainer or coordination body, the person authorized to speak, the minimum technical content needed to act, the channel, any contractual or customer restrictions, and who approves this exact contact. Treat a request for a public identifier as an external transfer requiring its own decision. Record a no-contact decision too.
5. **Coordinate.** Prefer the product's published security-contact route; verify a `security.txt` file or redirect genuinely belongs to the affected party. Seek an acknowledgement and a case reference. Track vendor questions, multi-party dependencies, fix progress, and communication to affected deployers. Escalate non-response or conflict to an appropriate coordinator when warranted — do not make a fixed timer do the thinking.
6. **Decide publication separately.** A fix, an elapsed interval, or a reserved identifier does not by itself authorize a public advisory. Decide audience, timing, content, attribution, and any continuing exposure with the responsible legal, communications, product, and customer owners. Publish no local configuration, credentials, customer names, or operational exploit path by default; an exceptional disclosure needs an explicit, documented authority decision.
7. **Close or transfer.** Preserve the exact notifications, acknowledgements, any identifier and advisory references, remediation and retest state, unresolved risks, and who owns the next step. "Vendor notified," "identifier assigned," "fix available," and "our exposure remediated" are distinct states.

## Disclosure case record (one per issue)

`case ID · discovery / source authorization · affected product / version / party · validation status · internal exposure and owner · evidence reference · severity / exploitation basis · identifier check · external recipient / channel · disclosure approval and exact payload · acknowledgement · coordination / timeline decisions · fix / mitigation · adopter retest · public decision / payload · residual open items · records location`

Keep raw exploit material and personal data out of the index record; point to the controlled evidence instead.

## Worked decision (fictional)

A scoped tester confirms a flaw in a third-party component the adopter deploys. The practice records the minimal proof and confirms the deployed version with the asset owner, who begins mitigation while a disclosure lead, legal function, and product contact agree a vendor report that omits local topology. The vendor acknowledges and asks for a revised reproduction note. A public identifier is considered only after checking the current assignment route and existing IDs. No public write-up is presumed; the case stays open until the local exposure and the external coordination are each separately recorded. *This illustrates the route, not an actual disclosure.*

## Review and adoption checks

- Can an authorized tester find both the internal route and the external decision-maker without improvising?
- Is there a safe way to notify affected parties urgently **without** assuming either permanent secrecy or automatic publication?
- Does each outward transfer identify the recipient, the exact released material, the authority, and a witness?
- Are attribution, legal and contractual duties, researcher protections, and records retention actually set by the adopting organization, not inferred from this template?

**Primary orientation.** CERT/CC's coordinated-disclosure guide describes discovery through deployment as distinct phases; [RFC 9116](https://www.rfc-editor.org/rfc/rfc9116.html) defines `security.txt`. Check the current [CVE Program](https://www.cve.org/) assignment route and the relevant numbering-authority scope before requesting an identifier, at the time of use. This component sets **no universal disclosure deadline** — a reasonable, case-driven timeline, informed by severity, exploitation, and vendor responsiveness, replaces a fixed clock.
