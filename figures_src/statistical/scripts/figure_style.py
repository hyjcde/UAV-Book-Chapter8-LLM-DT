"""Shared style for Chapter 8 statistical figures (book-local copy).

Default: Nature / AcademicSlate family (cool blues) matching architecture diagrams.
BookSlate (teal+copper) kept only for optional A/B via CH8_FIGURE_THEME.
"""

from __future__ import annotations

import colorsys
import os
from typing import Dict

import matplotlib as mpl

INK = "#1A2332"
GRID_ALPHA = 0.35

FILL_ALPHA = 0.58
BAND_ALPHA = 0.15
SCATTER_ALPHA = 0.40
LINE_ALPHA = 0.90
GUIDE_ALPHA = 0.70
LINEWIDTH = 2.5
RADAR_LINEWIDTH = 2.8
GUIDE_LINEWIDTH = 1.2

THEMES: Dict[str, Dict[str, str]] = {
    # Paper / AcademicSlate — default for monograph statistical panels
    "Nature": {
        "Ours": "#3C5488",
        "Atomic": "#4DBBD5",
        "Basic": "#00A087",
        "Raw": "#849184",
    },
    "AcademicSlate": {
        "Ours": "#2F4A6A",
        "Atomic": "#5B8FA8",
        "Basic": "#3D7A5A",
        "Raw": "#6B7280",
    },
    # Optional alternate (not used for architecture diagrams)
    "BookSlate": {
        "Ours": "#0F4C5C",
        "Atomic": "#E36414",
        "Basic": "#5C8001",
        "Raw": "#6B7280",
    },
}

DEFAULT_THEME = os.environ.get("CH8_FIGURE_THEME", "Nature")
if DEFAULT_THEME not in THEMES:
    DEFAULT_THEME = "Nature"

FIGURE_THEMES = {
    "performance_evaluation_stats": DEFAULT_THEME,
    "score_distribution": DEFAULT_THEME,
    "paradigm_spectrum": DEFAULT_THEME,
    "score_by_type": DEFAULT_THEME,
    "forest_score_diff": DEFAULT_THEME,
    "hallucination_rate": DEFAULT_THEME,
    "field_asset_id_stages": DEFAULT_THEME,
}


def _hex_to_rgb(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def _rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    return "#{:02X}{:02X}{:02X}".format(
        *(max(0, min(255, int(round(c * 255)))) for c in rgb)
    )


def _shift(hex_color: str, dh: float = 0.0, ds: float = 0.0, dl: float = 0.0) -> str:
    r, g, b = _hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = (h + dh) % 1.0
    s = max(0.0, min(1.0, s + ds))
    l = max(0.05, min(0.92, l + dl))
    return _rgb_to_hex(colorsys.hls_to_rgb(h, l, s))


def theme_colors(theme: str | None = None) -> Dict[str, str]:
    return dict(THEMES[theme or DEFAULT_THEME])


def external_group_colors(theme: str | None = None) -> Dict[str, str]:
    theme = theme or DEFAULT_THEME
    t = THEMES[theme]
    ours, atomic, basic, raw = t["Ours"], t["Atomic"], t["Basic"], t["Raw"]
    if theme in ("BookSlate", "AcademicSlate"):
        return {
            "D": ours,
            "E": raw,
            "F": atomic,
            "H": basic,
            "I": "#3D6B7C",
            "J": "#F0A06A",
        }
    if theme == "Nature":
        return {
            "D": ours,
            "E": raw,
            "F": atomic,
            "H": basic,
            "I": "#8491B4",
            "J": "#91D1C2",
        }
    return {
        "D": ours,
        "E": raw,
        "F": atomic,
        "H": basic,
        "I": _shift(ours, dh=0.06, dl=0.12, ds=-0.05),
        "J": _shift(atomic, dh=-0.05, dl=0.08, ds=-0.08),
    }


def series_pair(theme: str | None = None) -> tuple[str, str]:
    t = theme_colors(theme)
    return t["Ours"], t["Atomic"]


def apply_rcparams() -> None:
    mpl.rcParams.update(
        {
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "font.size": 14,
            "axes.linewidth": 1.0,
            "axes.edgecolor": INK,
            "axes.labelcolor": INK,
            "axes.titlecolor": INK,
            "xtick.color": INK,
            "ytick.color": INK,
            "xtick.major.size": 4,
            "ytick.major.size": 4,
            "legend.frameon": True,
            "legend.fancybox": False,
            "legend.shadow": False,
            "legend.framealpha": 0.95,
            "legend.edgecolor": "#cccccc",
        }
    )


def setup_academic_ax(ax, title=None, label=None, is_polar=False) -> None:
    if not is_polar:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(linestyle=":", alpha=GRID_ALPHA)
    ax.set_axisbelow(True)
    ax.tick_params(direction="out", length=4, width=1, colors=INK, labelsize=15)
    if title:
        ax.set_title(title, pad=12, fontsize=16, fontweight="bold", color=INK)
    if label:
        ax.text(
            -0.10,
            1.10,
            label,
            transform=ax.transAxes,
            fontsize=22,
            fontweight="bold",
            va="top",
            ha="right",
            color=INK,
        )


def style_bar(ax, x, heights, *, color, width=0.7, yerr=None, label=None, zorder=3):
    return ax.bar(
        x,
        heights,
        width=width,
        color=color,
        alpha=FILL_ALPHA,
        edgecolor=color,
        linewidth=LINEWIDTH * 0.45,
        yerr=yerr,
        capsize=3 if yerr is not None else 0,
        error_kw={"elinewidth": GUIDE_LINEWIDTH, "ecolor": INK, "alpha": GUIDE_ALPHA},
        label=label,
        zorder=zorder,
    )


def style_hbar(ax, y, widths, *, color, height=0.55, xerr=None, label=None, zorder=3):
    return ax.barh(
        y,
        widths,
        height=height,
        color=color,
        alpha=FILL_ALPHA,
        edgecolor=color,
        linewidth=LINEWIDTH * 0.45,
        xerr=xerr,
        capsize=3 if xerr is not None else 0,
        error_kw={"elinewidth": GUIDE_LINEWIDTH, "ecolor": INK, "alpha": GUIDE_ALPHA},
        label=label,
        zorder=zorder,
    )


FIG9 = THEMES[DEFAULT_THEME]
GROUP_COLORS = external_group_colors(DEFAULT_THEME)
OURS = FIG9["Ours"]
SERIES_DARK, SERIES_LIGHT = FIG9["Ours"], FIG9["Atomic"]
NAVY, CYAN, TEAL, SLATE = OURS, FIG9["Atomic"], FIG9["Basic"], "#3D6B7C"
