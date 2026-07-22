# Writing status — Chapter 8

**TOC spine:** 8.1–8.6 (reader-facing). Book order per proposal: **5 Dataset → 6 AI → 7 GIS → 8 DT+LLM**.  
**Subtitle:** *An End-to-End Framework from Autonomous Flight to Digital Twins* (proposal).  
**EN shell:** Overleaf / `manuscript_official` **SNmono** + local trim `latex/shared/springer_local_trim.tex`  
  (paper **160×241 mm**, body **117×191 mm**, matching published Springer OA monographs).  
**CN shell:** same trim/body via shared file; 10pt + slightly tighter `\linespread`; mirrored frontmatter stubs.  
**Author:** left empty for now.  
**Stance:** four-phase decision support; ready-to-use LLM + optional VLM crop reader; no site training agenda. Prefer 2024–2026 published cites.  
**Build:** `bash scripts/build.sh`.  
**Layout notes:**  
- Use `\begin{dedication}...\end{dedication}` (not `\dedication{...}`).  
- Letter/A4 canvas without trim correction causes fake huge side margins.

| Section | Status | Notes |
|---------|--------|-------|
| 8.1–8.6 | draft+ | body in `latex/en/ch08.tex` + `latex/en/cn/ch08_cn.tex` |

**Style notes:** `literature/springer_style_refs/MONOGRAPH_CHAPTER_STYLE.md`  
**Lit rule:** `cited_risky=0`.  
**Citation audit:** `literature/CITATION_AUDIT_2026-07-21.md` (Crossref + claim–cite fitness; `zhao2025icra` DOI fixed).  
**Figures:** architecture = AcademicSlate XML; transfer = paper originals; stats = BookInk module hexes + restored in §8.6. See `figures_src/README.md`. Regen: `bash figures_src/regenerate_all.sh`.  
**Caption sync:** EN+CN figure captions + read-figure prose aligned (2026-07-21).  
**DSS rewrite (2026-07-21):** §8.6 continuous spine.  
**Pipeline lit map (2026-07-21):** `tab:ch8-book-pipeline-lit` — book stages × group interfaces × community LLM/agent patterns × Ch.8 specialisation (EN+CN).  
**Memory-survey apply (2026-07-21):** externalised loop eqs + `tab:ch8-mem-app` (operators → already-built artefacts); passport/$k$-hop/cite-or-abstain eqs in §8.3. Unpublished survey stays in `AGENT_LIT_NOTES.md` only.  
**Book shell (2026-07-21):** local EN/CN `book_ch08.tex` drop `\part{}` pages; proposal TOC is chapter-only (8.1–8.6). `part0*.tex` kept unused for a future full-book merge.  
**§8.3/8.5 enrich (2026-07-21):** `tab:ch8-assembly-fail`; report walkthrough + `tab:ch8-report-accept` + lifecycle states/roles + `tab:ch8-cmms-map` + seasonal hygiene (EN+CN).  
**CMMS framing (2026-07-21):** `tab:ch8-cmms-map` demoted to optional export example (one sink among CMMS/BIM tracker/spreadsheet); core = schema draft + openable evidence.  
**Proposal align (2026-07-21):** shell Ch.5–7 order + subtitle; four-phase/USP abstracts; VLM in §8.4; historical-record + predictive framing EN/CN.  
**Front matter (2026-07-21):** title-first page (no author/date); proposal title+subtitle; dedication-style epigraph; preface without place/date signature; continuous §8.5 prose (fewer topic-label openers).  
**Reader-first float cut (2026-07-22):** EN/CN thinned to ~10 figs + ~12 tabs + 1 algorithm; removed paper-audit / lit-map stack; ablation kept as grounding-outcome teaching panel only.  
**Sync polish (2026-07-22):** keywords; shortened §8.2/§8.6 lit dumps; predictive maintenance as triage/conditional/external-prognosis; CN duplicate agent para removed; topic-label openers smoothed.
**Major revision (2026-07-22):** fixed TOC 8.1–8.6; §8.1 DT definition + maturity/`upstream` tables + governance; §8.2 harness I/O six-row table + lit compress; §8.3 Asset/Obs/Defect/Passport + typed graph + V1–V4 + ID map; §8.4 fusion scope/levels + VLM rules + JSON API + security; §8.5 claim-level schema + state machine + TRACE versions; **Fig 8.8 Scheme A** — keep `deterministic_ablation_exact_hit.pdf` + $N=200$, methods paragraph → `figures_src/statistical/data/`; §8.6 triage/conditional/predictive split + symbolic `eq:ch8-score` + `tab:ch8-cap-maturity` + `par:ch8-e2e` warehouse walkthrough (EN+CN).
**Fig 8.8 book framing (2026-07-22):** axis labels → packaging policy (Chunk-only / Host cards / Passport ± $k$); caption+prose as portable design lesson (not paper cell codes / not site KPI / not chat-model leaderboard); EN+CN.
**Sid + platform UI (2026-07-22):** §8.5 NLQ + §8.6 everyday prose — working front end named **Sid** (not SID); what it does / from Ch.2–7 twin + harness / how screens support triage DSS; `fig:ch8-platform` + `fig:ch8-ui-screens` + transfer fig (EN+CN).
