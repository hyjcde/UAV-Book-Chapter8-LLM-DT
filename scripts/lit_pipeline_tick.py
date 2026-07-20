#!/usr/bin/env python3
"""One tick of the Ch.8 literature + coverage pipeline.

Classifies bibliography / watchlist items, writes a timestamped tick report,
and refreshes STATE.yaml counts. Does NOT add unpublished items to references.bib.
"""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "literature"
BIB = ROOT / "latex" / "shared" / "references.bib"
EN = ROOT / "latex" / "en" / "ch08.tex"
CN = ROOT / "latex" / "cn" / "ch08_cn.tex"
STATE = LIT / "STATE.yaml"
TICKS = LIT / "ticks"
WATCH = LIT / "UNPUBLISHED_WATCHLIST.md"
CAND = LIT / "PUBLISHED_CANDIDATES.md"
AUDIT = LIT / "COVERAGE_AUDIT.md"


def classify_body(body: str) -> list[str]:
    bl = body.lower()
    flags: list[str] = []
    if "under review" in bl or "manuscript under review" in bl:
        flags.append("under-review")
    if "arxiv preprint" in bl or "eprint" in bl or "archiveprefix" in bl or "archivePrefix" in body:
        flags.append("preprint")
    if "verify" in bl or "placeholder" in bl:
        flags.append("unverified")
    if "ahead-of-print" in bl:
        flags.append("ahead-of-print")
    if "in press" in bl:
        flags.append("in-press")
    return flags or ["published-or-clean"]


def parse_bib(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    entries = []
    for m in re.finditer(r"@(\w+)\{([^,]+),([\s\S]*?)(?=\n@|\Z)", text):
        typ, key, body = m.group(1), m.group(2), m.group(3)
        flags = classify_body(body)
        title = ""
        tm = re.search(r"title\s*=\s*[\{]([^}]+)", body, re.I)
        if tm:
            title = re.sub(r"[{}]", "", tm.group(1))[:120]
        entries.append({"key": key, "type": typ, "flags": flags, "title": title})
    return entries


def cites_in(path: Path) -> set[str]:
    t = path.read_text(encoding="utf-8")
    keys: set[str] = set()
    for m in re.finditer(r"\\cite[tp]?\{([^}]+)\}", t):
        for k in m.group(1).split(","):
            keys.add(k.strip())
    return keys


def keyword_coverage(text: str) -> dict[str, bool]:
    low = text.lower()
    return {
        "twin": any(w in low for w in ["digital twin", "数字孪生", "geobim"]),
        "llm": any(w in low for w in ["transformer", "large language", "大语言模型", "instruct"]),
        "vlm": any(w in low for w in ["vision--language", "vision-language", "视觉—语言", "clip", "vlm"]),
        "rag": "rag" in low or "retrieval-augmented" in low or "检索增强" in low,
        "agent": any(w in low for w in ["agent", "智能体", "react", "toolformer"]),
        "memory": any(w in low for w in ["memory", "记忆", "memgpt", "parametric memory", "non-parametric"]),
        "frontier": any(w in low for w in ["frontier", "agentic rag", "cognitive twin", "前沿", "vlm-native"]),
        "delivery": any(w in low for w in ["report", "报告", "decision support", "决策支持"]),
    }


def main() -> int:
    LIT.mkdir(exist_ok=True)
    TICKS.mkdir(exist_ok=True)
    now = dt.datetime.now().astimezone()
    stamp = now.strftime("%Y%m%d_%H%M%S")

    entries = parse_bib(BIB)
    by_flag: dict[str, list[str]] = {}
    for e in entries:
        for f in e["flags"]:
            by_flag.setdefault(f, []).append(e["key"])

    en_cites = cites_in(EN)
    cn_cites = cites_in(CN)
    all_cites = en_cites | cn_cites

    risky_flags = {"under-review", "preprint", "unverified", "ahead-of-print"}
    cited_risky = []
    for e in entries:
        if e["key"] in all_cites and risky_flags.intersection(e["flags"]):
            cited_risky.append(e)

    en_text = EN.read_text(encoding="utf-8")
    cn_text = CN.read_text(encoding="utf-8")
    cov_en = keyword_coverage(en_text)
    cov_cn = keyword_coverage(cn_text)

    # Refresh watchlist (bib-driven quarantine list)
    watch_lines = [
        "# Unpublished / non-citable watchlist",
        "",
        "> Auto-refreshed by `scripts/lit_pipeline_tick.py`. **Do not** put these into `references.bib` cites until venue-confirmed.",
        "",
        f"_Last tick: {now.isoformat(timespec='seconds')}_",
        "",
        "| Key | Flags | Title (short) |",
        "|-----|-------|---------------|",
    ]
    for e in entries:
        if set(e["flags"]) - {"published-or-clean", "in-press"}:
            # in-press is borderline; keep listed separately below
            if "published-or-clean" in e["flags"] and len(e["flags"]) == 1:
                continue
            if e["flags"] == ["in-press"]:
                continue
            watch_lines.append(f"| `{e['key']}` | {', '.join(e['flags'])} | {e['title']} |")
    watch_lines += [
        "",
        "## In-press (use with caution; prefer final pagination when available)",
        "",
        "| Key | Title |",
        "|-----|-------|",
    ]
    for e in entries:
        if e["flags"] == ["in-press"]:
            watch_lines.append(f"| `{e['key']}` | {e['title']} |")
    WATCH.write_text("\n".join(watch_lines) + "\n", encoding="utf-8")

    # Coverage audit
    audit = [
        "# Professional-reader coverage audit (Ch.8)",
        "",
        f"_Last tick: {now.isoformat(timespec='seconds')}_",
        "",
        "## Layer checklist",
        "",
        "| Layer | EN keyword hit | CN keyword hit | Notes |",
        "|-------|----------------|----------------|-------|",
    ]
    notes = {
        "twin": "Need clear DT→language interface",
        "llm": "Foundations before applications",
        "vlm": "Must stay in-scope with LLM",
        "rag": "Classic → topology / graph ladder",
        "agent": "Tools + approval gates",
        "memory": "Parametric vs retrieval vs twin long-term store — often under-taught",
        "frontier": "Agentic RAG / cognitive twin / VLM-native outlook",
        "delivery": "Reports + DSS metrics",
    }
    for k in ["twin", "llm", "vlm", "rag", "agent", "memory", "frontier", "delivery"]:
        audit.append(
            f"| L-{k} | {'YES' if cov_en[k] else 'NO'} | {'YES' if cov_cn[k] else 'NO'} | {notes[k]} |"
        )
    audit += [
        "",
        "## Cited-but-risky (must clear or move to prose-without-cite)",
        "",
    ]
    if cited_risky:
        for e in cited_risky:
            audit.append(f"- `{e['key']}` — {', '.join(e['flags'])} — {e['title']}")
    else:
        audit.append("- none")
    audit += [
        "",
        "## Counts",
        "",
        f"- Bib entries: **{len(entries)}**",
        f"- EN unique cites: **{len(en_cites)}**",
        f"- CN unique cites: **{len(cn_cites)}**",
        f"- Cited risky: **{len(cited_risky)}**",
        f"- Flagged preprint/under-review/unverified/ahead: **{sum(1 for e in entries if risky_flags.intersection(e['flags']))}**",
        "",
        "## Next edit priorities (from gaps)",
        "",
    ]
    if not cov_en["memory"] or not cov_cn["memory"]:
        audit.append("1. Add a **Memory** subsection (parametric / context / RAG-as-memory / twin as long-term store). Cite only published works.")
    if cited_risky:
        audit.append("2. Remove or replace cited-risky keys; keep unpublished ideas in UNPUBLISHED_WATCHLIST only.")
    if not cov_en["frontier"]:
        audit.append("3. Strengthen frontier ladder wording (agentic RAG, cognitive twins) with published surveys.")
    AUDIT.write_text("\n".join(audit) + "\n", encoding="utf-8")

    if not CAND.exists():
        CAND.write_text(
            "# Published candidates to consider for Ch.8\n\n"
            "> Only peer-published (or firmly in-press with DOI) items belong here.\n\n"
            "| Rank | Venue hint | Topic layer | Title / DOI | Action |\n"
            "|------|------------|-------------|-------------|--------|\n",
            encoding="utf-8",
        )

    state = {
        "last_tick": now.isoformat(timespec="seconds"),
        "bib_entries": len(entries),
        "en_cites": len(en_cites),
        "cn_cites": len(cn_cites),
        "cited_risky": len(cited_risky),
        "coverage_en": cov_en,
        "coverage_cn": cov_cn,
        "flag_counts": {k: len(v) for k, v in sorted(by_flag.items())},
    }
    if yaml:
        STATE.write_text(yaml.safe_dump(state, sort_keys=False, allow_unicode=True), encoding="utf-8")
    else:
        STATE.write_text(str(state) + "\n", encoding="utf-8")

    report = [
        f"# Tick {stamp}",
        "",
        f"- time: {now.isoformat(timespec='seconds')}",
        f"- bib_entries: {len(entries)}",
        f"- en_cites: {len(en_cites)}",
        f"- cn_cites: {len(cn_cites)}",
        f"- cited_risky: {len(cited_risky)}",
        f"- coverage_en: {cov_en}",
        f"- coverage_cn: {cov_cn}",
        "",
        "See also: UNPUBLISHED_WATCHLIST.md, PUBLISHED_CANDIDATES.md, COVERAGE_AUDIT.md",
        "",
    ]
    (TICKS / f"tick_{stamp}.md").write_text("\n".join(report), encoding="utf-8")

    print(f"TICK {stamp}")
    print(f"bib={len(entries)} en_cites={len(en_cites)} cn_cites={len(cn_cites)} cited_risky={len(cited_risky)}")
    print("coverage_en", cov_en)
    print("coverage_cn", cov_cn)
    if cited_risky:
        print("RISKY_CITED:", ", ".join(e["key"] for e in cited_risky))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
