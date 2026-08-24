# Benchmark Methodology

## Question

How much static instruction context can progressive disclosure avoid compared with loading every reference and module for every task?

## Metrics

- **Core estimate:** characters in `SKILL.md` divided by four, rounded up.
- **Full estimate:** core plus all Markdown under `references/` and `modules/`.
- **Route estimate:** core plus files selected by the deterministic routing fixture.
- **Estimated savings:** `1 - route / full`.

These are regression proxies. Tokenization varies by model and language; caching, tool results, conversation history, output tokens, latency, price, and solution quality are outside this measurement.

## Gates

`./scripts/benchmark.sh --check` fails when:

- the core exceeds the configured estimate budget;
- a fixture references a missing route;
- median route savings fall below the configured threshold.

Gates protect architecture, not prose aesthetics. They may be revised with a documented reason and before/after results.

## Reproduce

```bash
./scripts/benchmark.sh
./scripts/benchmark.sh --format json
./scripts/benchmark.sh --check
```

For model-quality claims, use blinded repository tasks and score correctness, security, and verification independently. Do not infer quality from token estimates alone.
