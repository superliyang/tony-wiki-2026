---
type: tool
title: "Hermes Web UI Control Center"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - tools
  - hermes
  - web-ui
  - control-center
related:
  - "[[Hermes Usage Guide]]"
  - "[[AI First Personal Knowledge Stack]]"
  - "[[Personal AI Work Center Architecture]]"
---

# Hermes Web UI Control Center

Navigation: [[_index]] | [[Hermes Usage Guide]] | [[Personal AI Work Center Architecture]]

## Positioning

EKKO Learn AI's Hermes Web UI is the control panel for Hermes Agent. It should not become the canonical knowledge base.

Use it as:

- A chat console for Hermes sessions.
- A configuration page for models and messaging channels.
- A gateway dashboard for Weixin, Feishu, Slack, Telegram, Discord, WhatsApp, Matrix, and WeCom.
- A cron job panel for scheduled Hermes work.
- A usage and cost monitor.
- A log viewer when Hermes or a channel breaks.
- A skill and memory browser.
- A profile manager for separating personal learning, work, experiments, and production-like flows.

Do not use it as:

- The final place to store knowledge.
- The only place where decisions live.
- A broad file manager with unrestricted write access.
- A replacement for Obsidian, GitHub, or reviewed Markdown notes.

## Current Local State

- Installed version: `hermes-web-ui==0.6.7`.
- Local URL: `http://127.0.0.1:8648`.
- Web UI state: `~/.hermes-web-ui`.
- Hermes state: `~/.hermes`.
- Hermes model: DeepSeek `deepseek-v4-pro`.
- Configured messaging channel: Weixin.
- Not yet configured in Hermes: Feishu and GitHub provider.
- Scheduled jobs: none.

Start it from the vault:

```bash
cd /Users/tony/Vault/tony-wiki-2026
scripts/start-hermes-web-ui.sh
```

## What Each Page Is For

| Web UI area | What to use it for | Safe first use |
|---|---|---|
| Chat | Talk to Hermes and inspect model responses | Ask learning questions and request summaries |
| Sessions | See conversation history by source | Review Weixin interactions |
| Channels | Configure Weixin, Feishu, Slack, Telegram, Discord, WhatsApp, Matrix, WeCom | Keep Weixin enabled, add Feishu later |
| Models | Add providers and switch default model | Keep DeepSeek as default, add alternatives later |
| Scheduled Jobs | Create and manage cron-style Hermes tasks | Weekly review only after capture workflow is safe |
| Usage Analytics | Watch tokens, cost, session counts, and model usage | Check if daily use is getting expensive |
| Skills | Browse installed Hermes skills | Identify what Hermes can do before enabling more tools |
| Memory | Inspect or tune Hermes memory behavior | Keep memory as context, not as truth source |
| Logs | Debug gateway, bridge, model, and server issues | First stop when Weixin stops responding |
| Profiles | Separate contexts and credentials | Create `personal-learning` before adding more accounts |
| File Browser | Inspect profile files and outputs | Read-only habit unless a workflow is reviewed |
| Terminal | Run commands from browser | Use sparingly; prefer Codex terminal for repo work |

## Recommended Profile Design

Start with one profile:

```text
personal-learning
```

Later split profiles only when the boundaries are real:

| Profile | Purpose |
|---|---|
| `personal-learning` | Daily learning, notes, questions, study planning |
| `knowledge-curator` | Review staging inbox and propose wiki promotion |
| `engineering-agent` | ECC, code review, GitHub issue/PR workflows |
| `openhuman-ingest` | OpenHuman summaries and Memory Tree import review |

The reason to split profiles is not neatness. It prevents one memory stream from mixing personal learning, engineering work, and experimental ingestion.

## First Five Workflows

### 1. Weixin Learning Capture

```text
Weixin /note ...
-> Hermes receives
-> Append to 00-Inbox-AI/weixin/
-> Review later in Obsidian
-> Promote selected content into wiki/
```

This is the first workflow worth building because it teaches the computer your real interests with low friction.

### 2. Daily Learning Reflection

```text
Hermes Scheduled Job
-> Read recent inbox and wiki changes
-> Summarize today's learning signals
-> Suggest 1-3 topics for tomorrow
-> Write to 00-Inbox-AI/hermes/daily/
```

Do this after Weixin capture is stable.

### 3. Weekly Study Planning

```text
Hermes Scheduled Job
-> Read weekly notes and unresolved questions
-> Generate learning plan
-> Update staging review note
-> Notify via Weixin or Feishu
```

The weekly output should be a decision aid, not an automatic rewrite of the core wiki.

### 4. Source Intake Review

```text
OpenHuman or manual import
-> 00-Inbox-AI/openhuman/
-> Hermes/Codex summarize and tag
-> Human selects what becomes durable knowledge
```

OpenHuman should improve capture breadth without polluting the core vault.

### 5. Engineering Method Capture

```text
GitHub / Codex / Cursor work
-> ECC rules and playbooks
-> wiki/practice/
-> reusable prompts, checklists, and review flows
```

ECC is best used as a way to make engineering behavior repeatable.

## Safety Settings To Prefer

- Keep the Web UI bound to localhost unless there is a specific reason to expose it.
- Change the default `admin / 123456` password if it has not been changed.
- Keep provider secrets in `~/.hermes`, not committed to the vault.
- Do not give broad write workflows to `wiki/` before staging is proven.
- Use channel allowlists before adding group chats.
- Treat Hermes memory as personalization context, not audited truth.

## What This Means For Daily Use

Use the Web UI when you want to control the agent.

Use Weixin when you want to quickly tell the agent something.

Use Obsidian when you want to read, think, edit, and keep durable knowledge.

Use GitHub when you want history, backup, and portability.

Use Codex when you want careful repo edits, migration, review, and automation implementation.

## Sources

- [EKKOLearnAI Hermes Web UI](https://ekkolearnai.com/)
- [EKKOLearnAI/hermes-web-ui README](https://github.com/EKKOLearnAI/hermes-web-ui/blob/main/README.md)
