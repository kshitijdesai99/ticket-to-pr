# Workflow Stages

## Stage 1 — Ticket Intake

### Goal
Understand the requested outcome without changing code.

### Actions
- Read the ticket and linked context.
- Restate the desired behaviour in plain language.
- Identify current behaviour, acceptance criteria, constraints, and non-goals.
- Separate confirmed requirements from assumptions.
- Identify missing information that materially affects scope.

### Restrictions
- Do not modify code.
- Do not create an implementation plan.
- Do not invent acceptance criteria.

### Output
Include:
- requested outcome
- acceptance criteria
- constraints
- assumptions
- open questions

End with: `Is this understanding correct before I investigate the codebase?`

---

## Stage 2 — Requirements Confirmation

### Goal
Resolve material ambiguity before repository investigation.

### Actions
- Incorporate the user's corrections.
- Ask only questions that could change scope, architecture, data model, API behaviour, backward compatibility, or testing requirements.
- Ask one concrete question at a time.
- Mark minor assumptions explicitly when they do not justify blocking progress.

### Restrictions
- Do not inspect or modify code until requirements are confirmed.
- Do not repeat questions already answered.

End with: `Are the requirements confirmed so I can investigate the implementation?`

---

## Stage 3 — Codebase Investigation

### Goal
Find where the behaviour is implemented and determine the real scope.

### Actions
Inspect without modifying:
- entry points
- relevant modules and functions
- data flow
- existing tests
- callers and downstream consumers
- configuration or schema dependencies
- similar implementations
- repository conventions
- test, lint, format, type-check, and build commands

Separate:
- logic changes
- infrastructure changes

Surface hidden complexity such as migrations, public contracts, race conditions, external dependencies, missing test infrastructure, and unclear ownership.

### Restrictions
- Do not edit files.
- Do not commit changes.
- Do not claim certainty without evidence.

### Output
Include:
- relevant files
- current flow
- existing coverage
- smallest likely change
- hidden complexity
- open questions

End with: `Does this investigation look correct before I create the implementation plan?`

---

## Stage 4 — Implementation Plan

### Goal
Create a precise, reviewable plan based on repository evidence.

### Actions
Specify:
- exact files to change
- logic changes
- tests to add or update
- migrations or configuration changes
- error handling
- observability or documentation changes when relevant
- validation commands
- compatibility and rollback considerations
- known risks

Separate required work, optional improvements, and out-of-scope work.

### Restrictions
- Do not modify code.
- Do not include unrelated refactors.
- Do not hide unresolved architectural choices inside implementation steps.

End with: `Do you approve this plan for implementation?`

---

## Stage 5 — Implementation

### Goal
Implement only the approved plan.

### Actions
- Make the smallest coherent change.
- Follow repository conventions.
- Add or update tests with production code.
- Avoid unrelated cleanup.
- Track every changed file.

Stop and return to planning if implementation reveals a material flaw or requires an unapproved scope expansion.

### Restrictions
- Do not create a PR.
- Do not claim tests pass before running them.
- Do not silently expand scope.

### Output
Include:
- changed files
- behaviour implemented
- deviations from plan
- concise diff summary

End with: `Is the implementation scope acceptable before I run verification?`

---

## Stage 6 — Verification

### Goal
Collect evidence that the implementation works.

### Actions
Run the relevant available checks in this order where appropriate:
1. targeted tests
2. broader test suite
3. linting
4. formatting checks
5. type checking
6. build or compilation
7. integration tests
8. manual validation

Record the exact command and result.

If a check cannot be run, state why, what remains unverified, and how the user can run it.

If a check fails, show the failure, assess whether it is related, and propose the smallest next action.

### Restrictions
- Never claim unrun checks passed.
- Do not hide flaky or unrelated failures.
- Do not create the PR.

End with: `Is this verification sufficient before I review the diff?`

---

## Stage 7 — Self-Review

### Goal
Review the diff as an independent code reviewer.

Read `review-checklist.md` and classify findings as:
- Blocker
- Important
- Minor
- No finding

Present findings before further edits. Re-run affected checks after corrections.

### Output
Include:
- findings
- ticket compliance
- readiness recommendation

End with: `Do you agree with this review and want me to prepare the PR?`

---

## Stage 8 — PR Draft

### Goal
Prepare an accurate PR title and description from verified evidence.

Read `pr-template.md`.

### Rules
- Use actual results only.
- Do not exaggerate scope.
- Mention known limitations.
- Link the ticket when available.
- Include migration, rollout, or rollback notes when relevant.

End with: `Do you approve this PR title and description?`

---

## Stage 9 — PR Creation

### Goal
Create the PR only after final approval.

### Preconditions
Confirm:
- implementation is complete
- approved changes are committed
- branch is pushed
- verification results are known
- self-review is complete
- PR draft is approved
- repository and target branch are confirmed

### Actions
When tools and permissions are available:
- create or confirm the feature branch
- commit approved changes
- push the branch
- create the PR
- return the PR link

When unavailable:
- provide exact commands
- provide the approved PR title and body
- clearly state the PR was not created automatically

### Restrictions
- Do not merge unless separately requested.
- Do not force-push unless explicitly approved.
- Do not bypass required checks.

---

## Stage 10 — Optional Retrospective and Repository Knowledge Capture

### Goal
Preserve verified, reusable knowledge discovered during the ticket so future engineers or agents do not repeat the same investigation.

This stage is optional and must not block or delay the completed PR.

### Opt-in gate
After Stage 9, ask:

`Would you like me to run an optional retrospective and propose reusable repository documentation updates?`

If the user declines:
- do not create or update any retrospective files
- state that the workflow is complete
- stop

If the user accepts:
- read `retrospective.md`
- inspect the repository's existing documentation structure
- identify reusable knowledge candidates
- continue with the proposal step below

### Knowledge analysis
Separate findings into:

- **Ticket-specific outcome:** useful for the PR or ticket history, but not durable documentation
- **Reusable repository knowledge:** useful across future changes
- **Open or speculative finding:** not safe to document as fact

Examples of reusable knowledge:
- the canonical module that owns a behaviour
- an unexpected but verified data flow
- the correct command for targeted tests
- repository-specific implementation conventions
- a recurring integration constraint
- a verified setup, deployment, or debugging requirement

Examples that should not be persisted:
- raw debugging transcripts
- temporary branch or ticket details
- unverified theories
- credentials, tokens, secrets, customer data, or personal information
- facts already documented accurately elsewhere

### Choose target files
Prefer updating existing canonical files, such as:

- `AGENTS.md` or `CLAUDE.md` for repository-specific agent instructions
- `README.md` for setup and entry-point information
- `docs/architecture.md` for component ownership and data flow
- `docs/testing.md` for verified test commands and test structure
- `docs/development.md` for development workflows and conventions
- another existing document clearly responsible for the discovered knowledge

Create a new documentation file only when no suitable canonical file exists. Prefer a clear subject-specific file under `docs/` rather than a generic dumping ground.

### Proposal gate
Before editing repository files, present:

- reusable knowledge candidates
- evidence supporting each candidate
- exact files to create or update
- concise summary of each proposed edit
- items deliberately excluded and why

End with:

`Do you approve these retrospective documentation changes?`

Do not edit repository files until the user explicitly approves this proposal.

### Write approved documentation
After approval:

- create or update only the approved files
- integrate knowledge into the relevant existing sections
- keep wording factual, concise, and repository-specific
- avoid duplicating existing content
- preserve existing formatting and conventions
- do not modify production code as part of this stage

### Verify the retrospective changes
Review the documentation diff and confirm:

- every statement is supported by evidence
- no secrets or sensitive data were added
- no ticket-specific noise was promoted into durable docs
- links, paths, and commands are accurate
- no unrelated files changed

### Output
Include:

- files created or updated
- durable knowledge captured
- knowledge deliberately not persisted
- concise diff summary
- any remaining uncertainty

End with:

`Do you approve the retrospective documentation changes?`

If the user requests corrections, remain in Stage 10, update the documentation, and ask for approval again.
