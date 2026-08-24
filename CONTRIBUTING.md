# Contributing

Thank you for improving LeanCode Engineer. Contributions should preserve its central bargain: strong engineering judgment without loading irrelevant context.

## Before opening a change

1. Open an issue for broad behavior, compatibility, or architecture changes.
2. Keep one pull request focused on one outcome.
3. Add or update an observable test when behavior changes.
4. Avoid new dependencies unless they provide a measured, documented benefit.
5. Never include credentials, proprietary prompts, personal data, or copied internal policies.

## Local checks

```bash
./scripts/validate.sh
./scripts/test.sh
./scripts/benchmark.sh --check
```

The project intentionally uses only the Python standard library and portable shell for contributor checks. If a platform-specific change is needed, isolate it behind an adapter and document the support boundary.

## Writing guidance

- Keep `SKILL.md` short and decision-oriented.
- Put conditional detail in one discoverable reference or module.
- Remove duplication instead of keeping “quick” and “full” copies in sync.
- Use requirements that can be observed or tested; avoid style mandates without a concrete failure mode.
- Do not turn one incident into a universal rule without evidence.

## Pull requests

Describe the user-visible outcome, risk, verification evidence, and context-cost impact. Maintainers may request a routing case, benchmark update, or compatibility note.

By contributing, you agree that your contribution is licensed under the MIT License and that project discussion follows [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
