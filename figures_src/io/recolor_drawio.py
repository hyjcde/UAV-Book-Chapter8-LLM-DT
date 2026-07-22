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
    # Book labels: title case, no Subsystem A/B/C/D; sublines on upper modules only.
    sub = '&lt;br&gt;&lt;span style=&quot;font-size: 14px; color: rgb(90, 90, 90);&quot;&gt;{body}&lt;/span&gt;'
    subw = '&lt;br&gt;&lt;span style=&quot;font-size: 14px; color: rgb(255, 255, 255);&quot;&gt;{body}&lt;/span&gt;'
    rich_values = {
        "D5NGcvgCAcNfVg2UiYoK-238": f"&lt;b&gt;Immersive 3D visualization&lt;/b&gt;{sub.format(body='Web-based rendering engine&lt;br&gt;Real-time interaction')}",
        "D5NGcvgCAcNfVg2UiYoK-239": f"&lt;b&gt;Analytical dashboard&lt;/b&gt;{sub.format(body='Decision support views&lt;br&gt;Statistical charts')}",
        "D5NGcvgCAcNfVg2UiYoK-240": f"&lt;b&gt;Cognitive copilot&lt;/b&gt;{sub.format(body='Natural language interface&lt;br&gt;Grounded Q&amp;amp;A')}",
        "D5NGcvgCAcNfVg2UiYoK-246": f"&lt;b&gt;Photogrammetry pipeline&lt;/b&gt;{sub.format(body='Sparse/dense point clouds&lt;br&gt;Mesh reconstruction')}",
        "D5NGcvgCAcNfVg2UiYoK-247": f"&lt;b&gt;Model alignment&lt;/b&gt;{sub.format(body='Design model parsing&lt;br&gt;Geometric deviation check')}",
        "D5NGcvgCAcNfVg2UiYoK-250": f"&lt;b&gt;Automated defect recognition&lt;/b&gt;{sub.format(body='Deep learning detection&lt;br&gt;Feature extraction')}",
        "D5NGcvgCAcNfVg2UiYoK-251": f"&lt;b&gt;Semantic segmentation&lt;/b&gt;{sub.format(body='Pixel-level masking&lt;br&gt;Material classification')}",
        "D5NGcvgCAcNfVg2UiYoK-254": f"&lt;b&gt;IDP&lt;/b&gt;{subw.format(body='Integrated defect profile')}",
        "D5NGcvgCAcNfVg2UiYoK-260": f"&lt;b&gt;Large language model (LLM)&lt;/b&gt;{sub.format(body='Contextual understanding&lt;br&gt;Logical inference')}",
        "D5NGcvgCAcNfVg2UiYoK-261": f"&lt;b&gt;RAG orchestrator&lt;/b&gt;{sub.format(body='Retrieval augmented generation&lt;br&gt;Prompt engineering')}",
        "D5NGcvgCAcNfVg2UiYoK-264": f"&lt;b&gt;Knowledge graph&lt;/b&gt;{sub.format(body='Topological relationships&lt;br&gt;Domain schema')}",
        "D5NGcvgCAcNfVg2UiYoK-265": f"&lt;b&gt;Vector database&lt;/b&gt;{sub.format(body='High-dim embeddings&lt;br&gt;Similarity search')}",
        # Module I bottom row: title only, no sublines
        "D5NGcvgCAcNfVg2UiYoK-271": "&lt;b&gt;Multi-spectral imagery&lt;/b&gt;",
        "D5NGcvgCAcNfVg2UiYoK-272": "&lt;b&gt;Telemetry&lt;/b&gt;",
        "D5NGcvgCAcNfVg2UiYoK-276": "&lt;b&gt;Design models&lt;/b&gt;",
        "D5NGcvgCAcNfVg2UiYoK-277": "&lt;b&gt;Metadata&lt;/b&gt;",
        "D5NGcvgCAcNfVg2UiYoK-281": "&lt;b&gt;Raw storage&lt;/b&gt;",
        "D5NGcvgCAcNfVg2UiYoK-282": "&lt;b&gt;Edge computing&lt;/b&gt;",
    }
    center_card_ids = set(rich_values)
    for cid, val in rich_values.items():
        text = re.sub(
            rf'(id="{cid}"[^>]*value=")([^"]*)(" vertex="1")',
            rf"\1{val}\3",
            text,
            count=1,
        )
        if cid in center_card_ids:
            text = re.sub(
                rf'(id="{cid}"[^>]*style="[^"]*?)whiteSpace=wrap;',
                r"\1whiteSpace=wrap;align=center;verticalAlign=middle;spacingTop=4;spacingBottom=4;",
                text,
                count=1,
            )
    module_ids = (
        "D5NGcvgCAcNfVg2UiYoK-237",
        "D5NGcvgCAcNfVg2UiYoK-243",
        "D5NGcvgCAcNfVg2UiYoK-257",
        "D5NGcvgCAcNfVg2UiYoK-267",
    )
    section_ids = (
        "D5NGcvgCAcNfVg2UiYoK-245",
        "D5NGcvgCAcNfVg2UiYoK-249",
        "D5NGcvgCAcNfVg2UiYoK-259",
        "D5NGcvgCAcNfVg2UiYoK-263",
        "D5NGcvgCAcNfVg2UiYoK-253",
    )
    group_ids = (
        "D5NGcvgCAcNfVg2UiYoK-270",
        "D5NGcvgCAcNfVg2UiYoK-275",
        "D5NGcvgCAcNfVg2UiYoK-280",
    )
    card_ids = tuple(rich_values.keys())
    for cid in module_ids:
        text = re.sub(rf'(id="{cid}"[^>]*fontSize=)\d+', r"\g<1>22", text, count=1)
    for cid in section_ids:
        text = re.sub(rf'(id="{cid}"[^>]*fontSize=)\d+', r"\g<1>20", text, count=1)
    for cid in group_ids:
        text = re.sub(rf'(id="{cid}"[^>]*fontSize=)\d+', r"\g<1>19", text, count=1)
    for cid in card_ids:
        text = re.sub(rf'(id="{cid}"[^>]*fontSize=)\d+', r"\g<1>18", text, count=1)
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
