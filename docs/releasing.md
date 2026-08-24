# Release Checklist

1. Confirm the version matches `SKILL.md`, `.claude-plugin/plugin.json`, and `CHANGELOG.md`.
2. Run `./scripts/validate.sh`, `./scripts/test.sh`, and `./scripts/benchmark.sh --check` on supported platforms.
3. Run a Claude Code smoke test with `claude --plugin-dir .` and record the tested host version.
4. Review the final diff for credentials, generated junk, and unrelated changes.
5. Update compatibility claims from observed evidence only.
6. Create a signed tag and release notes only after CI passes.
7. Configure GitHub social preview and enable private vulnerability reporting after repository creation.

Publishing is deliberately manual in `0.x`; no workflow pushes tags, packages, or marketplace submissions.
