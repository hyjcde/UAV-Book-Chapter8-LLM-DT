# Chapter 8 figure plan (textbook-first, not paper-first)

## Principle

This chapter teaches a **decision layer** for UAV digital twins + LLM/VLM/RAG/Agent/Memory.  
Figures must explain **concepts and workflows for professional readers**, not defend one experiment or reprint one paper’s result plots.

| Allowed | Not the goal |
|---------|----------------|
| Original teaching schematics (TikZ / redraw) | Reusing a paper’s ablation/SOTA bar chart as “the” evidence |
| Book-pipeline diagrams linking Ch.4–7 → Ch.8 | Product UI screenshots as scientific claims |
| Generic ladders (memory / grounding / agent roles) | DefectGPT / IAP-RAG architecture dumps as chapter spine |

Paper-derived plots may appear as **rubric evidence** in §8.6 when framed against Table eval criteria, not as a bake-off lead.

---

## Must-have teaching figures (draw these)

| ID | Working title | Layer | Pedagogical job | Status |
|----|---------------|-------|-----------------|--------|
| F1 | Book pipeline → decision layer | L0 | Where Ch.8 sits after planning/recon/detect/GIS | **Reuse ok** (`framework_overview_overall`) |
| F2 | Twin inputs for language | L0 | Asset-ID + provenance + topology as interfaces | OK if caption stays “input interface” |
| F3 | LLM capability & failure ladder | L1 | Pretrain → instruct → CoT → hallucination/ID errors | **MISSING** |
| F4 | VLM vs detector vs LLM roles | L2 | Who writes observations / who retrieves / who narrates | **MISSING** |
| F5 | Memory ladder (4 boxes) | L5 | Parametric / context / RAG index / twin store | **Done** TikZ |
| F6 | Grounding stack / harness | L3–L4 | Intake → evidence → tools → validators → TRACE | **Done** TikZ |
| F7 | Query assembly (topology RAG) | L3 | Intent → passport → neighbours → cite-or-abstain | Partial: `rag_workflow_topology` |
| F8 | Observation → asset passport | L0/L3 | Generic records | Partial: `idp_construction_pipeline` |
| F9 | Agent role stack + approval gate | L4 | Retriever / topology / report / action + human gate | **Done** TikZ |
| F10 | Report schema → FM artefact | L7 | Constrained fields + evidence links | Table exists |
| F11 | Evaluation criteria | L7 | Grounding / topology / corpus / safety | Table + restored stats panels |
| F12 | Frontier outlook | L6 | Transfer / generalizability | Paper originals (PNG/PDF) |

---

## Statistical panels (restored in §8.6)

- `deterministic_ksweep_coverage`, `deterministic_ablation_exact_hit`, `deterministic_external_exact_hit`
- `score_by_type`, `hallucination_rate`
- `field_asset_id_stages`, `field_deployment_audit`

Colours: **BookInk** module hexes in `figures_src/statistical/scripts/figure_style.py` (`MODULES_BOOKINK`). Change series colours there; do not RGB-cast PDFs.

Still demoted as spine: `DefectGPT_V6_*.svg`, heavy `platform_demo.pdf`.

---

## Drawing order (recommended)

1. **F5 Memory ladder**  
2. **F3 + F6**  
3. **F4** — VLM placement  
4. **F7 + F8 redraw** — kill paper jargon in filenames/captions  

Style: Springer mono-friendly, grayscale-safe, English master + Chinese mirror.

---

## Automation note

The literature tick should **report figure gaps from this file**, not invent new paper plots.
