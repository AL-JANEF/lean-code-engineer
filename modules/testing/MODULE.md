# Testing Module

Load for test strategy, regression design, fixtures, flaky suites, or confidence gaps.

## Choose the boundary

- Test behavior at the lowest level that observes the real failure mechanism.
- Use integration or contract tests when serialization, persistence, framework wiring, or service boundaries matter.
- Keep a small end-to-end set for critical user journeys; do not use it to cover every branch.

## Design strong tests

- Arrange only the state relevant to the behavior; assert meaningful outputs and side effects.
- Include boundary, invalid, denied, empty, and failure cases according to risk.
- Prefer deterministic clocks, identifiers, randomness, and schedulers over sleeps and retries.
- Keep fixtures readable and representative; builders should expose important values.
- Avoid tests that merely mirror implementation, snapshots with unreviewed noise, or mocks that cannot fail like the real dependency.

## Flakiness

- Reproduce and classify timing, order, shared-state, network, resource, or environment causes.
- Fix isolation or synchronization. Quarantine only with an owner, issue, evidence, and expiry.

Run the focused regression first, then the smallest suite that crosses the affected boundary. Use [verification](../../references/verification.md) for completion evidence.
