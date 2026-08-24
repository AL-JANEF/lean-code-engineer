# Backend Module

Load for APIs, service logic, background jobs, concurrency, or external integrations.

## Contracts

- Specify input validation, authorization, response shape, error semantics, idempotency, and compatibility.
- Keep transport parsing separate from domain decisions and infrastructure adapters.
- Bound request bodies, pagination, retries, concurrency, and external response sizes.

## Reliability

- Set timeouts and cancellation on outbound work; retry only transient, idempotent operations with jitter and limits.
- Make transaction boundaries and side-effect ordering explicit. Use an outbox or compensating action when atomicity ends.
- Preserve error cause and correlation context without exposing internals or sensitive data.
- Design jobs for at-least-once delivery unless the platform proves otherwise; make duplicate handling safe.
- Avoid shared mutable process state when multiple workers or restarts are possible.

## Verification

- Test validation, unauthorized/forbidden access, duplicate/retry behavior, and dependency failure where relevant.
- Exercise the actual serialization and persistence boundary, not only mocked domain methods.
- Confirm observability can distinguish caller errors, server faults, and dependency failures.

Load [database](../database/MODULE.md) only when persistence decisions are central.
