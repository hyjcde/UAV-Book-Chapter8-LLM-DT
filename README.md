# Chapter 8 — Digital Twin with LLMs in Inspection Analysis

Contribution chapter for the Springer Nature monograph  
**AI-Driven UAV Building Inspection** (Unmanned Systems Research Group, CUHK).

This repository tracks **Chapter 8 only** (Lead: Yijun Huang).

## Start here

1. Read the living outline: [`OUTLINE.md`](OUTLINE.md)
2. Draft LaTeX (SNmono book project):  
   `../manuscript_official/book/ch08_llm_digital_twin.tex`
3. Overleaf: https://www.overleaf.com/project/6a5c99bcb69823c5f4cd30ee  
   Main file: `book/book.tex`

## Source material

Primary: DefectGPT / IAP-RAG paper & data under `../DefectGPT` (sibling project), especially:

- `paper/AIC-Rebuttal/manuscript_revised/main.tex`
- `paper/AIC-Rebuttal/figures/`
- `data/Asset_Health_Passport/`

## Sync Overleaf

```bash
cd ../manuscript_official
olcli sync
olcli pdf
```
