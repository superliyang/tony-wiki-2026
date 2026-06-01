---
type: meta
title: "Operation Log"
created: 2026-05-16
updated: 2026-06-01
status: evergreen
related:
  - "[[index]]"
  - "[[hot]]"
---

# Operation Log

Append-only. New entries go at the TOP.

## [2026-06-01] schedule | Daily AI Learning Scout installed in Hermes cron

- Created local-only wrapper: `~/.hermes/scripts/daily_ai_learning_scout.sh`
- Stored Feishu webhook in local-only `~/.hermes/.env`; not committed to repo
- Installed Hermes cron job: `daily-ai-learning-scout`
- Job id: `40de6bd11528`
- Schedule: `30 8 * * *`
- Verified: manual Hermes cron trigger completed with status `ok`
- Updated: [[Daily AI Learning Scout Demo]], [[hot]]

## [2026-06-01] promote | Scout candidate promoted into wiki

- Accepted: Daily AI Learning Scout candidate 2, `Exploring Autonomous Agentic Data Engineering for Model Specialization`
- Created: [[Exploring Autonomous Agentic Data Engineering for Model Specialization]]
- Created: [[Agentic Data Engineering for Model Specialization]]
- Created: `00-Inbox-AI/review-queue/accepted/2026-06-01-daily-ai-learning-scout-candidate-2.md`
- Created: `skills/daily-ai-learning-scout/SKILL.md`
- Updated: `00-Inbox-AI/agent-memory/learning-themes.md`
- Updated: [[papers/_index]], [[practice/_index]], [[index]], [[hot]]

## [2026-06-01] demo | Daily AI Learning Scout ran end-to-end

- Created: `scripts/daily_ai_learning_scout.py`
- Created: [[Daily AI Learning Scout Demo]]
- Generated: `00-Inbox-AI/signals/news/2026-06-01-daily-ai-learning-scout.jsonl`
- Generated: `00-Inbox-AI/reports/daily/2026-06-01-daily-ai-learning-scout.md`
- Generated: `00-Inbox-AI/candidates/topics/2026-06-01-daily-ai-learning-scout.md`
- Generated: `00-Inbox-AI/review-queue/pending/2026-06-01-daily-ai-learning-scout.md`
- Result: collected 25 signals and produced 5 candidate topics
- Notification: Feishu webhook proactive delivery succeeded
- Gap: Hermes Weixin `send` failed because no Weixin home channel is configured
- Decision: do not install Hermes cron until source quality and notification cadence are confirmed

## [2026-06-01] map | AI First work center collaboration visualized

- Created: [[AI First Work Center Collaboration Map]]
- Added: collaboration architecture diagram for Hermes, OpenHuman, ECC, Obsidian, and GitHub
- Added: daily autonomous learning flow from external signal to recommendation, review, promotion, and GitHub sync
- Added: memory ownership diagram separating hidden tool memory, shared reviewable memory, and canonical durable memory
- Updated: [[maps/_index]], [[index]], [[hot]]

## [2026-06-01] audit | OpenHuman configuration inspected

- Created: `00-Inbox-AI/reports/daily/openhuman-config-audit-2026-06-01.md`
- Found: OpenHuman active user is `local-tonylidemacbook-pro-local`
- Found: DeepSeek is configured for chat, reasoning, agentic, coding, and memory providers
- Found: one OpenHuman vault named `tony-wiki` points to `00-Inbox-AI/signals/openhuman/` and has indexed only `README.md`
- Found: one default `morning_briefing` cron exists but likely has low value until integrations are connected
- Found: Composio and hosted voice/integration calls are returning `401 Unauthorized`

## [2026-06-01] setup | OpenHuman installed and ECC adopted locally

- Installed: OpenHuman `0.56.0` to `/Applications/OpenHuman.app` from GitHub Release app tarball
- Verified: OpenHuman is signed and notarized; macOS `spctl` accepted it
- Launched: OpenHuman once; local state created under `~/.openhuman`
- Skipped: high-risk OpenHuman integrations such as Gmail, Drive, Slack, Notion, and browser history
- Installed: ECC npm dependencies inside `tools-sandbox/ECC`; no global ECC install was run
- Created: [[OpenHuman Usage Guide]]
- Created: [[ECC Usage Guide]]
- Created: `.cursor/rules/ecc-ai-first-knowledge.mdc`
- Created: `skills/ai-first-work-center/SKILL.md`
- Created: `00-Inbox-AI/signals/openhuman/README.md`

## [2026-06-01] architecture | Autonomous learning engine specified

- Created: [[Autonomous AI First Learning Engine]]
- Created: `00-Inbox-AI/MEMORY-PROTOCOL.md`
- Created: shared memory directories for `signals`, `candidates`, `review-queue`, `agent-memory`, and `reports`
- Created: seed agent-memory files for profile, preferences, learning themes, and negative signals
- Decision: Hermes, OpenHuman, and ECC should not share one opaque internal memory store
- Decision: the shared memory contract should be Markdown/Git-backed staging, candidate, review, preference, and promoted-knowledge files
- Proposed first autonomous workflow: `Daily AI Learning Scout`
- Updated: [[Personal AI Work Center Architecture]], [[AI First Layered Knowledge Architecture]], [[hot]], [[index]], [[practice/_index]]

## [2026-06-01] architecture | Personal AI work center designed

- Created: [[Hermes Web UI Control Center]]
- Created: [[Personal AI Work Center Architecture]]
- Confirmed: local Hermes Web UI is `hermes-web-ui==0.6.7`, running at `http://127.0.0.1:8648`
- Confirmed: Hermes uses DeepSeek `deepseek-v4-pro`, Weixin is configured, gateway is running, and no scheduled jobs exist yet
- Decision: EKKO Hermes Web UI is the control panel for Hermes, while Obsidian Markdown remains the durable knowledge source
- Proposed: start with Weixin capture into `00-Inbox-AI/weixin/`, then add review, OpenHuman intake, ECC playbooks, and GitHub publication

## [2026-06-01] policy | New vault made self-contained target

- Moved: active new wiki vault from `/Users/tony/Documents/vault/tony-wiki-2026` to `/Users/tony/Vault/tony-wiki-2026`
- Created: [[Hermes Usage Guide]]
- Created: [[Core Vault Publication Policy]]
- Created: `00-Inbox-AI/README.md`
- Decision: the legacy mature vault is included as staged historical material, not used as a live linked dependency
- Removed: copied legacy `90-Agent-System/.env.local` from staging; source vault was not modified
- Updated: [[Legacy Vault Migration Plan]], [[hot]], [[index]], [[practice/_index]]

## [2026-05-31] migration | Legacy vault inventory mapped

- Created: [[Legacy Vault Inventory]]
- Mapped: top-level legacy import counts and `01-Areas` domain counts
- Decision: start domain promotion from `专题总览.md`, `学习进度.md`, and `恢复笔记.md` instead of re-summarizing every legacy file

## [2026-05-31] migration | Legacy tony2026 vault staged

- Imported: filtered legacy mirror from `/Users/tony/Vault/tony2026` into `00-Inbox-AI/legacy-tony2026/`
- Preserved: the source vault was not modified
- Imported counts: 1760 Markdown, 11 Canvas, 8 Base, 2556 total files, 29M
- Excluded: `.git/`, `.obsidian/`, `.p_obsidian/`, `.makemd/`, `.space/`, `node_modules/`, `__pycache__/`, `.DS_Store`
- Created: [[Legacy Vault Migration Plan]]

## [2026-05-31] architecture | AI First knowledge stack boundary captured

- Created: [[AI First Layered Knowledge Architecture]]
- Captured: OpenHuman as ingestion layer, Hermes as long-running assistant, ECC as engineering capability layer, Obsidian as the knowledge asset center
- Decision: AI-generated external-source content must enter staging first and only move into the core vault after review
- Updated: [[AI First Personal Knowledge Stack]]

## [2026-05-31] setup | DeepSeek and Weixin connected to Hermes

- Configured: Hermes default model is `deepseek-v4-pro` via provider `deepseek`
- Verified: `hermes doctor` reports DeepSeek API connectivity as healthy
- Verified: `hermes -z` local one-shot returned successfully
- Connected: Weixin gateway state reports `connected`
- Observed: Weixin DM reached Hermes and produced a response
- Next: harden access policy, then add a vault capture workflow for Weixin commands

## [2026-05-31] setup | Hermes Web UI dashboard started

- Installed: `hermes-web-ui==0.6.7` via npm
- Started: Hermes Web UI at `http://localhost:8648`
- Fixed: passed `HERMES_AGENT_ROOT` to the uv-installed Hermes `site-packages` directory so the Web UI agent bridge can find `run_agent.py`
- Verified: Web UI HTTP returned 200, `agent-bridge` reached ready state, and Hermes gateway auto-started
- Reset: default Web UI login to `admin / 123456`
- Created: `scripts/start-hermes-web-ui.sh` for reliable restarts

## [2026-05-31] setup | AI First tool stack installation pass

- Installed: Hermes Agent via `uv tool install hermes-agent` (`hermes-agent==0.15.2`)
- Tested: `hermes --help`, `hermes version`, `hermes status`, `hermes doctor`
- Observed: Hermes is installed and healthy enough to run, but model/API providers are not configured yet
- Cloned: ECC into `tools-sandbox/ECC` for local inspection only
- Tested: ECC local consult CLI with `node scripts/ecc.js consult ...`
- Deferred: OpenHuman installation; Homebrew tap clone stalled on the current network
- Created: [[AI First Personal Knowledge Stack]]

## [2026-05-16] scaffold | Vault initialized for AI 全域知识体系

- Mode: E (Research) extended with 10 domains
- Structure: papers, concepts, entities, tools, open-source, ecosystem, practice, timeline, comparisons, maps
- Attachments: _attachments/ with panoramas/, diagrams/, infographics/, models/
- Templates: paper, concept, entity, source, comparison, question
- CSS: vault-colors.css with color-coded folders and custom callouts
