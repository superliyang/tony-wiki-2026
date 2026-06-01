---
type: tool
title: "ECC Usage Guide"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - tools
  - ecc
  - skills
  - rules
  - playbooks
related:
  - "[[AI First Personal Knowledge Stack]]"
  - "[[Autonomous AI First Learning Engine]]"
  - "[[Personal AI Work Center Architecture]]"
---

# ECC Usage Guide

Navigation: [[_index]] | [[AI First Personal Knowledge Stack]] | [[Autonomous AI First Learning Engine]]

## Current Local State

- Source checkout: `tools-sandbox/ECC`.
- Dependency install: `npm install` completed in the ECC sandbox.
- CLI smoke test: `node tools-sandbox/ECC/scripts/ecc.js --help`.
- Install mode for this vault: project-level selective use.
- Global install status: not installed into `~/.codex`, `~/.claude`, global MCP, or global hooks.

## Role In This System

ECC is the engineering operating method.

Use it to answer:

```text
When this workflow repeats, how should agents execute it reliably next time?
```

ECC is not the memory source of truth. It is a source of rules, skills, hooks, agent roles, and playbooks.

## Why Not Install Everything Globally

ECC has many powerful surfaces:

- rules
- skills
- commands
- hooks
- MCP configs
- agents
- platform adapters

Installing everything globally too early can create duplicate hooks, too many MCP tools, and confusing agent behavior.

This vault should adopt ECC gradually:

```text
Read ECC source
-> extract useful method
-> create project-local rules or skills
-> test in this vault
-> only then consider global install
```

## Current Project-Level Adoption

This vault now uses ECC principles through:

- `AGENTS.md` tool-role boundary.
- `.cursor/rules/ecc-ai-first-knowledge.mdc` project-local Cursor rule.
- `skills/ai-first-work-center/SKILL.md` project-local Agent Skill.
- `wiki/practice/Autonomous AI First Learning Engine.md`.
- `00-Inbox-AI/MEMORY-PROTOCOL.md`.

## Useful ECC Commands

From the vault root:

```bash
node tools-sandbox/ECC/scripts/ecc.js --help
node tools-sandbox/ECC/scripts/ecc.js catalog profiles
node tools-sandbox/ECC/scripts/ecc.js consult "knowledge ops and AI-first learning system"
node tools-sandbox/ECC/scripts/ecc.js plan --profile minimal --target codex
```

Important: treat `plan` output as advisory. Do not run full install until the target and scope are reviewed.

## Recommended Components To Study First

| ECC source | Why it matters |
|---|---|
| `skills/knowledge-ops/SKILL.md` | Multi-layer knowledge storage and sync workflow |
| `rules/common/development-workflow.md` | Research, plan, TDD, review, commit loop |
| `rules/common/security.md` | Secret and safety discipline |
| `rules/common/git-workflow.md` | Commit/push hygiene |
| `.codex/AGENTS.md` | Codex-specific boundaries and multi-agent guidance |
| `.codex-plugin/README.md` | Codex plugin distribution model and MCP warnings |

## How ECC Should Evolve Here

1. Turn repeated learning workflows into `wiki/practice/` playbooks.
2. Turn stable workflows into project-local skills under `skills/`.
3. Add Cursor rules only when they improve local editing behavior.
4. Add Codex plugin/global config only after the local workflow is stable.
5. Keep MCP count small and credentials outside the repo.

## Anti-Patterns

- Do not install ECC plugin and full installer together.
- Do not copy every rules directory.
- Do not enable all MCP servers by default.
- Do not let hooks modify or block this vault before we trust the workflow.
- Do not treat ECC memory as canonical knowledge.

## Sources

- [ECC README](https://github.com/affaan-m/ECC/blob/main/README.md)
- Local checkout: `tools-sandbox/ECC`
