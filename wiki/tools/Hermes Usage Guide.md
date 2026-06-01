---
type: tool
title: "Hermes Usage Guide"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - tools
  - hermes
  - ai-first
  - weixin
related:
  - "[[AI First Personal Knowledge Stack]]"
  - "[[AI First Layered Knowledge Architecture]]"
  - "[[Core Vault Publication Policy]]"
  - "[[Hermes Web UI Control Center]]"
---

# Hermes Usage Guide

Navigation: [[_index]] | [[AI First Personal Knowledge Stack]] | [[Hermes Web UI Control Center]] | [[Core Vault Publication Policy]]

## Current Setup

- Main vault path: `/Users/tony/Vault/tony-wiki-2026`.
- Hermes is installed as `hermes-agent==0.15.2`.
- Web UI is installed as `hermes-web-ui==0.6.7`.
- Default provider is DeepSeek, model `deepseek-v4-pro`.
- Weixin gateway is configured and has passed a direct-message test.

## Start and Stop

Start the Web UI:

```bash
cd /Users/tony/Vault/tony-wiki-2026
scripts/start-hermes-web-ui.sh
```

Open:

```text
http://localhost:8648
```

Start or stop the messaging gateway:

```bash
hermes gateway start
hermes gateway stop
hermes gateway restart
hermes gateway status
```

Check model and environment:

```bash
hermes status
hermes doctor
hermes model
```

## How To Think About Hermes

Hermes is a long-running assistant and message bridge. It is not the canonical knowledge base.

Use Hermes for:

- Weixin assistant conversations.
- Capturing rough thoughts into staging.
- Summarizing ideas before saving.
- Inspecting sessions in the Web UI.
- Later: reminders, weekly reviews, and lightweight scheduled work.

Do not use Hermes at first for:

- Rewriting canonical `wiki/` pages automatically.
- Broad filesystem writes.
- High-risk external integrations before staging rules are tested.
- Letting memory become the final source of truth.

## Recommended Weixin Commands

Start with a tiny command vocabulary:

```text
/note <想法>
/save <内容>
/todo <任务>
/query <问题>
```

Target write area:

```text
00-Inbox-AI/weixin/
00-Inbox-AI/hermes/
```

Rule: Hermes output goes to staging first. Human review or Codex later promotes useful content into `wiki/`.

## Daily Loop

1. Send a thought to Hermes from Weixin.
2. Hermes answers or captures it into `00-Inbox-AI/`.
3. Review the inbox later.
4. Promote only durable knowledge into `wiki/`.
5. Update `wiki/hot.md` when the operating context changes.

## Troubleshooting

If Web UI starts but the agent bridge fails, use `scripts/start-hermes-web-ui.sh` rather than launching `hermes-web-ui` directly. The script sets `HERMES_AGENT_ROOT` so the Web UI can find Hermes' `run_agent.py`.

If Weixin stops responding:

```bash
hermes gateway status
hermes gateway restart
```

If model calls fail:

```bash
hermes doctor
hermes model
```

## Next Build Step

Implement the first safe capture workflow:

```text
Weixin /note ...
-> Hermes receives
-> Append Markdown entry to 00-Inbox-AI/weixin/YYYY-MM.md
-> Human/Codex promotes selected entries into wiki/
```
