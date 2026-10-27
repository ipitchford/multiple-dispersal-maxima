"""Exact certificate for a low-contrast three-level witness (standard library only).

The witness is specified by a dispersal rate d0 and three equilibrium
densities theta_i at mean population M=1.  The resource levels are
m_i = theta_i + d0 - d0/theta_i, and the habitat fractions p_i are the
unique solution of
    sum p_i = 1,   sum p_i theta_i = 1,   sum p_i (1-theta_i)/A_i = 0,
which are the normalisation, the equilibrium closure and M'(d0)=0.
Everything is checked in rational arithmetic; M''(d0)>0 then gives a
nondegenerate local minimum and hence two strict local maxima.
"""
from fractions import Fraction as F
import argparse
import json
from pathlib import Path

D0 = F(76, 25)
THETA = [F(1) - F(1, 10**6), F(1) + F(1, 10**7), F(57, 5)]  # background, near, rich


def solve3(rows, rhs):
    aug = [list(r) + [b] for r, b in zip(rows, rhs)]
    for i in range(3):
        piv = next(j for j in range(i, 3) if aug[j][i])
        aug[i], aug[piv] = aug[piv], aug[i]
        c = aug[i][i]
        aug[i] = [v / c for v in aug[i]]
        for j in range(3):
            if j != i:
                c = aug[j][i]
                aug[j] = [v - c * w for v, w in zip(aug[j], aug[i])]
    return [r[-1] for r in aug]


def certify(d, theta):
    A = [t + d / t for t in theta]
    s = [(1 - t) / a for t, a in zip(theta, A)]
    p = solve3([[F(1)] * 3, theta, s], [F(1), F(1), F(0)])
    m = [t + d - d / t for t in theta]
    assert all(x > 0 for x in p) and sum(p) == 1
    assert all(x > 0 for x in m)
    assert all(d * (1 - t) + t * (r - t) == 0 for t, r in zip(theta, m))
    assert sum(w * t for w, t in zip(p, theta)) == 1          # M(d0) = 1
    D = 1 - d * sum(w / a for w, a in zip(p, A))
    assert D > 0 and D == sum(w * t * t / a for w, t, a in zip(p, theta, A))
    assert sum(w * x for w, x in zip(p, s)) == 0              # M'(d0) = 0
    C = sum(w * (x * x + x) / a for w, x, a in zip(p, s, A))
    M2 = -2 * C / D
    assert M2 > 0                                             # strict local minimum
    kappa = max(m) / min(m)
    return {"d0": str(d), "theta": [str(t) for t in theta],
            "resource_levels": [str(x) for x in m],
            "habitat_fractions": [str(x) for x in p],
            "M_at_d0": "1", "M_prime_at_d0": "0",
            "implicit_denominator_D": str(D),
            "M_second_at_d0": str(M2), "M_second_float": float(M2),
            "contrast_max_over_min": str(kappa), "contrast_float": float(kappa),
            "mean_resource": str(sum(w * x for w, x in zip(p, m)))}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="output")
    out = Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    result = {"low_contrast_witness": certify(D0, THETA),
              "original_witness": certify(F(3), [F(4, 5), F(4, 3), F(30)])}
    text = json.dumps(result, indent=2)
    (out / "contrast_witness.json").write_text(text + "\n")
    print(text)
