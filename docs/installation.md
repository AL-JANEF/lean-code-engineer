# Installation

## Requirements

- Claude Code for the primary runtime path.
- A POSIX shell for the installer.
- Python 3.9+ only for validation, routing demos, benchmarks, and contributor tests.

No API key or network connection is required.

## Claude Code plugin development

Run from the repository root:

```bash
claude --plugin-dir .
```

Claude Code discovers the root `SKILL.md` as a single-skill plugin and namespaces the invocation with the plugin name.

## Personal Claude Code installation

Preview, then install:

```bash
./scripts/install.sh --dry-run
./scripts/install.sh
```

The default destination is `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/lean-code-engineer`. Existing installs are never silently replaced.

To upgrade while preserving a rollback copy:

```bash
./scripts/install.sh --force
```

The previous directory is renamed with a UTC timestamp. The installer does not delete backups.

## Project-local installation

Use an explicit destination inside the target repository:

```bash
./scripts/install.sh --dest /absolute/project/.claude/skills/lean-code-engineer
```

## Codex experimental adapter

```bash
./scripts/install.sh --target codex
```

This installs to `${CODEX_HOME:-$HOME/.codex}/skills/lean-code-engineer` and includes `agents/openai.yaml`. It is packaged and structurally validated, but behavioral parity is not claimed yet.

## Safe removal

The project does not ship an automated uninstaller because installation directories can contain user modifications. Remove the exact `lean-code-engineer` directory manually after inspecting it. Keep or delete timestamped backups according to your retention policy.
