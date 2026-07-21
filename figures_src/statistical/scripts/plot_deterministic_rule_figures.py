#!/usr/bin/env python3
"""Rebuttal statistical figures with one shared Nature/Times style.

No in-figure titles (captions live in LaTeX). MH Exact Hit is omitted from
bar panels/tables. Zero-valued bars are drawn but not annotated.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from figure_style import (
    FILL_ALPHA,
    GUIDE_ALPHA,
    GUIDE_LINEWIDTH,
    INK,
    LINEWIDTH,
    apply_rcparams,
    external_group_colors,
    setup_academic_ax,
    style_bar,
    theme_colors,
)

apply_rcparams()

REPO = Path(__file__).resolve().parents[1]  # figures_src/statistical
REPRO = REPO / "data"
DEFAULT_OUT = REPO / "out"
STATS_CSV = REPO / "data" / "statistical_analysis_final.csv"

KSWEEP_COVERAGE = {0: 0 / 70, 1: 63 / 70, 2: 63 / 70, 3: 63 / 70}

LABEL_FS = 13
TICK_FS = 12
ANNOT_FS = 11
LEGEND_FS = 11

# Tick text is descriptive only (cell codes E/C'/F/D0/D1 stay in the LaTeX caption).
ABLATION_ORDER = [
    ("E chunk", "Chunk", "cell E"),
    ("C' atomic k=0", "Atomic $k=0$", "cell C$'$"),
    ("F atomic k=1", "Atomic $k=1$", "cell F"),
    ("D0 IAP k=0", "IAP $k=0$", r"cell $D_0$"),
    ("D1 IAP k=1", "IAP $k=1$", r"cell $D_1$"),
]

# MH Exact Hit intentionally omitted from figure panels.
ABLATION_METRICS = [
    ("retr_exact", "Retr. Exact Hit"),
    ("ans_exact", "Answer-ID Exact"),
    ("cited_in_ret", r"Cited-ID $\in$ retrieved"),
]

EXTERNAL_ORDER = [
    ("I", "RAPTOR"),
    ("J", "HyDE+Fusion"),
    ("K", "Corrective-RAG"),
    ("H_ner", "GraphRAG"),
    ("D", "IAP-RAG"),
]

EXTERNAL_METRICS = [
    ("retr_exact_hit", "Retr. Exact Hit"),
    ("ans_id_exact", "Answer-ID Exact"),
    ("cited_in_retr", r"Cited-ID $\in$ retrieved"),
]

METRIC_COLORS = ["#6B7280", "#5C8001", "#0F4C5C"]

FOREST_BASELINES = [
    ("E", "Naive Chunk-RAG"),
    ("F", "Graph-Neighbour"),
    ("H", "GraphRAG-style"),
    ("I", "RAPTOR"),
    ("J", "HyDE+Fusion"),
]
FOREST_CATS = [
    ("ALL", "Overall ($n=200$)"),
    ("spatial_awareness", "Spatial awareness ($n=70$)"),
    ("multi_hop_topological", "Multi-hop topological ($n=70$)"),
    ("analytical_aggregation", "Analytical aggregation ($n=60$)"),
]


def _save(fig, out_stem: Path) -> None:
    fig.savefig(out_stem.with_suffix(".pdf"), format="pdf", bbox_inches="tight", pad_inches=0.18)
    fig.savefig(out_stem.with_suffix(".png"), format="png", dpi=220, bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def _annotate_nonzero(ax, bars, heights, color) -> None:
    for rect, h in zip(bars, heights):
        if h <= 1e-12:
            continue
        ax.text(
            rect.get_x() + rect.get_width() / 2, h + 0.02,
            f"{h:.2f}", ha="center", va="bottom",
            fontsize=9, fontweight="bold", color=color,
        )


def _ablation_colors() -> list[str]:
    nat = theme_colors(None)
    eg = external_group_colors(None)
    return [eg["E"], eg["F"], eg["J"], eg["I"], nat["Ours"]]


def plot_ksweep(ksweep_csv: Path, out_stem: Path) -> None:
    ks = pd.read_csv(ksweep_csv).sort_values("k")
    colors = theme_colors(None)
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    x = ks["k"].to_numpy(dtype=int)
    coverage = np.array([KSWEEP_COVERAGE[int(k)] for k in x], dtype=float)

    style_bar(ax, x, coverage, color=colors["Ours"], width=0.55)
    for xi, yi in zip(x, coverage):
        if yi <= 1e-12:
            continue
        num = int(round(yi * 70))
        ax.text(
            xi, yi + 0.04, f"{num}/70",
            ha="center", va="bottom", fontsize=ANNOT_FS + 1,
            fontweight="bold", color=colors["Ours"],
        )

    ax.set_xticks(x)
    ax.set_xticklabels([f"$k={int(k)}$" for k in x], fontsize=TICK_FS)
    ax.set_ylabel(
        "Full culprit-set coverage\n(all 70 multi-hop questions)",
        fontweight="bold", fontsize=LABEL_FS,
    )
    ax.set_ylim(0, 1.18)
    ax.axhline(63 / 70, color=colors["Ours"], ls="--", lw=GUIDE_LINEWIDTH, alpha=GUIDE_ALPHA)
    ax.text(
        3.05, 63 / 70 + 0.03, "plateau = 63/70",
        ha="right", va="bottom", fontsize=10, color=colors["Ours"],
    )
    setup_academic_ax(ax, title=None)
    ax.set_xlabel(
        r"Topology hop depth  ($k_{\mathrm{seed}}=3$; deterministic)",
        fontweight="bold", fontsize=LABEL_FS,
    )
    fig.tight_layout()
    _save(fig, out_stem)
    print(f">>> ksweep -> {out_stem.with_suffix('.pdf')}")


def plot_ablation(csv_path: Path, out_stem: Path) -> None:
    df = pd.read_csv(csv_path).set_index("label")
    tick_colors = _ablation_colors()
    n_groups = len(ABLATION_ORDER)
    n_metrics = len(ABLATION_METRICS)
    x = np.arange(n_groups)
    width = 0.22

    fig, ax = plt.subplots(figsize=(9.6, 4.8))
    for mi, (col, mlab) in enumerate(ABLATION_METRICS):
        heights = [float(df.loc[lab, col]) for lab, _, _ in ABLATION_ORDER]
        offs = x + (mi - (n_metrics - 1) / 2) * width
        bars = ax.bar(
            offs, heights, width=width * 0.92,
            color=METRIC_COLORS[mi], alpha=FILL_ALPHA,
            edgecolor=METRIC_COLORS[mi], linewidth=LINEWIDTH * 0.35,
            label=mlab, zorder=3,
        )
        _annotate_nonzero(ax, bars, heights, METRIC_COLORS[mi])

    ax.axvspan(4 - 0.48, 4 + 0.48, color="#3C5488", alpha=0.07, zorder=0)
    ax.set_xticks(x)
    ax.set_xticklabels(
        [f"{name}\n({code})" for _, name, code in ABLATION_ORDER],
        fontsize=TICK_FS,
    )
    for tick, color in zip(ax.get_xticklabels(), tick_colors):
        tick.set_color(color)
    ax.get_xticklabels()[-1].set_fontweight("bold")

    ax.set_ylabel("Exact Hit / grounding rate", fontweight="bold", fontsize=LABEL_FS)
    ax.set_ylim(0, 1.12)
    ax.legend(loc="upper left", ncol=1, fontsize=LEGEND_FS, frameon=True, edgecolor="#cccccc")
    setup_academic_ax(ax, title=None)
    ax.set_xlabel(
        r"Controlled ablation cells ($N=200$ / cell; no LLM judge)",
        fontweight="bold", fontsize=LABEL_FS,
    )
    fig.tight_layout()
    _save(fig, out_stem)
    print(f">>> ablation -> {out_stem.with_suffix('.pdf')}")


def _load_external_rows(idp_dir: Path) -> list[tuple[str, str, dict]]:
    summary = json.loads((idp_dir / "rule_summary.json").read_text())
    h_ner = {
        "retr_exact_hit": 0.478,
        "ans_id_exact": 0.478,
        "cited_in_retr": 0.312,
    }
    rows = []
    for key, label in EXTERNAL_ORDER:
        if key == "H_ner":
            rows.append((key, label, h_ner))
        else:
            rows.append((key, label, summary[key]))
    return rows


def plot_external(idp_dir: Path, out_stem: Path) -> None:
    rows = _load_external_rows(idp_dir)
    eg = external_group_colors(None)
    color_map = {
        "I": eg["I"], "J": eg["J"], "K": "#7E6148",
        "H_ner": eg["H"], "D": eg["D"],
    }
    n_g, n_m = len(rows), len(EXTERNAL_METRICS)
    x = np.arange(n_g)
    width = 0.22

    fig, ax = plt.subplots(figsize=(9.8, 4.8))
    for mi, (col, mlab) in enumerate(EXTERNAL_METRICS):
        heights = [float(r[2][col]) for r in rows]
        offs = x + (mi - (n_m - 1) / 2) * width
        bars = ax.bar(
            offs, heights, width=width * 0.92,
            color=METRIC_COLORS[mi], alpha=FILL_ALPHA,
            edgecolor=METRIC_COLORS[mi], linewidth=LINEWIDTH * 0.35,
            label=mlab, zorder=3,
        )
        _annotate_nonzero(ax, bars, heights, METRIC_COLORS[mi])

    ax.axvspan(n_g - 1 - 0.48, n_g - 1 + 0.48, color="#3C5488", alpha=0.07, zorder=0)
    ax.set_xticks(x)
    ax.set_xticklabels([r[1] for r in rows], fontsize=TICK_FS)
    for tick, (key, _, _) in zip(ax.get_xticklabels(), rows):
        tick.set_color(color_map[key])
        if key == "D":
            tick.set_fontweight("bold")

    ax.set_ylabel("Exact Hit / grounding rate", fontweight="bold", fontsize=LABEL_FS)
    ax.set_ylim(0, 1.12)
    ax.legend(loc="upper left", ncol=1, fontsize=LEGEND_FS, frameon=True, edgecolor="#cccccc")
    setup_academic_ax(ax, title=None)
    ax.set_xlabel(
        "Peers: atomic IDP text + host Asset-IDs (no IAP / no VDPP); $N=200$",
        fontweight="bold", fontsize=LABEL_FS - 1,
    )
    fig.tight_layout()
    _save(fig, out_stem)
    print(f">>> external -> {out_stem.with_suffix('.pdf')}")


def _sig_stars(p: float) -> str:
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return "ns"


def plot_forest(stats_csv: Path, out_stem: Path) -> None:
    stats = pd.read_csv(stats_csv)
    stats = stats[stats["metric"] == "score"].copy()
    ours = theme_colors(None)["Ours"]
    worse = "#8491B4"
    ns_c = "#B0B0B0"

    fig, ax = plt.subplots(figsize=(10.2, 8.4))
    y_positions = []
    y_labels = []
    y = 0.0
    row_gap = 1.0
    block_gap = 0.55

    for ci, (cat, cat_lab) in enumerate(FOREST_CATS):
        if ci > 0:
            y += block_gap
        y_positions.append(y)
        y_labels.append(cat_lab)
        ax.axhspan(y - 0.35, y + 0.35, color="#F2F4F7", zorder=0)
        y += row_gap

        for bkey, blab in FOREST_BASELINES:
            row = stats[(stats["question_type"] == cat) & (stats["external"] == bkey)]
            if row.empty:
                continue
            r = row.iloc[0]
            d = float(r["mean_diff"])
            lo = float(r["bootstrap_ci_lo"])
            hi = float(r["bootstrap_ci_hi"])
            p = float(r["wilcoxon_p"])
            cohend = float(r["cohens_d"])
            stars = _sig_stars(p)
            if stars == "ns":
                color = ns_c
            elif d >= 0:
                color = ours
            else:
                color = worse

            ax.plot([lo, hi], [y, y], color=color, lw=2.0, solid_capstyle="round", zorder=3)
            ax.plot(d, y, "o", color=color, markersize=7.5, zorder=4)
            ax.text(
                4.55, y,
                f"{d:+.2f}  [{lo:+.2f}, {hi:+.2f}]  $d$={cohend:+.2f}  {stars}",
                va="center", ha="left", fontsize=9.5, color=INK,
                fontfamily="serif",
            )
            y_positions.append(y)
            y_labels.append(blab)
            y += row_gap

    ax.axvline(0, color=INK, ls="--", lw=GUIDE_LINEWIDTH, alpha=GUIDE_ALPHA, zorder=1)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels, fontsize=10.5)
    for lab, tick in zip(y_labels, ax.get_yticklabels()):
        if lab.startswith(("Overall", "Spatial", "Multi-hop", "Analytical")):
            tick.set_fontweight("bold")
            tick.set_fontsize(11.5)

    ax.set_xlim(-2.4, 7.2)
    ax.set_ylim(max(y_positions) + 0.8, min(y_positions) - 0.8)
    ax.set_xlabel(
        r"Score difference  (IAP-RAG $-$ baseline); bootstrap 95% CI",
        fontweight="bold", fontsize=LABEL_FS,
    )
    setup_academic_ax(ax, title=None)
    # No in-figure title / footer / color legend: caption carries the reading guide.
    fig.tight_layout()
    _save(fig, out_stem)
    print(f">>> forest -> {out_stem.with_suffix('.pdf')}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_dir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--ablation_csv", type=Path, default=REPRO / "ablation_gt_metrics.csv")
    ap.add_argument("--ksweep_csv", type=Path, default=REPRO / "ksweep_multihop_summary.csv")
    ap.add_argument("--idp_dir", type=Path, default=REPRO / "idp_only_external_sota_v1")
    ap.add_argument("--stats_csv", type=Path, default=STATS_CSV)
    args = ap.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    plot_ksweep(args.ksweep_csv, args.out_dir / "deterministic_ksweep_coverage")
    plot_ablation(args.ablation_csv, args.out_dir / "deterministic_ablation_exact_hit")
    plot_external(args.idp_dir, args.out_dir / "deterministic_external_exact_hit")
    if args.stats_csv.exists():
        plot_forest(args.stats_csv, args.out_dir / "forest_score_diff")


if __name__ == "__main__":
    main()
