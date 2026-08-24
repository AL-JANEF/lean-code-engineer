# Verification

Read this when selecting checks, judging completion, or communicating confidence.

## Risk-based ladder

Run the cheapest check that can disprove the change, then expand as warranted:

1. Static or structural check for edited files.
2. Focused test that exercises the changed behavior or regression.
3. Neighboring unit or integration tests across the affected boundary.
4. Build, type check, lint, migration validation, or end-to-end journey when the change can affect them.
5. Security, performance, compatibility, or rollback checks for high-impact paths.

## Match evidence to risk

- Public contract or schema: compatibility and consumer checks.
- Auth, payment, privacy, or destructive path: denied cases, audit behavior, and rollback.
- Concurrency or retry behavior: ordering, cancellation, idempotency, and race-sensitive tests.
- UI behavior: loading, empty, error, keyboard, responsive, and accessibility states where relevant.
- Configuration or deployment: parse, dry-run, environment differences, and safe rollback.

## Evidence rules

- Record the exact command, meaningful result, and scope.
- A passing test proves only what it asserts; inspect weak or newly changed assertions.
- Do not hide failures as “unrelated” without evidence.
- Do not claim runtime, platform, or host compatibility from static validation alone.

If a check is unavailable, explain the blocker, run the strongest safe alternative, and name the remaining step. Completion means the requested behavior and relevant invariants are supported by evidence, not merely that the edit is finished.
