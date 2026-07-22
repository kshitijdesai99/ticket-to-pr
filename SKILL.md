---
name: ticket-to-pr
description: Guides software engineering work from an issue or ticket through requirements clarification, repository investigation, implementation planning, coding, verification, self-review, pull request creation, and optional post-PR knowledge capture. Use when the user asks to implement a ticket, fix an issue, build a feature, take engineering work from ticket to PR, or preserve reusable repository knowledge discovered during the work.
---

# Ticket to PR

Guide engineering work through a controlled, human-approved workflow.

## Core rule

Never move to the next stage without explicit user approval.

Valid approval signals include `approved`, `continue`, `next`, `yes`, `yep`, and `ok` when they clearly answer the current approval question.

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
10. Optional retrospective and repository knowledge capture

Read `references/workflow-stages.md` before starting and follow the instructions for the current stage only.

Stage 10 is optional and does not block PR completion. Never create or update repository documentation for the retrospective unless the user explicitly opts in and approves the proposed file changes.

## Interaction protocol

At every stage:

1. Perform only the work allowed in that stage.
2. Present the result clearly.
3. Surface assumptions, risks, and unresolved questions.
4. Ask exactly one low-effort approval question.
5. Stop and wait for the user's response.

Do not perform hidden implementation work while waiting for approval.

## Scope control

The approved implementation plan defines the allowed implementation scope.

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
Use `references/retrospective.md` only after PR creation and only when the user opts in.

## Retrospective safeguards

The retrospective captures reusable repository knowledge, not a narrative summary of the ticket.

Only preserve findings that are:

- supported by repository evidence or completed verification
- useful across future tasks
- appropriate for version-controlled documentation
- unlikely to expose secrets, credentials, personal data, or sensitive operational details

Prefer updating an existing canonical document over creating a new notes file. Do not write speculative conclusions, transient debugging output, duplicated documentation, or ticket-specific history into the repository.

## Tool and permission limits

If repository, Git, GitHub, or CI tools are unavailable, do not pretend the action was completed. Provide the exact commands or content the user needs and clearly identify what remains manual.

Do not merge, force-push, bypass checks, or alter protected branches unless the user explicitly requests it and the available tools permit it.
