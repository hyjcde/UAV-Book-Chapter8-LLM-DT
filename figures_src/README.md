# Chapter 8 figure sources (book-local)

Copied from canonical paper repo **DefectGPT**, then recolored (**BookSlate**) and regenerated here.

## Layout

```
figures_src/
  statistical/
    scripts/     Python plotters (+ figure_style.py BookSlate theme)
    data/        CSV/JSON reproducibility inputs
    out/         regenerated statistical PDFs/PNGs
  io/
    drawio/      editable diagrams.net sources (recolored in place)
    drawio_original_backup/   pre-recolor backups
    svg/         DefectGPT architecture SVGs
    raster_originals/   screenshots / PNG schematics without .py
    out/         exported PDF/PNG after recolor
    recolor_drawio.py
  originals_book_copy/   snapshot of figures before this regen
  regenerate_all.sh
```

## Palette (BookSlate)

| Role | Hex |
|------|-----|
| Ours / primary | `#0F4C5C` |
| Accent | `#E36414` |
| Secondary | `#5C8001` |
| Neutral | `#6B7280` |
| Ink | `#1A2332` |

Paper Nature blues (`#3C5488` / `#4DBBD5` / …) are remapped so book figures are not a silent reprint.

## Regenerate

```bash
bash figures_src/regenerate_all.sh
```

Requires: Python 3 + matplotlib/pandas/numpy/pillow; macOS [draw.io](https://www.drawio.com/) app for IO export.

## Provenance

| Book figure | Generator / source |
|-------------|-------------------|
| `deterministic_*` | `plot_deterministic_rule_figures.py` |
| `score_by_type` | `plot_rebuttal_figures.py` |
| `hallucination_rate`, `field_asset_id_stages` | `plot_rebuttal_r4_r5.py` |
| `field_deployment_audit` | `plot_field_deployment_audit.py` |
| `framework_overview_overall` | `io/drawio/framework_overview_overall.drawio` |
| `rag_workflow_topology` | `io/drawio/rag_workflow_topology.drawio` |
| `framework_generalizability_concept` | `io/drawio/...` |
| `platform_transferability_implementation` | `io/drawio/...` |
| `idp_construction_pipeline` | `io/drawio/...` (+ raster JPG) |
| `dt_modeling_pipeline`, `platform_*`, `analysis_interface_nlq` | raster screenshots (mild cast only) |
