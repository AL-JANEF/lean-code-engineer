#!/bin/sh
set -eu

script_dir=$(CDPATH='' cd -- "$(dirname -- "$0")" && pwd)
project_root=$(dirname -- "$script_dir")
target="claude"
destination=""
force="false"
dry_run="false"

usage() {
  printf '%s\n' \
    "Usage: ./scripts/install.sh [--target claude|codex] [--dest ABSOLUTE_PATH] [--force] [--dry-run]" \
    "" \
    "Installs the runtime skill bundle. Existing installs are refused unless --force" \
    "is supplied; forced upgrades preserve the previous directory as a backup."
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      [ "$#" -ge 2 ] || { printf '%s\n' "ERROR: --target needs a value" >&2; exit 2; }
      target=$2
      shift 2
      ;;
    --dest)
      [ "$#" -ge 2 ] || { printf '%s\n' "ERROR: --dest needs a value" >&2; exit 2; }
      destination=$2
      shift 2
      ;;
    --force)
      force="true"
      shift
      ;;
    --dry-run)
      dry_run="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf '%s\n' "ERROR: unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$target" in
  claude|codex) ;;
  *) printf '%s\n' "ERROR: target must be claude or codex" >&2; exit 2 ;;
esac

if [ -z "$destination" ]; then
  case "$target" in
    claude)
      config_root="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}"
      destination="$config_root/skills/lean-code-engineer"
      ;;
    codex)
      config_root="${CODEX_HOME:-${HOME}/.codex}"
      destination="$config_root/skills/lean-code-engineer"
      ;;
  esac
else
  case "$destination" in
    /*) ;;
    *) printf '%s\n' "ERROR: --dest must be an absolute path" >&2; exit 2 ;;
  esac
fi

case "$destination" in
  /|/.) printf '%s\n' "ERROR: refusing unsafe destination" >&2; exit 2 ;;
esac

printf '%s\n' "Source: $project_root" "Destination: $destination" "Target: $target"
if [ "$dry_run" = "true" ]; then
  if [ -e "$destination" ] && [ "$force" != "true" ]; then
    printf '%s\n' "DRY RUN: existing destination would be refused (use --force to preserve and replace it)."
  elif [ -e "$destination" ]; then
    printf '%s\n' "DRY RUN: existing destination would be moved to a timestamped backup."
  else
    printf '%s\n' "DRY RUN: runtime bundle would be installed."
  fi
  exit 0
fi

if [ -e "$destination" ] && [ "$force" != "true" ]; then
  printf '%s\n' "ERROR: destination exists; use --force to preserve it as a backup" >&2
  exit 1
fi

destination_parent=$(dirname -- "$destination")
mkdir -p -- "$destination_parent"
stage_root=$(mktemp -d "${TMPDIR:-/tmp}/lean-code-engineer-install.XXXXXX")
staged="$stage_root/lean-code-engineer"
backup=""

cleanup() {
  if [ -d "$stage_root" ]; then
    rm -R -- "$stage_root"
  fi
}
trap cleanup EXIT HUP INT TERM

mkdir -- "$staged"
cp -- "$project_root/SKILL.md" "$project_root/LICENSE" "$staged/"
cp -R -- "$project_root/references" "$project_root/modules" "$project_root/assets" "$staged/"
if [ "$target" = "codex" ]; then
  cp -R -- "$project_root/agents" "$staged/"
fi

if [ -e "$destination" ]; then
  backup="${destination}.backup.$(date -u +%Y%m%dT%H%M%SZ)"
  if [ -e "$backup" ]; then
    printf '%s\n' "ERROR: backup path already exists: $backup" >&2
    exit 1
  fi
  mv -- "$destination" "$backup"
fi

if ! mv -- "$staged" "$destination"; then
  if [ -n "$backup" ] && [ ! -e "$destination" ]; then
    mv -- "$backup" "$destination"
  fi
  printf '%s\n' "ERROR: installation failed; previous install restored when possible" >&2
  exit 1
fi

printf '%s\n' "Installed LeanCode Engineer at $destination"
if [ -n "$backup" ]; then
  printf '%s\n' "Previous install preserved at $backup"
fi
