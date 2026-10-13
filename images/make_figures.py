"""Regenerate the figures this edition had to redraw, because the German originals are
PNGs with German text and no vector source.

    uv run python images/make_figures.py

Each figure is reproduced as closely as the original allows -- same geometry, same
colours, same message -- with English labels. Committing the script rather than only the
PNG means the next change is an edit instead of an archaeology project.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent

# The eight-colour Okabe-Ito palette, which is what the German figure shows.
OKABE_ITO = ["#000000", "#E69F00", "#56B4E9", "#009E73",
             "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]


# --------------------------------------------------------------- Simpson's paradox

def simpson() -> None:
    """Two groups that each rise, while the pooled trend falls."""
    rng = np.random.default_rng(23)

    # group 1 sits lower left, group 2 lower right; both rise, the pooled line falls
    x1 = rng.uniform(0.0, 3.2, 60)
    y1 = 4.1 + 0.95 * x1 + rng.normal(0, 0.45, 60)
    x2 = rng.uniform(4.3, 7.4, 60)
    y2 = 0.6 + 0.78 * (x2 - 4.3) + rng.normal(0, 0.45, 60)

    fig, ax = plt.subplots(figsize=(9, 5.6), dpi=100)
    ax.scatter(x1, y1, s=28, color="#1f77b4", label="Group 1 (e.g. small stones)")
    ax.scatter(x2, y2, s=28, color="#ff7f0e", label="Group 2 (e.g. large stones)")

    x_all = np.concatenate([x1, x2])
    y_all = np.concatenate([y1, y2])
    slope, intercept = np.polyfit(x_all, y_all, 1)
    grid = np.linspace(x_all.min() - 0.1, x_all.max() + 0.1, 2)
    ax.plot(grid, slope * grid + intercept, "r--", linewidth=2.2,
            label="Trend over all points")

    for x, y in ((x1, y1), (x2, y2)):
        s, b = np.polyfit(x, y, 1)
        line = np.linspace(x.min(), x.max(), 2)
        ax.plot(line, s * line + b, color="black", linewidth=2.0,
                label="Trend per group" if x is x1 else None)

    ax.set_title("Simpson's paradox: rising in each group, falling overall", fontsize=14)
    ax.set_xlabel("Feature x (e.g. dose)")
    ax.set_ylabel("Outcome y (e.g. success)")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(HERE / "simpson-paradox.png")
    plt.close(fig)


# ------------------------------------------------------- colour vision simulation

# Vienot, Brettel and Mollon (1999). Linear RGB to LMS, and the projection of LMS onto
# the plane each kind of dichromacy collapses it to. The matrix has to be the
# Smith-Pokorny one the paper's projection coefficients were derived against; pairing
# those coefficients with the Hunt-Pointer-Estevez matrix instead turns the whole palette
# green, which is how this was caught.
RGB_TO_LMS = np.array([[17.8824, 43.5161, 4.11935],
                       [3.45565, 27.1554, 3.86714],
                       [0.0299566, 0.184309, 1.46709]])
LMS_TO_RGB = np.linalg.inv(RGB_TO_LMS)
PROJECT = {
    "Protanopia":  np.array([[0, 2.02344, -2.52581], [0, 1, 0], [0, 0, 1]]),
    "Deuteranopia": np.array([[1, 0, 0], [0.494207, 0, 1.24827], [0, 0, 1]]),
    # Brettel and Vienot split tritanopia into two half-planes. The German figure uses
    # this one, and a least-squares fit against its pixels reproduces it to within
    # rounding; the other half-plane (-0.395913, 0.801109) renders the same palette in
    # yellows and blues instead of the pinks and teals a tritanope actually reports.
    "Tritanopia":  np.array([[1, 0, 0], [0, 1, 0], [-0.012245, 0.072035, 0]]),
}


def _to_linear(c: np.ndarray) -> np.ndarray:
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def _to_srgb(c: np.ndarray) -> np.ndarray:
    c = np.clip(c, 0.0, 1.0)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055)


def simulate(hex_colours: list[str], kind: str) -> list[tuple[float, float, float]]:
    rgb = np.array([plt.matplotlib.colors.to_rgb(c) for c in hex_colours])
    lms = _to_linear(rgb) @ RGB_TO_LMS.T
    out = (lms @ PROJECT[kind].T) @ LMS_TO_RGB.T
    return [tuple(c) for c in _to_srgb(out)]


def colour_vision() -> None:
    """The same palette as four kinds of colour vision see it."""
    panels = [("Normal colour vision", OKABE_ITO),
              ("Deuteranopia", simulate(OKABE_ITO, "Deuteranopia")),
              ("Protanopia", simulate(OKABE_ITO, "Protanopia")),
              ("Tritanopia", simulate(OKABE_ITO, "Tritanopia"))]

    fig, axes = plt.subplots(2, 2, figsize=(13.3, 7.4), dpi=100)
    fig.suptitle("The same palette as it appears under different kinds of colour vision",
                 fontsize=16)
    for ax, (title, colours) in zip(axes.flat, panels):
        for i, colour in enumerate(colours):
            ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=colour))
        ax.set_xlim(0, len(colours))
        ax.set_ylim(0, 1)
        ax.set_title(title, fontsize=14)
        ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(HERE / "colour-vision-simulation.png")
    plt.close(fig)


# ------------------------------------------------------------- distribution families

def _density_family(dists, title, filename, x, extra=None) -> None:
    fig, ax = plt.subplots(figsize=(9.6, 11.4), dpi=100)
    fig.suptitle(title, fontsize=13)
    for label, pdf in dists:
        ax.plot(x, pdf, label=label)
    if extra:
        label, pdf = extra
        ax.plot(x, pdf, label=label)
    ax.legend(loc="upper right")
    fig.savefig(HERE / filename)
    plt.close(fig)


def chi_squared() -> None:
    from scipy import stats
    x = np.linspace(0, 30, 600)
    _density_family(
        [(f"{k} degrees of freedom", stats.chi2.pdf(x, k)) for k in (4, 8, 16)],
        "$\\chi^2$ distributions with different parameters",
        "chi-squared-distributions.png", x)


def student_t() -> None:
    from scipy import stats
    x = np.linspace(-5, 5, 600)
    _density_family(
        [(f"{k} degrees of freedom", stats.t.pdf(x, k)) for k in (4, 8, 16)],
        "Student t distributions with different parameters, and the standard normal "
        "distribution",
        "student-t-distributions.png", x,
        extra=("standard normal distribution", stats.norm.pdf(x)))


if __name__ == "__main__":
    simpson()
    colour_vision()
    chi_squared()
    student_t()
    print("wrote simpson-paradox.png, colour-vision-simulation.png, "
          "chi-squared-distributions.png and student-t-distributions.png")
