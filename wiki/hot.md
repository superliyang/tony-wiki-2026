---
type: meta
title: "Hot Cache"
updated: 2026-06-01
tags:
  - meta
  - hot-cache
status: active
related:
  - "[[index]]"
  - "[[log]]"
  - "[[overview]]"
---

# Recent Context

Navigation: [[index]] | [[log]] | [[overview]]

## Last Updated

2026-06-01: Added the autonomous AI-first learning engine design: Hermes/OpenHuman/ECC should collaborate through a shared Markdown/Git memory protocol, not one shared opaque internal memory.

## Key Recent Facts

- Obsidian / Markdown vault remains the canonical knowledge source.
- Hermes Agent is installed via `uv tool install hermes-agent` as `hermes-agent==0.15.2`.
- Hermes Web UI is installed as `hermes-web-ui==0.6.7` and running at `http://localhost:8648`.
- EKKO Hermes Web UI should be used for chat sessions, channels, models, scheduled jobs, usage analytics, logs, profiles, skills, memory, file browser, and terminal access.
- EKKO Hermes Web UI should not be treated as the durable knowledge source; durable knowledge still belongs in Markdown under `wiki/`.
- Start Hermes Web UI with `scripts/start-hermes-web-ui.sh` so `HERMES_AGENT_ROOT` points to uv's `site-packages/run_agent.py`; otherwise the agent bridge fails.
- Main working vault path is now `/Users/tony/Vault/tony-wiki-2026`.
- Hermes default model is `deepseek-v4-pro` with provider `deepseek`.
- DeepSeek API connectivity passed `hermes doctor`, and `hermes -z` returned successfully.
- Weixin is configured and gateway state reports `connected`.
- A Weixin DM test reached Hermes and produced a response; session title: "Asking About Today's Weather".
- Architecture decision: OpenHuman is ingestion only, Hermes is the long-running assistant, ECC is the engineering capability layer, and Obsidian remains the knowledge asset center.
- Autonomy decision: Hermes should be the proactive runner, OpenHuman the broad ingestion and Memory Tree layer, ECC the procedural method layer; their shared truth should be `00-Inbox-AI/` plus reviewed `wiki/`, not hidden internal memory.
- First autonomous workflow should be `Daily AI Learning Scout`: collect current signals, compare with the vault, propose candidate topics, recommend `study/watch/discard/promote/build`, then notify through Weixin or Feishu.
- External-source AI summaries must go through staging before entering canonical wiki notes.
- Legacy vault migration decision: old vault is preserved unchanged; filtered copy lives at `00-Inbox-AI/legacy-tony2026/`.
- Publication decision: this new vault should become self-contained for GitHub and Obsidian reading; do not use symlinks, submodules, or live automation bridges back to `/Users/tony/Vault/tony2026`.
- Removed the copied legacy `90-Agent-System/.env.local` from staging; keep only example config files before GitHub publication.
- Imported legacy staging counts: 1760 Markdown, 11 Canvas, 8 Base, 2556 total files, 29M.
- Legacy inventory: `01-Areas/` contains 1498 Markdown files; largest AI-adjacent domains are AI-Learning, AI-Engineering, International-Payments, Security, AI-Applications, Skills-Gaming, Cloud-Native, and AI-Open-Source.
- Excluded legacy runtime/cache content: `.git/`, `.obsidian/`, `.p_obsidian/`, `.makemd/`, `.space/`, `node_modules/`, `__pycache__/`, `.DS_Store`.
- ECC is cloned locally under `tools-sandbox/ECC` for inspection only; no global Codex/Claude/MCP/rules install was performed.
- ECC dependencies were installed in `tools-sandbox/ECC`; ECC is adopted project-locally through a Cursor rule and `skills/ai-first-work-center`, not global hooks/MCP.
- OpenHuman is installed at `/Applications/OpenHuman.app` as version `0.56.0`, launched once, and created state under `~/.openhuman`; no high-risk integrations are connected.
- OpenHuman config audit: active user `local-tonylidemacbook-pro-local`, DeepSeek providers configured, one `tony-wiki` vault points at `00-Inbox-AI/signals/openhuman`, only `README.md` indexed, Composio/hosted integrations show 401 Unauthorized.

## Recent Changes

- Created: [[AI First Personal Knowledge Stack]]
- Created: [[AI First Layered Knowledge Architecture]]
- Created: [[Legacy Vault Migration Plan]]
- Created: [[Legacy Vault Inventory]]
- Created: [[Core Vault Publication Policy]]
- Created: [[Hermes Usage Guide]]
- Created: [[Hermes Web UI Control Center]]
- Created: [[Personal AI Work Center Architecture]]
- Created: [[Autonomous AI First Learning Engine]]
- Created: [[OpenHuman Usage Guide]]
- Created: [[ECC Usage Guide]]
- Created: `00-Inbox-AI/MEMORY-PROTOCOL.md`
- Created: `skills/ai-first-work-center/SKILL.md`
- Created: `.cursor/rules/ecc-ai-first-knowledge.mdc`
- Created: `00-Inbox-AI/agent-memory/profile.md`, `preferences.md`, `learning-themes.md`, and `negative-signals.md`
- Created: `00-Inbox-AI/README.md`
- Created: `00-Inbox-AI/legacy-tony2026/MIGRATION.md`
- Created: `scripts/start-hermes-web-ui.sh`
- Updated: [[AI First Personal Knowledge Stack]], [[tools/_index]], [[practice/_index]], [[index]], [[log]], [[hot]]

## Active Threads

- Next step: implement the first autonomous `Daily AI Learning Scout` using the shared memory protocol under `00-Inbox-AI/`.
- OpenHuman next step: configure only low-risk local/public inputs and export Memory Tree summaries to `00-Inbox-AI/signals/openhuman/`.
- OpenHuman audit report: `00-Inbox-AI/reports/daily/openhuman-config-audit-2026-06-01.md`.
- Current collaboration map: [[AI First Work Center Collaboration Map]]
- First demo run completed: [[Daily AI Learning Scout Demo]]
- Demo artifacts: `scripts/daily_ai_learning_scout.py`, `00-Inbox-AI/reports/daily/2026-06-01-daily-ai-learning-scout.md`, `00-Inbox-AI/review-queue/pending/2026-06-01-daily-ai-learning-scout.md`, and `00-Inbox-AI/candidates/topics/2026-06-01-daily-ai-learning-scout.md`.
- Demo notification: Feishu webhook delivery succeeded; Hermes Weixin `send` needs a home channel or target fix before it can be used for proactive Weixin notifications.
- First `promote` decision completed: Daily AI Learning Scout candidate 2 became [[Exploring Autonomous Agentic Data Engineering for Model Specialization]] and [[Agentic Data Engineering for Model Specialization]].
- Project-local ECC-style skill added: `skills/daily-ai-learning-scout/SKILL.md`.
- Hermes cron installed: `daily-ai-learning-scout` job `40de6bd11528`, schedule `30 8 * * *`, script `~/.hermes/scripts/daily_ai_learning_scout.sh`, last manual run ok.
- ECC next step: extract repeated scout/review workflows into project-local skills before considering global plugin or MCP setup.
- Parallel step: harden Weixin access policy, then create the first vault capture workflow under `00-Inbox-AI/weixin/`.
- First useful workflow: send a Weixin command such as `/save ...` or `/note ...` and have Hermes append it to a Markdown inbox in this vault.
- Recommended operating model: Weixin for quick capture, Hermes Web UI for control, Obsidian for reading and editing, GitHub for backup/publication, OpenHuman for low-risk staging intake, ECC for repeatable engineering methods.
- Next migration batch: start from legacy `AI-Engineering/专题总览.md`, `学习进度.md`, and `恢复笔记.md`, then promote selected material into the new `wiki/` topology.
- Before pushing the staged legacy import to GitHub, run a privacy/secrets scan and decide whether the full 29M staged mirror should be committed in one batch or split by domain.
- Later OpenHuman workflow: write only to staging such as `00-Inbox-AI/openhuman/`, then promote reviewed notes into the core wiki.
- Keep OpenHuman disconnected from sensitive integrations until the memory ownership boundary is explicit.
