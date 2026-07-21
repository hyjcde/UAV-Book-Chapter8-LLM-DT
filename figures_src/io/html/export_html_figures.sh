#!/usr/bin/env bash
# Render AcademicSlate HTML UI figures → PNG/PDF for the chapter.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
IO="$(cd "$HERE/.." && pwd)"
OUT="$IO/out"
BOOK="$(cd "$IO/../.." && pwd)"
SHARED="$BOOK/latex/shared/figures/ch08"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
mkdir -p "$OUT" "$SHARED"

export_one() {
  local stem="$1" w="$2" h="$3"
  local html="file://${HERE}/${stem}.html"
  local png="$OUT/${stem}.png"
  echo "  render $stem (${w}x${h})"
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars \
    --window-size="${w},${h}" \
    --screenshot="$png" \
    "$html" >/tmp/ch8_html_${stem}.log 2>&1 || true
  python3 - <<PY
from pathlib import Path
from PIL import Image
stem = "$stem"
png = Path("$png")
out = Path("$OUT")
shared = Path("$SHARED")
if not png.exists() or png.stat().st_size < 1000:
    raise SystemExit(f"screenshot failed: {png}")
im = Image.open(png).convert("RGBA")
bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
rgb = Image.alpha_composite(bg, im).convert("RGB")
# trim accidental browser chrome if any (keep full canvas)
rgb.save(out / f"{stem}.png")
rgb.save(out / f"{stem}.pdf", "PDF", resolution=200.0)
book = Path("$BOOK")
for dest in (
    shared,
    book / "latex" / "en" / "figures" / "ch08",
    book / "latex" / "cn" / "figures" / "ch08",
):
    dest.mkdir(parents=True, exist_ok=True)
    (dest / f"{stem}.png").write_bytes((out / f"{stem}.png").read_bytes())
    (dest / f"{stem}.pdf").write_bytes((out / f"{stem}.pdf").read_bytes())
print("  ok", stem, rgb.size)
PY
}


echo "== HTML UI figures (AcademicSlate) =="
export_one analysis_interface_nlq 1320 820
export_one multi_platform_field_interfaces 1320 760
export_one platform_demo 1320 800
echo "== done =="
