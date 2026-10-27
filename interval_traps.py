"""Certify the two population traps of Proposition 4 (low-contrast witness).

Standard library only.  For the three-level law of Proposition 4 the
population M(d) is the unique positive root of
    F(d, M) = sum_i p_i * Phi(m_i, d, M) - M,
    Phi(z, d, M) = ((z - d) + sqrt((z - d)^2 + 4 d M)) / 2,
and F(d, M) > 0 for 0 < M < M(d), F(d, M) < 0 for M > M(d)
(Lemma 3 of the paper).  Hence sign F(d, 1) = sign(M(d) - 1).
Square roots are enclosed rigorously with integer square roots on a scale
of 10**SCALE, so every sign below is certified, not floating point.

Traps checked (d0 = 76/25, where M(d0) = 1 exactly):
    (d0 - 1e-4, d0 - 1e-5, d0)   left trap
    (d0, d0 + 1e-2, 31/10)       right trap
Usage: python3 -I interval_traps.py [--out output]
"""
import argparse
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

SCALE = 80  # decimal digits for the square-root enclosures

d0 = F(76, 25)
theta = [1 - F(1, 10**6), 1 + F(1, 10**7), F(57, 5)]
m = [t + d0 - d0 / t for t in theta]
A = [t + d0 / t for t in theta]


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


rows = [[F(1)] * 3, theta[:], [(1 - t) / a for t, a in zip(theta, A)]]
rhs = [F(1), F(1), F(0)]
D0 = det3(rows)
p = []
for j in range(3):
    Mj = [r[:] for r in rows]
    for i in range(3):
        Mj[i][j] = rhs[i]
    p.append(det3(Mj) / D0)
assert D0 != 0 and all(x > 0 for x in p)


def sqrt_bounds(x):
    """Rational lo <= sqrt(x) <= hi for rational x >= 0."""
    s = 10**SCALE
    n = x.numerator * s * s
    q = x.denominator
    r = isqrt(n // q)
    return F(r, s), F(r + 1, s)


def closure_at_one(d):
    """Rigorous enclosure [lo, hi] of F(d, 1)."""
    lo = hi = F(-1)
    for pi, z in zip(p, m):
        a, b = sqrt_bounds((z - d) ** 2 + 4 * d)
        lo += pi * ((z - d) + a) / 2
        hi += pi * ((z - d) + b) / 2
    return lo, hi


def sign_M_minus_1(d):
    lo, hi = closure_at_one(d)
    if lo > 0:
        return 1
    if hi < 0:
        return -1
    raise AssertionError(f"sign not certified at d={d}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="output")
    a = ap.parse_args()
    e4, e5, e2 = F(1, 10**4), F(1, 10**5), F(1, 10**2)
    checks = {
        "d0-1e-4": (d0 - e4, -1),
        "d0-1e-5": (d0 - e5, 1),
        "d0+1e-2": (d0 + e2, 1),
        "31/10": (F(31, 10), -1),
    }
    out = {"d0": "76/25", "M_at_d0": "1 (exact; see contrast_witness.py)",
           "sqrt_scale_digits": SCALE, "signs_of_M_minus_1": {}}
    for k, (d, want) in checks.items():
        s = sign_M_minus_1(d)
        assert s == want, (k, s, want)
        lo, hi = closure_at_one(d)
        out["signs_of_M_minus_1"][k] = {
            "sign": s, "closure_F_d_1_enclosure": [f"{float(lo):.6e}", f"{float(hi):.6e}"]}
    out["left_trap"] = "(d0-1e-4, d0-1e-5, d0): M(d0-1e-5) > 1 = M(d0) > M(d0-1e-4)"
    out["right_trap"] = "(d0, d0+1e-2, 31/10): M(d0+1e-2) > 1 = M(d0) > M(31/10)"
    out["status"] = "certified by rational square-root enclosures"
    od = Path(a.out)
    od.mkdir(parents=True, exist_ok=True)
    (od / "interval_traps.json").write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
