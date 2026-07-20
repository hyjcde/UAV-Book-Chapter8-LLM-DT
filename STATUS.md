# Writing status — Chapter 8

**TOC spine:** 8.1–8.6 (reader-facing).  
**EN shell:** Overleaf / `manuscript_official` **SNmono** book template (`book_ch08.tex`): dedication, preface, acknowledgements, TOC, acronyms, four parts, Ch.1–7/9 stubs, full Ch.8, glossary, bibliography, index.  
**Author:** left empty for now.  
**Stance:** ready-to-use LLM + harness; no site training agenda. Prefer 2024–2026 published cites.  
**Build:** `bash scripts/build.sh` → EN ≈85 pp (SNmono shell + stubs + Ch.8); CN ≈52 pp.  
**Layout fix:** use `\begin{dedication}...\end{dedication}` (not `\dedication{...}`), or italic/`leftskip` leaks into the whole book.

| Section | Status | Notes |
|---------|--------|-------|
| 8.1–8.6 | draft+ | body in `latex/en/ch08.tex` |

**Style notes:** `literature/springer_style_refs/MONOGRAPH_CHAPTER_STYLE.md`  
**Lit rule:** `cited_risky=0`.
