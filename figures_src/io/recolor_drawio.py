#!/usr/bin/env python3
"""Remap paper Nature blues → BookSlate palette inside .drawio / .svg XML."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
DRAWIO = HERE / "drawio"
SVG = HERE / "svg"
OUT = HERE / "out"
BACKUP = HERE / "drawio_original_backup"

# Case-insensitive hex remaps (paper → book)
REMAP = {
    "#3C5488": "#0F4C5C",
    "#4DBBD5": "#E36414",
    "#00A087": "#5C8001",
    "#849184": "#6B7280",
    "#8491B4": "#3D6B7C",
    "#91D1C2": "#F0A06A",
    "#2c3e50": "#1A2332",
    "#2C3E50": "#1A2332",
    "#376A9E": "#0F4C5C",
    "#1f77b4": "#0F4C5C",
    "#1F77B4": "#0F4C5C",
    "#dae8fc": "#D6E5E8",  # light blue fills
    "#DAE8FC": "#D6E5E8",
    "#fff2cc": "#FDE8D4",  # light yellow → light copper
    "#FFF2CC": "#FDE8D4",
    "#d5e8d4": "#E4EFD0",  # light green
    "#D5E8D4": "#E4EFD0",
    "#f8cecc": "#FAD7C2",
    "#F8CECC": "#FAD7C2",
    "#e1d5e7": "#D9E4E7",
    "#E1D5E7": "#D9E4E7",
}


def recolor_text(text: str) -> str:
    out = text
    for old, new in REMAP.items():
        out = re.sub(re.escape(old), new, out, flags=re.IGNORECASE)
    return out


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    BACKUP.mkdir(parents=True, exist_ok=True)

    targets = list(DRAWIO.glob("*.drawio")) + list(SVG.glob("*.svg"))
    for path in targets:
        raw = path.read_text(encoding="utf-8", errors="replace")
        # backup once
        bak = BACKUP / path.name
        if not bak.exists():
            shutil.copy2(path, bak)
        new = recolor_text(raw)
        path.write_text(new, encoding="utf-8")
        print(f"recolored {path.relative_to(HERE)} ({len(raw)} -> chars)")


if __name__ == "__main__":
    main()
