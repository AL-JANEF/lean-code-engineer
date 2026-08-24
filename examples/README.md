# Examples

These examples show routing and evidence expectations, not canned answers. Repository instructions and the actual code remain authoritative.

- [Small feature](small-feature.md) — core plus ordinary engineering.
- [Production regression](production-regression.md) — debugging and backend guidance.
- [Security review](security-review.md) — threat-first routing and denied-path tests.
- [Optional team](optional-agent-team.md) — when parallel agents are and are not justified.

Preview the deterministic route for any prompt:

```bash
./scripts/route_context.py "Fix the auth bypass regression in the API" --format json
```
