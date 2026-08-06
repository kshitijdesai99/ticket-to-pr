# Self-Review Checklist

Read the complete diff and check each relevant category. Report concrete findings only; omit categories with no finding and never show a checklist transcript.

## Requirements and correctness

- Does the change satisfy every acceptance criterion?
- Are edge cases, error paths, state transitions, concurrency, and backward compatibility handled where relevant?

## Security, privacy, data, and infrastructure

- Are inputs, authentication, authorization, secrets, and sensitive data handled safely?
- Were repository scripts and documented commands inspected before execution?
- Did any command use credentials, deploy or migrate data, modify an external system, incur cost, or perform a destructive operation without explicit approval?
- Are migrations, configuration, deployment, rollback, or external-service changes required?

## Performance and reliability

- Does the change add unnecessary queries, calls, blocking work, memory growth, latency, retries, or failure modes?

## Tests and maintainability

- Does the change follow `references/implementation-principles.md`?
- Is user-facing or developer documentation required?

## Severity

- **Blocker:** must be corrected before declaring the work complete or delivering it.
- **Important:** should be corrected before completion or delivery unless the user accepts the risk.
- **Minor:** optional, in-scope polish.

Fix findings already covered by the approved plan, rerun affected checks, and report both the finding and correction. Pause only when a correction would materially change scope or require a user decision.
