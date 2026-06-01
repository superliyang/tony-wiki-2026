#!/usr/bin/env python3
"""
Daily AI Learning Scout demo.

Collects low-risk public signals, scores them against this vault's visible
memory, writes reviewable Markdown/JSONL artifacts, and optionally sends a
short Hermes notification.
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import html
import json
import os
import re
import sqlite3
import subprocess
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "00-Inbox-AI"
TODAY = dt.datetime.now().date().isoformat()

PUBLIC_SOURCES = [
    {
        "name": "Anthropic News",
        "kind": "news",
        "url": "https://www.anthropic.com/news/rss.xml",
        "category": "ai-engineering",
    },
    {
        "name": "Cloudflare Blog",
        "kind": "news",
        "url": "https://blog.cloudflare.com/rss/",
        "category": "cloud-security",
    },
    {
        "name": "arXiv cs.AI",
        "kind": "papers",
        "url": "https://export.arxiv.org/rss/cs.AI",
        "category": "papers",
    },
    {
        "name": "arXiv cs.CL",
        "kind": "papers",
        "url": "https://export.arxiv.org/rss/cs.CL",
        "category": "papers",
    },
]

GITHUB_REPOS = [
    "NousResearch/hermes-agent",
    "tinyhumansai/openhuman",
    "affaan-m/ECC",
    "langchain-ai/langgraph",
    "openai/codex",
]

FOCUS_TERMS = [
    "agent",
    "agents",
    "agentic",
    "memory",
    "context",
    "workflow",
    "automation",
    "knowledge",
    "obsidian",
    "github",
    "hermes",
    "openhuman",
    "ecc",
    "codex",
    "cursor",
    "skills",
    "mcp",
    "security",
    "evaluation",
    "eval",
    "open source",
    "rag",
    "reasoning",
    "learning",
]


def fetch_text(url: str, timeout: int = 20) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "tony-ai-first-learning-scout/0.1",
            "Accept": "application/rss+xml, application/json, text/xml, */*",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def strip_html(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value or "")
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def parse_date(value: str) -> str:
    if not value:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed:
            return parsed.date().isoformat()
    except Exception:
        pass
    return value[:40]


def text_of(node: ET.Element, names: Iterable[str]) -> str:
    for name in names:
        found = node.find(name)
        if found is not None and found.text:
            return found.text.strip()
    return ""


def parse_rss(source: Dict[str, str], body: str, limit: int) -> List[Dict[str, object]]:
    root = ET.fromstring(body)
    items = root.findall(".//item")
    if not items:
        items = root.findall("{http://www.w3.org/2005/Atom}entry")

    out: List[Dict[str, object]] = []
    for item in items[:limit]:
        title = text_of(item, ["title", "{http://www.w3.org/2005/Atom}title"])
        link = text_of(item, ["link"])
        atom_link = item.find("{http://www.w3.org/2005/Atom}link")
        if not link and atom_link is not None:
            link = atom_link.attrib.get("href", "")
        summary = text_of(
            item,
            [
                "description",
                "summary",
                "{http://www.w3.org/2005/Atom}summary",
                "{http://www.w3.org/2005/Atom}content",
            ],
        )
        published = text_of(
            item,
            [
                "pubDate",
                "published",
                "updated",
                "{http://www.w3.org/2005/Atom}published",
                "{http://www.w3.org/2005/Atom}updated",
            ],
        )
        if title:
            out.append(
                {
                    "source": source["name"],
                    "source_kind": source["kind"],
                    "category": source["category"],
                    "title": strip_html(title),
                    "url": link,
                    "summary": strip_html(summary)[:600],
                    "published": parse_date(published),
                    "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                }
            )
    return out


def collect_rss(limit_per_source: int) -> Tuple[List[Dict[str, object]], List[str]]:
    signals: List[Dict[str, object]] = []
    errors: List[str] = []
    for source in PUBLIC_SOURCES:
        try:
            body = fetch_text(source["url"])
            signals.extend(parse_rss(source, body, limit_per_source))
        except Exception as exc:
            errors.append(f"{source['name']}: {type(exc).__name__}: {exc}")
    return signals, errors


def collect_github(limit: int) -> Tuple[List[Dict[str, object]], List[str]]:
    signals: List[Dict[str, object]] = []
    errors: List[str] = []
    for repo in GITHUB_REPOS[:limit]:
        try:
            url = f"https://api.github.com/repos/{repo}/releases/latest"
            data = json.loads(fetch_text(url))
            signals.append(
                {
                    "source": "GitHub Releases",
                    "source_kind": "github",
                    "category": "open-source",
                    "title": f"{repo}: {data.get('name') or data.get('tag_name')}",
                    "url": data.get("html_url") or f"https://github.com/{repo}",
                    "summary": strip_html(data.get("body") or "")[:600],
                    "published": (data.get("published_at") or "")[:10],
                    "repo": repo,
                    "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                }
            )
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                signals.append(
                    {
                        "source": "GitHub",
                        "source_kind": "github",
                        "category": "open-source",
                        "title": f"{repo}: repository watch",
                        "url": f"https://github.com/{repo}",
                        "summary": "No latest release endpoint available. Keep on watchlist.",
                        "published": "",
                        "repo": repo,
                        "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                    }
                )
            else:
                errors.append(f"{repo}: HTTP {exc.code}")
        except Exception as exc:
            errors.append(f"{repo}: {type(exc).__name__}: {exc}")
    return signals, errors


def collect_cisa(limit: int = 8) -> Tuple[List[Dict[str, object]], List[str]]:
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    try:
        data = json.loads(fetch_text(url))
        vulns = data.get("vulnerabilities", [])
        vulns = sorted(vulns, key=lambda x: x.get("dateAdded", ""), reverse=True)[:limit]
        return [
            {
                "source": "CISA KEV",
                "source_kind": "security",
                "category": "security",
                "title": f"{v.get('cveID')}: {v.get('vendorProject')} {v.get('product')}",
                "url": url,
                "summary": strip_html(v.get("shortDescription") or "")[:600],
                "published": v.get("dateAdded", ""),
                "cve": v.get("cveID", ""),
                "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            }
            for v in vulns
        ], []
    except Exception as exc:
        return [], [f"CISA KEV: {type(exc).__name__}: {exc}"]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def load_context() -> str:
    parts = [
        read_text(ROOT / "wiki/hot.md"),
        read_text(INBOX / "agent-memory/profile.md"),
        read_text(INBOX / "agent-memory/preferences.md"),
        read_text(INBOX / "agent-memory/learning-themes.md"),
        read_text(INBOX / "agent-memory/negative-signals.md"),
        read_text(ROOT / "wiki/practice/Legacy Vault Inventory.md"),
    ]
    return "\n".join(parts).lower()


def openhuman_snapshot() -> Dict[str, object]:
    base = Path.home() / ".openhuman/users/local-tonylidemacbook-pro-local/workspace"
    snapshot = {
        "vaults": 0,
        "vault_files": 0,
        "memory_docs": 0,
        "memory_tree_chunks": 0,
        "cron_jobs": 0,
    }
    dbs = {
        "vault": base / "vault/vault.db",
        "memory": base / "memory/memory.db",
        "memory_tree": base / "memory_tree/chunks.db",
        "cron": base / "cron/jobs.db",
    }
    try:
        con = sqlite3.connect(str(dbs["vault"]))
        snapshot["vaults"] = con.execute("select count(*) from vaults").fetchone()[0]
        snapshot["vault_files"] = con.execute("select count(*) from vault_files").fetchone()[0]
        con.close()
    except Exception:
        pass
    try:
        con = sqlite3.connect(str(dbs["memory"]))
        snapshot["memory_docs"] = con.execute("select count(*) from memory_docs").fetchone()[0]
        con.close()
    except Exception:
        pass
    try:
        con = sqlite3.connect(str(dbs["memory_tree"]))
        snapshot["memory_tree_chunks"] = con.execute("select count(*) from mem_tree_chunks").fetchone()[0]
        con.close()
    except Exception:
        pass
    try:
        con = sqlite3.connect(str(dbs["cron"]))
        snapshot["cron_jobs"] = con.execute("select count(*) from cron_jobs").fetchone()[0]
        con.close()
    except Exception:
        pass
    return snapshot


def score_signal(signal: Dict[str, object], context: str) -> Tuple[int, List[str]]:
    haystack = f"{signal.get('title', '')} {signal.get('summary', '')} {signal.get('category', '')}".lower()
    reasons: List[str] = []
    score = 0
    for term in FOCUS_TERMS:
        if term in haystack:
            score += 3
            reasons.append(f"matches focus term `{term}`")
        elif term in context and term in haystack:
            score += 2
    if signal.get("source_kind") in {"github", "papers"}:
        score += 2
        reasons.append(f"{signal.get('source_kind')} signal")
    if "security" in haystack or signal.get("source_kind") == "security":
        score += 1
        reasons.append("security relevance")
    if signal.get("published") == TODAY:
        score += 2
        reasons.append("fresh today")
    elif str(signal.get("published", ""))[:7] == TODAY[:7]:
        score += 1
        reasons.append("fresh this month")
    if not reasons:
        reasons.append("general watchlist signal")
    return score, reasons[:4]


def dedupe(signals: List[Dict[str, object]]) -> List[Dict[str, object]]:
    seen = set()
    out = []
    for signal in signals:
        key = (signal.get("url") or signal.get("title") or "").strip().lower()
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(signal)
    return out


def action_for(score: int, signal: Dict[str, object]) -> str:
    text = f"{signal.get('title', '')} {signal.get('summary', '')}".lower()
    if score >= 9:
        return "study"
    if "release" in text or signal.get("source_kind") == "github":
        return "watch"
    if score >= 6:
        return "study"
    if score >= 4:
        return "watch"
    return "discard"


def candidate_topic(signal: Dict[str, object]) -> str:
    title = str(signal.get("title", "")).strip()
    title = re.sub(r"^[^:]+:\s*", "", title)
    title = re.sub(r"\s+", " ", title)
    return title[:90] or "Untitled signal"


def ensure_dirs() -> None:
    for path in [
        INBOX / "signals/news",
        INBOX / "signals/github",
        INBOX / "signals/papers",
        INBOX / "signals/industry",
        INBOX / "signals/openhuman",
        INBOX / "candidates/topics",
        INBOX / "review-queue/pending",
        INBOX / "reports/daily",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def write_jsonl(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def md_escape(value: object) -> str:
    return str(value or "").replace("\n", " ").strip()


def build_markdown(
    ranked: List[Dict[str, object]],
    errors: List[str],
    snapshot: Dict[str, object],
    max_candidates: int,
) -> Tuple[str, str, str]:
    top = ranked[:max_candidates]
    generated = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        "---",
        f'title: "Daily AI Learning Scout {TODAY}"',
        f"created: {TODAY}",
        "status: pending-review",
        "tags:",
        "  - ai-first",
        "  - daily-scout",
        "  - review-queue",
        "---",
        "",
        f"# Daily AI Learning Scout {TODAY}",
        "",
        f"Generated: {generated}",
        "",
        "## Executive Summary",
        "",
        f"- Signals collected: {len(ranked)}",
        f"- Candidate topics: {len(top)}",
        f"- OpenHuman snapshot: {snapshot.get('vault_files')} vault file(s), {snapshot.get('memory_docs')} memory doc(s), {snapshot.get('memory_tree_chunks')} memory-tree chunk(s)",
        "- Canonical wiki was not modified.",
        "",
    ]
    if errors:
        lines.extend(["## Collection Warnings", ""])
        lines.extend([f"- {e}" for e in errors[:8]])
        lines.append("")

    lines.extend(["## Candidate Topics", ""])
    for idx, item in enumerate(top, 1):
        signal = item["signal"]
        reasons = "; ".join(item["reasons"])
        summary = md_escape(signal.get("summary"))[:500].strip()
        lines.extend(
            [
                f"### {idx}. {candidate_topic(signal)}",
                "",
                f"- Action: `{item['action']}`",
                f"- Score: `{item['score']}`",
                f"- Source: {md_escape(signal.get('source'))} / {md_escape(signal.get('category'))}",
                f"- Published: {md_escape(signal.get('published'))}",
                f"- Why: {reasons}",
                f"- Link: {md_escape(signal.get('url'))}",
                f"- Summary: {summary}",
                "",
            ]
        )

    lines.extend(
        [
            "## Decision Commands",
            "",
            "Use these decisions in the next review loop:",
            "",
            "```text",
            "study <number>",
            "watch <number>",
            "discard <number>",
            "promote <number>",
            "build <number>",
            "```",
            "",
            "## Suggested Next Step",
            "",
            "Pick one `study` candidate and ask Codex/Hermes to promote it into a formal wiki note or learning plan.",
            "",
        ]
    )
    report = "\n".join(lines)

    review = report.replace("# Daily AI Learning Scout", "# Review Queue: Daily AI Learning Scout", 1)

    candidate_lines = [
        "---",
        f'title: "Candidate Topics {TODAY}"',
        f"created: {TODAY}",
        "status: pending-review",
        "tags:",
        "  - candidates",
        "  - learning-topics",
        "---",
        "",
        f"# Candidate Topics {TODAY}",
        "",
    ]
    for idx, item in enumerate(top, 1):
        signal = item["signal"]
        candidate_lines.extend(
            [
                f"## {idx}. {candidate_topic(signal)}",
                "",
                f"- action: `{item['action']}`",
                f"- score: `{item['score']}`",
                f"- source: {md_escape(signal.get('source'))}",
                f"- url: {md_escape(signal.get('url'))}",
                "",
            ]
        )
    candidates = "\n".join(candidate_lines)
    return report, review, candidates


def send_notification(target: str, report_path: Path, ranked: List[Dict[str, object]]) -> Tuple[bool, str]:
    top = ranked[:3]
    body_lines = [f"Daily AI Learning Scout {TODAY}", "", f"Report: {report_path}"]
    for idx, item in enumerate(top, 1):
        body_lines.append(f"{idx}. [{item['action']}] {candidate_topic(item['signal'])}")
    body = "\n".join(body_lines)
    try:
        result = subprocess.run(
            ["hermes", "send", "--to", target, "--subject", "[AI Scout Demo]", body],
            cwd=str(ROOT),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )
        return result.returncode == 0, result.stdout.strip()
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def send_feishu_webhook(webhook_url: str, report_path: Path, ranked: List[Dict[str, object]]) -> Tuple[bool, str]:
    top = ranked[:5]
    lines = [
        f"AI Scout Demo {TODAY}",
        "",
        f"Signals: {len(ranked)}",
        f"Report: {report_path}",
        "",
        "Top candidates:",
    ]
    for idx, item in enumerate(top, 1):
        lines.append(f"{idx}. [{item['action']}] {candidate_topic(item['signal'])}")
    payload = {"msg_type": "text", "content": {"text": "\n".join(lines)}}
    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8", errors="replace")
        ok = '"StatusCode":0' in body or '"code":0' in body
        return ok, body
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run the Daily AI Learning Scout demo.")
    parser.add_argument("--limit-per-source", type=int, default=8)
    parser.add_argument("--max-candidates", type=int, default=5)
    parser.add_argument("--notify-target", default="", help="Hermes send target, e.g. weixin")
    parser.add_argument(
        "--feishu-webhook-env",
        default="",
        help="Read a Feishu bot webhook URL from this environment variable.",
    )
    parser.add_argument("--no-network", action="store_true", help="Use only local OpenHuman/vault context.")
    args = parser.parse_args(argv)

    ensure_dirs()
    errors: List[str] = []
    signals: List[Dict[str, object]] = []

    if not args.no_network:
        rss, rss_errors = collect_rss(args.limit_per_source)
        gh, gh_errors = collect_github(limit=5)
        cisa, cisa_errors = collect_cisa(limit=8)
        signals.extend(rss)
        signals.extend(gh)
        signals.extend(cisa)
        errors.extend(rss_errors + gh_errors + cisa_errors)

    snapshot = openhuman_snapshot()
    signals.append(
        {
            "source": "OpenHuman Local Snapshot",
            "source_kind": "openhuman",
            "category": "personal-context",
            "title": "OpenHuman configuration and memory readiness",
            "url": "file://~/.openhuman",
            "summary": (
                f"OpenHuman has {snapshot.get('vaults')} vault(s), "
                f"{snapshot.get('vault_files')} indexed vault file(s), "
                f"{snapshot.get('memory_docs')} memory doc(s), and "
                f"{snapshot.get('memory_tree_chunks')} memory tree chunk(s)."
            ),
            "published": TODAY,
            "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
    )

    signals = dedupe(signals)
    context = load_context()
    ranked: List[Dict[str, object]] = []
    for signal in signals:
        score, reasons = score_signal(signal, context)
        ranked.append(
            {
                "score": score,
                "action": action_for(score, signal),
                "reasons": reasons,
                "signal": signal,
            }
        )
    ranked.sort(key=lambda item: item["score"], reverse=True)

    signal_rows = [
        {
            **item["signal"],
            "score": item["score"],
            "action": item["action"],
            "reasons": item["reasons"],
        }
        for item in ranked
    ]
    write_jsonl(INBOX / f"signals/news/{TODAY}-daily-ai-learning-scout.jsonl", signal_rows)

    report, review, candidates = build_markdown(ranked, errors, snapshot, args.max_candidates)
    report_path = INBOX / f"reports/daily/{TODAY}-daily-ai-learning-scout.md"
    review_path = INBOX / f"review-queue/pending/{TODAY}-daily-ai-learning-scout.md"
    candidates_path = INBOX / f"candidates/topics/{TODAY}-daily-ai-learning-scout.md"
    report_path.write_text(report, encoding="utf-8")
    review_path.write_text(review, encoding="utf-8")
    candidates_path.write_text(candidates, encoding="utf-8")

    print(f"signals={len(ranked)}")
    print(f"report={report_path}")
    print(f"review={review_path}")
    print(f"candidates={candidates_path}")
    for idx, item in enumerate(ranked[: args.max_candidates], 1):
        print(f"{idx}. [{item['action']}] score={item['score']} {candidate_topic(item['signal'])}")

    delivery_lines: List[str] = []
    exit_code = 0

    if args.notify_target:
        ok, message = send_notification(args.notify_target, report_path, ranked)
        print(f"notify={'ok' if ok else 'failed'}")
        if message:
            print(textwrap.shorten(message, width=500, placeholder=" ..."))
        delivery_lines.append(f"- Hermes send `{args.notify_target}`: {'ok' if ok else 'failed'}")
        if not ok:
            delivery_lines.append(f"  - Detail: {textwrap.shorten(message, width=300, placeholder=' ...')}")
            exit_code = 1

    if args.feishu_webhook_env:
        webhook_url = os.environ.get(args.feishu_webhook_env, "")
        if webhook_url:
            ok, message = send_feishu_webhook(webhook_url, report_path, ranked)
            print(f"feishu={'ok' if ok else 'failed'}")
            print(textwrap.shorten(message, width=500, placeholder=" ..."))
            delivery_lines.append(f"- Feishu webhook `{args.feishu_webhook_env}`: {'ok' if ok else 'failed'}")
            if not ok:
                delivery_lines.append(f"  - Detail: {textwrap.shorten(message, width=300, placeholder=' ...')}")
                exit_code = 1
        else:
            print(f"feishu=skipped missing env {args.feishu_webhook_env}")
            delivery_lines.append(f"- Feishu webhook `{args.feishu_webhook_env}`: skipped, env var missing")
            exit_code = 1

    if delivery_lines:
        delivery = "\n\n## Demo Delivery\n\n" + "\n".join(delivery_lines) + "\n"
        for path in (report_path, review_path):
            with path.open("a", encoding="utf-8") as fh:
                fh.write(delivery)

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
