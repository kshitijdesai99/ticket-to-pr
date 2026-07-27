# Ticket to PR Skill

A lightweight agent skill for taking an engineering ticket through investigation, implementation, verification, review, and pull request creation.

The workflow keeps two meaningful human approval gates:

1. approve the evidence-backed implementation plan before files change
2. approve the verified diff and PR draft before it is committed and published

Implementation, testing, and self-review run together without approval prompts between mechanical steps. The skill pauses again only for a blocker, a material scope change, or an unsettled diagnosis.

## Workflow

```text
Understand and plan
        ↓ approval to edit
Implement and validate
        ↓ automatic continuation
PR preview
        ↓ approval to publish
Publish PR
```

For teams that require more checkpoints, explicitly request `strict mode`; it adds an approval after implementation and validation.

## Principles

- Investigate before proposing changes.
- Confirm the diagnosis before planning when the evidence is contradictory or inconclusive.
- Preserve pre-existing work and repository conventions.
- Keep changes within the approved scope.
- Never claim an unrun check passed.
- Review the complete diff before publishing.
- Never push or create a PR before approval.
- Never merge or force-push unless separately requested.

## Structure

```text
ticket-to-pr/
├── SKILL.md
└── references/
    ├── review-checklist.md
    └── pr-template.md
```

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
