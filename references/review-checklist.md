# Self-Review Checklist

Read the complete diff and check each relevant category. Report concrete findings; summarize categories with no finding instead of producing a verbose checklist transcript.

## Requirements and correctness

- Does the change satisfy every acceptance criterion without expanding scope?
- Are edge cases, error paths, state transitions, concurrency, and backward compatibility handled where relevant?

## Security, privacy, data, and infrastructure

- Are inputs, authentication, authorization, secrets, and sensitive data handled safely?
- Are migrations, configuration, deployment, rollback, or external-service changes required?

## Performance and reliability

- Does the change add unnecessary queries, calls, blocking work, memory growth, latency, retries, or failure modes?

## Tests and maintainability

- Do tests verify observable behaviour, including regression and failure cases?
- Does every new or materially rewritten function or class have a short plain-language explanation and one concrete usage or input-to-output example?
- Does the code follow repository conventions and avoid dead code, misleading comments, unrelated cleanup, and needless complexity?
- Is user-facing or developer documentation required?

## Severity

- **Blocker:** must be corrected before PR creation.
- **Important:** should be corrected before PR creation unless the user accepts the risk.
- **Minor:** optional, in-scope polish.

Fix findings already covered by the approved plan, rerun affected checks, and report both the finding and correction. Pause only when a correction would materially change scope or require a user decision.
