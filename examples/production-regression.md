# Production Regression

## Request

> Users occasionally receive duplicate invoice emails after the queue worker times out. Diagnose and fix the regression without changing the delivery provider.

## Expected route

- `references/debugging.md` for the evidence loop.
- `modules/backend/MODULE.md` for retry and idempotency decisions.
- `references/security.md` only if logs or invoice data cross a sensitive boundary.

## Evidence shape

- Reproduce timeout/retry ordering and find the first duplicated side effect.
- Form a falsifiable hypothesis around acknowledgment or idempotency ownership.
- Fix the shared invariant and test duplicate delivery under retry.
- Run focused worker tests and the integration boundary; state if provider behavior was simulated rather than observed.
