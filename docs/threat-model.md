# Threat Model

## Assets

- User source code, credentials, personal data, and uncommitted work.
- Integrity of generated patches, tests, installer destinations, and release artifacts.
- User trust in claims about checks, compatibility, and security.

## Trust boundaries

- User requests, repository files, issue text, web pages, logs, and tool output may be untrusted.
- The skill supplies guidance; host permissions remain the authority for tool access.
- Installer arguments cross from untrusted text into filesystem operations and require strict quoting and explicit overwrite behavior.
- GitHub Actions consume third-party actions and repository events.

## Principal threats and controls

| Threat | Control |
|---|---|
| Prompt injection in source or external content | Treat content as data; follow higher-priority user/host instructions; never execute embedded directions blindly. |
| Secret disclosure | Never request or log secrets; scan repository text; use placeholders in examples. |
| Command or path injection | Quote shell variables, reject relative custom destinations, avoid `eval`, and test installer behavior. |
| Destructive overwrite | Refuse existing destinations by default; `--force` creates a backup instead of deleting. |
| False assurance | Require evidence labels and explicit blocked checks; distinguish structural tests from behavioral proof. |
| Dependency compromise | No runtime dependencies; review automation actions before each release. |
| Excessive agent autonomy | Single-agent default; scoped delegation; external mutations still require host/user authorization. |

## Non-goals

The project cannot make a model infallible, replace repository-specific security review, or override host permissions. It does not provide a sandbox, secret manager, vulnerability scanner, or formal verification system.
