---
type: practice
title: "Core Vault Publication Policy"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - practice
  - publication
  - migration
  - github
  - obsidian
related:
  - "[[Legacy Vault Migration Plan]]"
  - "[[AI First Layered Knowledge Architecture]]"
  - "[[AI First Personal Knowledge Stack]]"
---

# Core Vault Publication Policy

Navigation: [[_index]] | [[Legacy Vault Migration Plan]] | [[AI First Layered Knowledge Architecture]]

## Decision

This vault is the new main working vault. The old mature vault is not a live dependency. It is imported into this vault as staged historical material so the new vault can eventually be pushed to GitHub and read directly in Obsidian.

```text
/Users/tony/Vault/tony-wiki-2026
= new main vault, GitHub target, Obsidian reading target

/Users/tony/Vault/tony2026
= legacy mature vault, preserved as source history
```

The practical meaning: after import, daily work should open this new vault. The old vault can remain on disk as a backup and reference, but agents should not reach back to it during normal operation.

## Included, Not Linked

The legacy vault is included through a filtered copy:

```text
00-Inbox-AI/legacy-tony2026/
```

This is intentionally not a symlink, submodule, live sync, or automation bridge. A GitHub clone of this new vault should contain the selected legacy material without needing access to `/Users/tony/Vault/tony2026`.

## Publication Rules

- Keep `00-Inbox-AI/legacy-tony2026/` as staging and historical source material.
- Promote selected material into `wiki/` as reviewed canonical notes.
- Keep OpenHuman and Hermes outputs in `00-Inbox-AI/` until reviewed.
- Do not commit `.env.local`, API keys, OAuth tokens, session cookies, or account state.
- Do not commit Obsidian runtime state unless intentionally part of the public vault experience.
- Prefer portable relative paths and wikilinks over absolute local paths.

## Promotion Workflow

1. Read the relevant legacy restart pages, usually `专题总览.md`, `学习进度.md`, and `恢复笔记.md`.
2. Identify one high-value theme, playbook, comparison, or map.
3. Create or update a canonical page under `wiki/`.
4. Link back to the staged legacy source path when useful.
5. Update `wiki/index.md`, the nearest `_index.md`, `wiki/log.md`, and `wiki/hot.md`.

## GitHub Readiness Checklist

- No live dependency on `/Users/tony/Vault/tony2026`.
- No local secrets in tracked files.
- Legacy staged copy is filtered and intentional.
- Obsidian opens the new vault directly.
- New captures from OpenHuman/Hermes enter staging, not canonical pages.

## Current State

- Legacy import exists under `00-Inbox-AI/legacy-tony2026/`.
- The legacy source vault was not modified.
- A copied `90-Agent-System/.env.local` was removed from the staged import; keep only `.env.example` style configuration files.
- Next important step before publishing: review the staged legacy import size and privacy surface, then commit the intentional import batch.
