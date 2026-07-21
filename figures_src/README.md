# Chapter 8 figure sources (book-local)

## Policy (2026-07-21)

| Asset class | Policy |
|-------------|--------|
| **Transfer / generalizability** (`framework_generalizability_concept`, `platform_transferability_implementation`) | Use **paper originals** only (PNG/PDF). Do **not** recolor or re-export from drawio. |
| **Architecture drawio** (`framework_overview_overall`, `rag_workflow_topology`, `idp_construction_pipeline`, `platform_architecture`) | Editable `.drawio` under `io/drawio/`. Non-platform diagrams: restore from `drawio_original_backup`, then **AcademicSlate** hex remap. `platform_architecture` is a book-local layered redraw (paper PNG had no drawio; transparent RGBA must not be RGB-matted to black). No copper overlay. |
| **Raster screenshots** (`dt_modeling_pipeline`, `multi_platform_*`, `analysis_interface_nlq`) | Copy paper rasters **as-is**, composite RGBA onto **white** before PDF. Never apply RGB tint casts. |
| **Statistical panels** | Matplotlib with `CH8_FIGURE_THEME=BookInk` (default). Each series/module has its own hex in `figure_style.MODULES_BOOKINK` — edit those hexes, never tint a finished PDF. Chapter figures: ksweep, ablation, external, score_by_type, hallucination, field_asset_id_stages, field_deployment_audit. |

## Palette (AcademicSlate for architecture)

Architecture remaps stay in the same hue family as the paper Nature blues:

| Role | Hex |
|------|-----|
| Primary / navy | `#2F4A6A` (from `#3C5488`) |
| Secondary / steel | `#5B8FA8` (from `#4DBBD5`) |
| Accent green | `#3D7A5A` (from `#00A087`) |
| Light fill | `#E8EEF4` |
| Cream panel | `#F7F2E8` (not copper) |
| Ink | `#1A2332` |

### BookInk (statistical series — edit these hexes)

| Module | Hex | Role |
|--------|-----|------|
| D / Ours / Spatial / CitedInRet | `#1B4F72` | IAP-RAG primary |
| E / RetrExact | `#5D6D7E` | Chunk / residual |
| F / OK | `#117A65` | Graph-neighbour / complete |
| H | `#6C3483` | GraphRAG |
| I | `#1A5276` | RAPTOR |
| J / Warn / AnsExact | `#B9770E` / `#7D6608` | HyDE / answer-ID metric |
| K / Risk | `#7B241C` / `#922B21` | Corrective / risk |
| MultiHop | `#A04000` | Spatial contrast series |

`BookSlate` teal+copper is optional A/B only (`CH8_FIGURE_THEME=BookSlate`) — not used for chapter stats.

## Regenerate

```bash
bash figures_src/regenerate_all.sh
```

Requires: Python 3 + matplotlib/pandas/numpy/pillow; macOS [draw.io](https://www.drawio.com/) for architecture export.

## Layout

```
figures_src/
  statistical/   scripts + data + out
  io/
    drawio/                 editable sources (AcademicSlate after remap)
    drawio_original_backup/ paper .drawio before remap
    raster_originals/       paper PNG/JPG screenshots
    out/                    exports
    recolor_drawio.py       --from-backup --apply (skips transfer stems)
  originals_book_copy/      frozen paper PDFs for transfer
  regenerate_all.sh
```
