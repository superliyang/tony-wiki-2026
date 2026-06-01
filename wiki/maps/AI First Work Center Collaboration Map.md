---
type: map
title: "AI First Work Center Collaboration Map"
created: 2026-06-01
updated: 2026-06-01
status: active
tags:
  - maps
  - ai-first
  - hermes
  - openhuman
  - ecc
  - obsidian
related:
  - "[[Autonomous AI First Learning Engine]]"
  - "[[Personal AI Work Center Architecture]]"
  - "[[AI First Personal Knowledge Stack]]"
---

# AI First Work Center Collaboration Map

Navigation: [[_index]] | [[Autonomous AI First Learning Engine]] | [[Personal AI Work Center Architecture]]

## Diagram 1: Collaboration Architecture

This diagram answers: who does what, where memory lives, and what is allowed to write durable knowledge.

```mermaid
flowchart TB
    User["Tony<br/>goals, decisions, feedback"]:::person

    subgraph Entry["Entry and Interaction"]
        Weixin["Weixin<br/>quick capture"]
        Feishu["Feishu<br/>notifications and review"]
        WebUI["Hermes Web UI<br/>control panel"]
        Obsidian["Obsidian<br/>read and edit"]
        Codex["Codex / Cursor<br/>curation and implementation"]
    end

    subgraph Runtime["Active Agent Runtime"]
        Hermes["Hermes<br/>scheduler, scout, notifier"]
        HermesMemory["Hermes sessions<br/>short-term context"]
    end

    subgraph Intake["Ingestion and Personal Context"]
        OpenHuman["OpenHuman<br/>multi-source ingestion"]
        MemoryTree["Memory Tree<br/>personal context evidence"]
        External["External sources<br/>news, GitHub, papers, docs, chat"]
    end

    subgraph Protocol["Shared Memory Protocol"]
        Signals["signals/<br/>raw evidence"]
        Candidates["candidates/<br/>topic, project, skill proposals"]
        Review["review-queue/<br/>pending, accepted, deferred, discarded"]
        AgentMemory["agent-memory/<br/>profile, preferences, themes"]
        Reports["reports/<br/>daily, weekly, monthly"]
    end

    subgraph Method["Operating Method"]
        ECC["ECC<br/>rules, skills, hooks, playbooks"]
        ProjectRules["Project-local rules<br/>Cursor, skills, playbooks"]
    end

    subgraph Durable["Durable Knowledge Assets"]
        Wiki["wiki/<br/>canonical notes"]
        Maps["maps and indexes<br/>navigation layer"]
        Git["Git<br/>diff and history"]
        GitHub["GitHub<br/>backup and publication"]
    end

    User --> Weixin
    User --> Obsidian
    User --> WebUI
    Weixin --> Hermes
    Feishu --> User
    WebUI --> Hermes
    Codex --> Protocol
    Codex --> Wiki

    External --> OpenHuman
    OpenHuman --> MemoryTree
    MemoryTree --> Signals
    OpenHuman --> Signals

    Hermes --> Signals
    Hermes --> Candidates
    Hermes --> Reports
    Hermes --> Feishu
    Hermes --> Weixin
    Hermes --> HermesMemory

    Signals --> Candidates
    Candidates --> Review
    Review -->|"accepted or promoted"| Wiki
    Review -->|"discarded"| AgentMemory
    Reports --> User
    AgentMemory -.guides scoring.-> Hermes
    Wiki -.grounds recommendations.-> Hermes

    ECC --> ProjectRules
    ProjectRules --> Codex
    ProjectRules --> Hermes
    Review -->|"repeatable workflow"| ECC

    Wiki --> Maps
    Wiki --> Git
    Protocol --> Git
    Git --> GitHub
    Obsidian --> Wiki

    classDef person fill:#fff2cc,stroke:#d6b656,color:#1f1f1f;
    classDef runtime fill:#e1f5fe,stroke:#0288d1,color:#1f1f1f;
    classDef intake fill:#e8f5e9,stroke:#43a047,color:#1f1f1f;
    classDef protocol fill:#f3e5f5,stroke:#8e24aa,color:#1f1f1f;
    classDef method fill:#fff3e0,stroke:#fb8c00,color:#1f1f1f;
    classDef durable fill:#eceff1,stroke:#546e7a,color:#1f1f1f;

    class Hermes,HermesMemory runtime;
    class OpenHuman,MemoryTree,External intake;
    class Signals,Candidates,Review,AgentMemory,Reports protocol;
    class ECC,ProjectRules method;
    class Wiki,Maps,Git,GitHub,Obsidian durable;
```

## Diagram 2: Daily Autonomous Learning Flow

This diagram answers: how a real external signal becomes a learning recommendation or durable note.

```mermaid
flowchart LR
    A["External signal<br/>news, repo, paper, doc"]:::source
    B["Collect<br/>Hermes scout or OpenHuman import"]:::observe
    C["Normalize<br/>clean title, source, date, link"]:::observe
    D["Compare<br/>wiki, hot cache, agent-memory"]:::think
    E["Score<br/>relevance, novelty, timing"]:::think
    F{"Action?"}:::decision

    F -->|"study"| G["Study candidate<br/>candidates/topics"]
    F -->|"watch"| H["Trend watch<br/>reports/weekly"]
    F -->|"discard"| I["Negative signal<br/>agent-memory"]
    F -->|"promote"| J["Draft note<br/>review-queue/pending"]
    F -->|"build"| K["Project idea<br/>candidates/projects"]

    G --> L["Daily report<br/>reports/daily"]
    H --> L
    I --> L
    J --> L
    K --> L

    L --> M["Notify<br/>Weixin or Feishu"]
    M --> N["Tony decides<br/>accept, defer, discard"]

    N -->|"accept study"| O["Update learning themes"]
    N -->|"accept promote"| P["Codex/Hermes drafts wiki note"]
    N -->|"accept build"| Q["Create playbook or task"]
    N -->|"discard"| R["Update negative signals"]

    P --> S["Review and link<br/>indexes, maps, sources"]
    Q --> T["ECC extraction<br/>skill, rule, playbook"]
    O --> U["agent-memory updated"]
    R --> U
    S --> V["Git checkpoint"]
    T --> V
    U --> V
    V --> W["GitHub sync"]

    A --> B --> C --> D --> E --> F

    classDef source fill:#e8f5e9,stroke:#43a047,color:#1f1f1f;
    classDef observe fill:#e1f5fe,stroke:#0288d1,color:#1f1f1f;
    classDef think fill:#f3e5f5,stroke:#8e24aa,color:#1f1f1f;
    classDef decision fill:#fff2cc,stroke:#d6b656,color:#1f1f1f;
```

## Diagram 3: Memory Ownership

This diagram answers: which memory is allowed to be trusted.

```mermaid
flowchart TB
    subgraph Hidden["Tool-native memory<br/>useful but not canonical"]
        HM["Hermes sessions"]
        OHM["OpenHuman memory DB"]
        MT["OpenHuman Memory Tree"]
        Logs["Runtime logs"]
    end

    subgraph Shared["Shared reviewable memory<br/>cross-tool contract"]
        AM["agent-memory/*.md"]
        Cands["candidates/*.md"]
        Queue["review-queue/*.md"]
        Reports["reports/*.md"]
    end

    subgraph Canonical["Canonical durable memory"]
        Notes["wiki/*.md"]
        Indexes["wiki/index.md<br/>maps and indexes"]
        GitHist["Git history"]
    end

    HM --> Reports
    OHM --> Reports
    MT --> Cands
    Logs --> Reports

    Reports --> Queue
    Cands --> Queue
    Queue -->|"accepted"| Notes
    Queue -->|"discarded or deferred"| AM
    Notes --> Indexes
    Notes --> GitHist
    AM --> GitHist

    classDef hidden fill:#eeeeee,stroke:#9e9e9e,color:#1f1f1f;
    classDef shared fill:#f3e5f5,stroke:#8e24aa,color:#1f1f1f;
    classDef canonical fill:#e8f5e9,stroke:#43a047,color:#1f1f1f;
```

## Collaboration Rules

- Hermes can proactively collect, score, recommend, and notify.
- OpenHuman can ingest broad sources and produce personal-context evidence.
- ECC can capture repeatable workflows as skills, rules, hooks, and playbooks.
- Obsidian is where durable knowledge is read and shaped.
- GitHub is where reviewed knowledge becomes portable and recoverable.
- Hidden tool memory is useful, but Markdown plus Git is the shared truth.

## First Implementation Slice

Build `Daily AI Learning Scout`:

```text
Hermes scheduled job
-> collect sources
-> compare with wiki/hot.md and agent-memory
-> write candidates and daily report
-> notify Weixin or Feishu
-> Tony decides
-> accepted items become wiki notes or ECC playbooks
```
