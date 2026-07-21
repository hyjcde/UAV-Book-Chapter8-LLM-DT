# Chapter 8 — Digital Twin with LLMs in Inspection Analysis

Springer monograph chapter (Lead: **Yijun Huang**) for  
*AI-Driven UAV Building Inspection*.

**Target length:** ~50 pages · **Bilingual:** EN + CN synced

## Writing policy

See [`WRITING_POLICY.md`](WRITING_POLICY.md): this chapter is a **book synthesis**, not a reprint of the IAP-RAG manuscript. Cite group/community work first; treat `huang2026iaprag` as one case study.

## Quick start

```bash
# check EN/CN section labels
python3 scripts/sync_check.py

# compile BOTH languages (parallel)
./scripts/build.sh
```

Outputs:
- `latex/en/book_ch08.pdf`
- `latex/cn/book_ch08.pdf`

## Layout

| Path | Role |
|------|------|
| `OUTLINE.md` | Living writing outline (~50 pp) |
| `literature/AGENT_LIT_NOTES.md` | Agent / DT+LLM literature beyond RAG |
| `latex/SECTION_MAP.yaml` | EN↔CN section contract |
| `latex/en/book_ch08.tex` | EN root: SNmono shell (mirrors Overleaf `book.tex`) |
| `latex/shared/springer_local_trim.tex` | Shared 160×241 mm trim + 117×191 mm body (real-book margins) |
| `latex/en/ch08.tex` | English Chapter 8 body (expanded) |
| `latex/en/{dedication,preface,acknow,acronym,glossary}.tex` | Front/back matter from SNmono / Overleaf |
| `latex/en/ch0{1-7,9}_*.tex` + `part0*.tex` | Title stubs for numbering/TOC only |
| `latex/cn/ch08_cn.tex` | Chinese chapter body |
| `latex/shared/references.bib` | Shared bibliography |
| `latex/shared/figures/ch08/` | Figures from DefectGPT |

## Sync rule

1. Edit structure in **both** `ch08.tex` and `ch08_cn.tex` (same `\label{sec:...}`).
2. Run `python3 scripts/sync_check.py` before commit.
3. Run `./scripts/build.sh` so EN and CN both compile.

English is the Springer submission language; Chinese is the parallel working draft.

## Overleaf (full book)

Project: https://www.overleaf.com/project/6a5c99bcb69823c5f4cd30ee  
Chapter file mirrored at:  
`AI-Driven-UAV-Building-Inspection/manuscript_official/book/ch08_llm_digital_twin.tex`

```bash
cd ../AI-Driven-UAV-Building-Inspection/manuscript_official
olcli push --project 6a5c99bcb69823c5f4cd30ee .
```

## Source material

- DefectGPT / IAP-RAG paper (`../DefectGPT/paper/AIC-Rebuttal/`)
- Agent additions: Luo2025 robot+DT, Gao2026 IFC-Agent, BIM2RDT, Zhang2025 agent schema, …
