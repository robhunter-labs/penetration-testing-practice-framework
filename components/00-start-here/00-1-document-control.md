# 00.1 · Document control for a penetration-testing practice

> Framework component for adaptation. Publication does not authorize testing, certify conformance, or establish that an organization has adopted this practice.

An organization can have excellent testing guidance and still leave a reader wondering which version governed a test, who could change it, or whether an attractive template was ever approved. Document control answers those questions. It is not the testing method, the approval to test, or proof that a practice operates as written.

This component gives a practice a workable way to identify and maintain its standing direction. It is an adaptable framework component. A team adopting it must name its own authority, records requirements, approval roles, and systems of record before calling any local document “in force.” The framework's publication status is not an adopter's approval status.

## What this is for

Use this when standing documents have multiplied across methods, templates, guides, and team procedures. After applying it, a reader should be able to find one current artifact per identity, see its purpose and state, trace material changes, and locate gaps without treating a folder name as governance.

This component applies to **standing program direction**. A signed rules-of-engagement form, completed report, finding ticket, or evidence archive is a *record* governed by the adopter's records and security requirements. It is not a new controlled standard merely because its blank template is controlled.

## The five-question inclusion test

Create a controlled-document entry only when all five answers are yes.

| Question | Why it matters | If no |
|---|---|---|
| Will this guide recurring work rather than one event? | One-off material should not become permanent authority by accident. | Keep it with the engagement or decision record. |
| Is someone accountable for maintaining and reviewing it? | Stale standing direction is worse than a visible draft. | Name a steward and review trigger, or leave it as working material. |
| Does it direct or evidence a real practice capability? | The library should reflect work the practice must perform. | Retire, combine, or keep it as reference. |
| Does it contain substance rather than only links? | Navigation is useful but is not another controlled rule. | Make it a generated index or reader route. |
| Is this practice the authority for its content? | A testing team must not silently rewrite another function's policy or records. | Link to the authoritative owner and define only the local interface. |

For example, a blank report template can be controlled because it shapes recurring reports. Each completed report is a protected engagement record. An enterprise credential policy belongs to its policy owner; the testing practice may maintain a credential-handling guide that explains how testers comply within an engagement.

## Identity and register

Give each accepted component a stable name and a short handle. This framework uses a section number such as `30.5`: the folder number, then the component's place in that folder. A changed title does not change its identity, and a retired number is never reused for a different component. A citation should resolve to the current component and expose a prior-version trail when meaning changed.

Maintain **one authoritative register**. Every active ID resolves to exactly one current source, with these minimum fields:

| Field | Reader's question |
|---|---|
| ID, title, purpose, scope | What is this and what does it govern? |
| Capability and audience | Why is it in the library and who needs it? |
| Type or tier | Is it authority, a standard, a method, a template, or a record? |
| Accountable owner and approval role | Who maintains it, and who can place a local version in force? |
| Status, version, effective or candidate date | What state is true now? |
| Review trigger and dependency links | What change requires another look, and what else may be affected? |
| Location, revision record, and evidence of approval | Can a reviewer resolve and verify the claimed state? |

A register row is an index and a control check; it is not evidence that the described work actually happened. The public framework register should describe released **public components** and their maturity. An adopting organization's register describes **its own local implementation**. Neither copies the other's approval state.

Packages, role routes, website categories, folder trees, and capability maps are views over the register. They may make the library easier to use, but cannot become competing sources for version or status.

## Hierarchy without extra ceremony

This scheme uses five tiers. An adopter may rename them, but should preserve the distinction:

| Layer | Job | Example |
|---|---|---|
| Authority | Defines mandate, permission boundaries, and accountable decisions. | Program authorization. |
| Standard/framework | Defines standing outcomes and operating controls. | This document; umbrella methodology. |
| Procedure/method | Explains repeatable performance in a domain. | API testing method. |
| Template/job aid | Gives reusable structure without creating authority by itself. | Scope form; closing-deck template. |
| Record | Captures a completed activity or decision. | Signed scope; report; evidence set. |

Requirements move down; observed failures and learning move back up. A lower-level method or form may narrow execution for safety, but it must not expand testing authority beyond the locally approved boundary. Classifications are metadata and may change without renumbering the component.

## State, review, and approval

`Draft → In review → In force → Superseded → Retired` is a useful local state model. “In force” requires the adopter's recorded approval role and effective date. The public framework project uses publication labels separately: a public template can be available and still be *unadopted* by every reader organization.

Assign approval by **consequence**, not authorship or an imported org chart. A clarity correction may need a lighter path than a change to authorization, testing scope, safety, privacy, legal exposure, or external commitment. Route a specific legal or privacy decision to its actual owner; that does not automatically make that function the approver for every word of a testing method. The document owner maintains content. The approver authorizes a local baseline. A reviewer contributes bounded expertise. These roles may be held by different people.

At each material change, ask: Which downstream methods, forms, training aids, automation, reader routes, or records assumptions now disagree? Repair only the affected interfaces, and record what changed. The goal is truthful coordination, not a ceremonial signature chain.

## Revision history without invented facts

Keep a short, factual history: version, date, changed section/behavior, and resulting status. Put the latest entry last. Do not reconstruct an unrecorded approval, date, or change explanation to make the table look complete. Label an inherited gap honestly and correct it through the local authority.

An editorial edit fixes language, links, formatting, or accessibility without changing meaning. A material edit changes authority, scope, requirement, risk, or control effect. An urgent correction may need immediate containment followed by a recorded review. The label must describe what happened, not what the author hoped happened.

## Native artifacts are not defective prose

A spreadsheet, slide deck, or diagram may be the best form for the job. Do not remake it as Markdown merely to add a control header. Where a native artifact cannot carry sufficient metadata, keep a companion attestation bound to the exact artifact.

| Grade | Evidence | What to do |
|---|---|---|
| Witnessed | Valid ID/version/state inside the artifact | Verify it against the register. |
| Attested | Named, dated companion identifying the exact artifact and version; digest where feasible | Verify both files together and keep the weaker grade visible. |
| Unwitnessed | No trustworthy internal or companion control data | Do not claim the register row is verified. |

A companion that points to a missing file, an old version, or a different digest fails. An internal header takes precedence if both forms exist. Update the artifact and its companion in the same change.

## A practical adoption test

Try these five checks on one real method and one native artifact before migrating the library:

1. Can a new tester find the current method by ID without knowing the folder structure?
2. Can a lead tell who approves a material scope or safety change locally?
3. Can a reviewer trace the method's current status to a real approval, without inferring approval from a polished file?
4. Can the team point to the exact workbook or deck version, including its companion metadata if needed?
5. Can a lesson from a real engagement be recorded as a candidate change without silently rewriting the current method?

If any answer is no, the missing link becomes a named register or workflow gap. More documents are not the automatic remedy.

## Boundaries and next links

This component controls the *library*. It does not grant testing authorization, set records retention, establish a universal annual review cycle, assert compliance with ISO or another standard, or certify an adopting practice. The public register (§00.2), authorization boundary (§00.3), umbrella method (§20.1), completed-evidence guide (§30.1), and learning loop (§60.1) must be read as distinct components once their public versions are released. External standards and regulation references belong in the applicable component at a verified edition, not in an unqualified capability-equals-conformance table.

For local adoption, record: your accountable library owner; approval roles by consequence; authoritative record systems; status vocabulary; effective-date rule; review triggers; accessible location; and correction route. Those choices are local. The stable identity and evidence discipline are the transferable pattern.
