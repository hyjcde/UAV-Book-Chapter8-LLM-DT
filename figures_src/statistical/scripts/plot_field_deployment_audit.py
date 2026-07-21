#!/usr/bin/env python3
"""Create the publication figure for the Goodman field-record audit."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

from figure_style import INK as _INK
from figure_style import MODULES

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["Arial", "DejaVu Sans", "Liberation Sans"]
plt.rcParams["svg.fonttype"] = "none"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "field_deployment_record_audit_frozen.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "out" / "field_deployment_audit"

# BookInk module hexes — edit MODULES_BOOKINK in figure_style.py, not pixels.
COLORS = {
    "ink": _INK,
    "muted": MODULES["E"],
    "grid": "#E5E7EB",
    "light": "#F4F6F7",
    "blue": MODULES["D"],
    "blue_light": "#7FB3D5",
    "teal": MODULES["F"],
    "teal_light": "#76D7C4",
    "amber": MODULES["Warn"],
    "red": MODULES["Risk"],
}


def style() -> None:
    mpl.rcParams.update(
        {
            "font.size": 7.2,
            "axes.labelsize": 7.2,
            "axes.titlesize": 8.2,
            "xtick.labelsize": 6.5,
            "ytick.labelsize": 6.5,
            "axes.linewidth": 0.7,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "legend.frameon": False,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )


def panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.12,
        1.08,
        label,
        transform=ax.transAxes,
        fontsize=9,
        fontweight="bold",
        color=COLORS["ink"],
        va="top",
    )


def plot_inventory(ax: plt.Axes, audit: dict) -> None:
    field = audit["actual_field_records"]
    rgb = field["modalities"]["RGB"]
    ir = field["modalities"]["IR"]
    total = field["atomic_observations"]

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    panel_label(ax, "a")
    ax.text(
        0,
        0.98,
        "Actual deployment records",
        fontsize=8.2,
        fontweight="bold",
        color=COLORS["ink"],
        va="top",
    )
    ax.text(
        0,
        0.79,
        f"{total}",
        fontsize=25,
        fontweight="bold",
        color=COLORS["blue"],
        va="center",
    )
    ax.text(
        0.02,
        0.63,
        "field observations",
        fontsize=7,
        color=COLORS["muted"],
    )
    ax.text(
        0.02,
        0.50,
        f"{field['assets_with_observations']} BIM assets",
        fontsize=8.2,
        fontweight="bold",
        color=COLORS["ink"],
    )

    rgb_fraction = rgb / total
    left, bottom, width, height = 0.02, 0.34, 0.92, 0.085
    ax.add_patch(
        plt.Rectangle(
            (left, bottom),
            width * rgb_fraction,
            height,
            color=COLORS["blue"],
            linewidth=0,
        )
    )
    ax.add_patch(
        plt.Rectangle(
            (left + width * rgb_fraction, bottom),
            width * (1 - rgb_fraction),
            height,
            color=COLORS["amber"],
            linewidth=0,
        )
    )
    ax.text(
        left + 0.02,
        bottom + height / 2,
        f"RGB  {rgb}",
        color="white",
        fontsize=6.4,
        fontweight="bold",
        va="center",
    )
    ax.text(
        left + width * rgb_fraction + 0.008,
        bottom + height + 0.035,
        f"IR {ir}",
        color=COLORS["amber"],
        fontsize=6.2,
        fontweight="bold",
        va="bottom",
    )

    completeness = [
        ("Image", field["records_with_image_url"]),
        ("GPS", field["records_with_gps"]),
        ("Anchor", field["records_with_spatial_anchor"]),
    ]
    y = 0.205
    for index, (label, value) in enumerate(completeness):
        x = 0.07 + index * 0.30
        ax.scatter(
            x,
            y,
            s=22,
            color=COLORS["teal"],
            edgecolor="white",
            linewidth=0.5,
            zorder=3,
        )
        ax.text(
            x,
            y - 0.055,
            f"{label}\n{value}/{total}",
            va="top",
            ha="center",
            fontsize=5.9,
            linespacing=1.15,
        )
    ax.text(
        0.02,
        0.015,
        f"IR capture: {field['capture_date_min']} to {field['capture_date_max']}",
        fontsize=6.2,
        color=COLORS["muted"],
    )


def plot_stage_metrics(ax: plt.Axes, audit: dict) -> None:
    coverage = audit["field_record_reference_coverage"]
    model = audit["model_output_against_field_record_reference"]
    labels = [
        "Registration lookup",
        "Spatial retrieval",
        "Spatial answer ID",
        "Multi-hop retrieval",
        "Multi-hop ID recall",
    ]
    values = np.array(
        [
            coverage["spatial_registration"]["rate"],
            model["spatial_retrieval"]["rate"],
            model["spatial_answer_explicit_id"]["rate"],
            model["multi_hop_question_retrieval_non_roof"]["rate"],
            model["multi_hop_id_retrieval"]["rate"],
        ]
    ) * 100
    numerators = [
        coverage["spatial_registration"]["hits"],
        model["spatial_retrieval"]["hits"],
        model["spatial_answer_explicit_id"]["hits"],
        model["multi_hop_question_retrieval_non_roof"]["hits"],
        model["multi_hop_id_retrieval"]["hits"],
    ]
    denominators = [
        coverage["spatial_registration"]["total"],
        model["spatial_retrieval"]["total"],
        model["spatial_answer_explicit_id"]["total"],
        model["multi_hop_question_retrieval_non_roof"]["total"],
        model["multi_hop_id_retrieval"]["total"],
    ]
    colors = [
        COLORS["muted"],
        COLORS["blue"],
        COLORS["teal"],
        COLORS["blue"],
        COLORS["blue"],
    ]
    y = np.arange(len(labels))[::-1]

    panel_label(ax, "b")
    ax.set_title("Asset-ID performance by evaluation stage", loc="left", pad=10)
    ax.hlines(y, 0, values, color=colors, linewidth=2.2, alpha=0.7)
    ax.scatter(
        values,
        y,
        s=42,
        color=colors,
        edgecolor="white",
        linewidth=0.7,
        zorder=3,
    )
    for yi, value, numerator, denominator in zip(
        y,
        values,
        numerators,
        denominators,
    ):
        label_x = min(value + 3.0, 102)
        horizontal = "left" if value < 98 else "right"
        if value >= 98:
            label_x = value - 2.0
        ax.text(
            label_x,
            yi,
            f"{numerator}/{denominator}",
            va="center",
            ha=horizontal,
            fontsize=6.4,
            fontweight="bold",
            color=COLORS["ink"],
        )
    ax.set_yticks(y, labels)
    ax.set_xlim(0, 108)
    ax.set_xlabel("Rate (%)")
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.grid(axis="x", color=COLORS["grid"], linewidth=0.6)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.spines["left"].set_visible(False)


def plot_calibration(ax: plt.Axes, audit: dict) -> None:
    calibration = audit["paper_scale_and_judge_are_not_calibrated"]
    counts = calibration["confusion_matrix"]
    matrix = np.array(
        [
            [
                counts["field_miss_judge_fail"],
                counts["field_miss_judge_pass"],
            ],
            [
                counts["field_hit_judge_fail"],
                counts["field_hit_judge_pass"],
            ],
        ]
    )
    cmap = LinearSegmentedColormap.from_list(
        "audit_blue",
        ["#F7F9FA", COLORS["blue_light"], COLORS["blue"]],
    )

    panel_label(ax, "c")
    ax.set_title("Field audit vs LLM judge", loc="left", pad=10)
    image = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=matrix.max(), aspect="equal")
    del image
    for row in range(2):
        for column in range(2):
            value = matrix[row, column]
            text_color = "white" if value > matrix.max() * 0.55 else COLORS["ink"]
            ax.text(
                column,
                row,
                str(value),
                ha="center",
                va="center",
                fontsize=13,
                fontweight="bold",
                color=text_color,
            )
    ax.set_xticks([0, 1], ["Judge\nfail", "Judge\npass"])
    ax.set_yticks([0, 1], ["Audit miss", "Audit hit"])
    ax.tick_params(length=0, pad=4)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xlabel("LLM-judge threshold ≥3/5", labelpad=4)
    ax.text(
        0.5,
        -0.43,
        (
            f"Agreement {100 * calibration['agreement_rate']:.1f}% "
            f"({calibration['agreement_hits']}/140); "
            "different stages, not a substitute"
        ),
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=6.5,
        color=COLORS["muted"],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    style()
    audit = json.loads(args.input.read_text(encoding="utf-8"))
    # Explicit margins avoid constrained_layout collapse on tight Springer columns
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 3.7), gridspec_kw={"width_ratios": [1.0, 1.35, 1.15]})
    plot_inventory(axes[0], audit)
    plot_stage_metrics(axes[1], audit)
    plot_calibration(axes[2], audit)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.90, bottom=0.18, wspace=0.38)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    for ext, kw in [
        (".svg", {}),
        (".pdf", {}),
        (".png", {"dpi": 600}),
        (".tiff", {"dpi": 600, "pil_kwargs": {"compression": "tiff_lzw"}}),
    ]:
        fig.savefig(args.output.with_suffix(ext), bbox_inches="tight", **kw)
    plt.close(fig)
    print(f"[OK] Figure -> {args.output}.{{svg,pdf,png,tiff}}")


if __name__ == "__main__":
    main()
