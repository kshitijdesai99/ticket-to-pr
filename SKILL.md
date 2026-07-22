---
name: ticket-to-pr
description: Guides software engineering work from an issue or ticket through requirements clarification, repository investigation, implementation planning, coding, verification, self-review, and pull request creation. Use when the user asks to implement a ticket, fix an issue, build a feature, or take engineering work from ticket to PR.
---

# Ticket to PR

Guide engineering work through a controlled, human-approved workflow.

## Core rule

Never move to the next stage without explicit user approval.

Valid approval signals include `approved`, `continue`, `next`, `yes`, `yep`, and `ok`.

If the user provides corrections, questions, or new constraints, remain in the current stage, update the work, and ask for approval again.

Do not interpret silence as approval.

## Workflow

Follow these stages in order:

1. Ticket intake
2. Requirements confirmation
3. Codebase investigation
4. Implementation plan
5. Implementation
6. Verification
7. Self-review
8. PR draft
9. PR creation

Read `references/workflow-stages.md` before starting and follow the instructions for the current stage only.

## Interaction protocol

At every stage:

1. Perform only the work allowed in that stage.
2. Present the result clearly.
3. Surface assumptions, risks, and unresolved questions.
4. Ask exactly one low-effort approval question.
5. Stop and wait for the user's response.

Do not perform hidden implementation work while waiting for approval.

## Scope control

The approved implementation plan defines the allowed scope.

Stop and ask for approval when new information requires any of the following:

- changing a public API
- modifying a database schema
- adding a dependency
- changing authentication or permissions
- altering deployment infrastructure
- expanding acceptance criteria
- making a significant refactor
- modifying additional major components

Explain what was discovered, why it matters, the available options, and the scope impact of each option.

## Evidence rules

Never claim a test, linter, formatter, type checker, build, or other check passed unless it was actually run and passed.

Before creating a PR, require:

- confirmed ticket understanding
- repository investigation
- approved implementation plan
- changed-file summary
- verification evidence
- self-review findings
- approved PR title and description

Use `references/review-checklist.md` during self-review.
Use `references/pr-template.md` when preparing the PR.

## Tool and permission limits

If repository, Git, GitHub, or CI tools are unavailable, do not pretend the action was completed. Provide the exact commands or content the user needs and clearly identify what remains manual.

Do not merge, force-push, bypass checks, or alter protected branches unless the user explicitly requests it and the available tools permit it.
