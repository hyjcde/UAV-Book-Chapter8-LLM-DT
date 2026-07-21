#!/usr/bin/env python3
"""Restore paper UI screenshots with only a light accent polish.

- Keep original layout / content (no HTML redesign).
- Composite transparent corners onto white (avoid black matte).
- Optionally nudge purple/magenta UI accents toward navy/steel.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
IO = HERE.parent
RAS = IO / "raster_originals"
OUT = IO / "out"
BOOK = IO.parent.parent
SHARED = BOOK / "latex" / "shared" / "figures" / "ch08"

STEMS = (
    "analysis_interface_nlq",
    "multi_platform_field_interfaces",
    "platform_demo",
)


def composite_white(im: Image.Image) -> Image.Image:
    rgba = im.convert("RGBA")
    bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    return Image.alpha_composite(bg, rgba).convert("RGB")


def nudge_purple_to_navy(rgb: np.ndarray) -> np.ndarray:
    """Vectorized, subtle: purple/magenta chromas → steel navy family."""
    x = rgb.astype(np.float32)
    r, g, b = x[:, :, 0], x[:, :, 1], x[:, :, 2]
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    chroma = mx - mn
    # purple-ish chat accents (R≈B > G), skip near-gray
    mask = (chroma > 35) & (g + 18 < r) & (g + 18 < b) & (np.abs(r - b) < 55)
    if not mask.any():
        return rgb
    # blend toward AcademicSlate steel (#5B7BA6) while keeping brightness
    target = np.array([0x5B, 0x7B, 0xA6], dtype=np.float32)
    # strength scales with chroma so soft lavenders move less than vivid purple
    t = np.clip((chroma[mask] - 35) / 120.0, 0.15, 0.55)
    src = x[mask]
    bright = src.mean(axis=1, keepdims=True)
    tgt = target * (bright / max(float(target.mean()), 1.0))
    x[mask] = src * (1.0 - t[:, None]) + tgt * t[:, None]
    return np.clip(x, 0, 255).astype(np.uint8)


def process(stem: str) -> None:
    src = RAS / f"{stem}.png"
    if not src.exists():
        print("missing", src)
        return
    im = composite_white(Image.open(src))
    arr = nudge_purple_to_navy(np.array(im))
    out_im = Image.fromarray(arr, mode="RGB")
    OUT.mkdir(parents=True, exist_ok=True)
    out_im.save(OUT / f"{stem}.png")
    out_im.save(OUT / f"{stem}.pdf", "PDF", resolution=200.0)
    for dest in (
        SHARED,
        BOOK / "latex" / "en" / "figures" / "ch08",
        BOOK / "latex" / "cn" / "figures" / "ch08",
    ):
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f"{stem}.png").write_bytes((OUT / f"{stem}.png").read_bytes())
        (dest / f"{stem}.pdf").write_bytes((OUT / f"{stem}.pdf").read_bytes())
    print("restored+nudge", stem, out_im.size)


def main() -> None:
    for stem in STEMS:
        process(stem)


if __name__ == "__main__":
    main()
