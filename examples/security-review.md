# Security Review

## Request

> Review the document download endpoint after a report that one tenant can guess another tenant's document identifier.

## Expected route

- `references/security.md` for assets, trust boundaries, authorization, and denied paths.
- `modules/security/MODULE.md` for vulnerability remediation and adjacent-path review.
- `modules/backend/MODULE.md` only if API contract or object loading behavior needs domain detail.

## Evidence shape

- Verify object-level authorization at the protected action, not only route authentication.
- Reproduce with two isolated tenant identities and non-sequential identifiers.
- Fix the narrow shared access boundary.
- Add allowed, unauthenticated, and cross-tenant denied tests without exposing real records.
- Record affected versions and residual adjacent paths; avoid public exploit detail before mitigation exists.
