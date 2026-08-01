# Ticket to PR Skill

A lightweight agent skill for taking an engineering ticket through investigation, implementation, verification, review, and pull request creation.

The default workflow keeps three human approval gates, one for each decision that is expensive to undo:

1. approve the diagnosis before any plan is designed around it
2. approve the implementation plan before any file changes
3. approve the verified diff and PR draft before it is committed and published

Implementation, testing, and self-review run together without approval prompts between mechanical steps. The skill pauses again only for a blocker, a safety-sensitive command, or a material scope change.

User-facing updates use plain language, at most five useful bullets, and one precise question. Logs and patches are summarized unless detail is requested or needed to show material risk.

## Workflow

```text
Investigate
        ↓ approval of the diagnosis
Plan
        ↓ approval to edit
Implement and validate
        ↓ automatic continuation
PR preview
        ↓ approval to publish
Publish PR
        ↓ opt-in
Optional retrospective
```

Investigation is gated separately from planning on purpose. A plan built on a wrong diagnosis is wasted work, and a confidently wrong diagnosis is the hardest kind to catch — so the evidence is shown before any design is done around it.

When investigation reveals meaningful scope alternatives, the same diagnosis gate can select **Minimal**, **Adjacent**, or **Broader** depth. The default is **Minimal**, and no extra gate is added.

After the PR is created, the skill offers an optional retrospective that proposes durable repository documentation and asks for approval before writing anything.

For teams that require more checkpoints, explicitly request `strict mode`; it adds an approval after implementation and validation.

## Principles

- Confirm the diagnosis with evidence before designing anything.
- Keep user-facing reports plain and brief, and ask one precise question that states what approval permits.
- Align on the intended result before using repository tools and clarify only when a user decision matters.
- Use supplied code-navigation clues; otherwise announce a narrow search and continue independently.
- Inspect repository-supplied commands before running them and request approval for commands with sensitive or external side effects.
- Preserve pre-existing work and repository conventions.
- Keep changes within the approved scope.
- Follow repository documentation conventions and explain public, complex, or non-obvious behaviour without adding redundant comments.
- Never claim an unrun check passed.
- Bind publishing to the approved file list and patch, and re-approve material drift.
- Never push or create a PR before approval.
- Never merge or force-push unless separately requested.
- Never write documentation from a retrospective without approval.

## Structure

```text
ticket-to-pr/
├── .github/workflows/validate-skill.yml
├── SKILL.md
├── references/
│   ├── review-checklist.md
│   └── pr-template.md
└── scripts/
    └── validate_skill.py
```

## Validation

Run the dependency-free validator locally:

```bash
python3 scripts/validate_skill.py .
```

GitHub Actions runs the same check on pushes and pull requests.

## Installation

Place this directory in the skills location used by your agent. For Claude Code:

```bash
git clone https://github.com/kshitijdesai99/ticket-to-pr.git ~/.claude/skills/ticket-to-pr
```

Restart the agent session after installation.

## Usage

```text
Use the ticket-to-pr skill to implement TICKET-123 and open a pull request.
```

For additional approval checkpoints:

```text
Use the ticket-to-pr skill in strict mode for TICKET-123.
```

## License

MIT — see `LICENSE`.
