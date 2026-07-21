# IDP-only fair external gold200 — merged rule metrics (incl. GraphRAG H_ner)

- Generated: `2026-07-18T06:31:33.997963+00:00`
- IJK run: `logs/scientific_eval/messy_external_gold200_idp_only_external_sota_v1_20260718_021921`
- H_ner run: `logs/scientific_eval/messy_external_gold200_idp_only_hners_v1_20260718_142102`
- Locked D1: `logs/scientific_eval/external_full_appc_D_trace_20260716_160315.jsonl`

## Claim

On the **same IDP-only corpus** (604 atomic IDPs with host Asset-IDs; no IAP/VDPP),
compare RAPTOR, HyDE+Fusion, Corrective-RAG, and GraphRAG (Edge et al. 2024 style
NER→Louvain→community summaries) against organised IAP-RAG (locked D1).

## Primary metrics (deterministic Asset-ID checks)

| group | label | retr_exact_hit | mh_retr_exact_hit | ans_id_exact | cited_in_retr |
|-------|-------|----------------|-------------------|--------------|---------------|
| D | IAP-RAG (locked D1) | 0.609 | 0.926 | 0.500 | 0.878 |
| I | RAPTOR | 0.051 | 0.000 | 0.058 | 0.183 |
| J | HyDE+Fusion | 0.101 | 0.059 | 0.094 | 0.143 |
| K | Corrective-RAG | 0.130 | 0.088 | 0.087 | 0.193 |
| H_ner | GraphRAG (NER→Louvain) | 0.478 | 0.000 | 0.478 | 0.312 |

## Notes

- `H_ner` builds the entity graph from **IDP-only text** (no passport / BIM topology).
- Graph stats: 578 nodes, 5368 edges, 9 communities over 604 docs.
- Not Microsoft GraphRAG package bit-identical; core Edge et al. pipeline.
- Judge LLM scores skipped (`--skip-judge`); rule metrics are primary.
- Solver: I/J/K = `gemini-3-flash`; H_ner = `GPT-4o` (gemini NER empty).
