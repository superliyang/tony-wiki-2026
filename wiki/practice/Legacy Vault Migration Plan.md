---
type: practice
title: "Legacy Vault Migration Plan"
created: 2026-05-31
updated: 2026-05-31
status: active
tags:
  - practice
  - migration
  - obsidian
  - ai-first
related:
  - "[[AI First Layered Knowledge Architecture]]"
  - "[[AI First Personal Knowledge Stack]]"
---

# Legacy Vault Migration Plan

Navigation: [[_index]] | [[AI First Layered Knowledge Architecture]] | [[AI First Personal Knowledge Stack]]

## Migration Decision

The previous vault at `/Users/tony/Vault/tony2026` should remain complete and untouched. Its useful knowledge has been imported into this vault as a staged legacy mirror:

`00-Inbox-AI/legacy-tony2026/`

This avoids rebuilding the knowledge base from scratch while keeping the new AI First wiki structure clean.

The intended end state is not a live two-vault workflow. The intended end state is a self-contained new vault that can be pushed to GitHub and opened in Obsidian directly. The old vault remains preserved as a mature historical source, while the new vault carries a filtered copy plus promoted canonical notes.

## What Was Imported

Initial rsync import on 2026-05-31:

| Item | Count |
|---|---:|
| Markdown files | 1760 |
| Canvas files | 11 |
| Base files | 8 |
| Image files | 3 |
| Total files | 2556 |
| Imported size | 29M |

Excluded runtime and cache content:

- `.git/`, `.obsidian/`, `.p_obsidian/`, `.makemd/`, `.space/`
- `node_modules/`, `__pycache__/`, `.DS_Store`

## Why Staging First

The old vault already has a mature multi-domain structure under `01-Areas/`. The new vault is currently an AI-wide LLM Wiki with canonical knowledge under `wiki/`.

So the safe migration pattern is:

1. Preserve the old vault unchanged.
2. Import a filtered mirror into staging.
3. Promote reviewed material into the new `wiki/` topology.
4. Keep AI-generated summaries and unreviewed legacy material out of canonical notes until selected.

## Area Mapping

| Legacy area | New-system role | First action |
|---|---|---|
| `00-Agent-Inbox/` | Historical intake, daily/weekly digest patterns | Mine workflow templates for Hermes capture |
| `01-Areas/AI-Foundations/` | AI concepts, history, theory | Promote to `wiki/concepts/` and `wiki/timeline/` |
| `01-Areas/AI-Learning/` | Companies, systems, models, papers, maps | Promote to `wiki/entities/`, `wiki/papers/`, `wiki/comparisons/` |
| `01-Areas/AI-Engineering/` | Runtime, evaluation, coding agents, delivery patterns | Promote to `wiki/tools/`, `wiki/practice/`, `wiki/open-source/` |
| `01-Areas/AI-Open-Source/` | Open-source project research | Promote to `wiki/open-source/` and `wiki/tools/` |
| `01-Areas/AI-Applications/` | Use cases and product patterns | Promote to `wiki/practice/` |
| `01-Areas/AI-Architect/` | Architecture-level synthesis | Promote to `wiki/practice/` and `wiki/comparisons/` |
| `01-Areas/Big-Data/`, `Cloud-Native/`, `Security/` | Engineering support domains | Keep as staged domain packages, promote when they support AI engineering questions |
| `01-Areas/International-Payments/` | Business/domain knowledge | Keep as a separate future domain package unless tied to AI workflows |
| `01-Areas/English-Learning/`, `Engineering-Management/`, `Macro-Insight/`, `Skills-Gaming/` | Non-core but valuable personal knowledge | Keep staged; promote only when an active workflow needs them |
| `90-Agent-System/`, `.learnings/`, `obsidian-skills/`, `axton-obsidian-visual-skills/` | Agent operating methods and reusable skills | Review for ECC/Hermes/Codex playbooks |

## Promotion Rules

- Do not edit `/Users/tony/Vault/tony2026` during migration work.
- Do not treat `00-Inbox-AI/legacy-tony2026/` as the new canonical knowledge layer.
- Do not use symlinks, submodules, or automation bridges back to the old vault for normal reading.
- When promoting, synthesize into a new `wiki/` page instead of moving old files directly.
- Preserve useful old wikilinks in source references, but normalize canonical pages to the new wiki conventions.
- Before publishing to GitHub, remove local secrets and review the privacy surface of the staged legacy copy.
- Update `wiki/index.md`, relevant `_index.md` pages, `wiki/log.md`, and `wiki/hot.md` after each meaningful promotion batch.

## Next Batch

Start with `01-Areas/AI-Engineering/` and `01-Areas/AI-Open-Source/`, because they directly connect to the current Hermes, ECC, Codex, and AI First workflow setup.
