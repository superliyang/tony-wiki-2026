---
type: tool
title: "OpenHuman Usage Guide"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - tools
  - openhuman
  - memory-tree
  - ingestion
related:
  - "[[AI First Personal Knowledge Stack]]"
  - "[[Autonomous AI First Learning Engine]]"
  - "[[Core Vault Publication Policy]]"
---

# OpenHuman Usage Guide

Navigation: [[_index]] | [[AI First Personal Knowledge Stack]] | [[Autonomous AI First Learning Engine]]

## Current Local State

- Installed version: `OpenHuman 0.56.0`.
- Install path: `/Applications/OpenHuman.app`.
- Install source: GitHub Release `OpenHuman_0.56.0_aarch64-apple-darwin.app.tar.gz`.
- Code signing: accepted by macOS Gatekeeper as a notarized Developer ID app.
- Runtime state: `~/.openhuman`.
- Current mode: installed and launched once, no high-risk integrations connected.

Open it:

```bash
open -a OpenHuman
```

## Role In This System

OpenHuman is the ingestion and personal-context layer.

Use it to answer:

```text
Given my real inputs and habits, why does this signal matter to me?
```

Do not use it as the canonical knowledge base.

## Safe First Configuration

Start with low-risk sources only:

- Local test notes.
- Public URLs.
- Public GitHub repositories.
- Manually exported conversations or documents after review.

Delay high-risk integrations:

- Gmail.
- Google Drive.
- Calendar.
- Slack.
- Notion.
- Personal browser history.
- Any finance, identity, or private work accounts.

## Export Target

All OpenHuman-generated material should land in staging first:

```text
00-Inbox-AI/signals/openhuman/
```

If OpenHuman supports choosing an Obsidian or Markdown export folder, point it to:

```text
/Users/tony/Vault/tony-wiki-2026/00-Inbox-AI/signals/openhuman
```

If it creates its own Memory Tree elsewhere, periodically export or copy reviewed summaries into that folder.

## First Use Workflow

1. Open OpenHuman.
2. Complete local onboarding.
3. Do not connect OAuth integrations on the first pass.
4. Import one low-risk public source or local note.
5. Confirm where Memory Tree / Markdown files are stored.
6. Export or mirror the result into `00-Inbox-AI/signals/openhuman/`.
7. Let Hermes or Codex compare the result with the wiki before promotion.

## Promotion Rule

OpenHuman output is evidence, not truth.

```text
OpenHuman Memory Tree
-> 00-Inbox-AI/signals/openhuman/
-> candidates or review queue
-> human/Codex review
-> wiki/
```

## What Good Looks Like

OpenHuman is useful if it provides:

- Better personal-context relevance.
- Useful summaries of noisy sources.
- Memory Tree chunks that can be inspected in Markdown.
- A source trail that explains where a recommendation came from.

It is not useful if it:

- Creates hidden memory you cannot audit.
- Overwrites canonical notes.
- Pushes too many low-value summaries.
- Connects sensitive accounts before trust is established.

## Sources

- [OpenHuman Wiki](https://openhumanwiki.com/)
- [tinyhumansai/openhuman README](https://github.com/tinyhumansai/openhuman/blob/main/README.md)
- [OpenHuman Releases](https://github.com/tinyhumansai/openhuman/releases)
