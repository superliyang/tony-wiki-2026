---
type: practice
title: "Daily AI Learning Scout Demo"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - practice
  - ai-first
  - demo
  - hermes
  - openhuman
  - review-queue
related:
  - "[[Autonomous AI First Learning Engine]]"
  - "[[AI First Work Center Collaboration Map]]"
  - "[[Personal AI Work Center Architecture]]"
---

# Daily AI Learning Scout Demo

Navigation: [[_index]] | [[Autonomous AI First Learning Engine]] | [[AI First Work Center Collaboration Map]]

## What Ran

The first end-to-end demo of the AI First work center ran on 2026-06-01.

Command shape:

```bash
FEISHU_WEBHOOK_URL="<local env only>" \
  python3 scripts/daily_ai_learning_scout.py \
  --limit-per-source 6 \
  --max-candidates 5 \
  --feishu-webhook-env FEISHU_WEBHOOK_URL
```

The webhook value was not written to the repository.

## Flow Covered

```text
Public sources
-> Daily AI Learning Scout script
-> score against hot cache and agent-memory
-> write signals JSONL
-> write candidate topics
-> write Review Queue
-> write daily report
-> send Feishu proactive notification
```

## Artifacts

- Signals: `00-Inbox-AI/signals/news/2026-06-01-daily-ai-learning-scout.jsonl`
- Report: `00-Inbox-AI/reports/daily/2026-06-01-daily-ai-learning-scout.md`
- Candidates: `00-Inbox-AI/candidates/topics/2026-06-01-daily-ai-learning-scout.md`
- Review queue: `00-Inbox-AI/review-queue/pending/2026-06-01-daily-ai-learning-scout.md`
- Script: `scripts/daily_ai_learning_scout.py`

## Demo Result

- Signals collected: 25
- Candidate topics: 5
- OpenHuman snapshot included: 1 indexed vault file, 3 memory docs, 0 memory-tree chunks
- Feishu webhook delivery: success
- Canonical `wiki/` notes were not automatically modified
- Hermes cron job: installed and manually triggered successfully

## Top Candidates

1. `study`: Uncertainty-Aware and Temporally Regulated Expert Advice in Reinforcement Learning for Autonomous Driving
2. `study`: Exploring Autonomous Agentic Data Engineering for Model Specialization
3. `study`: OpenHuman v0.56.0
4. `study`: ECC v1.10.0
5. `study`: Announcing Claude Managed Agents on Cloudflare

## What This Proves

The first slice of the architecture is real:

- Hermes notification layer can be represented through Feishu webhook delivery.
- OpenHuman can contribute local readiness signals.
- ECC's contribution is currently procedural: this demo follows the shared memory protocol and project-local skill/rule boundary.
- Obsidian/GitHub-compatible Markdown artifacts are the durable output.
- Human review remains the gate before promotion to canonical `wiki/`.

## Known Gaps

- Hermes `send --to weixin` failed because no Weixin home channel is configured.
- Anthropic RSS URL returned 404 and should be replaced with a valid source.
- Scoring is keyword-based and should be improved with LLM classification.
- OpenHuman has only indexed the staging README, not meaningful personal-context sources yet.
- No Hermes cron job has been installed yet.

## To Schedule Later

Hermes requires scheduled scripts to live under `~/.hermes/scripts/`.

Installed local setup:

```bash
hermes cron create "30 8 * * *" \
  --name "daily-ai-learning-scout" \
  --script daily_ai_learning_scout.sh \
  --no-agent \
  --workdir /Users/tony/Vault/tony-wiki-2026
```

Current job:

```text
id: 40de6bd11528
name: daily-ai-learning-scout
schedule: 30 8 * * *
mode: no-agent
script: daily_ai_learning_scout.sh
last manual run: ok
```

Local-only wrapper:

```text
~/.hermes/scripts/daily_ai_learning_scout.sh
```

The Feishu webhook is loaded from `~/.hermes/.env` and is not committed to the repository.
