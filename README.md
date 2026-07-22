# Ticket to PR Skill

A Claude skill that guides software engineering work from a ticket to a pull request through a structured, human-approved workflow.

## Workflow

```text
Ticket intake
→ Requirements confirmation
→ Codebase investigation
→ Implementation plan
→ Implementation
→ Verification
→ Self-review
→ PR draft
→ PR creation
```

The skill pauses after every stage and waits for explicit user approval before continuing.

## Structure

```text
ticket-to-pr/
├── SKILL.md
└── references/
    ├── workflow-stages.md
    ├── review-checklist.md
    └── pr-template.md
```

## Key Principles

* No coding before investigation and planning
* No scope expansion without approval
* No claims that tests passed unless they were run
* No PR creation before final user approval
* Clear handling of failures, risks, and open questions

## Usage

Add the `ticket-to-pr` folder to your Claude skills directory, then ask Claude to take an engineering ticket through implementation and PR creation.

Example:

```text
Use the ticket-to-pr skill for this issue.
Work through one stage at a time and wait for my approval after each stage.
```
