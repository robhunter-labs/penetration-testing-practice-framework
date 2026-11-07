# Contributing to the Open Practice Framework

This framework was opened so other practitioners can question it, adapt it and make it better. Contributions of every size are welcome, from a one-word correction to a reworked component.

## Ways to help

- **Report a correction.** Something is wrong, out of date, unclear or contradicts a cited source. Open a [correction issue](https://github.com/robhunter-labs/penetration-testing-practice-framework/issues/new?template=correction.yml). Corrections are kept visible and dated, not silently rewritten.
- **Share how you adapted it.** Say what you changed for your team and why. Open an [adaptation note](https://github.com/robhunter-labs/penetration-testing-practice-framework/issues/new?template=adaptation.yml) or start a Discussion. Knowing where a component didn't fit is as useful as a fix.
- **Ask a question.** Use Discussions for "how would you handle…" questions that aren't defects.
- **Propose a change.** Pull requests are welcome. For anything larger than a wording fix, please open an issue first so we can agree on the shape before you spend time on it.

## Ground rules for every contribution

- **Synthetic only.** Never post credentials, customer or employer details, restricted reports, real targets or live exploit evidence. Every example in this repository is synthetic, and contributions must be too.
- **Keep component identities stable.** Components are cited by section number and name (for example §30.5, Report Standard & Template), and the links between them depend on their paths. Change content freely, but don't renumber, merge, or delete a component without discussing it first.
- **Cite, don't copy.** Link to established guidance (NIST, OWASP, PTES, CREST, MITRE, PCI SSC) and describe how it's applied. Don't paste large passages from those sources.
- **Say what's assumed.** If a change rests on a particular regulatory context, team size or tool, say so. The framework is one implementation to adapt, not a mandate.
- **Be kind.** Critique the work, not the person. The [code of conduct](CODE_OF_CONDUCT.md) applies everywhere in the project.

How proposals are decided, and how maintenance widens over time, is in [GOVERNANCE.md](GOVERNANCE.md). Notable changes are recorded in the [change log](../CHANGELOG.md).

## Before you open a pull request

Run the checks in the README's **Checks** section (`python3 .github/scripts/check_opf.py . --strict` and its test file). CI runs the same commands.

## Sensitive reports

If you've found something that shouldn't be discussed in public, use GitHub's private vulnerability reporting (the **Security** tab → **Report a vulnerability**) instead of opening an issue. See [SECURITY.md](../SECURITY.md).

## Licensing

By contributing, you agree that your contribution is licensed under this repository's [MIT License](../LICENSE).
