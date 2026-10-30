# Open Practice Framework

*This repository: `penetration-testing-practice-framework`.*

The Open Practice Framework (OPF) is a practitioner-built, inspectable implementation of the work **around** a penetration test: authority, preparation, technical methods, evidence, review, reporting, support, people, and improvement — and the links that make those parts a practice rather than a shelf of templates. It sits **beside** established testing and programme guidance. It is **not** an accreditation scheme, a replacement for those sources, a certification, or permission to test.

Its value is in the decisions it makes easier to see and improve — not in the number of documents in the repository. Use the parts that help, question the parts that don't, and bring a better path back.

## Start here

**Open the [component register](COMPONENTS.md) and enter through your problem.** The register lists every component, its job, its type, and its status. Pick the route that matches the question in front of you:

| If you are trying to… | You are a… | Begin with |
|---|---|---|
| Stand up or improve a testing service | **Practice lead** | [00.1](COMPONENTS.md) document control → [00.3](COMPONENTS.md) authority → [20.1](COMPONENTS.md) method → scoping, people, support, learning |
| Turn a bounded engagement into defensible tests and evidence | **Working tester** | [10.1](COMPONENTS.md)/[10.2](COMPONENTS.md) scope & rules → [20.1](COMPONENTS.md) → the relevant domain method ([20.2](COMPONENTS.md)–[20.13](COMPONENTS.md)) → [a synthetic API walkthrough](examples/api-engagement/README.md) → evidence, report, archive |
| Trace a conclusion back to what was actually done | **Reviewer / assurance partner** | [00.3](COMPONENTS.md) authority → [30.5](COMPONENTS.md) report standard → [60.2](COMPONENTS.md) self-assessment → [50.5](COMPONENTS.md)–[50.8](COMPONENTS.md) audit & disclosure |
| Copy, tailor, question, or improve a part without mistaking it for a mandate | **Adopter / contributor** | this README → the [register](COMPONENTS.md) → a component's own sources and limits → the [correction route](SECURITY.md) |

These are reader routes through one body of work, not prescribed job titles or an org chart.

## The baseline is human-led testing

A qualified person authorizes, plans, performs, reviews, and is accountable for the work. No component turns a scanner's suggestion or a generated sentence into an accepted finding, and no component transfers authority from a person.

**AI appears only as two distinct, versioned extensions:**
- **AI as a target** — testing an AI/LLM system (the AI/LLM method, §20.13).
- **AI as a testing capability** — an agent or tool that assists a human-led practice (§90.1, §90.2, §90.4).

Either extension must say where an agent may act, what it may read and send, how actions and evidence are recorded, who validates a finding, and where the work returns to a person. Claims about speed, quality, cost, or staffing need observed measurement; enthusiasm is not a method. A reader can understand and improve the human-led practice without first accepting any AI roadmap.

## Beside the standards, not over them

[CREST's Guide to Penetration Testing](https://www.crest-approved.org/wp-content/uploads/2023/04/A-Guide-to-Penetration-Testing-2022.pdf) covers establishing and managing a penetration-testing programme; [OWASP's testing guidance](https://wstg.owasp.org/) provides substantial domain method; NIST, PTES, and MITRE guidance remain first-class references. The framework does not condense, replace, or endorse them. It contributes an inspectable example of **one implementation**: connected, editable components showing how a team might translate that guidance into working roles, methods, records, review points, and a correction loop. Current external references are cited where used and should be read on their own terms, in their current edition at the time of an engagement.

## What is in this release

- **[56 active components](COMPONENTS.md)** across authority, engagement design, technical methods, evidence, operations, support, learning, and AI/R&D extensions. The register gives each component's job and direct path. §20.14 is deliberately a catalogue entry, not a distributed tactical workbook.
- **[A synthetic API engagement walkthrough](examples/api-engagement/README.md)** connects authority, scope, method, evidence, review, reporting, and retest in one paper example. It records no real test execution or observed outcome.
- **[§50.3 — Penetration Testing Consulting Guidebook](components/50-support/50-3-consulting-guidebook.md)** explains how a team gives post-test technical questions, retest, closure, escalation, and rotation a reliable home. Its companion essay, [*The Leverage Between Penetration Tests*](https://robhunterworks.com/writing/leverage-between-tests/), explains the experience behind the pattern. §50.3 is one support component, not the framework's front door.
- **[Conceptual diagrams](diagrams)** include an engagement flow and two consulting-service models. They illustrate decisions, not measured outcomes or staffing formulas.

## Downloads

Some components are usable only in their native format. The [download list](COMPONENTS.md#native-downloads) includes a fillable scoping form and worked example (§10.4), a decision-rights matrix (§40.5), and two training/meeting decks with PDF equivalents (§50.4, §40.11). The tactical-checklist identity (§20.14) is **catalogue-only**: it carries no workbook download by design — an adopter maintains its own checklists mapped to its scope and standards.

## Boundaries

This repository contains no employer procedures, customer records, issue data, credentials, controlled reports, or private engagement evidence. Every example is synthetic. A public document does not certify that any organization adopted it, prove a practice is operating, or grant authority to test. Adopters supply their own authority, obligations, people, systems of record, and risk decisions.

## Security and corrections

Use GitHub issues for corrections to public material. Do not post credentials, customer details, restricted reports, or live exploit evidence. For a sensitive report, use GitHub's private vulnerability reporting (the **Security** tab → **Report a vulnerability**) rather than opening a public issue. See [SECURITY.md](SECURITY.md).

---

Copyright © 2026 Rob Hunter. Original material is released under the [MIT License](LICENSE).

## Checks

The repository check needs Python 3.9+ (standard library only) and, for PDF text, `pdftotext` from poppler-utils.

```sh
python3 .github/scripts/check_opf.py . --strict      # links, prohibited paths, public markers
python3 .github/scripts/test_check_opf.py            # the checker's own planted-marker tests
```

To also check for terms you keep private, put them in a file **outside** the repository and run with `OPF_PRIVATE_TERMS=/path/to/terms.txt`. No private term is stored in this repository, hashed or plain.
