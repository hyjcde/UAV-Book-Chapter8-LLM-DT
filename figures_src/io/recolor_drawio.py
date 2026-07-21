#!/usr/bin/env python3
"""Optional academic colour refinement for Chapter 8 .drawio / .svg sources.

Policy (2026-07-21):
  - Transfer figures are NOT recolored; chapter uses paper PNG/PDF originals.
  - Architecture diagrams keep the paper's cool blue/grey hierarchy.
  - Do NOT map blues → copper/orange (that looked like a tint overlay).
  - This script only normalises a few inconsistent hexes toward one print-safe
    AcademicSlate family while preserving role semantics (fill / stroke / accent).

Default: dry-run prints planned remaps. Pass --apply to write files.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRAWIO = HERE / "drawio"
SVG = HERE / "svg"
BACKUP = HERE / "drawio_original_backup"

# Transfer / generalizability diagrams: never touch (paper originals in chapter).
SKIP_STEMS = {
    "framework_generalizability_concept",
    "platform_transferability_implementation",
}

# AcademicSlate: keep cool hierarchy; refine only paper Nature family + draw.io defaults.
# Intentionally no copper (#E36414) remap — architecture stays blue/grey/cream.
REMAP = {
    # Nature paper family → AcademicSlate (same hue family, print-safe)
    "#3C5488": "#2F4A6A",
    "#4DBBD5": "#5B8FA8",
    "#00A087": "#3D7A5A",
    "#849184": "#6B7280",
    "#8491B4": "#6B87A8",
    "#91D1C2": "#A8C9BE",
    "#2c3e50": "#1A2332",
    "#2C3E50": "#1A2332",
    "#376A9E": "#2F4A6A",
    "#1f77b4": "#2F4A6A",
    "#1F77B4": "#2F4A6A",
    # Light fills (draw.io defaults → soft academic)
    "#dae8fc": "#E8EEF4",
    "#DAE8FC": "#E8EEF4",
    "#fff2cc": "#F7F2E8",  # cream, not copper
    "#FFF2CC": "#F7F2E8",
    "#d5e8d4": "#E8F0EA",
    "#D5E8D4": "#E8F0EA",
    "#f8cecc": "#F5E6E4",
    "#F8CECC": "#F5E6E4",
    "#e1d5e7": "#EEE8F2",
    "#E1D5E7": "#EEE8F2",
    "#6c8ebf": "#5B7BA6",
    "#6C8EBF": "#5B7BA6",
    "#003366": "#1E3A5F",
    "#d6b656": "#8B7355",
    "#D6B656": "#8B7355",
}


def recolor_text(text: str) -> str:
    out = text
    for old, new in REMAP.items():
        out = re.sub(re.escape(old), new, out, flags=re.IGNORECASE)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write recolored sources")
    ap.add_argument(
        "--from-backup",
        action="store_true",
        help="Start from drawio_original_backup before remapping",
    )
    args = ap.parse_args()

    BACKUP.mkdir(parents=True, exist_ok=True)
    targets = sorted(DRAWIO.glob("*.drawio")) + sorted(SVG.glob("*.svg"))
    for path in targets:
        if path.stem in SKIP_STEMS:
            print(f"skip transfer {path.name}")
            continue
        bak = BACKUP / path.name
        if args.from_backup and bak.exists():
            raw = bak.read_text(encoding="utf-8", errors="replace")
        else:
            raw = path.read_text(encoding="utf-8", errors="replace")
            if not bak.exists():
                shutil.copy2(path, bak)
        new = recolor_text(raw)
        n_changed = sum(1 for a, b in zip(raw, new) if a != b) if len(raw) == len(new) else abs(len(new) - len(raw))
        if args.apply:
            path.write_text(new, encoding="utf-8")
            print(f"applied {path.relative_to(HERE)} (delta≈{n_changed})")
        else:
            print(f"dry-run {path.relative_to(HERE)} would_change={new != raw}")


if __name__ == "__main__":
    main()
