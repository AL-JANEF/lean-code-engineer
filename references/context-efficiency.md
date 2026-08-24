# Context Efficiency

Read this for large repositories, noisy tools, long sessions, or repeated context pressure.

## Load by decision

- Start with repository instructions, the target symbol, its callers, and its focused tests.
- Search filenames and symbols before opening full files; read narrow ranges around relevant matches.
- Load one specialist reference or module when it changes the next decision. Do not preload the catalog.
- Prefer summaries of established evidence over copying logs, generated files, lockfiles, or entire directories.

## Spend context where risk lives

- Keep API contracts, security boundaries, migrations, concurrency, and failures visible.
- Compress boilerplate and already-settled facts, not unresolved evidence.
- Use deterministic scripts for repeated validation and measurement.
- Delegate only when context isolation or parallelism saves more than coordination costs.

## Stop conditions

- Stop exploring when acceptance criteria, affected boundaries, and a falsifiable implementation path are clear.
- Re-open context when a test contradicts the model, a hidden caller appears, or scope changes.
- Do not use token targets to justify skipped tests, guessed interfaces, weakened errors, or incomplete fixes.

Estimate savings honestly. Character-based token estimates are useful for regressions but are not provider billing measurements or quality evidence.
