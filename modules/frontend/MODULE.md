# Frontend Module

Load for browser UI, component state, rendering, accessibility, or client-side security.

## Boundaries

- Treat the server as authoritative for permissions and protected data; client checks improve UX, not authorization.
- Keep server state, URL state, form state, and transient UI state distinct.
- Reuse the project's component, styling, routing, data-fetching, and error patterns.

## Implementation

- Define loading, empty, success, stale, and error states before polishing the happy path.
- Preserve semantic HTML and native interaction behavior; add ARIA only when semantics are insufficient.
- Keep keyboard order, focus restoration, labels, reduced motion, contrast, zoom, and responsive layout observable.
- Avoid unsafe HTML injection. Encode for the rendering context and review any sanitizer configuration.
- Prevent race-driven stale updates with cancellation, request identity, or the framework's established data layer.
- Do not add a state library or abstraction for local state without demonstrated cross-component need.

## Verification

- Test user-visible behavior rather than component internals.
- Cover one failure/empty state and keyboard interaction when relevant.
- Measure bundle or render changes only when the task affects them; do not optimize from intuition.

Use [security](../../references/security.md) for trust boundaries and [verification](../../references/verification.md) for the final ladder.
