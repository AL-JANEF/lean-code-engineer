# Architecture

Read this when a change crosses components, introduces a durable boundary, changes dependency direction, or creates a hard-to-reverse trade-off.

## Decision frame

- What current and expected use cases must the design serve?
- Which invariants and quality attributes matter: reliability, security, latency, scale, operability, portability, or cost?
- What is the smallest boundary that localizes change without hiding essential behavior?
- Which option is easiest to test, observe, migrate, and remove?

## Design rules

- Keep domain policy separate from transport, storage, framework, and vendor adapters.
- Depend toward stable contracts; avoid cycles and shared mutable state.
- Make ownership of data, transactions, retries, timeouts, and cleanup explicit.
- Prefer boring, existing technology unless a measured constraint demands a new dependency or service.
- Design migrations for mixed versions, rollback, and partial failure.
- Add observability at boundaries where failures otherwise become ambiguous.

## When to record a decision

Write an ADR when the choice affects multiple components, introduces infrastructure or a dependency, changes a public contract, has meaningful alternatives, or will be costly to reverse. Capture context, decision, alternatives, consequences, migration, and rollback—without turning the ADR into a tutorial.

Do not redesign unrelated layers to make a local change look cleaner. Architecture should reduce the cost of known change, not speculate about every future possibility.
