# A synthetic API engagement through the practice

> **Fictional paper walkthrough.** No request described here was sent to a system; the accounts, responses, records, and review decisions are invented to exercise the framework. This example does not authorize testing, certify conformance, or show that any organization has adopted the practice.

The [component register](../../COMPONENTS.md) offers several ways into the framework. This example takes the working tester's route all the way through one bounded decision. Its job is to show what each component contributes, where a question changes hands, and what remains uncertain. The names, endpoint, records, responses, and dates below are invented.

## The scenario and the permission

Meridian Notes is a fictional application with an API at `https://api.meridian.invalid`. Two synthetic tenants, Alder and Birch, each own a note. The fictional owner confirms that neither note is shared: only its owning tenant may read it. The test question is narrow: can an Alder user read Birch's note by changing an object ID in a GET request?

The fictional target owner signs an engagement record permitting only `GET /v1/notes/{id}` against a resettable test environment. The record names the two test identities, two synthetic note IDs, a ten-request-per-minute ceiling, the evidence destination, the on-call contact, and the stop condition for unexpected data or behavior. It excludes writes, enumeration, production, other tenants, and third-party systems. [§00.3](../../components/00-start-here/00-3-authority-to-operate.md) describes the authority boundary; [§10.1](../../components/10-engagement/10-1-scoping-guide.md) and [§10.2](../../components/10-engagement/10-2-rules-of-engagement.md) provide the scope and rules-of-engagement decisions. This single-authorizer example does not need [§10.5](../../components/10-engagement/10-5-operational-brief.md); if a component later needs another party's decision, that brief can coordinate its component-level GO / NO-GO without granting permission. None of these templates grants permission by itself.

| Local record in this example | Value |
|---|---|
| Authorized target | `api.meridian.invalid`, resettable test environment only |
| Identity A | Synthetic Alder account `alder-tester` |
| Identity B | Synthetic Birch account `birch-tester` |
| In-scope objects | `note-A-101` and `note-B-202`, both fictional |
| Allowed action | Read-only GET against those two object IDs |
| Excluded | Writes, enumeration, production, other records, real customer data |
| Safety limit | At most ten requests per minute; stop on unexpected data or effect |

The tester would record the actual signed permission and local record IDs in the adopter's approved system, not in this example. [§30.3](../../components/30-evidence/30-3-credential-handling.md) governs account and secret handling, and [§30.4](../../components/30-evidence/30-4-opsec.md) constrains testing operational security.

## Design the test, then read the evidence

[§20.1](../../components/20-methods/20-1-method-framework.md) supplies the general method. [§20.3](../../components/20-methods/20-3-api.md) supplies the API-specific method: establish a known-good request for each identity, change one object reference at a time, compare the response with the ownership rule, and do not turn a tool's suggested **broken object-level authorization (BOLA)** label into a finding without an observed unauthorized effect. The fictional decision table is:

| Attempt | Caller | Requested note | Expected under the stated ownership rule | Fictional response | State |
|---|---|---|---|---|---|
| E1 | Alder | Alder's `note-A-101` | Content returned | `200`, Alder marker only | Positive control |
| E2 | Birch | Birch's `note-B-202` | Content returned | `200`, Birch marker only | Positive control |
| E3 | Alder | Birch's `note-B-202` | Denial without Birch content | `200`, Birch marker returned | Candidate weakness |
| E4 | Alder, fresh session | Birch's `note-B-202` | Denial without Birch content | `200`, same Birch marker returned | Reproduced under tested conditions |

These are **invented observations** to exercise the method. A real engagement would retain the raw requests and responses in a controlled evidence store, with account, environment, build, time, correlation ID, authorization record, redactions, and the precise note state. The owner-safe report copy would exclude tokens and unnecessary data. [§30.1](../../components/30-evidence/30-1-archival-files.md) and [§30.2](../../components/30-evidence/30-2-archive-storage.md) help decide what to retain and where; [§30.5](../../components/30-evidence/30-5-report-standard.md) defines the report/evidence presentation.

The result supports a narrow conclusion: in the fictional test build and state, an Alder identity retrieved Birch's in-scope synthetic note twice. It does not establish access to all Birch notes, production exposure, durable persistence, or any broader tenant pattern. A qualified reviewer should check that E1 and E2 prove the accounts and objects were correctly set up, that E3/E4 were authorized and not session mix-ups, and that the Birch marker came from the service rather than a cached or fabricated response. The reviewed disposition, not the first fluent explanation, travels into the report.

## Keep an unresolved question unresolved

The same fictional API advertises `DELETE /v1/notes/{id}`, but DELETE is excluded from this engagement. Documentation suggests a cross-tenant delete risk, and a scanner labels it high severity. Neither is a tested result. The report records that path as **not tested under this authorization**; no finding or severity is assigned. If the target owner wants that question answered, it returns to scope and permission rather than being slipped into the current test. [§10.3](../../components/10-engagement/10-3-scoping-map.md) helps map that changed scope to a method; §10.2 records the new limits if approved.

## Review, report, hand off, and retest

The report under §30.5 would identify the observed condition, its exact tested identities and object, reproducible steps within the authorized window, relevant evidence IDs, a scoped impact statement, uncertainty, and a remediation direction: enforce tenant ownership at the server-side object access decision. It would also state the untested DELETE question and any coverage limit. The closing meeting can use [§50.4](../../downloads/50-4-closing-meeting-deck.pptx) to put the result and the next decision owner in front of the right people.

After the issue enters the adopter's vulnerability-management route, the consulting service in [§50.3](../../components/50-support/50-3-consulting-guidebook.md) can explain the evidence and help an owner prepare a retest request. It does not silently enlarge scope or close the issue by email. A fictional retest would require a changed test build, the original condition and identities, authorized access, and a new evidence record. If Alder now receives a denial while each tenant still accesses its own note, the tester can report that the **original condition was not reproduced in that build**. The local issue owner, not this paper walkthrough, decides formal closure under local policy.

## What this route tests about the framework

A reader can start at permission, jump to the API method, follow a candidate through evidence and review, and see where the testing practice hands the issue to another owner. The route is intentionally small. If a component cannot tell the reader what record, decision, or handoff it owns in this example, the framework needs a correction. The same check can be repeated with a physical, mobile, infrastructure, or AI target, but those tests require their own authority, method, and safety constraints.
