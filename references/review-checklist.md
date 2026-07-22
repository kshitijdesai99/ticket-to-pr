# Self-Review Checklist

Review the completed diff for:

## Requirements
- Does the implementation match the ticket?
- Were any acceptance criteria missed?
- Were any assumptions left unresolved?

## Correctness
- Are edge cases handled?
- Are error paths correct?
- Could the change create race conditions or inconsistent state?
- Does the code preserve backward compatibility where required?

## Security and privacy
- Is input validated safely?
- Are permissions or authentication affected?
- Could sensitive data be logged or exposed?

## Data and infrastructure
- Is a migration required?
- Are configuration, deployment, or rollback changes needed?
- Are external dependencies handled safely?

## Performance
- Could the change introduce extra queries, network calls, blocking work, memory growth, or latency?

## Tests
- Do tests verify behaviour rather than implementation details?
- Are positive, negative, and regression cases covered?
- Are any tests misleading, flaky, or too broad?

## Code quality
- Are names and comments accurate?
- Is dead or unrelated code included?
- Does the change follow repository conventions?
- Is documentation required?

## Finding severity

- **Blocker:** Must be fixed before PR.
- **Important:** Should be fixed before PR.
- **Minor:** Optional improvement that does not block the PR.
- **No finding:** Explicitly state when no issue was found in a category.
