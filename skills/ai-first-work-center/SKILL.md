---
name: ai-first-work-center
description: Operate Tony's AI First personal learning work center by coordinating Hermes, OpenHuman, ECC, Obsidian, GitHub, staging memory, candidate review, and promotion into durable wiki notes.
---

# AI First Work Center

Use this skill when working on Tony's autonomous personal knowledge and skill-learning system.

## System Roles

- Hermes: proactive execution, cron, Weixin/Feishu notifications, candidate recommendations.
- OpenHuman: multi-source ingestion, Memory Tree, personal-context signals.
- ECC: engineering method, repeatable skills, project-local rules, playbooks.
- Obsidian Markdown: canonical knowledge.
- GitHub: durable history, backup, publication, and review.

## Shared Memory Contract

Use `00-Inbox-AI/MEMORY-PROTOCOL.md`.

Write automated output to:

```text
00-Inbox-AI/signals/
00-Inbox-AI/candidates/
00-Inbox-AI/review-queue/pending/
00-Inbox-AI/reports/
00-Inbox-AI/agent-memory/
```

Only reviewed content should be promoted to `wiki/`.

## Operating Loop

1. Observe external signals or user captures.
2. Compare them against `wiki/hot.md`, `wiki/index.md`, `00-Inbox-AI/agent-memory/`, and legacy inventory.
3. Generate candidates with one of these actions: `study`, `watch`, `discard`, `promote`, `build`.
4. Persist evidence and recommendations in staging.
5. Notify Tony through Hermes when appropriate.
6. Promote accepted items into `wiki/`.
7. Extract repeated methods into `wiki/practice/`, project-local skills, or Cursor rules.

## Guardrails

- Do not connect high-risk OpenHuman integrations without explicit review.
- Do not let Hermes cron jobs write canonical wiki notes directly.
- Do not run global ECC installs or MCP sync automatically.
- Do not commit secrets, auth files, OAuth state, or runtime app data.
- Do not publish staged legacy imports before a privacy scan.

## Good Output

Prefer concise, evidence-backed recommendations:

```text
Topic: Agent memory governance
Why now: 3 current sources + repeated vault theme
Suggested action: study
Output target: wiki/practice/
Risk: high noise, needs source quality check
```
