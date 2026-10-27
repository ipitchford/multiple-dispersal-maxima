#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy==2.4.6",
#     "scipy==1.17.1",
#     "matplotlib==3.11.2",
# ]
# ///
"""Numerical illustrations. Exact arithmetic and analytic proofs are separate."""
from pathlib import Path
import argparse
import json
import os
import platform
import tempfile
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "dispersal-mpl-cache"))
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_ap = argparse.ArgumentParser()
_ap.add_argument("--out", default="output", help="output directory for figures and peak data")
OUT = Path(_ap.parse_args().out)
OUT.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "axes.spines.top": False, "axes.spines.right": False,
                     "savefig.facecolor": "white"})
m = np.array([1/20, 25/12, 329/10])
p = np.array([2405, 1095, 4])/3504
teal, plum, grey = "#126B67", "#9C315C", "#72717A"

def equilibrium(d):
    def theta(M):
        z = m-d
        h = np.sqrt(z*z+4*d*M)
        return np.where(z >= 0, (z+h)/2, 2*d*M/(h-z))
    M = brentq(lambda M: np.dot(p, theta(M))-M,
               min(m), np.sqrt(np.dot(p, m*m)), xtol=1e-14)
    return M


def dM(d, h=1e-6):
    return (equilibrium(d * (1 + h)) - equilibrium(d * (1 - h))) / (2 * d * h)


# Critical points located by Brent's method on a central-difference M'.
first_peak = brentq(dM, 1.2, 2.6, xtol=1e-12)
second_peak = brentq(dM, 6.0, 30.0, xtol=1e-12)
P1 = (first_peak, equilibrium(first_peak))
P2 = (second_peak, equilibrium(second_peak))
assert dM(first_peak * 0.9) > 0 > dM(first_peak * 1.1)
assert dM(second_peak * 0.9) > 0 > dM(second_peak * 1.1)

fig, axes = plt.subplots(1, 2, figsize=(10, 5.625))
dd = np.geomspace(.002, 2000, 1200)
axes[0].plot(dd, [equilibrium(d) for d in dd], color=teal, lw=2.2)
axes[0].axhline(1, color=grey, ls="--", lw=1)
axes[0].axhline(np.dot(p, m), color=grey, ls=":", lw=1)
axes[0].text(.003, .738, r"Mean resource $347/480$", color=grey, fontsize=9)
axes[0].scatter([3], [1], color=plum, s=46, zorder=5)
axes[0].scatter([P2[0]], [P2[1]], color=teal, s=35)
axes[0].annotate("Second peak", P2, xytext=(6.0, 1.072),
                 fontsize=10, arrowprops={"arrowstyle": "-", "color": teal})
axes[0].set(xscale="log", xlim=(.002, 2000), ylim=(.70, 1.095),
            xlabel=r"Dispersal rate $d$", ylabel=r"Total population $M(d)$")
axes[0].set_title("The full response", loc="left", fontweight="bold", fontsize=12)
axes[0].grid(alpha=.15)

dd = np.linspace(1.35, 4.2, 500)
axes[1].plot(dd, [equilibrium(d) for d in dd], color=teal, lw=2.2)
axes[1].axhline(1, color=grey, ls="--", lw=1)
axes[1].scatter([3], [1], color=plum, s=46, zorder=5)
axes[1].scatter([P1[0]], [P1[1]], color=teal, s=35)
axes[1].annotate(r"Exact minimum: $d=3$", (3, 1), xytext=(2.25, .99962),
                 fontsize=9.5, color=plum,
                 arrowprops={"arrowstyle": "-", "color": plum})
axes[1].annotate("First peak", P1, xytext=(1.52, 1.00115),
                 fontsize=10, arrowprops={"arrowstyle": "-", "color": teal})
axes[1].set(xlim=(1.35, 4.2), ylim=(.99945, 1.00165), xlabel=r"Dispersal rate $d$")
axes[1].ticklabel_format(axis="y", style="plain", useOffset=False)
axes[1].set_title("The shallow first peak, enlarged", loc="left", fontweight="bold", fontsize=12)
axes[1].grid(alpha=.15)
fig.subplots_adjust(left=.085, right=.98, top=.87, bottom=.15, wspace=.33)
fig.text(.085, .045, "Numerical curves illustrate the exact three-level example. The proof certifies M'(3) = 0 and M''(3) > 0.",
         fontsize=8.9, color="#494750")
for ext in ("pdf", "png"):
    fig.savefig(OUT / f"three_level_population.{ext}", dpi=220)

def response_kernel(r, d):
    """g_r(d) with a=1, using t-1=(r-1)/(1+(h-z)/2) to avoid cancellation."""
    z = r-d
    h = np.sqrt(z*z+4*d)
    h_minus_z = np.where(z >= 0, 4*d/(h+z), h-z)
    t = np.where(z >= 0, (z+h)/2, 2*d/h_minus_z)
    t_minus_1 = (r-1)/(1+h_minus_z/2)
    return d*t_minus_1**2/t

fig, ax = plt.subplots(figsize=(10, 5.625))
dd = np.geomspace(.2, 1e9, 2600)
levels = [100., 1e5, 1e8]
curves = [response_kernel(r, dd)/r**2 for r in levels]
for curve, colour, lab in zip(curves, ["#126B67", "#9C315C", "#9A761C"], [r"$r=10^2$", r"$r=10^5$", r"$r=10^8$"]):
    ax.plot(dd, curve, color=colour, lw=1.5, alpha=.8, ls="--", label=lab)
ax.plot(dd, np.sum(curves, axis=0), color="#303039", lw=2.1, label=r"Sum $G(d)$")
ax.set(xscale="log", xlim=(.2, 1e9), ylim=(-.008, .30),
       xlabel=r"Dispersal rate $d$ (logarithmic scale)", ylabel="First-order population excess")
ax.set_title("Separated resource levels create separated response peaks", loc="left", fontweight="bold", fontsize=13)
ax.legend(frameon=False, ncol=4, loc="upper right", fontsize=10)
ax.grid(alpha=.16)
fig.subplots_adjust(left=.085, right=.975, top=.87, bottom=.16)
fig.text(.085, .045, "Illustration of the analytic response kernels. The theorem proves the construction for any finite number of peaks.",
         fontsize=9.1, color="#494750")
for ext in ("pdf", "png"):
    fig.savefig(OUT / f"separated_response_kernels.{ext}", dpi=220)
import matplotlib, scipy
(OUT / "three_level_peaks.json").write_text(json.dumps({
    "method": "brentq on central-difference M'(d); numerical illustration only",
    "first_maximum": {"d": P1[0], "M": P1[1]},
    "certified_minimum": {"d": 3, "M": 1},
    "second_maximum": {"d": P2[0], "M": P2[1]},
    "relative_depth_first_peak_over_minimum": P1[1] - 1,
    "versions": {"python": platform.python_version(), "numpy": np.__version__,
                 "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
}, indent=2) + "\n")
print("Created the three-level example and response-kernel illustrations.")
