# Chapter 8 citation audit (2026-07-21)

Scope: all `\cite{...}` keys in `latex/en/ch08.tex` (68 unique; CN mirrored for the same fixes).

## Metadata (Crossref)

| Result | Count | Notes |
|--------|------:|-------|
| Title/DOI match OK | 51+ | After `zhao2025icra` DOI fix |
| No DOI in bib (NeurIPS/ICLR/TMLR) | 11 | Acceptable for those venues; keys still correct |
| Year soft-mismatch fixed | 3 | `li2025b`/`li2025c` → print year 2026; `peng2024` → TOIS 2026 |
| **Critical DOI error fixed** | 1 | `zhao2025icra` pointed to Open3DTrack (`…11128112`); corrected to CUPID paper (`…11127758`) + author names |

`huang2026iaprag` remains in bib as under-review and is **not** cited in the chapter.

## Claim → cite fitness (fixes applied)

| Issue | Fix |
|-------|-----|
| `wu2022` (NLP survey) used for Asset-ID / cite-or-abstain / twin interfaces | Split: checklist/provenance → `zhang2022`+`chen2023facility`; cite-or-abstain → `lewis2020`+`shuster2021`+`ji2023`; document-store NLP → `wu2022` only where claim is about unstructured texts |
| `park2023generativeagents` used for O&M write gates / CMMS tickets | Kept for memory-stream analogy; write gates → `luo2025llmdtrobot`+`gao2026ifcagent`+`rawat2025llmmas`; ticket procedures → `luo2025llmdtrobot` |
| Heritage “geometry without provenance ornamental” overstated vs Bruno/Tsilimantou | Softened to diagnosis-linked semantics + monitoring provenance |
| Strong empirical claims (`lu2026highwaymas` cognitive load; `pan2026graphdtgpt` answer correctness) | Spot-checked against abstracts: **supported** |

## Still intentional (not bugs)

- Cluster cites that bundle a contrast (e.g. document RAG vs graph RAG) may list both sides.
- `ji2023` near Asset-ID/abstention wording supports **hallucination risk**, not the Asset-ID concept itself.
- `peng2024` supports graph-vs-embedding retrieval structure, not façade moisture physics.

## Watchlist (do not cite until published)

See `literature/UNPUBLISHED_WATCHLIST.md` (`huang2026iaprag`, harness arXivs, GraphRAG preprints, etc.).
