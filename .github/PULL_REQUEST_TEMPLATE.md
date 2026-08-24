## Outcome

<!-- What user-visible behavior or project capability changes? -->

## Scope and risk

<!-- Name affected boundaries, compatibility impact, and intentionally excluded work. -->

## Verification

- [ ] `./scripts/validate.sh`
- [ ] `./scripts/test.sh`
- [ ] `./scripts/benchmark.sh --check`
- [ ] Host smoke test when compatibility claims change

<!-- Include exact results and any check that could not run. -->

## Context cost

<!-- Does this add core, conditional, or zero runtime context? Include before/after benchmark data when relevant. -->

## Safety

- [ ] No secrets, personal data, or proprietary content are included.
- [ ] Existing behavior and user-owned work are preserved unless explicitly changed.
- [ ] New external mutation, destructive action, or dependency is documented and justified.
