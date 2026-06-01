#!/usr/bin/env bash
set -euo pipefail

port="${1:-8648}"
hermes_bin="${HERMES_BIN:-$(command -v hermes)}"

if [[ -z "${hermes_bin}" ]]; then
  echo "hermes not found on PATH. Install Hermes first." >&2
  exit 1
fi

resolved_bin="$(readlink "${hermes_bin}" || true)"
if [[ -z "${resolved_bin}" ]]; then
  resolved_bin="${hermes_bin}"
fi

tool_home="$(cd "$(dirname "${resolved_bin}")/.." && pwd)"
agent_root="$(find "${tool_home}/lib" -path '*/site-packages/run_agent.py' -print -quit | xargs dirname)"

if [[ -z "${agent_root}" || ! -f "${agent_root}/run_agent.py" ]]; then
  echo "Could not find Hermes run_agent.py under ${tool_home}/lib." >&2
  exit 1
fi

export HERMES_BIN="${hermes_bin}"
export HERMES_AGENT_ROOT="${HERMES_AGENT_ROOT:-${agent_root}}"

exec hermes-web-ui start "${port}"
