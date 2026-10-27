# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy==2.4.6",
#     "scipy==1.17.1",
#     "matplotlib==3.11.2",
# ]
# ///
"""Numerical search for the smallest resource contrast giving two maxima
among three-level laws (evidence only; certificates are in contrast_witness.py).

Part 1: multistart SLSQP over (d, theta_1, theta_2, theta_3) at M=1, with the
habitat fractions solved from the stationarity system, minimising
max(m)/min(m) subject to p_i>0, m_i>0 and M''(d)>0.
Part 2: the rare-patch limit.  With background a=1, a rare level R and a
second level tending to 1, the first-order excess is c*d/(1+d)^2 + w*g_R(d).
We locate R* = inf{R: some c>0 gives a stationary point with F''>0} by
bisection on a dense d-grid.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize, brentq


def parts(x):
    d = np.exp(x[0]); t = np.exp(x[1:4])
    A = t + d / t; s = (1 - t) / A
    p = np.linalg.solve(np.array([np.ones(3), t, s]), [1, 1, 0])
    m = t + d - d / t
    C = np.sum(p * (s * s + s) / A); sc = np.sum(p * s * s)
    return d, t, p, m, C, sc


def part1(starts, seed=1):
    rng = np.random.default_rng(seed)
    f = lambda x: np.log(parts(x)[3].max() / parts(x)[3].min())
    cons = [{"type": "ineq", "fun": lambda x: parts(x)[2] - 1e-12},
            {"type": "ineq", "fun": lambda x: parts(x)[3] - 1e-12},
            {"type": "ineq", "fun": lambda x: -parts(x)[4] / parts(x)[5] - 1e-9}]
    best = np.inf
    with np.errstate(all="ignore"):
        for _ in range(starts):
            x0 = rng.uniform(-4, 4, 4)
            try:
                d, t, p, m, C, sc = parts(x0)
                if np.any(p <= 0) or np.any(m <= 0) or C >= 0:
                    continue
                r = minimize(f, x0, constraints=cons, method="SLSQP",
                             options={"maxiter": 500, "ftol": 1e-14})
                d, t, p, m, C, sc = parts(r.x)
                if r.success and np.all(p >= 0) and np.all(m > 0) and C <= 0:
                    best = min(best, float(np.exp(r.fun)))
            except np.linalg.LinAlgError:
                pass
    return best


def g(R, d):
    z = R - d; h = np.sqrt(z * z + 4 * d)
    hz = np.where(z >= 0, 4 * d / (h + z), h - z)
    t = np.where(z >= 0, (z + h) / 2, 2 * d / hz)
    return d * ((R - 1) / (1 + hz / 2)) ** 2 / t


def margin(R, d=np.geomspace(0.5, 50, 20001), e=1e-4):
    def D(fun, k):
        if k == 1:
            return (fun(d * (1 + e)) - fun(d * (1 - e))) / (2 * d * e)
        return (fun(d * (1 + e)) - 2 * fun(d) + fun(d * (1 - e))) / (d * e) ** 2
    h0 = lambda x: x / (1 + x) ** 2
    gR = lambda x: g(R, x)
    c = -D(gR, 1) / D(h0, 1)
    F2 = c * D(h0, 2) + D(gR, 2)
    ok = c > 0
    return float(np.max(F2[ok] / np.abs(D(gR, 2)[ok])))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="output")
    ap.add_argument("--starts", type=int, default=2000)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    Rstar = brentq(margin, 13.0, 15.0, xtol=1e-6)
    res = {"part1_best_contrast_found": part1(a.starts),
           "part1_starts": a.starts,
           "part2_rare_patch_limit_threshold_Rstar": Rstar,
           "status": "numerical evidence only; not a proof of optimality"}
    (out / "contrast_search.json").write_text(json.dumps(res, indent=2) + "\n")
    print(json.dumps(res, indent=2))
