---
name: daily-ai-learning-scout
description: Run and improve the Daily AI Learning Scout loop: collect external AI signals, compare with Tony's vault and agent memory, produce candidates, process review decisions, and promote accepted items into durable Obsidian notes or ECC-style playbooks.
---

# Daily AI Learning Scout

Use this skill when operating or improving the autonomous scout workflow.

## Inputs

- `wiki/hot.md`
- `wiki/index.md`
- `00-Inbox-AI/agent-memory/*.md`
- `00-Inbox-AI/signals/**/*.jsonl`
- `00-Inbox-AI/review-queue/{pending,accepted,deferred,discarded}/`
- Public source feeds and GitHub releases
- OpenHuman local snapshot or exports under `00-Inbox-AI/signals/openhuman/`

## Outputs

- `00-Inbox-AI/signals/news/YYYY-MM-DD-daily-ai-learning-scout.jsonl`
- `00-Inbox-AI/candidates/topics/YYYY-MM-DD-daily-ai-learning-scout.md`
- `00-Inbox-AI/review-queue/pending/YYYY-MM-DD-daily-ai-learning-scout.md`
- `00-Inbox-AI/reports/daily/YYYY-MM-DD-daily-ai-learning-scout.md`
- Optional Feishu or Hermes notification

## Promotion Workflow

1. Pick one candidate from the review queue.
2. Verify the primary source.
3. Create a durable note in the correct `wiki/` layer.
4. Create or update a practice playbook if the candidate changes the operating method.
5. Add an accepted review record.
6. Update `agent-memory` so the decision affects future recommendations.
7. Update relevant indexes and `wiki/hot.md`.

## Guardrails

- Do not write secrets into the repo.
- Do not use hidden tool memory as source truth.
- Do not auto-promote into `wiki/`.
- Keep source links on promoted notes.
- Use discarded decisions as negative training examples.
