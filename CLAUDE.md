# AI 全域知识体系: LLM Wiki

Mode: E (Research) extended
Purpose: AI 领域全维度知识库 — 公司、人物、论文、产品、模型、工具、开源项目、生态、实战落地
Owner: Tony
Created: 2026-05-16

## Structure

```
.raw/               immutable source documents — never modify
wiki/
├── index.md        master catalog: update on every ingest
├── log.md          append-only operation log
├── hot.md          hot cache: ~500-word recent context
├── overview.md     executive summary
├── papers/         paper summaries with key claims and methodology
├── concepts/       AI concepts, model architectures, frameworks
├── entities/       companies, people, products
├── tools/          tools, platforms, infrastructure
├── open-source/    open source project tracking
├── ecosystem/      chips, compute, policy, investment
├── practice/       real-world cases, methodology, best practices
├── timeline/       AI development milestones
├── comparisons/    side-by-side analyses
├── questions/      filed answers to user queries
├── sources/        one summary page per raw source
├── maps/           Image2 panoramic visual maps
└── meta/           dashboards, lint reports
_attachments/
├── panoramas/      Image2 generated panoramas
├── diagrams/       architecture diagrams
├── infographics/   infographics
└── models/         model structure visualizations
_templates/         Obsidian Templater templates
```

## Conventions

- All notes use YAML frontmatter: type, status, created, updated, tags
- Wikilinks use [[Note Name]] format: filenames are unique, no paths needed
- .raw/ contains source documents: never modify them
- wiki/index.md is the master catalog: update on every ingest
- wiki/log.md is append-only: never edit past entries
- New log entries go at the TOP of the file

## Operations

- Ingest: drop source in .raw/, say "ingest [filename]"
- Query: ask any question: reads index first, then drills in
- Lint: say "lint the wiki" for health check
- Panorama: generate Image2 panoramas into _attachments/panoramas/

## Cross-Project Access

To reference this wiki from another Claude Code project, add to that project's CLAUDE.md:

```markdown
## Wiki Knowledge Base
Path: /Users/tony/Vault/tony-wiki-2026

When you need context not already in this project:
1. Read wiki/hot.md first (recent context, ~500 words)
2. If not enough, read wiki/index.md
3. If you need domain specifics, read wiki/<domain>/_index.md
4. Only then read individual wiki pages

Do NOT read the wiki for general coding questions or things already in this project.
```
