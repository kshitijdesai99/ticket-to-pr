# Request to Code Skill

A lightweight agent skill for turning a direct chat request or optional ticket into a verified code change. Commit, push, and pull-request delivery are optional.

The default workflow keeps two approval gates before editing:

1. approve the diagnosis before any plan is designed around it
2. approve the implementation plan before any file changes

When commit, push, or PR delivery is requested, a third gate approves the verified diff and exact delivery actions.

Implementation, testing, and self-review run together without approval prompts between mechanical steps. The skill pauses again only for a blocker, a safety-sensitive command, or a material scope change.

User-facing updates use plain language, at most five useful bullets, and one precise question. Logs and patches are summarized unless detail is requested or needed to show material risk.

## Workflow

```text
Investigate
        ↓ approval of the diagnosis
Plan
        ↓ approval to edit
Implement and validate
        ├── local verified change (default)
        └── requested delivery
                ↓ approval of exact actions
            Commit, push, or PR
```

Investigation is gated separately from planning on purpose. A plan built on a wrong diagnosis is wasted work, and a confidently wrong diagnosis is the hardest kind to catch — so the evidence is shown before any design is done around it.

When investigation reveals meaningful scope alternatives, the same diagnosis gate can select **Minimal**, **Adjacent**, or **Broader** depth. The default is **Minimal**, and no extra gate is added.

Tickets add context but are never required. The current chat request remains the primary source of intent unless the user explicitly asks to follow a ticket exactly.

The retrospective runs only when explicitly requested.

For teams that require more checkpoints, explicitly request `strict mode`; it adds an approval after implementation and validation.

## Principles

- Confirm the diagnosis with evidence before designing anything, and keep changes inside the approved scope.
- Never claim an unrun check passed, and never commit, push, or create a PR unless it was requested and approved.
- Preserve pre-existing work and repository conventions.

`SKILL.md` is the single source of truth: workflow, coding standards, self-review checklist, and fallback PR template all live in that one file.

## Structure

```text
request-to-code/
├── .github/workflows/validate-skill.yml
├── SKILL.md
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
git clone https://github.com/kshitijdesai99/request-to-code.git ~/.claude/skills/request-to-code
```

Restart the agent session after installation.

## Usage

```text
Use request-to-code to add input validation to the signup endpoint.
```

An optional ticket and delivery request can be included:

```text
Use request-to-code to implement TICKET-123 and open a pull request.
```

For an additional checkpoint after implementation:

```text
Use request-to-code in strict mode to refactor the cache module.
```

## License

MIT — see `LICENSE`.
