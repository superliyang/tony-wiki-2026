# Tony AI First Wiki: Agent Instructions

This repository is Tony's new main AI First knowledge workspace. Treat it as an Obsidian-readable, GitHub-publishable knowledge base, not a temporary automation scratchpad.

## Tony Operating Boundary

- New main vault: `/Users/tony/Vault/tony-wiki-2026`.
- Legacy mature vault: `/Users/tony/Vault/tony2026`.
- The legacy vault must remain read-only unless Tony explicitly asks otherwise.
- The legacy vault is included in this new vault as a filtered staged copy under `00-Inbox-AI/legacy-tony2026/`.
- Do not create symlinks or live coupling from this vault back to the legacy vault; the new vault should work when pushed to GitHub and opened in Obsidian elsewhere.
- OpenHuman, Hermes, and ECC may write only to staging/inbox areas by default. Canonical wiki pages under `wiki/` require review and intentional promotion.
- Never commit secrets, tokens, local auth files, or runtime account state. Keep examples, remove `.env.local` copies.

## Tool Roles

- OpenHuman: ingestion layer. It may create drafts under `00-Inbox-AI/openhuman/`.
- Hermes: long-running personal agent. It may capture Weixin/assistant notes under `00-Inbox-AI/hermes/` or `00-Inbox-AI/weixin/`.
- ECC: engineering capability layer. It is a source of methods, rules, skills, and playbooks; do not let it globally modify Codex/Claude/MCP/hooks without an explicit reviewed install plan.
- ECC is currently adopted project-locally through `.cursor/rules/ecc-ai-first-knowledge.mdc`, `skills/ai-first-work-center/SKILL.md`, and wiki playbooks. Do not run global ECC installers unless Tony explicitly asks.
- Obsidian/Markdown: canonical knowledge asset layer.
- Codex/Cursor/Claude Code: engineering and curation agents that promote staged material into `wiki/`.

# claude-obsidian: Base Agent Instructions

This repo is a Claude Code plugin **and** an Obsidian vault that builds persistent, compounding knowledge bases using Andrej Karpathy's LLM Wiki pattern. It works with **any AI coding agent** that supports the Agent Skills standard, including Codex CLI, OpenCode, and similar.

Originally built for Claude Code, the skills follow the cross-platform Agent Skills spec. Newer skills (`wiki-fold`, `wiki-ingest`, `wiki-lint`) use only `name` and `description` frontmatter (kepano convention). Some older skills still carry an optional `allowed-tools` field for Claude Code compatibility; cross-platform agents that do not recognize it should ignore it.

## Skills Discovery

All skills live in `skills/<name>/SKILL.md`. Codex / OpenCode / other Agent Skills compatible agents will auto-discover them when you symlink the directory:

```bash
# Codex CLI
ln -s "$(pwd)/skills" ~/.codex/skills/claude-obsidian

# OpenCode
ln -s "$(pwd)/skills" ~/.opencode/skills/claude-obsidian
```

Or run the bundled installer:

```bash
bash bin/setup-multi-agent.sh
```

## Available Skills

| Skill | Trigger phrases |
|---|---|
| `wiki` | `/wiki`, set up wiki, scaffold vault |
| `wiki-ingest` | ingest, ingest this url, ingest this image, batch ingest |
| `wiki-query` | query, what do you know about, query quick:, query deep: |
| `wiki-lint` | lint the wiki, health check, find orphans |
| `wiki-fold` | fold the log, run a fold, log rollup (DragonScale Mechanism 1, opt-in) |
| `save` | /save, file this conversation |
| `autoresearch` | autoresearch, autonomous research loop |
| `canvas` | /canvas, add to canvas, create canvas |
| `defuddle` | clean this url, defuddle |
| `obsidian-markdown` | obsidian syntax, wikilink, callout |
| `obsidian-bases` | obsidian bases, .base file, dynamic table |
| `ai-first-work-center` | AI First work center, Hermes/OpenHuman/ECC, autonomous learning scout, candidate review |

## Key Conventions

- **Vault root**: the directory containing `wiki/` and `.raw/`
- **Hot cache**: `wiki/hot.md` (read at session start, updated at session end)
- **Source documents**: `.raw/` (immutable: agents never modify these)
- **Generated knowledge**: `wiki/` (agent-owned, links to sources via wikilinks)
- **Manifest**: `.raw/.manifest.json` tracks ingested sources (delta tracking)

## Bootstrap

When the user opens this project for the first time:

1. Read this file (`AGENTS.md`) and the project `CLAUDE.md` for full context
2. Read `skills/wiki/SKILL.md` for the orchestration pattern
3. If `wiki/hot.md` exists, read it silently to restore recent context
4. If the user types `/wiki` (or "set up wiki"), follow the wiki skill's scaffold workflow

## Reference

- Plugin homepage: https://github.com/AgriciDaniel/claude-obsidian
- Pattern source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Cross-reference: https://github.com/kepano/obsidian-skills (authoritative Obsidian-specific skills)
