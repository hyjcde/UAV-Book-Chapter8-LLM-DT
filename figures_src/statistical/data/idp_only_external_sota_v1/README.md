# idp_only_external_sota_v1

Primary fair external peer comparison: peers index **atomic IDP text with host Asset-IDs**
(no IAP aggregation, no VDPP topology hop). Organised IAP-RAG is locked D1.

## Why this corpus (not messy-raw)

Messy-raw is a harsh stress test (peers ≈0 Exact Hit) because most GUID-bearing
evidence lives in a small IFC subset. That result is real but too weak as a peer
table: near-floor scores do not distinguish retrieval designs. IDP-only gives peers
a non-trivial floor while still withholding IAP packaging and VDPP.

## Claim

Peer RAG improvements (RAPTOR, HyDE+Fusion, Corrective-RAG, GraphRAG-NER) on
`idp_only_corpus.jsonl` recover some Asset-IDs but remain well below IAP-RAG on
multi-hop Exact Hit (peers ≤0.088; GraphRAG-NER MH Exact = 0.000 vs IAP-RAG 0.926)
and cited-ID grounding.

## How to reproduce

```bash
# Main fair peers (I/J/K) — solver gemini-3-flash
python3 scripts/eval/run_messy_external_gold200.py \
  --corpus-mode idp --n 200 --skip-judge --tag idp_only_external_sota_v1 \
  --methods I J K

# Fair GraphRAG peer (H_ner) on the same IDP-only corpus
# NER+solver: GPT-4o (gemini-3-flash NER returned empty entities)
python3 scripts/eval/run_messy_external_gold200.py \
  --corpus-mode idp --n 200 --skip-judge --tag idp_only_hners_v1 \
  --methods H_ner \
  --cache-dir logs/scientific_eval/idp_only_hners_cache_v1 \
  --solver-model GPT-4o
```

Stable index caches:

- I/J/K: `logs/scientific_eval/idp_only_index_cache_v1/`
- H_ner: `logs/scientific_eval/idp_only_hners_cache_v1/`
  (578 nodes / 5368 edges / 9 communities; no BIM/IAP)

## Primary numbers (`rule_summary.csv` + H_ner merge)

| Method | Retr Exact | Retr Any | MH Exact | MH Any | Ans-ID Exact | Cited∈Retr |
|--------|------------|----------|----------|--------|--------------|------------|
| RAPTOR | 0.051 | 0.051 | 0.000 | 0.000 | 0.058 | 0.183 |
| HyDE+Fusion | 0.101 | 0.225 | 0.059 | 0.309 | 0.094 | 0.143 |
| Corrective-RAG | 0.130 | 0.167 | 0.088 | 0.162 | 0.087 | 0.193 |
| GraphRAG (H_ner, IDP-only) | **0.478** | **0.609** | **0.000** | 0.265 | 0.478 | 0.312 |
| IAP-RAG (D1 locked) | **0.609** | **0.645** | **0.926** | **1.000** | **0.500** | **0.878** |

Sources:

- I/J/K: `logs/scientific_eval/messy_external_gold200_idp_only_external_sota_v1_20260718_021921`
- H_ner: `logs/scientific_eval/messy_external_gold200_idp_only_hners_v1_20260718_142102`
- Merged: `logs/scientific_eval/idp_only_with_hners_merged_20260718_143130`
- D1: `logs/scientific_eval/external_full_appc_D_trace_20260716_160315.jsonl`

### Readout for the response letter

1. **Manuscript fair main table** still centres on IDP-only RAPTOR / HyDE+Fusion /
   Corrective-RAG vs IAP-RAG (Response §选型理由). GraphRAG remains a §2.3 conceptual
   neighbour unless authors choose to promote H_ner into the printed table.
2. **Fairer GraphRAG check (this pack):** putting Edge-style NER→Louvain on the
   *same* IDP-only corpus (not messy-raw floor) raises Retr Exact to 0.478 — stronger
   than text-centric peers — but **MH Exact stays 0.000** while IAP-RAG reaches 0.926
   ($63/68$). Community GraphRAG does not substitute VDPP topology hops.
3. **Solver note:** I/J/K used `gemini-3-flash`; H_ner used `GPT-4o` because
   gemini-3-flash NER was empty. Retr/MH Exact are retrieval-side metrics.

## Related pack

Harsh messy-raw stress test (near-floor peers, including H_ner = 0.000):
`../messy_external_gold200/` and `../messy_raw_external_sota_v1/`.
