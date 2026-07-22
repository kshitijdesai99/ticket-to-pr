# Retrospective and Knowledge Capture

Use this reference only after the pull request has been created or prepared and the user explicitly opts into the retrospective.

## Purpose

Convert expensive investigation and implementation discoveries into durable repository knowledge without turning documentation into a ticket log.

## Durable knowledge test

A finding is a good documentation candidate when most of the following are true:

- Future work is likely to need it.
- Discovering it required meaningful repository exploration.
- It is verified by code, tests, configuration, or successful execution.
- It explains component ownership, data flow, commands, constraints, or conventions.
- It remains useful after the current ticket is closed.
- There is a clear canonical document where it belongs.

Do not persist a finding merely because it was difficult to discover.

## Exclusion test

Do not add:

- ticket chronology or conversational summaries
- implementation details already obvious from the code
- speculative architectural conclusions
- one-off failures that are unlikely to recur
- raw logs or large command outputs
- credentials, access details, tokens, customer data, or personal information
- duplicate or conflicting instructions
- claims that were not verified

## Preferred destination order

1. Update an existing canonical document.
2. Add a focused section to an existing document.
3. Create a focused subject document under `docs/`.
4. Create a generic notes file only when the repository already uses that convention.

Do not create a new `docs/` folder solely to store a trivial observation.

## Proposal template

```markdown
## Stage 10 — Retrospective Proposal

### Reusable knowledge candidates

1. **Finding**
   - Evidence: ...
   - Future value: ...
   - Proposed destination: `path/to/document.md`
   - Proposed change: ...

### Excluded findings

- Finding — excluded because it is ticket-specific, speculative, sensitive, duplicated, or too transient.

### Proposed file changes

- Update `path/to/document.md`: ...
- Create `docs/topic.md`: ...
```

End with:

`Do you approve these retrospective documentation changes?`

## Documentation style

Write facts as direct repository guidance.

Weak:

```text
During TICKET-123 we eventually found that tests need a special command.
```

Strong:

```text
Run DOB workflow tests with `pytest tests/test_capture_dob.py`; the generic API test suite does not cover workflow-level date parsing.
```

Weak:

```text
The agent spent time looking in schemas.py, but the code was elsewhere.
```

Strong:

```text
Date-of-birth parsing is owned by `app/workflow/capture_dob.py`; API schemas validate shape but do not define accepted date formats.
```

## Final report template

```markdown
## Stage 10 — Retrospective Complete

### Files changed
- `path/to/document.md`: ...

### Durable knowledge captured
- ...

### Not persisted
- ...

### Verification
- Documentation diff reviewed
- Paths and commands verified
- Sensitive-data check completed
- No production code changed
```
