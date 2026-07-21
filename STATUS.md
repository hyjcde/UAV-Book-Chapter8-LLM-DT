# Writing status — Chapter 8

**TOC spine:** 8.1–8.6 (reader-facing).  
**EN shell:** Overleaf / `manuscript_official` **SNmono** + local trim `latex/shared/springer_local_trim.tex`  
  (paper **160×241 mm**, body **117×191 mm**, matching published Springer OA monographs).  
**CN shell:** same trim/body via shared file; 10pt + slightly tighter `\linespread`; mirrored frontmatter stubs.  
**Author:** left empty for now.  
**Stance:** ready-to-use LLM + harness; no site training agenda. Prefer 2024–2026 published cites.  
**Build:** `bash scripts/build.sh` → EN ≈70 pp, CN ≈61 pp (synced shells; Ch.8 expanded).  
**Layout notes:**  
- Use `\begin{dedication}...\end{dedication}` (not `\dedication{...}`).  
- Letter/A4 canvas without trim correction causes fake huge side margins.

| Section | Status | Notes |
|---------|--------|-------|
| 8.1–8.6 | draft+ | body in `latex/en/ch08.tex` + `latex/cn/ch08_cn.tex` |

**Style notes:** `literature/springer_style_refs/MONOGRAPH_CHAPTER_STYLE.md`  
**Lit rule:** `cited_risky=0`.  
**Citation audit:** `literature/CITATION_AUDIT_2026-07-21.md` (Crossref + claim–cite fitness; `zhao2025icra` DOI fixed).
