# Performance Module

Load for measured latency, throughput, memory, CPU, bundle size, startup, or infrastructure cost problems.

## Measure first

- Define the user-visible metric, workload, percentile, environment, and acceptable threshold.
- Reproduce with representative data and isolate measurement noise before editing.
- Profile the dominant resource and trace the critical path; averages can hide tail pain.

## Optimize

- Remove unnecessary work before caching, parallelizing, or changing infrastructure.
- Fix algorithmic or query complexity before micro-optimizing syntax.
- Bound caches by memory, lifetime, invalidation, and tenant/security scope.
- Treat concurrency as a trade-off involving contention, rate limits, ordering, and failure amplification.
- Preserve readability unless the measured gain justifies complexity and is protected by tests.

## Verify

- Compare before/after under the same workload and report variance, not only the best run.
- Check correctness, resource transfer, cold/warm behavior, and regression on adjacent workloads.
- Add a budget or benchmark only when the environment is stable enough to produce actionable failures.

Do not claim production improvement from a synthetic microbenchmark alone.
