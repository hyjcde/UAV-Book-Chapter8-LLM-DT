#!/usr/bin/env python3
"""R1–R3: Nature palette, bar-first composite layouts, no overlapping labels."""

from __future__ import annotations

import argparse
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
    style_hbar,
)

apply_rcparams()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = PROJECT_ROOT / "out"
RAW_INPUTS = [
    PROJECT_ROOT / "data" / "external_full_appc_D_metrics_20260716_160315.csv",
    PROJECT_ROOT / "data" / "external_full_appc_EF_metrics_20260716_160530.csv",
    PROJECT_ROOT / "data" / "external_full_appc_HIJ_metrics_20260716_160531.csv",
]
STATS_CSV = PROJECT_ROOT / "data" / "statistical_analysis_final.csv"

COLORS = external_group_colors(None)
GROUP_NAMES = {
    "D": "IAP-RAG (Ours)",
    "E": "Naive Chunk-RAG",
    "F": "Graph-Neighbour",
    "H": "GraphRAG",
    "I": "RAPTOR",
    "J": "HyDE+Fusion",
}
SHORT = {
    "D": "IAP-RAG",
    "E": "Chunk-RAG",
    "F": "Graph-Neighbour",
    "H": "GraphRAG",
    "I": "RAPTOR",
    "J": "HyDE+Fusion",
}
PARADIGM = {
    "D": "Entity-centric IAP",
    "E": "Flat dense",
    "F": "Graph (no IAP)",
    "H": "Graph community",
    "I": "Hierarchical",
    "J": "Query transform",
}
SPECTRUM_ORDER = ["E", "J", "I", "F", "H", "D"]
QUESTION_TYPES = ["spatial_awareness", "multi_hop_topological", "analytical_aggregation"]
TYPE_LABELS = {
    "spatial_awareness": "Spatial Awareness",
    "multi_hop_topological": "Multi-hop Topological",
    "analytical_aggregation": "Analytical Aggregation",
}
TYPE_SHORT = {
    "spatial_awareness": "Spatial",
    "multi_hop_topological": "Multi-hop",
    "analytical_aggregation": "Analytical",
}


def _norm(g: str) -> str:
    return g[len("Group_"):] if str(g).startswith("Group_") else g


def load_raw() -> pd.DataFrame:
    frames = []
    for p in RAW_INPUTS:
        df = pd.read_csv(p)
        df["group"] = df["group"].map(_norm)
        frames.append(df)
    return pd.concat(frames, ignore_index=True).query("group in @GROUP_NAMES").copy()


def load_stats() -> pd.DataFrame:
    return pd.read_csv(STATS_CSV).query("metric == 'score'").copy()


def sem(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    return float(np.std(x, ddof=1) / np.sqrt(len(x))) if len(x) > 1 else 0.0


def stat_row(stats: pd.DataFrame, qtype: str, ext: str) -> pd.Series:
    return stats[(stats["question_type"] == qtype) & (stats["external"] == ext)].iloc[0]


def plot_r1(df: pd.DataFrame, out_pdf: Path, out_png: Path) -> None:
    fig, ax = plt.subplots(figsize=(9.4, 4.8))
    means, errs = [], []
    for g in SPECTRUM_ORDER:
        vals = df[df["group"] == g]["score"].to_numpy(dtype=float)
        means.append(vals.mean())
        errs.append(sem(vals))
    x = np.arange(len(SPECTRUM_ORDER))
    for i, g in enumerate(SPECTRUM_ORDER):
        style_bar(ax, [i], [means[i]], color=COLORS[g], width=0.64, yerr=[[errs[i]], [errs[i]]])
        ax.text(
            i, means[i] + errs[i] + 0.22, f"$\\mu$={means[i]:.2f}",
            ha="center", fontsize=13, fontweight="bold", color=COLORS[g],
        )
    ax.set_xticks(x)
    ax.set_xticklabels([f"{PARADIGM[g]}\n({g})" for g in SPECTRUM_ORDER], fontsize=12)
    ax.set_ylabel("Overall diagnostic judge score (0–10)", fontweight="bold", fontsize=15)
    ax.set_ylim(0, max(means) + max(errs) + 1.4)
    setup_academic_ax(ax, "RAG paradigm spectrum: mean score by paradigm (±1 SEM)")
    fig.tight_layout()
    fig.savefig(out_pdf, format="pdf", bbox_inches="tight")
    fig.savefig(out_png, dpi=220, bbox_inches="tight")
    plt.close(fig)
    print(f">>> R1 -> {out_pdf}")


def plot_r2(df: pd.DataFrame, stats: pd.DataFrame, out_pdf: Path, out_png: Path) -> None:
    """Composite: (a) grouped bars; (b) three stacked Δ hbars (no side-by-side label clash)."""
    groups = ["E", "F", "H", "I", "J", "D"]
    baselines = ["E", "F", "H", "I", "J"]

    # Taller bottom stack so y-tick labels (full baseline names) are not cramped.
    fig = plt.figure(figsize=(10.4, 12.6))
    gs = fig.add_gridspec(2, 1, height_ratios=[0.95, 2.05], hspace=0.26)
    ax = fig.add_subplot(gs[0, 0])

    x = np.arange(len(QUESTION_TYPES), dtype=float) * 1.40
    width = 0.86 / len(groups)
    for i, g in enumerate(groups):
        means = [df[(df["group"] == g) & (df["type"] == t)]["score"].mean() for t in QUESTION_TYPES]
        errs = [sem(df[(df["group"] == g) & (df["type"] == t)]["score"].to_numpy()) for t in QUESTION_TYPES]
        offset = (i - (len(groups) - 1) / 2) * width
        bars = style_bar(
            ax, x + offset, means, color=COLORS[g], width=width * 0.90,
            yerr=[errs, errs], label=GROUP_NAMES[g],
        )
        if g == "D":
            for rect, m, e in zip(bars, means, errs):
                ax.text(
                    rect.get_x() + rect.get_width() / 2, m + e + 0.22,
                    f"{m:.2f}", ha="center", fontsize=12,
                    fontweight="bold", color=COLORS[g], clip_on=False,
                )

    ax.set_xticks(x)
    ax.set_xticklabels([TYPE_LABELS[t] for t in QUESTION_TYPES], fontsize=13)
    ax.set_ylabel("Mean judge score (0–10)", fontweight="bold", fontsize=15)
    ax.set_ylim(0, 9.2)
    ax.set_xlim(x[0] - 0.80, x[-1] + 0.80)
    setup_academic_ax(ax, "(a)  Mean diagnostic score by question type  (±1 SEM)")
    ax.legend(
        loc="upper left", fontsize=10, ncol=3, frameon=True,
        columnspacing=0.8, handlelength=1.2, borderpad=0.4,
    )

    # ---- (b) three Δ panels stacked (full width → labels never collide) ----
    gs_b = gs[1, 0].subgridspec(3, 1, hspace=0.62)
    for j, t in enumerate(QUESTION_TYPES):
        axb = fig.add_subplot(gs_b[j, 0])
        diffs, elo, ehi = [], [], []
        for b in baselines:
            r = stat_row(stats, t, b)
            d = float(r["mean_diff"])
            diffs.append(d)
            elo.append(d - float(r["bootstrap_ci_lo"]))
            ehi.append(float(r["bootstrap_ci_hi"]) - d)
        # Extra vertical padding between category rows
        y = np.arange(len(baselines), dtype=float)[::-1] * 1.55
        for yi, b, d, lo, hi in zip(y, baselines, diffs, elo, ehi):
            style_hbar(
                axb, [yi], [d], color=COLORS[b], height=0.78,
                xerr=[[lo], [hi]],
            )
            # Labels sit outside CI; roomy x-lim avoids clipping
            x_lab = (d + hi + 0.18) if d >= 0 else (d - lo - 0.18)
            axb.text(
                x_lab, yi, f"{d:+.2f}", va="center",
                ha="left" if d >= 0 else "right",
                fontsize=12, fontweight="bold", color=COLORS[b], clip_on=False,
            )

        axb.axvline(0, color=INK, linestyle="--", linewidth=GUIDE_LINEWIDTH, alpha=GUIDE_ALPHA)
        axb.set_yticks(y)
        axb.set_yticklabels([SHORT[b] for b in baselines], fontsize=11)
        axb.set_ylim(y.min() - 1.05, y.max() + 1.05)
        axb.set_xlim(-5.0, 5.8)
        title = f"(b)  $\\Delta$ by baseline — {TYPE_SHORT[t]}" if j == 0 else TYPE_SHORT[t]
        setup_academic_ax(axb, title)
        if j == 2:
            axb.set_xlabel(
                r"$\Delta$ = IAP-RAG $-$ baseline (bootstrap 95% CI)",
                fontweight="bold", fontsize=14,
            )

    fig.savefig(out_pdf, format="pdf", bbox_inches="tight", pad_inches=0.28)
    fig.savefig(out_png, dpi=220, bbox_inches="tight", pad_inches=0.28)
    plt.close(fig)
    print(f">>> R2 -> {out_pdf}")


def plot_r3(stats: pd.DataFrame, out_pdf: Path, out_png: Path) -> None:
    """2×2 composite horizontal bars (more information than thin line panels)."""
    categories = ["ALL", "spatial_awareness", "multi_hop_topological", "analytical_aggregation"]
    cat_labels = ["(a) Overall", "(b) Spatial", "(c) Multi-hop", "(d) Analytical"]
    baselines = ["E", "F", "H", "I", "J"]

    fig, axes = plt.subplots(2, 2, figsize=(11.0, 8.4), gridspec_kw={"wspace": 0.38, "hspace": 0.42})
    axes = axes.ravel()
    for ax, cat, lab in zip(axes, categories, cat_labels):
        diffs, elo, ehi = [], [], []
        for b in baselines:
            r = stat_row(stats, cat, b)
            d = float(r["mean_diff"])
            diffs.append(d)
            elo.append(d - float(r["bootstrap_ci_lo"]))
            ehi.append(float(r["bootstrap_ci_hi"]) - d)
        y = np.arange(len(baselines), dtype=float)[::-1] * 1.30
        for yi, b, d, lo, hi in zip(y, baselines, diffs, elo, ehi):
            style_hbar(ax, [yi], [d], color=COLORS[b], height=0.70, xerr=[[lo], [hi]])
            if d >= 0:
                ax.text(d + hi + 0.10, yi, f"{d:+.2f}", va="center", ha="left",
                        fontsize=11, fontweight="bold", color=COLORS[b], clip_on=False)
            else:
                ax.text(d - lo - 0.10, yi, f"{d:+.2f}", va="center", ha="right",
                        fontsize=11, fontweight="bold", color=COLORS[b], clip_on=False)
        ax.axvline(0, color=INK, linestyle="--", linewidth=GUIDE_LINEWIDTH, alpha=GUIDE_ALPHA)
        ax.set_yticks(y)
        ax.set_yticklabels([SHORT[b] for b in baselines], fontsize=10)
        ax.set_ylim(y.min() - 0.75, y.max() + 0.75)
        ax.set_xlim(-4.6, 5.6)
        setup_academic_ax(ax, lab)
        ax.set_xlabel(r"$\Delta$", fontweight="bold", fontsize=13)

    fig.suptitle(
        "Score difference vs baselines (bootstrap 95% CI)",
        fontsize=17, fontweight="bold", color=INK, y=0.995,
    )
    fig.savefig(out_pdf, format="pdf", bbox_inches="tight", pad_inches=0.22)
    fig.savefig(out_png, dpi=220, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)
    print(f">>> R3 -> {out_pdf}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_dir", type=Path, default=FIG_DIR)
    args = ap.parse_args()
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    preview = out / "_preview"
    preview.mkdir(exist_ok=True)
    df, stats = load_raw(), load_stats()
    plot_r1(df, out / "paradigm_spectrum.pdf", preview / "paradigm_spectrum.png")
    plot_r2(df, stats, out / "score_by_type.pdf", preview / "score_by_type.png")
    plot_r3(stats, out / "forest_score_diff.pdf", preview / "forest_score_diff.png")
    print(">>> Done.")


if __name__ == "__main__":
    main()
