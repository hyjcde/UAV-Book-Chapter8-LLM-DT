#!/usr/bin/env bash
# Regenerate Chapter 8 statistical + IO figures with BookSlate palette.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
BOOK="$(cd "$ROOT/.." && pwd)"
STAT="$ROOT/statistical"
IO="$ROOT/io"
DRAWIO_BIN="/Applications/draw.io.app/Contents/MacOS/draw.io"
SHARED="$BOOK/latex/shared/figures/ch08"

echo "== 1. Statistical plots (BookSlate) =="
cd "$STAT/scripts"
python3 plot_deterministic_rule_figures.py --out_dir "$STAT/out"
python3 plot_rebuttal_figures.py --out_dir "$STAT/out"
python3 plot_rebuttal_r4_r5.py --out_dir "$STAT/out"
python3 plot_field_deployment_audit.py \
  --input "$STAT/data/field_deployment_record_audit_frozen.json" \
  --output "$STAT/out/field_deployment_audit"

echo "== 2. Recolor IO drawio/svg =="
python3 "$IO/recolor_drawio.py"

echo "== 3. Export drawio → PDF/PNG =="
mkdir -p "$IO/out"
for f in "$IO/drawio"/*.drawio; do
  base="$(basename "$f" .drawio)"
  echo "  export $base"
  "$DRAWIO_BIN" -x -f pdf -o "$IO/out/${base}.pdf" "$f" --crop
  "$DRAWIO_BIN" -x -f png -o "$IO/out/${base}.png" "$f" --scale 2
done
# SVG copies (already recolored)
cp "$IO/svg/"*.svg "$IO/out/" 2>/dev/null || true

echo "== 4. Raster-only assets → PDF/PNG (do not overwrite drawio exports) =="
# Basenames that already have drawio PDF exports — never overwrite those.
DRAWIO_OWNED="framework_overview_overall rag_workflow_topology framework_generalizability_concept platform_transferability_implementation idp_construction_pipeline DefectGPT_V6_Workflow"
python3 << 'PY'
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "-q"])
    from PIL import Image

ras = Path("/Users/huangyijun/Projects/UAV-Book-Chapter8-LLM-DT/figures_src/io/raster_originals")
out = Path("/Users/huangyijun/Projects/UAV-Book-Chapter8-LLM-DT/figures_src/io/out")
out.mkdir(exist_ok=True)
drawio_owned = {
    "framework_overview_overall",
    "rag_workflow_topology",
    "framework_generalizability_concept",
    "platform_transferability_implementation",
    "idp_construction_pipeline",
    "DefectGPT_V6_Workflow",
}
# Raster-only chapter assets
raster_only = {
    "dt_modeling_pipeline",
    "platform_architecture",
    "multi_platform_field_interfaces",
    "analysis_interface_nlq",
    "platform_demo",
}
for p in sorted(ras.glob("*")):
    if p.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        continue
    if p.stem in drawio_owned:
        # keep JPG/PNG companion for chapter if needed, write under _raster_ suffix for pdf
        im = Image.open(p).convert("RGB")
        r, g, b = im.split()
        r = r.point(lambda x: int(x * 0.96))
        g = g.point(lambda x: int(min(255, x * 1.01)))
        b = b.point(lambda x: int(min(255, x * 1.03)))
        im2 = Image.merge("RGB", (r, g, b))
        if p.suffix.lower() == ".jpg":
            im2.save(out / p.name, quality=92)
            print("raster companion jpg->", p.name)
        continue
    if p.stem not in raster_only and p.stem not in {"framework_overview"}:
        continue
    im = Image.open(p).convert("RGB")
    r, g, b = im.split()
    r = r.point(lambda x: int(x * 0.96))
    g = g.point(lambda x: int(min(255, x * 1.01)))
    b = b.point(lambda x: int(min(255, x * 1.03)))
    im2 = Image.merge("RGB", (r, g, b))
    pdf = out / (p.stem + ".pdf")
    im2.save(pdf, "PDF", resolution=200.0)
    if p.suffix.lower() == ".jpg":
        im2.save(out / p.name, quality=92)
    else:
        im2.save(out / p.name)
    print("raster->", pdf.name)
PY

# Restore drawio PDFs if a prior run overwrote them (re-export quick for owned names)
for name in framework_overview_overall rag_workflow_topology framework_generalizability_concept platform_transferability_implementation idp_construction_pipeline; do
  if [ -f "$IO/drawio/${name}.drawio" ]; then
    "$DRAWIO_BIN" -x -f pdf -o "$IO/out/${name}.pdf" "$IO/drawio/${name}.drawio" --crop
  fi
done

echo "== 5. Sync into latex/shared/figures/ch08 =="
mkdir -p "$SHARED"
# statistical
for name in \
  deterministic_ablation_exact_hit \
  deterministic_external_exact_hit \
  deterministic_ksweep_coverage \
  score_by_type \
  hallucination_rate \
  field_asset_id_stages \
  field_deployment_audit
do
  if [ -f "$STAT/out/${name}.pdf" ]; then
    cp "$STAT/out/${name}.pdf" "$SHARED/"
    echo "  synced stat $name.pdf"
  fi
done
# IO drawio exports (preferred)
for name in \
  framework_overview_overall \
  rag_workflow_topology \
  framework_generalizability_concept \
  platform_transferability_implementation
do
  if [ -f "$IO/out/${name}.pdf" ]; then
    cp "$IO/out/${name}.pdf" "$SHARED/"
    echo "  synced io-drawio $name.pdf"
  fi
done
# idp: chapter uses .jpg; keep both
if [ -f "$IO/out/idp_construction_pipeline.pdf" ]; then
  cp "$IO/out/idp_construction_pipeline.pdf" "$SHARED/"
fi
if [ -f "$IO/out/idp_construction_pipeline.jpg" ]; then
  cp "$IO/out/idp_construction_pipeline.jpg" "$SHARED/"
elif [ -f "$IO/raster_originals/idp_construction_pipeline.jpg" ]; then
  cp "$IO/raster_originals/idp_construction_pipeline.jpg" "$SHARED/"
fi
# raster-only chapter figures
for name in \
  dt_modeling_pipeline \
  platform_architecture \
  multi_platform_field_interfaces \
  analysis_interface_nlq \
  platform_demo
do
  [ -f "$IO/out/${name}.pdf" ] && cp "$IO/out/${name}.pdf" "$SHARED/" && echo "  synced raster $name.pdf"
  [ -f "$IO/out/${name}.png" ] && cp "$IO/out/${name}.png" "$SHARED/"
done
# SVG architecture
cp "$IO/out/"DefectGPT_V6_*.svg "$SHARED/" 2>/dev/null || true

# mirror to en/cn (no --delete: keep any local-only assets)
for lang in en cn; do
  mkdir -p "$BOOK/latex/$lang/figures/ch08"
  rsync -a "$SHARED/" "$BOOK/latex/$lang/figures/ch08/"
done

echo "== done =="
ls -la "$STAT/out"/*.pdf 2>/dev/null | head -20
ls -la "$IO/out"/*.pdf 2>/dev/null | head -20
