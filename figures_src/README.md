# Chapter 8 figure sources (book-local)

## Policy (2026-07-21)

| Asset class | Policy |
|-------------|--------|
| **Transfer / generalizability** (`framework_generalizability_concept`, `platform_transferability_implementation`) | Use **paper originals** only (PNG/PDF). Do **not** recolor or re-export from drawio. |
| **Architecture drawio** (`framework_overview_overall`, `rag_workflow_topology`, `idp_construction_pipeline`) | Restore from `drawio_original_backup`, then apply **AcademicSlate** hex remap in XML (cool blue/grey/cream). No copper overlay. |
| **Raster screenshots** (`dt_modeling_pipeline`, `platform_architecture`, `multi_platform_*`, `analysis_interface_nlq`) | Copy paper rasters **as-is**. Never apply RGB tint casts. |
| **Statistical panels** | Matplotlib with `CH8_FIGURE_THEME=Nature` (default). |

## Palette (AcademicSlate)

Architecture remaps stay in the same hue family as the paper Nature blues:

| Role | Hex |
|------|-----|
| Primary / navy | `#2F4A6A` (from `#3C5488`) |
| Secondary / steel | `#5B8FA8` (from `#4DBBD5`) |
| Accent green | `#3D7A5A` (from `#00A087`) |
| Light fill | `#E8EEF4` |
| Cream panel | `#F7F2E8` (not copper) |
| Ink | `#1A2332` |

`BookSlate` teal+copper is optional only via `CH8_FIGURE_THEME=BookSlate` for statistical A/B — **not** used on architecture diagrams.

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
