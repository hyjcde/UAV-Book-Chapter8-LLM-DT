#!/usr/bin/env python3
"""AcademicSlate colour refinement for Chapter 8 .drawio / .svg sources.

Policy (2026-07-21):
  - Transfer figures are NOT recolored; chapter uses paper PNG/PDF originals.
  - platform_architecture is book-local: never restore from paper backup.
  - Architecture diagrams use one print-safe AcademicSlate family
    (aligned with platform_architecture layers). No copper overlay.

Default: dry-run. Pass --apply to write files.
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

# Transfer / generalizability: never touch (paper originals in chapter).
SKIP_STEMS = {
    "framework_generalizability_concept",
    "platform_transferability_implementation",
}

# Book-local redraw: keep working drawio; do not clobber from backup.
BOOK_LOCAL_STEMS = {
    "platform_architecture",
}

# AcademicSlate — same family as platform_architecture / BookInk ink.
REMAP = {
    # Nature paper family → AcademicSlate
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
    # draw.io defaults → soft academic
    "#dae8fc": "#E8EEF4",
    "#DAE8FC": "#E8EEF4",
    "#fff2cc": "#F7F2E8",
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
    # leftover Material / paper accents → AcademicSlate
    "#e8f5e9": "#E8F0EA",
    "#E8F5E9": "#E8F0EA",
    "#fff3e0": "#F7F2E8",
    "#FFF3E0": "#F7F2E8",
    "#fffbf0": "#F7F2E8",
    "#FFFBF0": "#F7F2E8",
    "#fff8e1": "#F7F2E8",
    "#FFF8E1": "#F7F2E8",
    "#e3f2fd": "#E8EEF4",
    "#E3F2FD": "#E8EEF4",
    "#ede7f6": "#EEE8F2",
    "#EDE7F6": "#EEE8F2",
    "#f0f0f0": "#ECEFF1",
    "#F0F0F0": "#ECEFF1",
    "#f5f5f5": "#ECEFF1",
    "#F5F5F5": "#ECEFF1",
    "#82b366": "#3D7A5A",
    "#82B366": "#3D7A5A",
    "#9673a6": "#6C3483",
    "#9673A6": "#6C3483",
    "#e65100": "#8B7355",
    "#E65100": "#8B7355",
    "#b85450": "#922B21",
    "#B85450": "#922B21",
    "#90a4ae": "#5D6D7E",
    "#90A4AE": "#5D6D7E",
    "#bdbdbd": "#6B7280",
    "#BDBDBD": "#6B7280",
    "#333333": "#2F4A6A",
    "#000000": "#1A2332",
    "#cccccc": "#A8B0B8",
    "#CCCCCC": "#A8B0B8",
    "#e6e6e6": "#A8B0B8",
    "#E6E6E6": "#A8B0B8",
}


def recolor_text(text: str) -> str:
    out = text
    # Longer / more specific hexes first is unnecessary (all fixed length).
    for old, new in REMAP.items():
        out = re.sub(re.escape(old), new, out, flags=re.IGNORECASE)
    return out


def polish_framework_overview(text: str) -> str:
    """Slight role banding: twin = slate, cognitive = cream/lilac, HMI = cream."""
    # Module II outer panel (was grey) → presentation slate
    text = text.replace(
        'value="&lt;b&gt;MODULE II: TWIN CONSTRUCTION&lt;/b&gt;"',
        'value="&lt;b&gt;MODULE II: TWIN CONSTRUCTION&lt;/b&gt;"',
    )
    # Soften harsh pure-black card strokes already remapped to ink;
    # lift twin/cognitive subsystem shells toward role fills when still white+grey.
    # MODULE II container behind title: look for nearby fill on grey panels — handled by REMAP.
    # Cognitive module shell: prefer lilac wash on the Module III outer box.
    text = re.sub(
        r'(value="&lt;b&gt;MODULE III: COGNITIVE REASONING&lt;/b&gt;"[^>]*>.*?'
        r'<mxCell id="D5NGcvgCAcNfVg2UiYoK-256"[^>]*style="[^"]*fillColor=)#ECEFF1',
        r"\1#EEE8F2",
        text,
        count=1,
        flags=re.DOTALL,
    )
    # If the Module III panel is the cell BEFORE the title, remap by id directly.
    text = text.replace(
        'id="D5NGcvgCAcNfVg2UiYoK-256" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#A8B0B8;',
        'id="D5NGcvgCAcNfVg2UiYoK-256" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#EEE8F2;strokeColor=#6C3483;',
    )
    text = text.replace(
        'id="D5NGcvgCAcNfVg2UiYoK-241" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#A8B0B8;',
        'id="D5NGcvgCAcNfVg2UiYoK-241" parent="1" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#E8EEF4;strokeColor=#5B7BA6;',
    )
    # Twin construction cards: steel stroke instead of heavy ink
    for cid in (
        "D5NGcvgCAcNfVg2UiYoK-246",
        "D5NGcvgCAcNfVg2UiYoK-247",
        "D5NGcvgCAcNfVg2UiYoK-250",
        "D5NGcvgCAcNfVg2UiYoK-251",
    ):
        text = re.sub(
            rf'(id="{cid}"[^>]*strokeColor=)#1A2332',
            r"\1#5B7BA6",
            text,
            count=1,
        )
    # Cognitive cards → purple stroke
    for cid in (
        "D5NGcvgCAcNfVg2UiYoK-260",
        "D5NGcvgCAcNfVg2UiYoK-261",
        "D5NGcvgCAcNfVg2UiYoK-264",
        "D5NGcvgCAcNfVg2UiYoK-265",
    ):
        text = re.sub(
            rf'(id="{cid}"[^>]*strokeColor=)#1A2332',
            r"\1#6C3483",
            text,
            count=1,
        )
    # Module band titles: title case, not ALL CAPS (book readability).
    text = text.replace(
        'value="&lt;b&gt;MODULE IV: HUMAN-MACHINE INTERACTION &amp;amp; SERVICE&lt;/b&gt;"',
        'value="&lt;b&gt;Module IV: Human–machine interaction and service&lt;/b&gt;"',
    )
    text = text.replace(
        'value="&lt;b&gt;MODULE II: TWIN CONSTRUCTION&lt;/b&gt;"',
        'value="&lt;b&gt;Module II: Twin construction&lt;/b&gt;"',
    )
    text = text.replace(
        'value="&lt;b&gt;MODULE III: COGNITIVE REASONING&lt;/b&gt;"',
        'value="&lt;b&gt;Module III: Cognitive reasoning&lt;/b&gt;"',
    )
    text = text.replace(
        'value="&lt;b&gt;MODULE I: PHYSICAL ASSET &amp;amp; DATA ACQUISITION&lt;/b&gt;"',
        'value="&lt;b&gt;Module I: Physical asset and data acquisition&lt;/b&gt;"',
    )
    text = text.replace(
        'value="&lt;b&gt;SEMANTIC&lt;br&gt;FUSION&lt;br&gt;ENGINE&lt;/b&gt;"',
        'value="&lt;b&gt;Semantic fusion engine&lt;/b&gt;"',
    )
    # Book figure: drop grey/italic sublines; keep title-only boxes readable.
    text = re.sub(
        r'&lt;br&gt;&lt;span style=&quot;color: rgb\(102, 102, 102\);&quot;&gt;.*?&lt;/span&gt;',
        '',
        text,
        flags=re.DOTALL,
    )
    text = re.sub(r'&lt;br&gt;&lt;i&gt;.*?&lt;/i&gt;', '', text)
    text = text.replace(
        ' value="&lt;span style=&quot;color: rgb(85, 85, 85);&quot;&gt;Mapping 2D Masks&lt;br&gt;to 3D Coordinates&lt;/span&gt;"',
        ' value=""',
    )
    text = text.replace(
        'value="&lt;b&gt;IDP&lt;/b&gt;&lt;br&gt;&lt;span&gt;(Integrated&lt;br&gt;Defect&lt;br&gt;Profile)&lt;/span&gt;"',
        'value="&lt;b&gt;IDP&lt;/b&gt;"',
    )
    module_ids = (
        'D5NGcvgCAcNfVg2UiYoK-237',
        'D5NGcvgCAcNfVg2UiYoK-243',
        'D5NGcvgCAcNfVg2UiYoK-257',
        'D5NGcvgCAcNfVg2UiYoK-267',
    )
    title_ids = (
        'D5NGcvgCAcNfVg2UiYoK-245',
        'D5NGcvgCAcNfVg2UiYoK-249',
        'D5NGcvgCAcNfVg2UiYoK-259',
        'D5NGcvgCAcNfVg2UiYoK-263',
        'D5NGcvgCAcNfVg2UiYoK-253',
        'D5NGcvgCAcNfVg2UiYoK-270',
        'D5NGcvgCAcNfVg2UiYoK-275',
        'D5NGcvgCAcNfVg2UiYoK-280',
        'D5NGcvgCAcNfVg2UiYoK-254',
    )
    for cid in module_ids:
        text = re.sub(rf'(id="{cid}"[^>]*fontSize=)\d+', r'\g<1>19', text, count=1)
    for cid in title_ids:
        text = re.sub(rf'(id="{cid}"[^>]*fontSize=)\d+', r'\g<1>17', text, count=1)
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write recolored sources")
    ap.add_argument(
        "--from-backup",
        action="store_true",
        help="Start from drawio_original_backup before remapping (skipped for book-local)",
    )
    args = ap.parse_args()

    BACKUP.mkdir(parents=True, exist_ok=True)
    targets = sorted(DRAWIO.glob("*.drawio")) + sorted(SVG.glob("*.svg"))
    for path in targets:
        if path.stem in SKIP_STEMS:
            print(f"skip transfer {path.name}")
            continue

        bak = BACKUP / path.name
        if path.stem in BOOK_LOCAL_STEMS:
            raw = path.read_text(encoding="utf-8", errors="replace")
            if not bak.exists():
                shutil.copy2(path, bak)
            print(f"book-local {path.name} (no backup restore)")
        elif args.from_backup and bak.exists():
            raw = bak.read_text(encoding="utf-8", errors="replace")
        else:
            raw = path.read_text(encoding="utf-8", errors="replace")
            if not bak.exists():
                shutil.copy2(path, bak)

        new = recolor_text(raw)
        if path.stem == "framework_overview_overall":
            new = polish_framework_overview(new)

        if args.apply:
            path.write_text(new, encoding="utf-8")
            print(f"applied {path.relative_to(HERE)}")
        else:
            print(f"dry-run {path.relative_to(HERE)} would_change={new != raw}")


if __name__ == "__main__":
    main()
