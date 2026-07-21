#!/usr/bin/env python3
"""Publication-style stage-wise Asset-ID figure for the Goodman deployment audit.

Two clean panels suited to the discrete outcome data:
  a) Grouped bars of stage-wise success rates (registration audit, retrieved-ID
     recall, answer-ID recall, LLM-judge accuracy/5) for Spatial vs Multi-hop,
     with bootstrap 95% CIs. Shows that the 98.5% headline is a registration /
     localization audit, not generated-answer accuracy.
  b) 100% stacked horizontal bars of per-case outcome levels (none / partial /
     full recall) for each task x stage condition.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from run_field_asset_id_verification import extract_guids, load_judge_accuracy, load_trace

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "font.size": 7.5,
        "axes.labelsize": 7.5,
        "axes.titlesize": 8.5,
        "xtick.labelsize": 7,
        "ytick.labelsize": 7,
        "legend.fontsize": 7,
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "legend.frameon": False,
    }
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VERIFICATION = (
    PROJECT_ROOT / "data" / "eval" / "field_asset_id_verification_set.json"
)
DEFAULT_PASSPORTS = (
    PROJECT_ROOT / "data" / "Asset_Health_Passport" / "component_passports.json"
)
DEFAULT_TRACE = (
    PROJECT_ROOT
    / "logs"
    / "scientific_eval"
    / "external_full_d_v2_trace_20260706_114749.jsonl"
)
DEFAULT_METRICS = (
    PROJECT_ROOT
    / "logs"
    / "scientific_eval"
    / "external_full_d_v2_metrics_20260706_114749.csv"
)
DEFAULT_AUDIT = (
    PROJECT / "data" / "field_asset_id_stage_source_data.csv"
)
DEFAULT_SOURCE = (
    PROJECT_ROOT
    / "paper"
    / "AIC-Rebuttal"
    / "experiments"
    / "metrics"
    / "field_asset_id_stage_source_data.csv"
)

SPATIAL = "#4C78A8"
MULTI_HOP = "#E29A54"
INK = "#2C3338"
GRID = "#D9DEE2"
NONE_C = "#CFCECE"
PARTIAL_C = "#9CB4C7"
FULL_C = "#2E5C8A"
AGREE_C = "#7FA77A"
DISAGREE_C = "#D98C7A"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def bootstrap_ci(values: np.ndarray, n: int = 10000, seed: int = 0) -> Tuple[float, float]:
    rng = np.random.default_rng(seed)
    if len(values) == 0:
        return (np.nan, np.nan)
    means = np.array(
        [values[rng.integers(0, len(values), len(values))].mean() for _ in range(n)]
    )
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def build_rows(
    records: List[Dict[str, Any]],
    traces: Dict[int, Dict[str, Any]],
    judge: Dict[int, float],
    passport_ids: Set[str],
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for record in records:
        q_id = int(record["q_id"])
        trace = traces.get(q_id, {})
        gold = set(record.get("gold_asset_ids", []))
        retrieved = set(trace.get("retrieved_asset_ids", []))
        answer_ids = extract_guids(trace.get("answer", ""), passport_ids)
        is_roof = bool(record.get("empty_above_floor_defects"))

        denominator = len(gold)
        retrieval_recall = (
            len(gold & retrieved) / denominator if denominator else None
        )
        answer_recall = (
            len(gold & answer_ids) / denominator if denominator else None
        )
        # Paper-scale registration/localization audit (binary pass per case).
        if record["type"] == "spatial_awareness":
            reg_pass = 1  # spatial verifies the stored IDP-to-BIM registration.
        else:
            reg_pass = 0 if is_roof else 1  # ROOF-F fail strict retrieval.
        rows.append(
            {
                "q_id": q_id,
                "task_type": (
                    "Spatial"
                    if record["type"] == "spatial_awareness"
                    else "Multi-hop"
                ),
                "roof_no_asset_case": int(is_roof),
                "gold_id_count": denominator,
                "registration_audit_pass": reg_pass,
                "retrieved_id_recall": retrieval_recall,
                "answer_id_recall": answer_recall,
                "llm_judge_accuracy_0_5": judge.get(q_id),
            }
        )
    return rows


def write_source_data(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def _panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.16,
        1.06,
        label,
        transform=ax.transAxes,
        fontsize=9.5,
        fontweight="bold",
        va="top",
        color=INK,
    )


def _style(ax: plt.Axes) -> None:
    ax.spines["left"].set_linewidth(0.8)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.tick_params(direction="out", length=3, width=0.8, color=INK)


def stage_per_case(rows: List[Dict[str, Any]], task: str, field: str) -> np.ndarray:
    out = []
    for r in rows:
        if r["task_type"] != task:
            continue
        v = r[field]
        if v is None:
            continue
        out.append(float(v))
    return np.asarray(out, dtype=float)


def plot_stage_bars(ax: plt.Axes, rows: List[Dict[str, Any]]) -> None:
    stages = ["registration_audit_pass", "retrieved_id_recall", "answer_id_recall"]
    labels = ["Registration\naudit", "Retrieved-ID\nrecall", "Answer-ID\nrecall"]
    x = np.arange(len(stages))
    width = 0.36

    for offset, task, color, seed in (
        (-width / 2, "Spatial", SPATIAL, 11),
        (width / 2, "Multi-hop", MULTI_HOP, 22),
    ):
        means, lo, hi = [], [], []
        for stage in stages:
            vals = stage_per_case(rows, task, stage)
            means.append(float(np.mean(vals)) if len(vals) else np.nan)
            ci = bootstrap_ci(vals, seed=seed + len(means))
            lo.append(means[-1] - ci[0])
            hi.append(ci[1] - means[-1])
        ax.bar(
            x + offset,
            means,
            width,
            color=color,
            edgecolor="white",
            linewidth=0.5,
            label=task,
            zorder=3,
        )
        ax.errorbar(
            x + offset,
            means,
            yerr=[lo, hi],
            fmt="none",
            ecolor=INK,
            elinewidth=0.7,
            capsize=2.2,
            capthick=0.7,
            zorder=4,
        )

    # LLM-judge accuracy normalised to 0-1 (acc / 5).
    for offset, task, color, seed in (
        (-width / 2, "Spatial", SPATIAL, 33),
        (width / 2, "Multi-hop", MULTI_HOP, 44),
    ):
        vals = stage_per_case(rows, task, "llm_judge_accuracy_0_5") / 5.0
        m = float(np.mean(vals)) if len(vals) else np.nan
        ci = bootstrap_ci(vals, seed=seed)
        ax.bar(
            3 + offset, m, width, color=color, edgecolor="white", linewidth=0.5, zorder=3
        )
        ax.errorbar(
            3 + offset,
            m,
            yerr=[[m - ci[0]], [ci[1] - m]],
            fmt="none",
            ecolor=INK,
            elinewidth=0.7,
            capsize=2.2,
            capthick=0.7,
            zorder=4,
        )

    ax.axhline(0.985, color=INK, linestyle=(0, (3, 2)), linewidth=0.6, alpha=0.55, zorder=1)
    ax.text(
        3.45, 0.992, "98.5% headline", ha="right", va="bottom",
        fontsize=6.2, color=INK, alpha=0.85,
    )

    ax.set_xticks(np.append(x, 3), labels + ["LLM-judge\naccuracy / 5"])
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(0, 1.08)
    ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_ylabel("Success rate (per-case mean)")
    ax.set_title("Stage-wise Asset-ID performance", fontweight="bold", pad=6)
    ax.yaxis.grid(True, color=GRID, linewidth=0.5, alpha=0.8)
    ax.set_axisbelow(True)
    ax.legend(loc="lower right", bbox_to_anchor=(0.98, 0.02),
              handlelength=1.1, handletextpad=0.5, borderaxespad=0.3)
    _style(ax)
    _panel_label(ax, "a")


def _outcome_label(v: float) -> str:
    if v <= 1e-9:
        return "none"
    if v >= 1 - 1e-9:
        return "full"
    return "partial"


def plot_stacked(ax: plt.Axes, rows: List[Dict[str, Any]]) -> None:
    conditions = [
        ("Spatial", "retrieved_id_recall", "Spatial\nretrieved ID"),
        ("Spatial", "answer_id_recall", "Spatial\nanswer ID"),
        ("Multi-hop", "retrieved_id_recall", "Multi-hop\nretrieved ID"),
        ("Multi-hop", "answer_id_recall", "Multi-hop\nanswer ID"),
    ]
    levels = ["none", "partial", "full"]
    colors = [NONE_C, PARTIAL_C, FULL_C]

    y_positions = np.arange(len(conditions))[::-1]
    for ypos, (task, field, label) in zip(y_positions, conditions):
        vals = stage_per_case(rows, task, field)
        total = len(vals)
        counts = {lvl: 0 for lvl in levels}
        for v in vals:
            counts[_outcome_label(v)] += 1
        left = 0.0
        for lvl, color in zip(levels, colors):
            n = counts[lvl]
            if n == 0:
                continue
            frac = n / total
            ax.barh(
                ypos, frac, left=left, color=color, edgecolor="white",
                linewidth=0.5, height=0.6, zorder=3,
            )
            if frac >= 0.07:
                ax.text(
                    left + frac / 2, ypos, f"{n}  ({frac * 100:.0f}%)",
                    ha="center", va="center", fontsize=6.3,
                    color="white" if lvl != "none" else INK,
                )
            left += frac

    ax.set_yticks(y_positions, [c[2] for c in conditions])
    ax.set_xlim(0, 1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_xlabel("Share of cases")
    ax.set_title("Per-case outcome distribution", fontweight="bold", pad=6)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_linewidth(0.8)
    ax.tick_params(axis="y", length=0, pad=2)
    ax.tick_params(axis="x", direction="out", length=3, width=0.8, color=INK)
    ax.xaxis.grid(True, color=GRID, linewidth=0.5, alpha=0.8)
    ax.set_axisbelow(True)

    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in colors]
    ax.legend(
        handles, ["None (0)", "Partial (0.5)", "Full (1.0)"],
        loc="upper center", bbox_to_anchor=(0.5, 1.30), ncol=3,
        handlelength=1.1, handletextpad=0.4, columnspacing=1.2,
    )
    _panel_label(ax, "b")


def plot_confusion(ax: plt.Axes, audit: Dict[str, Any]) -> None:
    block = audit["paper_scale_and_judge_are_not_calibrated"]
    cm = block["confusion_matrix"]
    matrix = np.array(
        [
            [cm["field_miss_judge_fail"], cm["field_miss_judge_pass"]],
            [cm["field_hit_judge_fail"], cm["field_hit_judge_pass"]],
        ]
    )
    total = int(matrix.sum())
    agree = int(block["agreement_hits"])

    # Neutral single-hue heatmap by count. These two metrics measure DIFFERENT
    # stages (field registration audit vs LLM-judge answer accuracy), so an
    # agree/disagree (green/red) coding would falsely imply calibration.
    cmap = plt.get_cmap("Blues")
    vmax = float(matrix.max()) if matrix.max() > 0 else 1.0
    for i in range(2):
        for j in range(2):
            n = matrix[i, j]
            ax.add_patch(
                plt.Rectangle((j, 1 - i), 1, 1,
                              facecolor=cmap(0.22 + 0.62 * n / vmax),
                              edgecolor="white", linewidth=1.5, zorder=2)
            )
            ax.text(
                j + 0.5, 1 - i + 0.5, f"{int(n)}\n{100 * n / total:.1f}%",
                ha="center", va="center", fontsize=8,
                color="white" if (n / vmax > 0.55) else INK, zorder=3,
            )

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xticks([0.5, 1.5], ["Judge fail", "Judge pass"])
    ax.set_yticks([0.5, 1.5], ["Field hit", "Field miss"])
    ax.set_xlabel("LLM-judge accuracy (>=3 threshold)")
    ax.set_ylabel("Field-record audit")
    ax.set_title(
        "Field-audit x LLM-judge co-occurrence\n"
        f"(different stages; agree {agree}/{total} = {100 * agree / total:.1f}%; "
        "not a substitute for answer quality)",
        fontweight="bold", pad=6,
    )
    ax.tick_params(direction="out", length=0, color=INK)
    for spine in ax.spines.values():
        spine.set_visible(False)
    _panel_label(ax, "c")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verification-set", type=Path, default=DEFAULT_VERIFICATION)
    parser.add_argument("--passports", type=Path, default=DEFAULT_PASSPORTS)
    parser.add_argument("--trace", type=Path, default=DEFAULT_TRACE)
    parser.add_argument("--metrics", type=Path, default=DEFAULT_METRICS)
    parser.add_argument("--audit", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--source-data", type=Path, default=DEFAULT_SOURCE)
    args = parser.parse_args()

    records = load_json(args.verification_set)["records"]
    passport_ids = {row["asset_id"] for row in load_json(args.passports)}
    rows = build_rows(
        records,
        load_trace(args.trace),
        load_judge_accuracy(args.metrics),
        passport_ids,
    )
    write_source_data(args.source_data, rows)

    fig = plt.figure(figsize=(7.2, 4.6))
    grid = fig.add_gridspec(2, 1, height_ratios=[1.15, 1.0], hspace=0.45)
    ax_a = fig.add_subplot(grid[0, 0])
    ax_b = fig.add_subplot(grid[1, 0])

    plot_stage_bars(ax_a, rows)
    plot_stacked(ax_b, rows)

    fig.subplots_adjust(left=0.16, right=0.985, bottom=0.10, top=0.93)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output.with_suffix(".svg"), bbox_inches="tight")
    fig.savefig(args.output.with_suffix(".pdf"), bbox_inches="tight")
    fig.savefig(args.output.with_suffix(".png"), dpi=600, bbox_inches="tight")
    fig.savefig(
        args.output.with_suffix(".tiff"),
        dpi=600,
        bbox_inches="tight",
        pil_kwargs={"compression": "tiff_lzw"},
    )
    plt.close(fig)
    print(f"[OK] Source data -> {args.source_data}")
    print(f"[OK] Figure -> {args.output}.{{svg,pdf,png,tiff}}")


if __name__ == "__main__":
    main()
