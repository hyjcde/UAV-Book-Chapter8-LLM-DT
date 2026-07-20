# Chapter 8 literature & coverage pipeline

## Goal

Every tick (default **10 minutes** in the agent session loop):

1. **Search** more LLM / VLM / RAG / Agent / Memory / Digital-Twin papers for building inspection.
2. **Classify** each hit: `published` | `ahead-of-print` | `preprint` | `under-review` | `unverified`.
3. **Quarantine**: anything not peer-published goes to `UNPUBLISHED_WATCHLIST.md` — **never** add to `references.bib` / `\cite{}`.
4. **Count** and write a tick report under `ticks/`.
5. **Coverage audit** (professional reader): does Ch.8 truly teach DT→LLM→RAG→Agent→Memory→frontier, layer by layer?
6. **Propose** chapter edits only from `PUBLISHED_CANDIDATES.md`.

## Hard rules

- Unpublished / under-review / placeholder metadata → watchlist only.
- Preprints may be *read* for ideas; they are **not** bibliography entries until venue-confirmed.
- Do not invent DOIs or page numbers.
- Only edit `latex/en/ch08.tex` + `latex/cn/ch08_cn.tex` (+ shared bib) for Chapter 8.

## Layer checklist (professional reader)

| Layer | Must cover | Status file field |
|-------|------------|-------------------|
| L0 Twin interface | DT/BIM/GIS products from Ch.4–7 | `coverage.twin` |
| L1 LLM foundations | Transformer, instruct, CoT, hallucination | `coverage.llm` |
| L2 VLM | CLIP-class / multimodal instruction | `coverage.vlm` |
| L3 RAG | classic → adaptive → graph / topology | `coverage.rag` |
| L4 Agents | ReAct/tools, multi-agent, approval gates | `coverage.agent` |
| L5 Memory | parametric vs non-parametric; short/long; twin as memory | `coverage.memory` |
| L6 Frontier | agentic RAG, cognitive twins, VLM-native twins | `coverage.frontier` |
| L7 Delivery | reports, Asset-ID hygiene, DSS metrics | `coverage.delivery` |

## Commands

```bash
# One tick (also used by the 10-minute loop)
python3 scripts/lit_pipeline_tick.py

# Full rebuild after accepted prose edits
bash scripts/build.sh
```

## Session loop

Agent arms: `sleep 600` + sentinel `AGENT_LOOP_TICK_ch08_lit` every 10 minutes until stopped.
