---
type: tool
title: "AI First Personal Knowledge Stack"
created: 2026-05-31
updated: 2026-05-31
status: active
tags:
  - tools
  - ai-first
  - knowledge-system
  - hermes
  - ecc
  - openhuman
related:
  - "[[_index]]"
  - "[[hot]]"
  - "[[AI First Layered Knowledge Architecture]]"
  - "[[Hermes Usage Guide]]"
  - "[[Hermes Web UI Control Center]]"
  - "[[Personal AI Work Center Architecture]]"
  - "[[OpenHuman Usage Guide]]"
  - "[[ECC Usage Guide]]"
---

# AI First Personal Knowledge Stack

## Principle

[[overview|Obsidian / Markdown vault]] is the only truth source. Agent memory is cache, routing context, and personalization. Durable knowledge must land in Markdown so it can be searched, diffed, backed up, and migrated.

## Roles

| Layer | Tool | Role | Current state |
|---|---|---|---|
| Truth source | Obsidian / Markdown vault | Canonical notes, logs, indexes, maps | Active |
| Execution layer | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Long-running agent runtime, cron, sessions, tools, skills, memory | Installed via `uv tool install hermes-agent`; smoke tested |
| Operating method | [ECC](https://github.com/affaan-m/ECC) | Rules, skills, MCP hygiene, install planning | Cloned into local sandbox; no global install |
| Frontend experiment | [OpenHuman](https://github.com/tinyhumansai/openhuman) | Personal AI front end and Memory Tree experience | Deferred; Homebrew tap clone was too slow |

## Installation Notes

- Hermes installed as a uv tool on 2026-05-31: `hermes-agent==0.15.2`.
- Executables created: `~/.local/bin/hermes`, `~/.local/bin/hermes-agent`, `~/.local/bin/hermes-acp`.
- Hermes created local state under `~/.hermes/`, including `sessions/`, `logs/`, `skills/`, `memories/`, and `cron/`.
- Hermes smoke tests passed: `hermes --help`, `hermes version`, `hermes status`, and `hermes doctor`.
- Hermes is connected to DeepSeek as the default model provider, using `deepseek-v4-pro`.
- ECC was cloned to `tools-sandbox/ECC` and its local CLI can run `node scripts/ecc.js consult ...`.
- ECC was not installed into Codex, Claude, OpenCode, MCP, hooks, or global rules.
- OpenHuman was installed from GitHub Release `v0.56.0` as `/Applications/OpenHuman.app` on 2026-06-01 after the Homebrew tap clone stalled again.
- OpenHuman was launched once and created local state under `~/.openhuman`; no high-risk integrations were connected.
- Hermes Web UI was installed via npm on 2026-05-31: `hermes-web-ui==0.6.7`.
- Hermes Web UI is running at `http://localhost:8648`.
- The Web UI agent bridge requires `HERMES_AGENT_ROOT` to point at the uv-installed Hermes `site-packages` directory containing `run_agent.py`; use `scripts/start-hermes-web-ui.sh` to start it reliably.
- Default Web UI login was reset to `admin / 123456`.
- DeepSeek was configured as Hermes' default model provider on 2026-05-31: `deepseek-v4-pro`.
- Weixin was connected on 2026-05-31 and gateway state reports `connected`.
- A Weixin direct-message test reached Hermes and produced a model response.
- Main vault moved to `/Users/tony/Vault/tony-wiki-2026` on 2026-06-01; start Hermes Web UI from this path.

## Safety Boundaries

- Do not let ECC full/manual install write global agent config until a dry-run plan is reviewed.
- Do not connect OpenHuman to Gmail, Drive, Slack, Calendar, Notion, or other high-sensitivity integrations in the first test.
- Do not make Hermes, OpenHuman, and ECC all write durable memory independently. This vault remains canonical.
- Use Hermes for scheduled work only after model provider, workspace scope, and write policy are explicit.
- OpenHuman may write staging drafts, but not canonical notes.
- ECC belongs primarily in engineering workflow rules, skills, hooks, review templates, and playbooks.

## Architecture

See [[AI First Layered Knowledge Architecture]] for the durable operating model:

- OpenHuman = information ingestion into staging.
- Hermes = long-running assistant over the vault.
- ECC = engineering agent capability layer.
- Obsidian = knowledge asset center.

See [[Personal AI Work Center Architecture]] for the integrated GitHub / Obsidian / OpenHuman / Hermes / ECC operating model.

See [[Hermes Web UI Control Center]] for how to use the current EKKO Hermes Web UI as a control panel instead of a knowledge source.

See [[OpenHuman Usage Guide]] for the OpenHuman staging and Memory Tree boundary.

See [[ECC Usage Guide]] for the project-local ECC adoption path.

## Next Configuration Step

Harden Weixin access policy, then create a narrow Weixin-to-vault capture workflow that appends intentional notes to a Markdown inbox inside this vault.

See [[Hermes Usage Guide]] for start/stop commands and safe first workflows.
