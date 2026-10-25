# Contributing

Contributions from finance, accounts, tax, legal and compliance professionals are welcome.

## Adding or improving a skill

1. Put the skill under the plugin it belongs to: `plugins/<plugin>/skills/<skill-name>/SKILL.md`, with `references/` and `scripts/` folders if needed.
2. The SKILL.md needs YAML frontmatter with `name` (matching the folder) and a `description` that says what the skill does and when to use it.
3. Cite the regulation or standard behind every rule, and mark anything that changes often (rates, thresholds, timelines) as "confirm against the latest notification".
4. No client data, company names or real figures. Use made-up examples.
5. If you add a slash command, put it in `plugins/<plugin>/commands/`.
6. Run `claude plugin validate .` before opening a pull request.

## Reporting a problem

Open an issue with the skill name, what you asked, what Claude did and what the correct treatment is (with the rule reference).
