#!/usr/bin/env bash
# Regenerate Chapter 8 figures with clear policy:
#   - Transfer / generalizability: paper originals only (no recolor, no drawio overwrite)
#   - Architecture drawio: AcademicSlate remap from backup, then export
#     (platform_architecture: book-local drawio; do not RGB-matte paper PNG)
#   - Raster screenshots: composite RGBA onto white, no RGB tint cast
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
BOOK="$(cd "$ROOT/.." && pwd)"
STAT="$ROOT/statistical"
IO="$ROOT/io"
DRAWIO_BIN="/Applications/draw.io.app/Contents/MacOS/draw.io"
SHARED="$BOOK/latex/shared/figures/ch08"
ORIG="$ROOT/originals_book_copy"
RAS="$IO/raster_originals"

mkdir -p "$SHARED" "$IO/out" "$STAT/out"

echo "== 1. Statistical plots (AcademicSlate = Nature family for print) =="
cd "$STAT/scripts"
# BookInk: per-module hexes in figure_style.py (not RGB casts on finished PDFs)
export CH8_FIGURE_THEME="${CH8_FIGURE_THEME:-BookInk}"
python3 plot_deterministic_rule_figures.py --out_dir "$STAT/out"
python3 plot_rebuttal_figures.py --out_dir "$STAT/out"
python3 plot_rebuttal_r4_r5.py --out_dir "$STAT/out"
python3 plot_field_deployment_audit.py \
  --input "$STAT/data/field_deployment_record_audit_frozen.json" \
  --output "$STAT/out/field_deployment_audit"

echo "== 2. Architecture drawio: restore backup → AcademicSlate remap =="
python3 "$IO/recolor_drawio.py" --from-backup --apply

echo "== 3. Export architecture drawio (non-transfer only) =="
for name in framework_overview_overall rag_workflow_topology idp_construction_pipeline platform_architecture; do
  f="$IO/drawio/${name}.drawio"
  [ -f "$f" ] || continue
  echo "  export $name"
  "$DRAWIO_BIN" -x -f pdf -o "$IO/out/${name}.pdf" "$f" --crop
  "$DRAWIO_BIN" -x -f png -o "$IO/out/${name}.png" "$f" --scale 2
done
cp "$IO/svg/"*.svg "$IO/out/" 2>/dev/null || true

echo "== 4. Transfer figures: paper originals only =="
cp -f "$ORIG/framework_generalizability_concept.pdf" "$SHARED/"
cp -f "$RAS/framework_generalizability_concept.png" "$SHARED/"
cp -f "$ORIG/platform_transferability_implementation.pdf" "$SHARED/"
# keep PNG companion for editors
cp -f "$RAS/platform_transferability_implementation.png" "$IO/out/" 2>/dev/null || true
echo "  synced paper transfer PDFs/PNGs"

echo "== 5. Raster screenshots: originals on white (no tint, no black matte) =="
python3 << PY
from pathlib import Path
from PIL import Image

ras = Path("$RAS")
out = Path("$IO/out")
shared = Path("$SHARED")
out.mkdir(parents=True, exist_ok=True)
for stem in [
    "dt_modeling_pipeline",
    "multi_platform_field_interfaces",
    "analysis_interface_nlq",
]:
    cands = sorted(ras.glob(stem + ".*"))
    cands = [p for p in cands if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
    if not cands:
        print("missing", stem, "in", ras)
        continue
    p = cands[0]
    src = Image.open(p)
    # RGBA paper exports use transparent (0,0,0,0) corners; convert("RGB")
    # mattes them black. Always composite onto white for print PDFs.
    if src.mode in ("RGBA", "LA") or (src.mode == "P" and "transparency" in src.info):
        rgba = src.convert("RGBA")
        bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
        im = Image.alpha_composite(bg, rgba).convert("RGB")
    else:
        im = src.convert("RGB")
    pdf = out / f"{stem}.pdf"
    im.save(pdf, "PDF", resolution=200.0)
    dest_png = out / f"{stem}.png"
    im.save(dest_png)
    shared.joinpath(pdf.name).write_bytes(pdf.read_bytes())
    shared.joinpath(dest_png.name).write_bytes(dest_png.read_bytes())
    print("clean", stem)
idp = ras / "idp_construction_pipeline.jpg"
if idp.exists():
    shared.joinpath(idp.name).write_bytes(idp.read_bytes())
    print("paper idp jpg")
PY

echo "== 6. Sync architecture + stats into latex/shared =="
for name in framework_overview_overall rag_workflow_topology idp_construction_pipeline platform_architecture; do
  [ -f "$IO/out/${name}.pdf" ] && cp -f "$IO/out/${name}.pdf" "$SHARED/" && echo "  arch $name.pdf"
  [ -f "$IO/out/${name}.png" ] && cp -f "$IO/out/${name}.png" "$SHARED/"
done
# Prefer AcademicSlate drawio PDF for IDP; keep paper JPG as archive companion
[ -f "$IO/out/idp_construction_pipeline.pdf" ] && cp -f "$IO/out/idp_construction_pipeline.pdf" "$SHARED/"
[ -f "$RAS/idp_construction_pipeline.jpg" ] && cp -f "$RAS/idp_construction_pipeline.jpg" "$SHARED/"

for name in \
  deterministic_ablation_exact_hit \
  deterministic_external_exact_hit \
  deterministic_ksweep_coverage \
  score_by_type \
  hallucination_rate \
  field_asset_id_stages \
  field_deployment_audit
do
  [ -f "$STAT/out/${name}.pdf" ] && cp -f "$STAT/out/${name}.pdf" "$SHARED/" && echo "  stat $name.pdf"
done

for lang in en cn; do
  mkdir -p "$BOOK/latex/$lang/figures/ch08"
  rsync -a "$SHARED/" "$BOOK/latex/$lang/figures/ch08/"
done

echo "== done =="
ls -la "$SHARED"/*generalizability* "$SHARED"/*transferability* "$SHARED"/framework_overview* "$SHARED"/rag_workflow* 2>/dev/null
