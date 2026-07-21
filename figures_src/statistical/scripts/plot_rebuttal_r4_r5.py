#!/usr/bin/env python3
"""R4 / R5 — Nature craft, bar-first, no overlapping labels."""

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
    apply_rcparams,
    external_group_colors,
    series_pair,
    setup_academic_ax,
    style_bar,
)

apply_rcparams()
COLORS = external_group_colors("BookSlate")

PROJECT = Path(__file__).resolve().parents[1]
FIG_DIR = PROJECT / "out"
STAGE_CSV = PROJECT / "data" / "field_asset_id_stage_source_data.csv"


def bootstrap_ci(vals: np.ndarray, n: int = 8000, seed: int = 0):
    rng = np.random.default_rng(seed)
    if len(vals) == 0:
        return np.nan, np.nan, np.nan
    means = np.array([vals[rng.integers(0, len(vals), len(vals))].mean() for _ in range(n)])
    return float(vals.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def plot_r4(out_pdf: Path, out_png: Path) -> None:
    """Grouped bars for field audit stages (bar-first, clearer than lines)."""
    # Distinct Spatial / Multi-hop pair (blue / orange), not the cool Nature pair
    # which made both series read as blue-cyan and broke the figure colour language.
    dark, light = "#0F4C5C", "#E36414"
    df = pd.read_csv(STAGE_CSV)
    sp = df[df.task_type == "Spatial"]
    mh = df[df.task_type == "Multi-hop"]
    nr = mh[mh.roof_no_asset_case == 0]

    stages = ["Field-record\naudit", "Retrieved-ID\nrecall", "Answer-ID\nrecall", "LLM-judge\naccuracy / 5"]
    sp_vals = [
        np.ones(70),
        (sp.retrieved_id_recall == 1).astype(float).to_numpy(),
        (sp.answer_id_recall == 1).astype(float).to_numpy(),
        (sp.llm_judge_accuracy_0_5 / 5.0).to_numpy(),
    ]
    mh_vals = [
        np.concatenate([np.ones(68), np.zeros(2)]),
        (nr.retrieved_id_recall == 1).astype(float).to_numpy(),
        (nr.answer_id_recall == 1).astype(float).to_numpy(),
        (mh.llm_judge_accuracy_0_5 / 5.0).to_numpy(),
    ]

    fig, ax = plt.subplots(figsize=(9.2, 4.8))
    x = np.arange(len(stages))
    width = 0.36

    def series(vals, color, label, seed, offset):
        means, elo, ehi = [], [], []
        for k, v in enumerate(vals):
            m, lo, hi = bootstrap_ci(v, seed=seed + k)
            means.append(m)
            elo.append(m - lo)
            ehi.append(hi - m)
        bars = style_bar(
            ax, x + offset, means, color=color, width=width,
            yerr=[elo, ehi], label=label,
        )
        notes = (["70/70", None, None, None] if "Spatial" in label else ["68/70", None, None, None])
        for rect, m, e, note in zip(bars, means, ehi, notes):
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                min(m + e + 0.05, 1.18),
                note or f"{m:.2f}",
                ha="center", fontsize=11, fontweight="bold", color=color, clip_on=False,
            )

    series(sp_vals, dark, "Spatial ($n$ = 70)", 11, -width / 2)
    series(mh_vals, light, "Multi-hop ($n$ = 70)", 22, width / 2)

    ax.axhline(138 / 140, color=INK, linestyle="--", linewidth=GUIDE_LINEWIDTH, alpha=GUIDE_ALPHA)
    ax.text(3.35, 138 / 140 + 0.02, r"$138/140$", va="bottom", ha="left", fontsize=12, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=12)
    ax.set_ylim(0, 1.32)
    ax.set_ylabel("Success rate", fontweight="bold", fontsize=15)
    setup_academic_ax(ax, title=None)
    ax.set_xlabel("Evaluation stage", fontweight="bold", fontsize=12)
    ax.legend(loc="upper right", fontsize=12, frameon=True)
    fig.savefig(out_pdf, format="pdf", bbox_inches="tight", pad_inches=0.22)
    fig.savefig(out_png, dpi=220, bbox_inches="tight", pad_inches=0.22)
    plt.close(fig)
    print(f">>> R4 -> {out_pdf}")


def plot_r5(out_pdf: Path, out_png: Path) -> None:
    """Composite: (a) overall hbars; (b) grouped bars by type — no lines."""
    raw_paths = [
        PROJECT / "data/external_full_appc_D_metrics_20260716_160315.csv",
        PROJECT / "data/external_full_appc_EF_metrics_20260716_160530.csv",
        PROJECT / "data/external_full_appc_HIJ_metrics_20260716_160531.csv",
    ]
    frames = []
    for p in raw_paths:
        df = pd.read_csv(p)
        df["group"] = df["group"].astype(str).str.replace("Group_", "", regex=False)
        h = df["hallucination"]
        df["hallucination"] = h.astype(float) if h.dtype == bool else (
            h.astype(str).str.strip()
            .map({"True": 1.0, "False": 0.0, "true": 1.0, "false": 0.0, "1": 1.0, "0": 0.0})
            .fillna(0.0)
        )
        frames.append(df[["group", "hallucination", "type"]])
    raw = pd.concat(frames, ignore_index=True)

    order = ["D", "E", "F", "H", "I", "J"]
    full = {
        "D": "IAP-RAG (Ours)", "E": "Naive Chunk-RAG", "F": "Graph-Neighbour",
        "H": "GraphRAG", "I": "RAPTOR", "J": "HyDE+Fusion",
    }
    types = ["spatial_awareness", "multi_hop_topological", "analytical_aggregation"]
    type_labs = ["Spatial", "Multi-hop", "Analytical"]

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6), gridspec_kw={"wspace": 0.34, "width_ratios": [1.05, 1.15]})

    # (a) horizontal bars
    ax = axes[0]
    means, elo, ehi = [], [], []
    for i, g in enumerate(order):
        m, lo, hi = bootstrap_ci(raw[raw.group == g]["hallucination"].to_numpy(dtype=float), seed=100 + i)
        means.append(m)
        elo.append(m - lo)
        ehi.append(hi - m)
    y = np.arange(len(order))[::-1]
    for yi, g, m, lo, hi in zip(y, order, means, elo, ehi):
        ax.barh(
            yi, m, height=0.62, color=COLORS[g], alpha=FILL_ALPHA,
            edgecolor=COLORS[g], linewidth=1.1, zorder=3,
        )
        ax.errorbar(
            m, yi, xerr=[[lo], [hi]], fmt="none", ecolor=INK,
            elinewidth=GUIDE_LINEWIDTH, capsize=3, alpha=GUIDE_ALPHA, zorder=4,
        )
        ax.text(m + hi + 0.015, yi, f"{m:.2f}", va="center", ha="left",
                fontsize=12, fontweight="bold", color=COLORS[g], clip_on=False)
    ax.set_yticks(y)
    ax.set_yticklabels([full[g] for g in order], fontsize=11)
    ax.set_xlim(0, 1.18)
    ax.set_xlabel("Judge-flagged hallucination rate", fontweight="bold", fontsize=13)
    setup_academic_ax(ax, "(a)  Overall  ($n$ = 200)")

    # (b) grouped bars — wider category gaps
    ax2 = axes[1]
    x2 = np.arange(len(types), dtype=float) * 1.30
    width = 0.88 / len(order)
    for i, g in enumerate(order):
        vals = [raw[(raw.group == g) & (raw.type == t)]["hallucination"].mean() for t in types]
        offset = (i - (len(order) - 1) / 2) * width
        style_bar(ax2, x2 + offset, vals, color=COLORS[g], width=width * 0.90, label=full[g])
    ax2.set_xticks(x2)
    ax2.set_xticklabels(type_labs, fontsize=13)
    ax2.set_ylim(0, 1.15)
    ax2.set_xlim(x2[0] - 0.70, x2[-1] + 0.70)
    ax2.set_ylabel("Hallucination rate", fontweight="bold", fontsize=13)
    setup_academic_ax(ax2, "(b)  By question type")
    ax2.legend(
        loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=3,
        fontsize=10, frameon=True, columnspacing=0.8, handlelength=1.2,
    )

    fig.savefig(out_pdf, format="pdf", bbox_inches="tight", pad_inches=0.25)
    fig.savefig(out_png, dpi=220, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f">>> R5 -> {out_pdf}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_dir", type=Path, default=FIG_DIR)
    args = ap.parse_args()
    out = args.out_dir
    out.mkdir(parents=True, exist_ok=True)
    preview = out / "_preview"
    preview.mkdir(exist_ok=True)
    plot_r4(out / "field_asset_id_stages.pdf", preview / "field_asset_id_stages.png")
    plot_r5(out / "hallucination_rate.pdf", preview / "hallucination_rate.png")
    print(">>> Done.")


if __name__ == "__main__":
    main()
