# Compatibility

| Host | Packaging | Status | Notes |
|---|---|---|---|
| Claude Code | Root `SKILL.md`, `.claude-plugin/plugin.json`, standalone installer | Primary | Strict plugin validation passed locally with Claude Code 2.1.239; an interactive behavioral smoke test remains before release. |
| Agent Skills standard | Portable frontmatter and relative resources | Designed | Core avoids dynamic host-only syntax. |
| Codex | `agents/openai.yaml`, installer target | Experimental | Metadata and structure are validated locally; behavioral evaluation remains. |
| Cursor | No adapter yet | Planned | Add only after host contract and invocation behavior are tested. |
| OpenCode | No adapter yet | Planned | Add only after host contract and invocation behavior are tested. |

“Primary” means the repository is designed around that host, not that every future host version is automatically supported. Release notes should record the exact versions used for runtime checks.

## Portability rules

- Keep the root `SKILL.md` usable without plugin-only variables or commands.
- Put host metadata in adapter directories rather than branching the core instructions.
- Treat unsupported frontmatter fields as optional enhancements, never correctness requirements.
- Add a compatibility test before changing a host from planned or experimental to supported.
