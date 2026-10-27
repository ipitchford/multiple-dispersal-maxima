"""Exact fingerprints for the uniform global logistic dispersal construction.

Run with Python 3 (standard library only). The output JSON records three
positive three-level distributions with a stationary strict minimum at
d=3, M=1. No numerical optimisation or root finder is used.

This is an object-identity aid for prior-art searching, not a novelty test.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import lcm
from pathlib import Path
import argparse


def solve_exact(matrix, rhs):
    aug = [[F(v) for v in row] + [F(b)] for row, b in zip(matrix, rhs)]
    n = len(rhs)
    for i in range(n):
        pivot = next(j for j in range(i, n) if aug[j][i])
        aug[i], aug[pivot] = aug[pivot], aug[i]
        c = aug[i][i]
        aug[i] = [v / c for v in aug[i]]
        for j in range(n):
            if i != j:
                c = aug[j][i]
                aug[j] = [v - c * w for v, w in zip(aug[j], aug[i])]
    return [row[-1] for row in aug]


def fractions(values):
    return [str(v) for v in values]


def scaled(values):
    denominator = lcm(*(v.denominator for v in values))
    return {"denominator": denominator,
            "integer_numerators": [int(v * denominator) for v in values]}


def matrix_hash(matrix):
    text = json.dumps([[str(x) for x in row] for row in matrix],
                      separators=(",", ":"))
    return sha256(text.encode()).hexdigest()


def charpoly(matrix):
    """Exact characteristic polynomial coefficients (Faddeev--LeVerrier),
    highest degree first: det(lambda*I - matrix)."""
    n = len(matrix)
    A = [[F(v) for v in row] for row in matrix]
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    mul = lambda X, Y: [[sum(X[i][k] * Y[k][j] for k in range(n))
                         for j in range(n)] for i in range(n)]
    coeffs = [F(1)]
    Mk = [[F(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        Mk = [[Mk[i][j] + coeffs[-1] * I[i][j] for j in range(n)]
              for i in range(n)]
        AM = mul(A, Mk)
        c = -sum(AM[i][i] for i in range(n)) / k
        coeffs.append(c)
        Mk = AM
    return coeffs


def rank(matrix):
    rows = [[F(v) for v in row] for row in matrix]
    r = 0
    for c in range(len(rows[0])):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                f = rows[i][c] / rows[r][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def poly_text(coeffs):
    n = len(coeffs) - 1
    terms = []
    for k, c in enumerate(coeffs):
        if c:
            terms.append(f"({c})*lambda^{n-k}")
    return " + ".join(terms)


def rational_roots(coeffs, candidates):
    """Multiset of roots among candidates, by exact repeated division."""
    roots, c = [], list(coeffs)
    for x in candidates:
        while len(c) > 1:
            q, acc = [], F(0)
            for a in c:
                acc = acc * x + a
                q.append(acc)
            if q[-1] != 0:
                break
            roots.append(x)
            c = q[:-1]
    assert len(c) == 1, "not all roots are among the candidates"
    return [str(r) for r in sorted(roots, reverse=True)]


def invariants(matrix, candidates):
    cp = charpoly(matrix)
    n = len(matrix)
    return {"rank": rank(matrix),
            "trace": str(sum(F(matrix[i][i]) for i in range(n))),
            "determinant": str((-1) ** n * cp[-1]),
            "characteristic_polynomial": poly_text(cp),
            "eigenvalues": rational_roots(cp, candidates)}


def instance(v):
    d = F(3)
    theta = [F(4, 5), F(4, 3), F(v)]
    slope_numerator = [(1 - t) * t / (t * t + d) for t in theta]
    p = solve_exact([[1] * 3, theta, slope_numerator], [1, 1, 0])
    resource = [t + d - d / t for t in theta]
    A = [2 * t + d - m for t, m in zip(theta, resource)]
    slope = [(1 - t) / b for t, b in zip(theta, A)]
    expectation = lambda vals: sum(w * x for w, x in zip(p, vals))
    D = 1 - d * expectation([1 / b for b in A])
    C = expectation([(h * h + h) / b for h, b in zip(slope, A)])
    second = -2 * C / D
    assert all(x > 0 for x in p + resource)
    assert sum(p) == 1 and expectation(theta) == 1
    assert expectation(slope) == 0 and second > 0
    assert all(d * (1 - t) + t * (m - t) == 0
               for t, m in zip(theta, resource))
    P = [p.copy() for _ in p]
    generator = [[d * (p[j] - int(i == j)) for j in range(3)]
                 for i in range(3)]
    assert all(sum(row) == 1 for row in P)
    assert all(sum(row) == 0 for row in generator)
    return {
        "v": v, "d": "3", "M": "1", "M_prime": "0",
        "theta": fractions(theta), "resource": fractions(resource),
        "probabilities": fractions(p), "probability_common_scaling": scaled(p),
        "mean_resource": str(expectation(resource)), "A": fractions(A),
        "theta_prime": fractions(slope), "D": str(D),
        "curvature_expectation": str(C), "M_second": str(second),
        "mixing_matrix_P_ij_pj": [fractions(row) for row in P],
        "mixing_matrix_sha256_canonical_order": matrix_hash(P),
        "mixing_matrix_sha256_transpose": matrix_hash(list(zip(*P))),
        **{"mixing_matrix_" + k: v
           for k, v in invariants(P, [F(1), F(0)]).items()},
        "generator": [fractions(row) for row in generator],
        **{"generator_" + k: v
           for k, v in invariants(generator, [F(0), -d]).items()},
        "generator_stationary_probability": fractions(p),
    }


def kernel_taylor(a=F(1), r=F(2), degree=12):
    """Expand t^2+(d-r)t-ad=0, then g=(a+d)(t-a)/a-(r-a)."""
    t = [r]
    for n in range(1, degree + 1):
        convolution = sum(t[i] * t[n-i] for i in range(1, n))
        coefficient = t[n-1] - (a if n == 1 else 0)
        t.append(-(convolution + coefficient) / r)
    g = [F(0)] + [t[n] + (t[n-1] - (a if n == 1 else 0)) / a
                    for n in range(1, degree + 1)]
    # Check the eliminated quadratic through the requested Taylor order.
    for n in range(degree + 1):
        residual = a * sum(g[i] * g[n-i] for i in range(n + 1))
        residual += a * r * g[n]
        if n >= 1:
            residual += (3 * a - r) * g[n-1]
        if n >= 2:
            residual += g[n-2]
        if n == 1:
            residual -= (r - a) ** 2
        assert residual == 0
    return {
        "a": str(a), "r": str(r),
        "g_coefficients_degrees_0_through_12": fractions(g),
        "g_coefficients_common_scaling": scaled(g),
        "t_coefficients_degrees_0_through_12": fractions(t),
        "g_polynomial": "a*g^2+(d^2+(3*a-r)*d+a*r)*g-d*(r-a)^2",
        "t_polynomial": "t^2+(d-r)*t-a*d",
        "initial_branch": "g(0)=0, t(0)=r",
        "coefficient_recurrence":
            "r*t_n=-t_(n-1)-sum_(i=1)^(n-1)t_i*t_(n-i)+a*1_(n=1)",
        "interpretation":
            "Elementary algebraic response kernel, not claimed as a new named function.",
    }


if __name__ == "__main__":
    output = {
        "date": "2026-10-27",
        "model": "d*(M-theta)+theta*(m-theta)=0; M=E(theta)",
        "normalisation": "Unit habitat measure; local quadratic coefficient 1.",
        "finite_instances": [instance(v) for v in (30, 50, 100)],
        "kernel_fingerprint": kernel_taylor(),
    }
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="output",
                    help="output directory (the shipped receipt is never overwritten)")
    out = Path(ap.parse_args().out)
    out.mkdir(parents=True, exist_ok=True)
    destination = out / "resource_fingerprints.json"
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print("Verified three exact strict-minimum witnesses and twelve kernel coefficients.")
    print(destination)
