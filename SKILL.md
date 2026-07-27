---
name: ticket-to-pr
description: Take an engineering ticket through repository investigation, an approved implementation plan, coding, verification, self-review, and pull request creation. Use when the user explicitly asks for an end-to-end ticket-to-PR workflow or wants controlled approval before implementation and publishing; do not trigger for ordinary standalone coding requests that do not ask for this workflow.
license: MIT
---

# Ticket to PR

Move a ticket to a pull request with evidence, tight scope, and two meaningful approval gates.

## Default workflow

Use four phases:

1. **Understand and plan** — read-only investigation followed by approval to edit.
2. **Implement and validate** — branch, edit, test, and self-review without artificial pauses.
3. **PR preview** — present the verified change and request approval to publish.
4. **Publish** — commit the approved diff, push, and create the PR.

Open each progress report with `## Phase N — <name>` so the current position remains clear across sessions or handovers.

In the default mode, pause only at the end of Phases 1 and 3, or when a blocker or scope-control trigger requires a decision.

Treat `approved`, `continue`, `next`, `yes`, `yep`, and `ok` as approval only when they clearly answer the active gate. If the same message materially changes the requested scope, update the proposal and request approval again.

### Strict mode

When the user asks for `strict mode`, strict approval, or fully staged approval, also pause at the end of Phase 2 and wait before preparing the PR preview.

Announce that strict mode is active and which gates apply. Never select it yourself and never infer it from the size of the ticket.

## Phase 1 — Understand and plan

Do not modify files, create a branch, or commit during this phase.

### Establish the baseline

- Read the ticket and linked context.
- Check the current branch, base branch, working-tree state, and remotes.
- Report pre-existing changes and preserve them.
- Read repository instructions and conventions such as `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, CI configuration, task runners, and the repository PR template.

### Investigate with evidence

- Restate the requested behaviour, acceptance criteria, constraints, and non-goals.
- Reproduce or confirm the problem when practical. Record the command, input, output, test, log, or code evidence used.
- Trace the relevant path from entry point to observable result, including validation, transformations, persistence or external services, and existing tests.
- Identify the smallest boundary where expected and actual behaviour diverge.
- Separate the likely root cause from symptoms, unrelated weaknesses, and optional improvements.
- State uncertainty plainly when reproduction or confirmation is blocked.

### Stop instead of planning

Propose a plan only when the diagnosis is settled and the requirements are clear enough to scope. Ask one focused question instead of proposing a plan when:

- the evidence contradicts the ticket
- more than one root cause remains plausible on the available evidence
- reproduction is blocked in a way that leaves the root cause unconfirmed
- a material ambiguity would change scope, architecture, data model, API behaviour, backward compatibility, or acceptance criteria

Report the diagnosis and any competing possibilities with the evidence for and against each, then ask the user to confirm the direction. Do not resolve one of these conditions by silently choosing the most likely option and planning around it.

Minor ambiguity does not justify stopping. State the assumption, continue, and list it in the report.

### Propose the implementation

Present one concise report containing:

- confirmed requirements and remaining assumptions
- evidence and likely root cause
- required files and logic changes
- tests to add or update
- validation commands sourced from CI first, then task runners and repository documentation
- branch name and relevant repository conventions
- risks, rollback or compatibility concerns when relevant
- optional and out-of-scope work

End with one approval question authorizing the proposed implementation. Do not implement until the user approves.

## Phase 2 — Implement and validate

After approval:

1. Recheck the branch and working tree. Create the approved feature branch before editing when appropriate. Never move, discard, reset, or include pre-existing user changes without approval.
2. Make the smallest coherent change that satisfies the approved plan. Add or update tests alongside the code.
3. Run targeted checks first, followed by the relevant broader CI checks. Record exact commands and results. Never describe an unrun check as passing.
4. Read the complete diff and use `references/review-checklist.md`. Fix in-scope findings, rerun affected checks, and record the correction. Do not require another approval for corrections already covered by the plan.
5. Leave unrelated improvements out of the diff.

Do not commit, push, or create the PR yet. If strict mode is active, report the implementation and validation evidence and wait for approval before preparing the PR preview.

### Failure handling

- For an in-scope implementation or test failure, diagnose it, make the narrowest correction, and rerun the affected checks.
- For a likely pre-existing failure, compare against the base branch when safe and report the evidence.
- If a check is unavailable, state why, what remains unverified, and the exact command the user can run.
- Do not weaken or delete a valid test merely to obtain a passing result.

## Phase 3 — PR preview

Prefer the repository's PR template in this order:

1. `.github/pull_request_template.md`
2. `.github/PULL_REQUEST_TEMPLATE/*.md`
3. `docs/pull_request_template.md`
4. `references/pr-template.md`

Present:

- changed files and behaviour
- acceptance-criterion coverage
- exact verification results, including failures, skipped checks, and unavailable checks
- self-review findings and corrections
- remaining risks or limitations
- diff summary
- proposed commit message
- target branch, PR title, and complete PR description
- the exact publish actions that will follow approval

Do not claim the ticket is resolved if material limitations remain. Do not commit, push, or create the PR in this phase.

End with one question asking approval to commit the displayed changes, push the branch, and create the PR.

## Phase 4 — Publish

After approval:

1. Confirm the branch, base branch, remote, and working-tree contents again.
2. Stage only the approved files. Do not include unrelated user changes.
3. Commit using the approved message and repository convention.
4. Push the feature branch without force.
5. Create the PR using the approved title and body without silently rewriting them.
6. Return the PR URL, commands performed, and observed CI state.

If a required tool or permission is unavailable, provide exact manual commands and clearly state what was not completed. Do not merge, force-push, bypass checks, or modify a protected branch unless the user separately requests and authorizes it.

The PR completes the workflow. If the work revealed durable repository knowledge, mention the documentation opportunity briefly; update documentation only if the user explicitly asks. Do not turn ticket history, speculative conclusions, logs, secrets, personal data, or already-documented facts into permanent repository documentation.

## Scope control

Pause and request approval when new evidence requires a material departure from the approved plan, including:

- changing a public API or database schema
- adding a dependency
- changing authentication, authorization, or permissions
- altering deployment infrastructure
- expanding acceptance criteria
- performing a significant refactor
- modifying additional major components

Explain the evidence, available options, recommendation, and scope impact. Minor implementation details and in-scope review corrections do not require another approval.
