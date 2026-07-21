# Writing status — Chapter 8

**TOC spine:** 8.1–8.6 (reader-facing).  
**EN shell:** Overleaf / `manuscript_official` **SNmono** + local trim `latex/shared/springer_local_trim.tex`  
  (paper **160×241 mm**, body **117×191 mm**, matching published Springer OA monographs).  
**CN shell:** same trim/body via shared file; 10pt + slightly tighter `\linespread`; mirrored frontmatter stubs.  
**Author:** left empty for now.  
**Stance:** ready-to-use LLM + harness; no site training agenda. Prefer 2024–2026 published cites.  
**Build:** `bash scripts/build.sh` → EN ≈64 pp, CN ≈57 pp.  
**Layout notes:**  
- Use `\begin{dedication}...\end{dedication}` (not `\dedication{...}`).  
- Letter/A4 canvas without trim correction causes fake huge side margins.

| Section | Status | Notes |
|---------|--------|-------|
| 8.1–8.6 | draft+ | body in `latex/en/ch08.tex` + `latex/cn/ch08_cn.tex` |

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
