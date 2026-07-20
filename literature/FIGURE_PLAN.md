# Chapter 8 figure plan (textbook-first, not paper-first)

## Principle

This chapter teaches a **decision layer** for UAV digital twins + LLM/VLM/RAG/Agent/Memory.  
Figures must explain **concepts and workflows for professional readers**, not defend one experiment or reprint one paper’s result plots.

| Allowed | Not the goal |
|---------|----------------|
| Original teaching schematics (TikZ / redraw) | Reusing a paper’s ablation/SOTA bar chart as “the” evidence |
| Book-pipeline diagrams linking Ch.4–7 → Ch.8 | Product UI screenshots as scientific claims |
| Generic ladders (memory / grounding / agent roles) | DefectGPT / IAP-RAG architecture dumps as chapter spine |

Paper-derived plots may appear later only as **optional appendix illustrations**, clearly labeled, and never as the only proof.

---

## Must-have teaching figures (draw these)

| ID | Working title | Layer | Pedagogical job | Status |
|----|---------------|-------|-----------------|--------|
| F1 | Book pipeline → decision layer | L0 | Where Ch.8 sits after planning/recon/detect/GIS | **Reuse ok** if redrawn as book schematic (`framework_overview_overall`) — caption must stay book-level |
| F2 | Twin inputs for language | L0 | Asset-ID + provenance + topology as interfaces | Need clean schematic (current `dt_modeling_pipeline` is OK if caption stays “input interface”) |
| F3 | LLM capability & failure ladder | L1 | Pretrain → instruct → CoT → hallucination/ID errors | **MISSING** — draw new |
| F4 | VLM vs detector vs LLM roles | L2 | Who writes observations / who retrieves / who narrates | **MISSING** — draw new |
| F5 | Memory ladder (4 boxes) | L5 | Parametric / context / RAG index / twin store | **MISSING** — draw new (highest priority) |
| F6 | Grounding stack | L3–L4 | Prompt/schema → RAG → tools/agents → structured IDs | **MISSING** — draw new |
| F7 | Query assembly (topology RAG) | L3 | Intent → passport → neighbours → cite-or-abstain | Partial: `rag_workflow_topology` — **redraw** to remove paper-specific module names |
| F8 | Observation → asset passport | L0/L3 | Generic records, not IDP acronym dump | Partial: `idp_construction_pipeline` — **replace** with textbook naming |
| F9 | Agent role stack + approval gate | L4 | Retriever / topology / report / action + human gate | **MISSING** — draw new |
| F10 | Report schema → FM artefact | L7 | Constrained fields + evidence links | Table exists; optional one schematic |
| F11 | Evaluation criteria (not bake-off) | L7 | Grounding / topology / corpus / safety checklist | **MISSING** — replace ablation bars |
| F12 | Frontier outlook | L6 | Agentic RAG / cognitive twin / VLM-native (dashed) | Partial: `framework_generalizability_concept` — keep only if generic |

---

## Demote / do not lead with (paper residue)

These files look like **single-study result panels**. Do not use them as the chapter’s main story figures:

- `deterministic_ablation_exact_hit.pdf`
- `deterministic_external_exact_hit.pdf`
- `deterministic_ksweep_coverage.pdf`
- `hallucination_rate.pdf`
- `score_by_type.pdf`
- `DefectGPT_V6_Architecture.svg` / `DefectGPT_V6_Research_Architecture.svg`
- Heavy product shots: `platform_demo.pdf`, `analysis_interface_nlq.png` (optional “interface pattern” only)

**Action (done in 2026-07-20 prose rewrite):** main EN/CN chapter text no longer includes ablation/SOTA/hallucination bar charts; DSS emphasises evaluation criteria. Still to draw: F3–F6, F9, F11 as original teaching schematics.

---

## Drawing order (recommended)

1. **F5 Memory ladder** — closes the biggest conceptual gap  
2. **F3 + F6** — foundations + grounding in one visual spine  
3. **F4** — VLM placement  
4. **F9** — agents with approval  
5. **F7 + F8 redraw** — kill paper jargon in filenames/captions  
6. **F11** — stop leading with ablation bars  

Style: Springer mono-friendly, grayscale-safe, English master + Chinese mirror labels later.

---

## Automation note

The 10-minute literature tick should **report figure gaps from this file**, not invent new paper plots.  
Cursor cloud Automations: user-owned; this repo only keeps `FIGURE_PLAN.md` + tick scripts.
