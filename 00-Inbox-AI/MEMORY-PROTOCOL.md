---
title: "AI Shared Memory Protocol"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - ai-first
  - memory
  - staging
  - protocol
---

# AI Shared Memory Protocol

This directory is the shared external memory protocol for Hermes, OpenHuman, Codex, and ECC.

It exists because these systems should not directly share one opaque internal memory database. They can collaborate safely by reading and writing scoped, reviewable files.

## Directory Contract

```text
signals/
  news/          External news and official blog signals
  github/        GitHub trending, releases, issues, advisories
  papers/        arXiv, papers, research notes
  industry/      Industry reports and market signals
  openhuman/     OpenHuman exports and Memory Tree summaries

candidates/
  topics/        Candidate learning topics
  projects/      Candidate build or automation projects
  skills/        Candidate skills or playbooks to extract
  sources/       Candidate sources worth following

review-queue/
  pending/       Needs human decision
  accepted/      Approved for study, promotion, or build
  deferred/      Interesting but not urgent
  discarded/     Negative examples and noise signals

agent-memory/
  profile.md             What the system believes about Tony
  preferences.md         Positive preferences and output styles
  learning-themes.md     Current learning directions
  negative-signals.md    Things to avoid recommending again

reports/
  daily/         Daily scout reports
  weekly/        Weekly synthesis and study suggestions
  monthly/       Longer-term trend review
```

## Rules

- Automated tools may write `signals/`, `candidates/`, `reports/`, and `review-queue/pending/`.
- Human/Codex review moves items into `accepted/`, `deferred/`, or `discarded/`.
- Canonical notes live in `wiki/`, not here.
- Secrets and credentials never belong in this directory.
- OpenHuman exports go under `signals/openhuman/` first.
- Hermes cron jobs must persist state here if a future run needs memory.
- ECC extracts repeatable methods from accepted workflows, then promotes them into `wiki/practice/`, `skills/`, or project-level rules after review.

## First Workflow

```text
Daily AI Learning Scout
-> collect signals
-> deduplicate and score
-> compare with wiki and agent-memory
-> write candidates
-> send Weixin or Feishu summary
-> wait for human decision
```

See [[Autonomous AI First Learning Engine]] for the full design.
