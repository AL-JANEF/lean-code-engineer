# Debugging

Read this for regressions, flaky behavior, unclear failures, performance anomalies, or build errors.

## Evidence loop

1. State the expected and actual behavior precisely.
2. Reproduce with the smallest reliable command, input, or test. Preserve the first meaningful error.
3. Bound the failure by layer, data path, time, environment, and last known good state.
4. Form one falsifiable hypothesis and choose the cheapest observation that distinguishes it.
5. Fix the cause at the narrowest correct boundary.
6. Add a regression test that fails for the original mechanism, then run nearby and broader checks.

## Useful evidence

- Stack traces and exit codes before wrapper noise.
- Recent diffs, dependency or configuration changes, and environment differences.
- Data shape and lifecycle at the last good and first bad boundary.
- Timing, ordering, ownership, and cancellation for concurrent failures.

## Avoid

- Shotgun edits, random retries, cache deletion, or dependency upgrades without a hypothesis.
- Catch-all exception handling that hides the original failure.
- “Fixing” tests to match broken behavior unless the contract itself changed.
- Large refactors before a minimal reproduction proves they are necessary.

If reproduction is impossible, make observability the smallest next change and state what evidence it should collect. Use [security](security.md) before logging sensitive data and [verification](verification.md) for the completion gate.
