---
title: "OpenHuman Configuration Audit 2026-06-01"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - openhuman
  - config-audit
  - ai-first
---

# OpenHuman Configuration Audit 2026-06-01

## Summary

OpenHuman is installed, running, and partially configured.

It currently works as a local chat/planner and has indexed one small Obsidian staging folder, but it is not yet a mature multi-source ingestion system.

## Installed State

- App path: `/Applications/OpenHuman.app`
- Version: `0.56.0`
- Active user: `local-tonylidemacbook-pro-local`
- Local state path: `~/.openhuman`
- Local service: `127.0.0.1:7788`
- Debug port: `127.0.0.1:19222`

## Model Configuration

- `chat_provider`: `deepseek:deepseek-v4-pro`
- `reasoning_provider`: `deepseek:deepseek-v4-pro`
- `agentic_provider`: `deepseek:deepseek-v4-pro`
- `coding_provider`: `deepseek:deepseek-v4-pro`
- `memory_provider`: `deepseek:deepseek-v4-pro`
- `heartbeat_provider`: `openhuman`
- `learning_provider`: `openhuman`
- `subconscious_provider`: `openhuman`

DeepSeek provider profile exists. Secrets are stored outside the vault under OpenHuman local state.

## Onboarding And Permissions

- `onboarding_completed`: true
- `chat_onboarding_completed`: false
- Accessibility permission: false
- Local model consent: false
- Local model download: false
- Screen intelligence: disabled
- Autocomplete: disabled
- Computer control: disabled
- Browser tool: disabled

## Autonomy

- Autonomy level: `supervised`
- Workspace only: true
- Medium risk requires approval: true
- High-risk commands blocked: true
- Tool install not allowed

This is a reasonable starting safety posture.

## Memory And Vault

- Memory backend: SQLite
- Memory auto-save: enabled
- Memory docs: 3
- Conversation segments: 1
- Vector chunks: 6
- Memory Tree: one tree record, no chunks or summaries yet
- Vaults configured: 1
- Vault files indexed: 1

Configured vault:

```text
name: tony-wiki
root: /Users/tony/Vault/tony-wiki-2026/00-Inbox-AI/signals/openhuman
indexed file: README.md
```

Interpretation: OpenHuman successfully imported the staging OpenHuman inbox, but it has only indexed the README file. It has not indexed the main `wiki/` or the full vault.

## Agent Profiles

Active profile:

```text
planner
```

Available built-in profiles:

- Default
- Research
- Planner
- Review

The first observed interaction used Planner mode.

## Cron

One default cron job exists:

```text
name: morning_briefing
schedule: 0 7 * * *
next_run: 2026-06-01T14:00:00+00:00
```

The prompt asks OpenHuman to review calendar, tasks, emails, and connected integrations. Since external integrations are not connected, this job will likely be low-value or noisy until integrations are configured.

## Integrations

OpenHuman's app has managed integrations available, but external Composio connections are not authorized.

Observed status:

- Connected sources: none
- Composio: disabled in config, but UI/backend is repeatedly trying to list connections
- Gmail/Notion/GitHub/Slack/Drive/Calendar: not connected
- Logs show repeated `401 Unauthorized` when checking Composio connections
- Voice synthesis also showed `401 Unauthorized` for OpenHuman hosted speech

Interpretation: local OpenHuman works, but hosted-account-backed features are not authenticated correctly yet.

## Recommended Next Steps

1. Disable or ignore the default morning briefing until useful sources are connected.
2. Keep high-risk integrations disconnected for now.
3. Add a low-risk test source first, such as a public URL or public GitHub repository.
4. Keep OpenHuman vault root pointed at `00-Inbox-AI/signals/openhuman/`.
5. If broader Obsidian indexing is needed, add only reviewed subfolders, not the whole vault at once.
6. Decide whether to sign in to OpenHuman hosted services to fix Composio and voice 401 errors.
7. Use Hermes/Codex for the `Daily AI Learning Scout`; use OpenHuman as an optional personal-context signal source, not the scheduler.
